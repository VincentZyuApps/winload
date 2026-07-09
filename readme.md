![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> A lightweight, real-time CLI tool for monitoring network bandwidth and traffic, inspired by Linux's nload.

> **[📖 English](readme.md)**
> **[📖 简体中文(大陆)](readme.zh-cn.md)**
> **[📖 繁體中文(台灣)](readme.zh-tw.md)**
> **[📖 文言文](readme.lzh.md)**
> **[📖 日本語](readme.jp.md)**
> **[📖 한국어](readme.ko.md)**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VincentZyuApps/winload)
[![Gitee](https://img.shields.io/badge/Gitee-C71D23?style=for-the-badge&logo=gitee&logoColor=white)](https://gitee.com/vincent-zyu/winload)

[![Windows x64 | ARM64](https://img.shields.io/static/v1?label=Windows&message=x64%20%7C%20ARM64&color=0078D4&style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTAgMGgxMS4zNzd2MTEuMzcySDB6TTEyLjYyMyAwSDI0djExLjM3MkgxMi42MjN6TTAgMTIuNjIzaDExLjM3N1YyNEgweiBNMTIuNjIzIDEyLjYyM0gyNFYyNEgxMi42MjN6IiBmaWxsPSIjZmZmIi8+PC9zdmc+)](https://github.com/VincentZyuApps/winload/releases)
[![Linux x64 | ARM64](https://img.shields.io/badge/Linux-x64_|_ARM64-FCC624?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![macOS x64 | ARM64](https://img.shields.io/badge/macOS-x64_|_ARM64-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Android x64 | ARM64](https://img.shields.io/badge/Android-x64_|_ARM64-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)

[![PyPI](https://img.shields.io/badge/PyPI-3776AB?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/winload/)
[![Python Versions](https://img.shields.io/pypi/pyversions/winload.svg?label=version&style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/winload/)

[![Crates.io](https://img.shields.io/badge/Crates.io-000000?style=for-the-badge&logo=rust&logoColor=white)](https://crates.io/crates/winload)

[![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/@vincentzyuapps/winload)

[![Scoop.sh](https://img.shields.io/badge/Scoop.sh-7B4AE2?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSI4IiByPSI1IiBmaWxsPSIjRUM3MEExIi8+PGNpcmNsZSBjeD0iOCIgY3k9IjEyIiByPSI0LjUiIGZpbGw9IiNFQkYzQTEiLz48Y2lyY2xlIGN4PSIxNiIgY3k9IjEyIiByPSI0LjUiIGZpbGw9IiM4RTZFQzgiLz48cGF0aCBkPSJNMTYuNSA0bC0xLjUtMS41TDExLjUgNmwxLjUgMS41eiIgZmlsbD0iI2ZmZmZmZiIvPjxwYXRoIGQ9Ik0zIDEzaDE4YzAgNC40LTMuNiA4LTggOGgtNGMtNC40IDAtOC0zLjYtOC04eiIgZmlsbD0iIzRGNEI1MyIvPjwvc3ZnPg==)](https://scoop.sh/#/apps?q=%22https%3A%2F%2Fgithub.com%2FVincentZyuApps%2Fscoop-bucket%22&o=false)
[![AUR](https://img.shields.io/badge/AUR-1793D1?style=for-the-badge&logo=archlinux&logoColor=white)](https://aur.archlinux.org/packages/winload-rust-bin)
[![APT](https://img.shields.io/badge/APT-E95420?style=for-the-badge&logo=debian&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![RPM](https://img.shields.io/badge/RPM-CB1626?style=for-the-badge&logo=redhat&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Homebrew](https://img.shields.io/badge/Homebrew-FBB040?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABIFBMVEXjojpVVVU0NTYKD2ZeX18uLS1nUzSccjT%2F9IudnZ34zZzV1dWVaWb%2Fyme5hzk4PkY5QEfo6utiYF6Pgm89QkI5SWS%2Bv8D%2Fu1H%2FwF38wmkuLi5%2FgIAvb88AAJEkLkJpaWkuLCySk5RFQj9GOyxBOCsAAAD8s0L5rTtIR0bW2NlUVFRXWFn%2F%2F%2F%2F%2FtDv7wWI7Ozv%2F4Jc8PDxJSUt%2Bfn77xnpmZmYNDQ14dnFHR0iLhHs7OzrIystWVlWqq6x0dXX1rUFlZWU3PUY4ODdZWVlFRkZiYmL%2FwkpTVViJiotoaGg1NTW3uLlQUVMkJCRjY2Lo6utbW1tmZmYqKimYmJgnKi86OjtOXGv%2B3ZJJSUmBfnT%2F6Ij%2BulKGhoZERUX7uln%2F3IiiD4zCAAAAYHRSTlP%2BMtgYsU7T%2F0kSFgYccf6mmv7SKTJM%2F5yc0Dz8EA5Ndp%2F%2FpMSUAP79sv0EqwTR%2FG3%2BBG8LU0lESY9PqP%2FS%2Ffr9m5op8cUs%2FVn9%2BpT%2Fcwyt%2B48YdgxIyDP%2BUFA0tD39yE55c4A0AAABtUlEQVR42rXTV1fbMBQAYCchiw3dE2h75StbSYid1K5XiO3svYAy%2F%2F%2B%2FQHGhsQ3pW%2FXgo3P0Hd3hKwH%2BLuyqUIb4ElZby7YSkJ6sA2UwTNO%2F9JCVXwYSuJ2DT0nn4%2FoQg2PH7pxBYrAGTL22d9tZWG2nO2PPgATTNqUj0%2BxRemBjXo0BFVxnRKlJgzVqp1f1Co8l6CdOpxcc92yTYhwAJJOua7zt2dTp9n3bY%2FEclEUDoHrbnXoGD%2BhbKEXBa2PGVFXrA5RaUhkYXGIUzPXldxsGTz1oxMDMUKqfV7WfK%2Bg%2BpfmYw9YCM5kfen%2F%2BlaeHmNTyW%2FEyXxWKNUHYzX5jqWxOGcrYCgMJUCucFgVCmtk3qd0cbCcmfgNYCMha4aIo1kQiZr4LufqG1VLSkRv%2BAEJqRBSblT3QhqWfUfCLh%2BCAC0Iq%2B5vVs3WAEJFU6uy%2Fg314BjYiYO%2FmaPwvcN8ayhN9Hg3xO3zDckL8fBxckKAPNbF5Xzd0XQ06HerkdZMfC8sr7jYxPnIc3MDVzvvrD3fvdq74D%2Bdjz6JDq2D%2F%2FEuwS%2FFxKb3wshJjGY1D6xBRHjdCT%2B8BOSqpSBALHToAAAAASUVORK5CYII%3D)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)

> **[📖 Build Docs](.github/workflows/build.md)**

## 🚀 Introduction
`Winload` brings an intuitive, visual network monitor to the modern terminal. It started as a Windows-focused tool to fill the `nload` gap, and now targets Linux and macOS as well.

## 🙏 Acknowledgements
Winload is inspired by the classic 「[nload](https://github.com/rolandriegel/nload)」 project by Roland Riegel. Many thanks for the original idea and experience.
https://github.com/rolandriegel/nload

## ✨ Key Features
- **Dual implementations**
	- **Rust edition**: fast, memory-safe, single static binary—great for everyday monitoring.
	- **Python edition**: easy to hack and extend for prototyping or integrations.
- **Cross-platform**: Windows, Linux, and macOS (x64 & ARM64).
- **Real-time visualization**: live incoming/outgoing graphs and throughput stats.
- **Minimal UI**: clean TUI that mirrors nload's ergonomics.

## 📊 Performance Benchmarks
> ⚡ Winload (Rust) achieves **~10ms startup** and **<2MB binary size**, significantly outperforming Python and matching C++ nload in efficiency.

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 Run from Source

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# or clone from Gitee (faster in China Mainland):
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv run python -m winload
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # Show help
cargo run --release -- --version # Show version
```

## 🐍 Python Edition Installation
> 💡 **Implementation Note**: Only PyPI and GitHub/Gitee provide Python edition.  
> Only Cargo provides Rust source code for local compilation.  
> All other package managers (Scoop, AUR, npm, APT, RPM) and GitHub Releases distribute **Rust binaries only**.
### Python (pip)
```bash
pip install winload
# recommend use uv:
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run python -c "import shutil; print(shutil.which('winload'))"
uv run winload
```

## 📥 Rust Edition Installation (recommended)
### npm (cross-platform)
```bash
# Recommended (scoped)
npm install -g @vincentzyuapps/winload
# Alternative (unscoped)
npm install -g winload-rust-bin
# Alternative (GitHub Packages)
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# on Windows, use win-nload to avoid conflict with System32\winload.exe
# on Linux/macOS, both winload and win-nload work
# or use npx directly
npx @vincentzyuapps/winload
```

> Includes 4 precompiled binaries for x86_64 & ARM64 across Windows, Linux, and macOS.

### Cargo (Build from source)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# or from Gitee:
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # optional: manually refresh bucket list before install
scoop install winload
# execute bin file
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 Recommended: use [Windows Terminal](https://github.com/microsoft/terminal) instead of the legacy Windows Console for correct CJK character rendering and better TUI experience.
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **All builds require Windows 10+** (Rust 1.77+ dropped Windows 7/8 support). Scoop and npm provide **MSVC + Npcap** for **x86_64** and **ARM64** by default. These builds now delay-load `wpcap.dll`, reducing startup failures before `--npcap` is used, but loopback capture still requires Npcap installed on the system.

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat Distros / Termux (one-liner)
> Supports Debian/Ubuntu and derivatives — Linux Mint, Pop!_OS, Deepin, UOS, etc. (apt)

> Supports Fedora/RHEL and derivatives — Rocky Linux, AlmaLinux, CentOS Stream, etc. (dnf)

> Also supports Termux on Android (aarch64)

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [View install script source](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Gitee mirror (faster in China Mainland):**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [View Gitee install script](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ The two `curl ... | bash` install scripts above support **x86_64 / aarch64** systems with **apt** (Debian/Ubuntu), **dnf** (Fedora/RHEL), or **Termux** (Android). For other platforms, use **npm** (`npm install -g @vincentzyuapps/winload`) or **Cargo** (`cargo install winload`) instead.

### macOS / Linux (Homebrew)
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> Recent Homebrew versions may require trusting third-party tap formulae before installation.
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# or from Gitee (manual tap clone):
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew supports **macOS** (Intel & Apple Silicon) and **Linux** (x86_64 & ARM64).

<details>
<summary>Manual install</summary>

**DEB (Debian/Ubuntu):**
```bash
# Download the latest .deb from GitHub Releases
sudo dpkg -i ./winload*.deb
# or use apt (auto-resolves dependencies)
sudo apt install ./winload*.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**Or download binaries directly from [GitHub Releases](https://github.com/VincentZyuApps/winload/releases).**

</details>

## ⌨️ Usage

```bash
winload              # Monitor all active network interfaces
winload -t 200       # Set refresh interval to 200ms
winload -d "Wi-Fi"   # Start with a specific device
winload --title "My Monitor" # Use a custom header title
winload -e           # Enable emoji decorations 🎉
winload --max-mode smart --max-half-life 10 # Smooth adaptive Y-axis (default)
winload --max-mode legacy # nload-style visible-history scaling
winload --max-mode fixed --max-y-value 10M # Fixed Y-axis max
winload --npcap      # Capture 127.0.0.1 loopback traffic (Windows, requires Npcap)
winload --netlink    # Manually enable RTNETLINK (Linux/Android, off by default)
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-t`, `--interval <MS>` | Refresh interval in milliseconds | `500` |
| `-a`, `--average <SEC>` | Average calculation window in seconds | `300` |
| `-d`, `--device <NAME>` | Default device name (partial match) | — |
| `--title [TITLE]` | Add a title line above device header: no value shows `winload <version>`; empty string (or omitted) shows only the default device header | — |
| `-e`, `--emoji` | Enable emoji decorations in TUI 🎉 | off |
| `-U`, `--unicode` | Use Unicode block characters for graph (█▓░·) | off |
| `-u`, `--unit <UNIT>` | Display unit: `bit` or `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | Bar style: `fill`, `color`, or `plain` | `plain` |
| `--in-color <HEX>` | Incoming graph color, hex RGB (e.g. `0x00d7ff`) | cyan |
| `--out-color <HEX>` | Outgoing graph color, hex RGB (e.g. `0xffaf00`) | gold |
| `--max-mode <MODE>` | Y-axis scaling mode: `smart`, `legacy`, or `fixed` | `smart` |
| `--max-half-life <SECS>` | Half-life for smart Y-axis decay | `10` |
| `--max-y-value <VALUE>` | Fixed Y-axis max for `--max-mode fixed` (e.g. `10M`, `1G`, `500K`) | — |
| `-n`, `--no-graph` | Hide graph, show stats only | off |
| `--hide-separator` | Hide the separator line (row of equals signs) | off |
| `--no-color` | Disable all TUI colors (monochrome mode) | off |
| `--npcap` | **[Windows Rust Only]** Capture loopback traffic via Npcap (recommended) | off |
| `--netlink` | **[Linux/Android Only]** Use RTNETLINK instead of the default backend (for Termux proot distro or restricted environments) | off |
| `--debug-info` | Print network interface debug info and exit | — |
| `-h`, `--help` | Print help (`--help --emoji` for emoji version!) | — |
| `-V`, `--version` | Print version | — |

> **Y-axis scaling modes**
>
> | Mode | Flag | Behavior |
> |------|------|----------|
> | **smart** | `--max-mode smart --max-half-life 10` | Default. Jumps up on traffic spikes, then smoothly decays back down. |
> | **legacy** | `--max-mode legacy` | nload-style scaling based on the visible graph history peak. |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Locks the Y-axis to the specified value. |
>
> `--max-y-value` is only valid with `--max-mode fixed`; `--max-half-life` is only valid with `--max-mode smart`.

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` / `→` or `↑` / `↓` | Switch network device |
| `F3` | Toggle debug info overlay (Minecraft-style) |
| `=` | Toggle separator line visibility |
| `c` | Toggle color on/off |
| `q` / `Esc` | Quit |

## 🪟 Windows Loopback (127.0.0.1)

Windows cannot report loopback traffic through standard APIs — this is a [functional deficiency in Windows' network stack](docs/win_loopback.md).

**To capture loopback traffic on Windows**, use the `--npcap` flag:

```bash
winload --npcap
```

This requires [Npcap](https://npcap.com/#download) installed with "Support loopback traffic capture" enabled during setup.

> I previously tried polling Windows' own `GetIfEntry` API directly, but the counters are always 0 for loopback — there is simply no NDIS driver behind the loopback pseudo-interface to count anything. That code path has been removed.

> 📖 For a deep dive into why Windows loopback is broken, see [docs/win_loopback.md](docs/win_loopback.md)

## 🐧 Linux / Android / Termux Netlink

On Linux and macOS, loopback traffic works out of the box — no extra flags needed.

On **Linux/Android**, if `/proc/net/dev` is not accessible (e.g. inside a Termux proot distro or other restricted environments), use `--netlink` to collect network stats via RTNETLINK directly:

```bash
winload --netlink
```

> Note: `--netlink` is an **opt-in backend**, similar to `--npcap`; it is never enabled unless you pass the flag. Normal Linux/Android runs still use the default backend (Rust: sysinfo, Python: psutil). The Python edition uses `pyroute2` for RTNETLINK on Linux/Android. macOS does not support netlink.
>
> 📖 For a deep dive into Linux/Android network statistics collection, see [docs/linux_android_netlink.md](docs/linux_android_netlink.md)

## 🖼️ Previews
#### Python Edition Preview
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust Edition Preview
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust Edition Preview GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### Terminal Recording
[![asciicast](https://asciinema.org/a/1030894.svg)](https://asciinema.org/a/1030894?t=30)

> ↑ Recorded by [asciinema](https://github.com/asciinema/asciinema)

## 📦 Dependencies

### Python Edition

| Package | Version | Description |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | Programming language |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | Process and system utilities |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | RTNETLINK backend on Linux/Android |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses support |

### Rust Edition

| Package | Version | Description |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | Programming language |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | Terminal UI framework |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | Cross-platform terminal library |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | System information library |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | Command-line argument parser |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | Packet capture (optional, Windows) |
## 🧭 Epilogue

Network traffic flows formless through the void — yet Winload gives it shape. Packets traverse the terminal, silent and unseen, but through this window, every thread of throughput takes form before your eyes. If you seek to know the pulse of a machine's connection to the world, this tool is at once a humble lamp upon your desk and a guiding star for the journey ahead.

