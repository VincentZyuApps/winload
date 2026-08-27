#!/bin/bash
# winload installer — supports apt (deb) / dnf (rpm) / Termux on x86_64 / aarch64
# Usage: curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
# Install specific version: WINLOAD_VERSION=v0.1.7-rc.10 bash -c "$(curl -fsSL https://...)"
set -e

REPO="VincentZyuApps/winload"
API_URL="https://api.github.com/repos/${REPO}/releases/latest"

# ── Detect Termux ──────────────────────────────────────────
IS_TERMUX=false
if [ -n "${PREFIX:-}" ] && [ -d "${PREFIX}/bin" ]; then
  IS_TERMUX=true
fi

# ── Detect architecture ──────────────────────────────────
ARCH=$(uname -m)
case "$ARCH" in
  x86_64|amd64)  ARCH_NAME="x86_64" ;;
  aarch64|arm64)  ARCH_NAME="aarch64" ;;
  *)
    echo "❌ Unsupported architecture: $ARCH"
    echo "   Only x86_64 and aarch64 are supported."
    echo ""
    echo "   Alternatives:"
    echo "   • npm (cross-platform): npm install -g @vincentzyuapps/winload"
    echo "     https://www.npmjs.com/package/@vincentzyuapps/winload"
    echo "   • Manual download: https://github.com/${REPO}/releases"
    echo "   • Build from source: https://github.com/${REPO}"
    exit 1
    ;;
esac

# ── Detect package manager ───────────────────────────────
if $IS_TERMUX; then
  PKG_MGR="termux"
elif command -v apt-get >/dev/null 2>&1; then
  PKG_MGR="apt"
elif command -v dnf >/dev/null 2>&1; then
  PKG_MGR="dnf"
else
  echo "❌ Unsupported package manager."
  echo "   This installer only supports apt (Debian/Ubuntu), dnf (Fedora/RHEL), and Termux."
  echo ""
  echo "   For other platforms, download the binary manually:"
  echo "   • https://github.com/${REPO}/releases"
  echo "   • Build from source: cargo install winload"
  exit 1
fi

# ── Hint for Arch Linux users ────────────────────────────
if command -v pacman >/dev/null 2>&1; then
  echo ""
  echo "💡 Arch Linux detected! You can also install via AUR:"
  echo "   paru -S winload-rust-bin"
  echo "   https://aur.archlinux.org/packages/winload-rust-bin"
  echo ""
fi

echo "🔍 Detected: arch=$ARCH pkg_mgr=$PKG_MGR${IS_TERMUX:+ termux=true}"

# ── Fetch release version ─────────────────────────────────
if [ -n "${WINLOAD_VERSION:-}" ]; then
  VERSION="$WINLOAD_VERSION"
  echo "📌 Using specified version: $VERSION"
else
  echo "📡 Fetching latest version..."
  VERSION=$(curl -fsSL "$API_URL" | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": *"\([^"]*\)".*/\1/')
  if [ -z "$VERSION" ]; then
    echo "❌ Failed to fetch latest version from GitHub API."
    exit 1
  fi
  echo "📦 Latest version: $VERSION"
fi

# ── Download & Install ───────────────────────────────────
BASE_URL="https://github.com/${REPO}/releases/download/${VERSION}"
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT
CHECKSUM_FILE="winload-checksums-${VERSION}.txt"

echo "📥 Downloading ${CHECKSUM_FILE}..."
curl -fSL -o "${TMP_DIR}/${CHECKSUM_FILE}" "${BASE_URL}/${CHECKSUM_FILE}"

download_and_verify() {
  local asset="$1"
  local target="${TMP_DIR}/${asset}"
  local checksum

  echo "📥 Downloading ${asset}..."
  curl -fSL -o "$target" "${BASE_URL}/${asset}"
  checksum=$(awk -v asset="$asset" '$2 == asset { print $1; exit }' "${TMP_DIR}/${CHECKSUM_FILE}")
  if [ -z "$checksum" ]; then
    echo "❌ No SHA-256 checksum found for ${asset}."
    exit 1
  fi
  if ! printf '%s  %s\n' "$checksum" "$target" | sha256sum --check --status; then
    echo "❌ SHA-256 verification failed for ${asset}."
    exit 1
  fi
  echo "✅ SHA-256 verified: ${asset}"
}

if [ "$PKG_MGR" = "termux" ]; then
  ANDROID_ASSET="winload-android-${ARCH_NAME}-${VERSION}"
  download_and_verify "$ANDROID_ASSET"
  echo "📦 Installing to ${PREFIX}/bin/..."
  install -Dm755 "${TMP_DIR}/${ANDROID_ASSET}" "${PREFIX}/bin/winload"
elif [ "$PKG_MGR" = "apt" ]; then
  PLATFORM="linux-${ARCH_NAME}"
  PKG_FILE="winload-${PLATFORM}-${VERSION}.deb"
  download_and_verify "$PKG_FILE"
  echo "📦 Installing via apt..."
  sudo dpkg -i "${TMP_DIR}/${PKG_FILE}" || sudo apt-get install -f -y
elif [ "$PKG_MGR" = "dnf" ]; then
  PLATFORM="linux-${ARCH_NAME}"
  PKG_FILE="winload-${PLATFORM}-${VERSION}.rpm"
  download_and_verify "$PKG_FILE"
  echo "📦 Installing via dnf..."
  sudo dnf install -y "${TMP_DIR}/${PKG_FILE}"
fi

echo ""
echo "✅ winload installed successfully!"
echo "   Run 'winload' to start monitoring."
echo ""
echo "   To uninstall:"
if [ "$PKG_MGR" = "termux" ]; then
  echo "   rm ${PREFIX}/bin/winload"
elif [ "$PKG_MGR" = "apt" ]; then
  echo "   sudo apt remove winload"
elif [ "$PKG_MGR" = "dnf" ]; then
  echo "   sudo dnf remove winload"
fi
echo ""
echo "   📖 GitHub: https://github.com/${REPO}"
echo "   📖 Gitee:  https://gitee.com/vincent-zyu/winload"
echo ""
echo "   🇨🇳 Gitee mirror (faster in China / 国内镜像，下载更快):"
echo "   curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash"
