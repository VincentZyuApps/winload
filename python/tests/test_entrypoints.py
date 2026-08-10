# Verifies the installed and module entry points without opening the TUI.
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from winload.diagnostics import get_version


class EntrypointTests(unittest.TestCase):
    def test_installed_prerelease_version_uses_project_spelling(self):
        with patch("winload.diagnostics.get_pkg_version", return_value="0.1.13a2"):
            self.assertEqual(get_version(), "0.1.13-alpha.2")

    def test_python_module_version(self):
        python_root = Path(__file__).resolve().parents[1]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(python_root / "src")
        result = subprocess.run(
            [sys.executable, "-m", "winload", "--version"],
            cwd=python_root,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("winload 0.1.13-alpha.2 (Python edition)", result.stdout)


if __name__ == "__main__":
    unittest.main()
