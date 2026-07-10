# 🧾 Resolves git or packaged build metadata for Python version output.
"""Build metadata helpers for version output."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess


@dataclass(frozen=True)
class BuildInfo:
    commit_hash: str
    commit_time: str
    dirty: bool = False


UNKNOWN_BUILD_INFO = BuildInfo("unknown", "unknown", False)


def get_build_info() -> BuildInfo:
    """Return source checkout info first, then packaged build info."""
    return _source_git_info() or _packaged_build_info()


def format_build_info() -> str:
    info = get_build_info()
    commit_hash = info.commit_hash
    if info.dirty and commit_hash != "unknown":
        commit_hash = f"{commit_hash} (dirty)"
    return f"Commit Hash: {commit_hash} | Commit Time: {info.commit_time}"


def _source_git_info() -> BuildInfo | None:
    package_dir = Path(__file__).resolve().parent
    repo_root_text = _git_output(["rev-parse", "--show-toplevel"], package_dir)
    if not repo_root_text:
        return None

    repo_root = Path(repo_root_text).resolve()
    try:
        relative_package_dir = package_dir.relative_to(repo_root)
    except ValueError:
        return None

    if relative_package_dir != Path("python/src/winload"):
        return None

    commit_hash = _git_output(["rev-parse", "--short=7", "HEAD"], repo_root)
    commit_time = _git_output(["show", "-s", "--format=%cI", "HEAD"], repo_root)
    if not commit_hash or not commit_time:
        return None

    status = _git_output(["status", "--porcelain"], repo_root)
    return BuildInfo(commit_hash, commit_time, bool(status))


def _packaged_build_info() -> BuildInfo:
    try:
        from . import _build_info
    except Exception:
        return UNKNOWN_BUILD_INFO

    commit_hash = getattr(_build_info, "GIT_COMMIT_HASH", "unknown")
    commit_time = getattr(_build_info, "GIT_COMMIT_TIME", "unknown")
    dirty = bool(getattr(_build_info, "GIT_DIRTY", False))
    return BuildInfo(str(commit_hash), str(commit_time), dirty)


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
