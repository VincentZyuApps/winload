#!/usr/bin/env python3
"""Tests for the generated README source-tree maintenance tool."""

from __future__ import annotations

import codecs
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[2] / "scripts" / "update_readme_tree.py"
SPEC = importlib.util.spec_from_file_location("update_readme_tree", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
TREE_TOOL = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = TREE_TOOL
SPEC.loader.exec_module(TREE_TOOL)


class ReadmeTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.write_source("python/_build_info.py", "# Resolves Python build metadata.\n")
        self.write_source("python/src/winload/main.py", "# Starts the Python application.\n")
        self.write_source("python/src/winload/ui/panels.py", "# Draws Python panels.\n")
        self.write_source("rust/_build_info.rs", "// Injects Rust build metadata.\n")
        self.write_source("rust/src/main.rs", "// Starts the Rust application.\n")
        self.write_source("rust/src/ui/panels.rs", "// Draws Rust panels.\n")
        for name in TREE_TOOL.README_FILES:
            self.write_readme(name)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write_source(self, relative_path: str, content: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="")
        return path

    def write_readme(
        self,
        name: str,
        *,
        newline: str = "\n",
        bom: bool = False,
        trailing_newline: bool = True,
    ) -> Path:
        text = newline.join(
            (
                "# winload",
                "",
                TREE_TOOL.START_MARKER,
                "old content",
                TREE_TOOL.END_MARKER,
            )
        )
        if trailing_newline:
            text += newline
        raw = text.encode("utf-8")
        if bom:
            raw = codecs.BOM_UTF8 + raw
        path = self.root / name
        path.write_bytes(raw)
        return path

    def invoke(self, *, dry_run: bool) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        code = TREE_TOOL.run(self.root, dry_run, stdout, stderr)
        return code, stdout.getvalue(), stderr.getvalue()

    def test_cli_dry_run_aliases_are_equivalent(self) -> None:
        for alias in ("-d", "--dry-run", "--dryrun"):
            with self.subTest(alias=alias):
                self.assertTrue(TREE_TOOL.parse_args([alias]).dry_run)
        self.assertFalse(TREE_TOOL.parse_args([]).dry_run)

    def test_update_renders_deterministic_directory_first_tree(self) -> None:
        code, stdout, stderr = self.invoke(dry_run=False)
        self.assertEqual(0, code, stderr)
        self.assertIn("updated readme.md", stdout)
        content = (self.root / "readme.md").read_text(encoding="utf-8")
        self.assertIn(
            "python/\n"
            "├── src/\n"
            "│   └── winload/\n"
            "│       ├── ui/\n"
            "│       │   └── panels.py // 1 lines | Draws Python panels.\n"
            "│       └── main.py // 1 lines | Starts the Python application.\n"
            "└── _build_info.py // 1 lines | Resolves Python build metadata.",
            content,
        )
        self.assertIn("rust/", content)
        self.assertEqual(1, content.count(TREE_TOOL.START_MARKER))
        self.assertEqual(1, content.count(TREE_TOOL.END_MARKER))

        second_code, second_stdout, second_stderr = self.invoke(dry_run=False)
        self.assertEqual(0, second_code, second_stderr)
        self.assertEqual("", second_stdout)

    def test_dry_run_reports_stale_content_without_writing(self) -> None:
        path = self.root / "readme.md"
        before = path.read_bytes()
        code, stdout, stderr = self.invoke(dry_run=True)
        self.assertEqual(1, code, stderr)
        self.assertIn("--- ", stdout)
        self.assertIn("+++ ", stdout)
        self.assertIn("-old content", stdout)
        self.assertEqual(before, path.read_bytes())

        self.assertEqual(0, self.invoke(dry_run=False)[0])
        code, stdout, stderr = self.invoke(dry_run=True)
        self.assertEqual(0, code, stderr)
        self.assertEqual("", stdout)

    def test_preserves_bom_crlf_and_missing_final_newline(self) -> None:
        path_with_newline = self.write_readme(
            "readme.md", newline="\r\n", bom=True, trailing_newline=True
        )
        path_without_newline = self.write_readme(
            "readme.zh-cn.md", newline="\r\n", bom=True, trailing_newline=False
        )
        code, _, stderr = self.invoke(dry_run=False)
        self.assertEqual(0, code, stderr)
        for path in (path_with_newline, path_without_newline):
            raw = path.read_bytes()
            self.assertTrue(raw.startswith(codecs.BOM_UTF8))
            payload = raw[len(codecs.BOM_UTF8) :]
            self.assertNotIn(b"\n", payload.replace(b"\r\n", b""))
        self.assertTrue(path_with_newline.read_bytes().endswith(b"\r\n"))
        self.assertFalse(path_without_newline.read_bytes().endswith(b"\n"))

    def test_rejects_invalid_or_non_english_role_header(self) -> None:
        cases = ("print('missing')\n", "# \n", "# 仅中文职责\n")
        for content in cases:
            with self.subTest(content=content):
                self.write_source("python/src/winload/main.py", content)
                code, _, stderr = self.invoke(dry_run=True)
                self.assertEqual(2, code)
                self.assertIn("first-line role", stderr)

        self.write_source(
            "python/src/winload/main.py", "# 🚦 Starts the Python application.\n"
        )
        code, _, stderr = self.invoke(dry_run=False)
        self.assertEqual(0, code, stderr)

    def test_warns_over_400_lines_and_rejects_over_500_lines(self) -> None:
        warning_source = "# Starts the Python application.\n" + "pass\n" * 400
        self.write_source("python/src/winload/main.py", warning_source)
        code, _, stderr = self.invoke(dry_run=False)
        self.assertEqual(0, code, stderr)
        self.assertIn("warning:", stderr)
        self.assertIn("401 lines", stderr)

        invalid_source = "# Starts the Python application.\n" + "pass\n" * 500
        self.write_source("python/src/winload/main.py", invalid_source)
        code, _, stderr = self.invoke(dry_run=True)
        self.assertEqual(2, code)
        self.assertIn("501 lines", stderr)
        self.assertIn("hard limit", stderr)

    def test_rejects_missing_duplicate_reversed_and_non_final_markers(self) -> None:
        invalid_documents = (
            "# winload\n",
            f"{TREE_TOOL.START_MARKER}\n{TREE_TOOL.START_MARKER}\n{TREE_TOOL.END_MARKER}\n",
            f"{TREE_TOOL.END_MARKER}\n{TREE_TOOL.START_MARKER}\n",
            f"{TREE_TOOL.START_MARKER}\n{TREE_TOOL.END_MARKER}\ntrailing section\n",
        )
        for content in invalid_documents:
            with self.subTest(content=content):
                (self.root / "readme.md").write_text(content, encoding="utf-8")
                code, _, stderr = self.invoke(dry_run=True)
                self.assertEqual(2, code)
                self.assertIn("readme.md", stderr)

    def test_ignores_symlinked_sources(self) -> None:
        target = self.write_source(
            "outside.py", "print('this file has no required role header')\n"
        )
        link = self.root / "python" / "src" / "winload" / "linked.py"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation is unavailable")
        code, _, stderr = self.invoke(dry_run=False)
        self.assertEqual(0, code, stderr)
        content = (self.root / "readme.md").read_text(encoding="utf-8")
        self.assertNotIn("linked.py", content)


if __name__ == "__main__":
    unittest.main()
