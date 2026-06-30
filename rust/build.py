#!/usr/bin/env python3
"""
Cross-compile winload for Windows x64 and Linux x64 from WSL.
Usage: python3 build.py [--clean]
"""

import os
import re
import sys
import shutil
import argparse
import subprocess
from pathlib import Path
from multiprocessing import cpu_count

# 路径配置
RUST_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = RUST_DIR.parent
OUTPUT_DIR = RUST_DIR / "dist"

TARGETS = [
    ("x86_64-unknown-linux-musl", "winload", "winload-linux-x86_64"),
    # ("x86_64-pc-windows-gnu", "winload.exe", "winload-windows-x86_64.exe"), # Suspended for local dev
]


def robust_rmtree(path: Path):
    """删除目录树，兼容 WSL 9p 挂载的权限问题"""
    if not path.exists():
        return
    if sys.platform == "win32":
        shutil.rmtree(path)
        return

    # Linux / WSL: 依次尝试多种方式
    # 1) rm -rf
    ret = subprocess.run(["rm", "-rf", str(path)], check=False)
    if ret.returncode == 0 and not path.exists():
        return

    # 2) WSL 特有: 通过 cmd.exe 走 Windows 原生删除
    #    /mnt/d/foo/bar -> D:\foo\bar
    str_path = str(path)
    if str_path.startswith("/mnt/"):
        parts = str_path.split("/")          # ['', 'mnt', 'd', 'foo', ...]
        drive = parts[2].upper() + ":"       # 'D:'
        win_path = drive + "\\" + "\\".join(parts[3:])
        ret = subprocess.run(
            ["cmd.exe", "/c", "rmdir", "/s", "/q", win_path],
            check=False,
        )
        if ret.returncode == 0 and not path.exists():
            return

    # 3) 最后兜底: shutil（可能也会失败，但至少试一下）
    try:
        shutil.rmtree(path)
    except Exception:
        print(f"   ⚠️  Warning: Could not fully remove {path}, continuing...")


def extract_version_from_cargo_toml():
    """从 Cargo.toml 提取版本号"""
    cargo_toml = RUST_DIR / "Cargo.toml"
    if not cargo_toml.exists():
        print("❌ Cargo.toml not found")
        return None
    
    with open(cargo_toml, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配 version = "x.y.z" 格式
    match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if match:
        raw_version = match.group(1)
        # 去掉 SemVer build metadata (+...) 部分，避免文件名/tag 出问题
        version = raw_version.split("+")[0]
        if version != raw_version:
            print(f"📦 Extracted version from Cargo.toml: v{raw_version}")
            print(f"   (stripped build metadata for filename: v{version})")
        else:
            print(f"📦 Extracted version from Cargo.toml: v{version}")
        return f"v{version}"
    
    print("⚠️  Could not extract version from Cargo.toml")
    return None


def run_command(cmd, cwd=None, check=True):
    """运行命令并打印输出"""
    print(f"\n▶ {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=False,
        text=True,
        check=check,
    )
    return result.returncode == 0


def ensure_target_installed(target):
    """确保 Rust target 已安装"""
    print(f"\n📦 Checking target: {target}")
    result = subprocess.run(
        ["rustup", "target", "list", "--installed"],
        capture_output=True,
        text=True,
        check=True,
    )
    if target not in result.stdout:
        print(f"   → Installing {target}...")
        run_command(["rustup", "target", "add", target])
    else:
        print(f"   ✓ {target} already installed")


def build_target(target, binary_name, output_name, version=None):
    """编译指定 target"""
    print(f"\n🔨 Building {target}...")
    
    # 先清理该 target 的编译产物
    target_dir = RUST_DIR / "target" / target
    if target_dir.exists():
        print(f"   → Cleaning {target} artifacts...")
        try:
            robust_rmtree(target_dir)
        except Exception as e:
            print(f"   ⚠️  Warning: Could not clean {target_dir}: {e}")
    
    # 编译 - 使用一半的核心数量（向下取整）以避免过度占用系统资源
    parallel_jobs = max(1, cpu_count() // 2)  # 至少 1 个 job
    success = run_command(
        ["cargo", "build", "--release", "--target", target, "-j", str(parallel_jobs)],
        cwd=RUST_DIR,
    )
    
    if not success:
        print(f"❌ Build failed for {target}")
        return False
    
    # 生成带版本号的输出文件名
    if version:
        # 在扩展名前插入版本号
        # winload-linux-x86_64 -> winload-linux-x86_64-v0.1.0
        # winload-windows-x86_64.exe -> winload-windows-x86_64-v0.1.0.exe
        base_name = output_name
        ext = ""
        if "." in output_name:
            base_name, ext = output_name.rsplit(".", 1)
            ext = "." + ext
        output_name_versioned = f"{base_name}-{version}{ext}"
    else:
        output_name_versioned = output_name
    
    # 复制产物到 dist 目录
    source = RUST_DIR / "target" / target / "release" / binary_name
    dest = OUTPUT_DIR / output_name_versioned
    
    if not source.exists():
        print(f"❌ Binary not found: {source}")
        return False
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)
    
    # 显示文件信息
    size_mb = dest.stat().st_size / 1024 / 1024
    print(f"✓ {output_name_versioned} ({size_mb:.2f} MB)")
    
    return True


def main():
    """主构建流程"""
    # 参数解析
    parser = argparse.ArgumentParser(
        description="Cross-compile winload for multiple platforms"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Run 'cargo clean' before building",
    )
    args = parser.parse_args()
    
    print("=" * 60)
    print("🚀 Building winload for multiple platforms")
    print("=" * 60)
    
    # 提取版本号
    version = extract_version_from_cargo_toml()
    if not version:
        print("⚠️  Building without version number in filename")
    
    # 检查是否在 WSL 中
    if not Path("/proc/version").exists():
        print("❌ This script must be run in WSL")
        sys.exit(1)
    
    with open("/proc/version") as f:
        if "microsoft" not in f.read().lower():
            print("⚠️  Warning: This doesn't look like WSL")
    
    # 如果指定了 --clean，先执行 cargo clean
    if args.clean:
        print("\n🧹 Running cargo clean...")
        if run_command(["cargo", "clean"], cwd=RUST_DIR, check=False):
            print("   ✓ Cleaned successfully")
        else:
            print("   ⚠️  cargo clean failed, continuing anyway...")
    
    # 检查工具链
    for target, _, _ in TARGETS:
        ensure_target_installed(target)
    
    # 清理旧的 dist 目录
    if OUTPUT_DIR.exists():
        print(f"\n🧹 Cleaning {OUTPUT_DIR}...")
        robust_rmtree(OUTPUT_DIR)
    
    # 编译所有 target
    success_count = 0
    for target, binary, output in TARGETS:
        if build_target(target, binary, output, version):
            success_count += 1
    
    # 总结
    print("\n" + "=" * 60)
    print(f"📊 Build Summary: {success_count}/{len(TARGETS)} succeeded")
    print("=" * 60)
    
    if OUTPUT_DIR.exists():
        print(f"\n📦 Output directory: {OUTPUT_DIR}")
        for item in sorted(OUTPUT_DIR.iterdir()):
            size_mb = item.stat().st_size / 1024 / 1024
            print(f"   • {item.name} ({size_mb:.2f} MB)")
    
    sys.exit(0 if success_count == len(TARGETS) else 1)


if __name__ == "__main__":
    main()
