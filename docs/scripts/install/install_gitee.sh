#!/bin/bash
# winload installer (Gitee 镜像) — 适用于中国大陆用户，解决 GitHub 下载慢的问题
# 支持 apt (deb) / dnf (rpm) / Termux，架构 x86_64 / aarch64
#
# 用法:
#   curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
#
# 安装指定版本:
#   WINLOAD_VERSION=v0.1.7-rc.19 bash -c "$(curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh)"
set -e

OWNER="vincent-zyu"
REPO="winload"
API_URL="https://gitee.com/api/v5/repos/${OWNER}/${REPO}/releases/latest"

# ── 检测 Termux ──────────────────────────────────────────
IS_TERMUX=false
if [ -n "${PREFIX:-}" ] && [ -d "${PREFIX}/bin" ]; then
  IS_TERMUX=true
fi

# ── 检测架构 ─────────────────────────────────────────────
ARCH=$(uname -m)
case "$ARCH" in
  x86_64|amd64)  ARCH_NAME="x86_64" ;;
  aarch64|arm64)  ARCH_NAME="aarch64" ;;
  *)
    echo "❌ 不支持的架构: $ARCH"
    echo "   仅支持 x86_64 和 aarch64。"
    echo ""
    echo "   其他安装方式:"
    echo "   • npm (跨平台): npm install -g @vincentzyuapps/winload"
    echo "   • 手动下载: https://gitee.com/${OWNER}/${REPO}/releases"
    echo "   • 从源码构建: https://gitee.com/${OWNER}/${REPO}"
    exit 1
    ;;
esac

# ── 检测包管理器 ──────────────────────────────────────────
if $IS_TERMUX; then
  PKG_MGR="termux"
elif command -v apt-get >/dev/null 2>&1; then
  PKG_MGR="apt"
elif command -v dnf >/dev/null 2>&1; then
  PKG_MGR="dnf"
else
  echo "❌ 不支持的包管理器。"
  echo "   本安装脚本仅支持 apt (Debian/Ubuntu)、dnf (Fedora/RHEL) 和 Termux。"
  echo ""
  echo "   其他安装方式:"
  echo "   • 手动下载: https://gitee.com/${OWNER}/${REPO}/releases"
  echo "   • 从源码构建: cargo install winload"
  exit 1
fi

# ── Arch Linux 用户提示 ──────────────────────────────────
if command -v pacman >/dev/null 2>&1; then
  echo ""
  echo "💡 检测到 Arch Linux! 你也可以通过 AUR 安装:"
  echo "   paru -S winload-rust-bin"
  echo "   https://aur.archlinux.org/packages/winload-rust-bin"
  echo ""
fi

echo "🔍 检测到: 架构=$ARCH 包管理器=$PKG_MGR${IS_TERMUX:+ termux=true}"

# ── 获取版本号 ────────────────────────────────────────────
if [ -n "${WINLOAD_VERSION:-}" ]; then
  VERSION="$WINLOAD_VERSION"
  echo "📌 使用指定版本: $VERSION"
else
  echo "📡 正在从 Gitee API 获取最新版本..."
  VERSION=$(curl -fsSL "$API_URL" | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": *"\([^"]*\)".*/\1/')
  if [ -z "$VERSION" ]; then
    echo "❌ 从 Gitee API 获取最新版本失败。"
    echo "   你可以手动指定版本:"
    echo "   WINLOAD_VERSION=v0.1.7-rc.19 bash -c \"\$(curl -fsSL ...)\""
    exit 1
  fi
  echo "📦 最新版本: $VERSION"
fi

# ── 下载并安装 ────────────────────────────────────────────
BASE_URL="https://gitee.com/${OWNER}/${REPO}/releases/download/${VERSION}"
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT
CHECKSUM_FILE="winload-checksums-${VERSION}.txt"

echo "📥 正在下载 ${CHECKSUM_FILE}..."
curl -fSL -o "${TMP_DIR}/${CHECKSUM_FILE}" "${BASE_URL}/${CHECKSUM_FILE}"

download_and_verify() {
  local asset="$1"
  local target="${TMP_DIR}/${asset}"
  local checksum

  echo "📥 正在下载 ${asset}..."
  curl -fSL -o "$target" "${BASE_URL}/${asset}"
  checksum=$(awk -v asset="$asset" '$2 == asset { print $1; exit }' "${TMP_DIR}/${CHECKSUM_FILE}")
  if [ -z "$checksum" ]; then
    echo "❌ 未找到 ${asset} 的 SHA-256 校验值。"
    exit 1
  fi
  if ! printf '%s  %s\n' "$checksum" "$target" | sha256sum --check --status; then
    echo "❌ ${asset} 的 SHA-256 校验失败。"
    exit 1
  fi
  echo "✅ SHA-256 校验通过: ${asset}"
}

if [ "$PKG_MGR" = "termux" ]; then
  ANDROID_ASSET="winload-android-${ARCH_NAME}-${VERSION}"
  download_and_verify "$ANDROID_ASSET"
  echo "📦 安装到 ${PREFIX}/bin/ ..."
  install -Dm755 "${TMP_DIR}/${ANDROID_ASSET}" "${PREFIX}/bin/winload"
elif [ "$PKG_MGR" = "apt" ]; then
  PLATFORM="linux-${ARCH_NAME}"
  PKG_FILE="winload-${PLATFORM}-${VERSION}.deb"
  download_and_verify "$PKG_FILE"
  echo "📦 通过 apt 安装中..."
  sudo dpkg -i "${TMP_DIR}/${PKG_FILE}" || sudo apt-get install -f -y
elif [ "$PKG_MGR" = "dnf" ]; then
  PLATFORM="linux-${ARCH_NAME}"
  PKG_FILE="winload-${PLATFORM}-${VERSION}.rpm"
  download_and_verify "$PKG_FILE"
  echo "📦 通过 dnf 安装中..."
  sudo dnf install -y "${TMP_DIR}/${PKG_FILE}"
fi

echo ""
echo "✅ winload 安装成功!"
echo "   运行 'winload' 开始监控网络流量。"
echo ""
echo "   卸载方式:"
if [ "$PKG_MGR" = "termux" ]; then
  echo "   rm ${PREFIX}/bin/winload"
elif [ "$PKG_MGR" = "apt" ]; then
  echo "   sudo apt remove winload"
elif [ "$PKG_MGR" = "dnf" ]; then
  echo "   sudo dnf remove winload"
fi
echo ""
echo "   📖 GitHub: https://github.com/VincentZyuApps/winload"
echo "   📖 Gitee:  https://gitee.com/${OWNER}/${REPO}"
echo ""
echo "   🌐 GitHub install script (GitHub 安装脚本):"
echo "   curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash"
