# 🧾 Resolves source or packaged Git metadata for Python version output.
"""Build metadata helpers for source checkouts and packaged distributions."""

from __future__ import annotations

from pathlib import Path
import subprocess


GIT_COMMIT_HASH = "unknown"
GIT_COMMIT_TIME = "unknown"
GIT_DIRTY = False

BuildInfo = tuple[str, str, bool]


def get_build_info() -> BuildInfo:
    """Return source checkout info first, then packaged build info."""
    return _source_git_info() or _packaged_build_info()


def format_build_info() -> str:
    commit_hash, commit_time, dirty = get_build_info()
    if dirty and commit_hash != "unknown":
        commit_hash = f"{commit_hash} (dirty)"
    return f"Commit Hash: {commit_hash} | Commit Time: {commit_time}"


def _source_git_info() -> BuildInfo | None:
    module_path = Path(__file__).resolve()
    repo_root_text = _git_output(["rev-parse", "--show-toplevel"], module_path.parent)
    if not repo_root_text:
        return None

    repo_root = Path(repo_root_text).resolve()
    try:
        relative_module_path = module_path.relative_to(repo_root)
    except ValueError:
        return None

    if relative_module_path != Path("python/_build_info.py"):
        return None

    commit_hash = _git_output(["rev-parse", "--short=7", "HEAD"], repo_root)
    commit_time = _git_output(["show", "-s", "--format=%cI", "HEAD"], repo_root)
    if not commit_hash or not commit_time:
        return None

    status = _git_output(["status", "--porcelain"], repo_root)
    return commit_hash, commit_time, bool(status)


def _packaged_build_info() -> BuildInfo:
    return str(GIT_COMMIT_HASH), str(GIT_COMMIT_TIME), bool(GIT_DIRTY)


def _git_output(args: list[str], cwd: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None
