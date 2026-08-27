![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> 轻量级实时终端网络流量监控工具，灵感来自 Linux 的 nload。

> **[📖 English](readme.md)**
> **[📖 简体中文(大陆)](readme.zh-cn.md)**
> **[📖 繁體中文(台灣)](readme.zh-tw.md)**
> **[📖 文言文](readme.lzh.md)**
> **[📖 日本語](readme.jp.md)**
> **[📖 한국어](readme.ko.md)**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-6e7681?style=for-the-badge&logo=github&logoColor=white&labelColor=181717)](https://github.com/VincentZyuApps/winload)
[![Gitee](https://img.shields.io/badge/Gitee-Mirror-6e7681?style=for-the-badge&logo=gitee&logoColor=white&labelColor=C71D23)](https://gitee.com/vincent-zyu/winload)

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

> **[📖 构建文档](.github/workflows/build.zh-cn.md)**

## 🚀 简介
`Winload` 是一个直观的终端网络流量监控工具。最初为 Windows 打造，弥补 `nload` 在 Windows 上的空白，现已支持 Linux 和 macOS。

## 🙏 致谢
Winload 的灵感来自 Roland Riegel 的经典 「[nload](https://github.com/rolandriegel/nload)」 项目，感谢原作者的创意与体验。
https://github.com/rolandriegel/nload

## ✨ 主要特性
- **双实现版本**
	- **Rust 版**: 快速、内存安全、单静态二进制文件，适合日常监控。
	- **Python 版**: 易于修改和扩展，适合原型开发或集成。
- **跨平台**: Windows、Linux、macOS（x64 & ARM64）。
- **实时可视化**: 实时上行/下行流量图和吞吐量统计。
- **简洁界面**: 干净的 TUI，沿袭 nload 的人体工程学设计。

## 📊 性能基准测试
> ⚡ Winload (Rust) 实现 **~10ms 启动速度** 和 **<2MB 二进制体积**，在效率上显著优于 Python 并与 C++ nload 相当。

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 从源码运行

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# 或从 Gitee 克隆（中国大陆更快）：
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv run python -m winload
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # 显示帮助
cargo run --release -- --version # 显示版本
```

## 🐍 Python 版本安装
> 💡 **实现说明**：仅 PyPI 和 GitHub/Gitee 源代码是 Python 版本。  
> 仅 Cargo 提供 Rust 源码供本地编译。  
> 所有其他包管理器（Scoop、AUR、npm、APT、RPM）及 GitHub Releases 均提供 **Rust 二进制文件**。
### Python (pip)
```bash
pip install winload
# 推荐使用 uv：
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run python -c "import shutil; print(shutil.which('winload'))"
uv run winload
```

## 📥 Rust 版本安装（推荐）
### npm (跨平台)
```bash
# 推荐（scoped）
npm install -g @vincentzyuapps/winload
# 备选（unscoped）
npm install -g winload-rust-bin
# 备选（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# 在 Windows 上使用 win-nload 以避免与 System32\winload.exe 冲突
# 在 Linux/macOS 上，winload 和 win-nload 均可使用
# 或直接使用 npx
npx @vincentzyuapps/winload
```

> 包含 4 个预编译二进制文件：x86_64 & ARM64 版本，支持 Windows、Linux 和 macOS。

### Cargo (源码编译)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# 或从 Gitee 克隆：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # optional: 提前手动更新 bucket 列表
scoop install winload
# 执行二进制文件
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 推荐使用 [Windows Terminal](https://github.com/microsoft/terminal) 而非旧版 Windows Console，以获得正确的中文字符渲染和更好的 TUI 体验。
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **所有构建均需 Windows 10+**（Rust 1.77+ 已放弃支持 Windows 7/8）。Scoop 和 npm 默认提供 **x86_64** 和 **ARM64** 的 **MSVC + Npcap** 构建。这些构建现在会延迟加载 `wpcap.dll`，可降低未使用 `--npcap` 前的启动失败风险，但回环抓包仍然需要系统已安装 Npcap。

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 系发行版 / Termux（一键安装脚本）
> 支持 Debian/Ubuntu 及其下游 —— Linux Mint、Pop!_OS、Deepin、统信 UOS 等 (apt)

> 支持 Fedora/RHEL 及其下游 —— Rocky Linux、AlmaLinux、CentOS Stream 等 (dnf)

> 也支持 Android 上的 Termux (aarch64)

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [查看安装脚本源码](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Gitee 镜像（大陆地区下载更快）：**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [查看 Gitee 安装脚本源码](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ 以上两个 `curl ... | bash` 安装脚本支持 **x86_64 / aarch64** 架构上使用 **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）或 **Termux**（Android）的系统。其他平台请使用 **npm**（`npm install -g @vincentzyuapps/winload`）或 **Cargo**（`cargo install winload`）安装。

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> 较新的 Homebrew 可能要求先信任第三方 tap 的 formula 后再安装。
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# 或从 Gitee（手动克隆 tap）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew 支持 **macOS**（Intel 和 Apple Silicon）和 **Linux**（x86_64 和 ARM64）。

<details>
<summary>手动安装</summary>

**DEB (Debian/Ubuntu):**
```bash
# 从 GitHub Releases 下载最新 .deb 包
sudo dpkg -i ./winload*.deb
# 或使用 apt（自动处理依赖）
sudo apt install ./winload*.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**或者直接从 [GitHub Releases](https://github.com/VincentZyuApps/winload/releases) 下载二进制文件。**

</details>

## ⌨️ 用法

```bash
winload              # 监控所有活跃网络接口
winload -t 200       # 设置刷新间隔为 200ms
winload -d "Wi-Fi"   # 启动时定位到 Wi-Fi 网卡
winload --title "我的监视器" # 使用自定义顶部标题
winload -e           # 启用 emoji 装饰 🎉
winload --max-mode smart --max-half-life 10 # 平滑自适应 Y 轴（默认）
winload --max-mode legacy # nload 风格的可见历史峰值缩放
winload --max-mode fixed --max-y-value 10M # 固定 Y 轴上限
winload --graph-style line --x-axis 5s --y-axis unit # Rust：折线图及时间、流量坐标轴
winload --npcap      # 捕获 127.0.0.1 回环流量 (Windows，需安装 Npcap)
winload --netlink    # 手动启用 RTNETLINK（Linux/Android，默认关闭）
```

### Rust 版本额外功能

Rust 版本覆盖 Python 的全部用户操作，包括 `C`、`PageUp` 和 `PageDown`，并额外提供：

- `Esc` 退出、四种图形风格、可选 X/Y 轴，以及运行时 `g`/`x`/`y` 图形控制。
- 安装 Npcap 后可使用 Windows `--npcap` 捕获回环流量。

### 参数选项

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-t`, `--interval <MS>` | 刷新间隔（毫秒） | `500` |
| `-a`, `--average <SEC>` | 平均值计算窗口（秒） | `300` |
| `-d`, `--device <NAME>` | 默认设备名（模糊匹配） | — |
| `--title [TITLE]` | 在设备标题上方添加标题行：不带值时显示 `winload <版本号>`；空字符串（或省略）时仅显示默认设备标题 | — |
| `-e`, `--emoji` | 启用 emoji 装饰 🎉 | 关闭 |
| `-U`, `--unicode` | 为 `classic` 图形使用 Unicode 方块字符（█▓░·） | 关闭 |
| `--graph-style <STYLE>` | **[仅 Rust]** 图形风格：`classic`、`line`、`scatter` 或 `bar` | `classic` |
| `--x-axis <MODE>` | **[仅 Rust]** X 轴网格：`none` 或 `5s` 等正整数秒间隔 | `none` |
| `--y-axis <MODE>` | **[仅 Rust]** Y 轴标签和网格：`none`、`percent` 或 `unit` | `none` |
| `-u`, `--unit <UNIT>` | 显示单位：`bit` 或 `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | 状态栏样式：`fill`、`color` 或 `plain` | `plain` |
| `--in-color <HEX>` | 下行图形颜色，十六进制 RGB（如 `0x00d7ff`） | 青色 |
| `--out-color <HEX>` | 上行图形颜色，十六进制 RGB（如 `0xffaf00`） | 金色 |
| `--max-mode <MODE>` | Y 轴缩放模式：`smart`、`legacy` 或 `fixed` | `smart` |
| `--max-half-life <SECS>` | smart 模式指数衰减半衰期 | `10` |
| `--max-y-value <VALUE>` | fixed 模式固定 Y 轴上限（如 `10M`、`1G`、`500K`） | — |
| `-n`, `--no-graph` | 隐藏图形，仅显示统计信息 | 关闭 |
| `--hide-separator` | 隐藏分隔线（等于号一行） | 关闭 |
| `--no-color` | 禁用所有 TUI 颜色（单色模式） | 关闭 |
| `--npcap` | **[Windows Rust Only]** 通过 Npcap 捕获回环流量（推荐） | 关闭 |
| `--netlink` | **[Linux/Android Only]** 使用 RTNETLINK 替代默认后端（在 Termux proot distro 或受限环境中适用） | 关闭 |
| `--debug-info` | 打印网络接口调试信息后退出 | — |
| `-h`, `--help` | 打印帮助（`--help --emoji` 可查看 emoji 版！） | — |
| `-V`, `--version` | 打印版本号 | — |

> **Y 轴缩放模式**
>
> | 模式 | 参数 | 行为 |
> |------|------|------|
> | **smart** | `--max-mode smart --max-half-life 10` | 默认。流量突增时立即跳升，随后平滑指数回落。 |
> | **legacy** | `--max-mode legacy` | nload 风格，按当前可见图形窗口峰值自动缩放。 |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Y 轴锁定为指定值。 |
>
> `--max-y-value` 仅可用于 `--max-mode fixed`；`--max-half-life` 仅可用于 `--max-mode smart`。

### 快捷键

| 按键 | 功能 |
|------|------|
| `←` / `↑` | 切换到上一个网络设备 |
| `→` / `↓` | 切换到下一个网络设备 |
| `Tab` / `Enter` | 切换到下一个网络设备 |
| `PageUp` / `PageDown` | 切换到上一个/下一个网络设备 |
| `F3` | 切换调试信息界面（Minecraft 风格） |
| `=` | 切换分隔线的显示/隐藏 |
| `c` | 切换颜色开/关 |
| `C` | 切换颜色开/关 |
| `g` / `G` | **[仅 Rust]** 循环切换 `classic` → `line` → `scatter` → `bar` |
| `x` / `X` | **[仅 Rust]** 切换时间轴；未配置间隔时使用 `5s` |
| `y` / `Y` | **[仅 Rust]** 循环切换 Y 轴：`none` → `percent` → `unit` |
| `q` / `Q` 或 `Ctrl+C` | 退出 |
| `Esc` | **[仅 Rust]** 退出 |

> **实现说明：** Rust 额外提供 `Esc` 以及 `g`/`x`/`y` 图形控制。`classic` 仍是 Rust 的默认图形风格，运行时切换只影响当前会话。四种 Rust 图形风格共享同一套 X/Y 网格和缩放视口；`--unicode` 只影响 `classic`，Ratatui 风格使用各自的原生标记。

## 🪟 Windows 回环流量 (127.0.0.1)

Windows 无法通过标准 API 报告回环流量——这是 [Windows 网络栈的功能缺失](docs/win_loopback.zh-cn.md)。

**要在 Windows 上捕获回环流量**，使用 `--npcap` 参数：

```bash
winload --npcap
```

需要安装 [Npcap](https://npcap.com/#download)，安装时勾选 "Support loopback traffic capture"。

> 我之前尝试过直接轮询 Windows 自带的 `GetIfEntry` API，但 loopback 的计数器始终为 0——loopback 伪接口背后根本没有 NDIS 驱动在计数。该代码路径已被移除。

> 📖 深入了解 Windows 回环为何失效，请阅读 [docs/win_loopback.zh-cn.md](docs/win_loopback.zh-cn.md)

## 🐧 Linux / Android / Termux Netlink

在 Linux 和 macOS 上，回环流量开箱即用，无需额外参数。

在 **Linux/Android** 上，如果无法访问 `/proc/net/dev`（例如在 Termux proot distro 或其他受限环境中），可使用 `--netlink` 通过 RTNETLINK 直接收集网络统计信息：

```bash
winload --netlink
```

> 注意：`--netlink` 和 `--npcap` 一样是**手动启用的可选后端**，默认不会启用；普通 Linux/Android 仍使用默认后端（Rust：sysinfo，Python：psutil）。Python 版在 Linux/Android 上通过 `pyroute2` 使用 RTNETLINK。macOS 不支持 netlink。
>
> 📖 深入了解 Linux/Android 网络统计采集原理，请阅读 [docs/linux_android_netlink.zh-cn.md](docs/linux_android_netlink.zh-cn.md)

## 🖼️ 预览
#### Python 版预览
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust 版预览
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust 版预览 GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### 终端录制
[![asciicast](https://asciinema.org/a/1030894.svg)](https://asciinema.org/a/1030894?t=30)

> ↑ 使用 [asciinema](https://github.com/asciinema/asciinema) 录制

## 📦 依赖

### Python 版本

| 包 | 版本 | 说明 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | 编程语言 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | 进程和系统工具 |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | Linux/Android 上的 RTNETLINK 后端 |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses 支持 |

### Rust 版本

| 包 | 版本 | 说明 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | 编程语言 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | 终端 UI 框架 |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | 跨平台终端库 |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | 系统信息库 |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | 命令行参数解析器 |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | 数据包捕获（可选，Windows） |
## 🧭 结语

网络流量本是无形无影之物，而 Winload 却能让它具象于眼前。数据包在终端中穿行，无声无息，却能将千丝万缕的吞吐之状尽数呈现。若你想读懂一台机器的网络脉搏，此工具既可作案头的一盏小灯，也可作夜航时的一颗星。

## 🧱 源码目录

<!-- winload-source-tree:start -->
<!-- Generated by scripts/update_readme_tree.py; do not edit manually. -->
```text
python/
├── src/
│   └── winload/
│       ├── i18n/
│       │   ├── __init__.py // 32 lines | Selects the active language and exposes stable translation helpers.
│       │   ├── en_us.py // 154 lines | Stores the English localization catalog.
│       │   ├── zh_cn.py // 154 lines | Stores the Simplified Chinese localization catalog.
│       │   └── zh_tw.py // 154 lines | Stores the Traditional Chinese localization catalog.
│       ├── ui/
│       │   ├── __init__.py // 266 lines | Coordinates curses layout, colors, application state, and public UI access.
│       │   ├── debug.py // 111 lines | Draws the interactive F3 diagnostics overlay.
│       │   └── panels.py // 219 lines | Draws classic traffic graphs and formatted statistics panels.
│       ├── __init__.py // 2 lines | 📦 Marks the Python package and exposes package-level metadata.
│       ├── __main__.py // 6 lines | ▶️ Runs the Python CLI entry point when invoked with python -m winload.
│       ├── app.py // 135 lines | Owns mutable application state, traffic updates, and device navigation.
│       ├── cli.py // 219 lines | Builds, localizes, parses, and validates the Python command-line interface.
│       ├── collector.py // 121 lines | 📡 Collects network interface counters with psutil or the optional Netlink backend.
│       ├── config.py // 73 lines | Defines immutable, strongly typed runtime configuration for the Python application.
│       ├── diagnostics.py // 162 lines | Reports version, build, system, and network-interface diagnostic information.
│       ├── emoji.py // 48 lines | ✨ Decorates CLI-facing labels with optional emoji icons.
│       ├── graph.py // 108 lines | 📊 Renders incoming and outgoing traffic graphs for terminal display.
│       ├── main.py // 46 lines | Wires the Python CLI to diagnostics or the interactive terminal runtime.
│       ├── netlink.py // 120 lines | 🔗 Reads Linux and Android network counters directly through RTNETLINK.
│       ├── runtime.py // 62 lines | Manages the curses lifecycle, input mapping, refresh cadence, and UI rendering loop.
│       └── stats.py // 208 lines | 📈 Calculates rolling traffic rates, totals, and adaptive graph scale values.
└── _build_info.py // 73 lines | 🧾 Resolves source or packaged Git metadata for Python version output.

rust/
├── src/
│   ├── i18n/
│   │   ├── en_us.rs // 130 lines | Provides the complete English localization catalog.
│   │   ├── mod.rs // 54 lines | 🌐 Provides localized UI, help, and debug strings for supported languages.
│   │   ├── zh_cn.rs // 130 lines | Provides the complete Simplified Chinese localization catalog.
│   │   └── zh_tw.rs // 130 lines | Provides the complete Traditional Chinese localization catalog.
│   ├── ui/
│   │   ├── debug.rs // 105 lines | Draws the F3 runtime diagnostics overlay.
│   │   ├── mod.rs // 261 lines | Coordinates the ratatui layout, header, help bar, panels, and debug overlay.
│   │   └── panels.rs // 488 lines | Draws traffic histories in classic, line, scatter, and bar styles with optional axes.
│   ├── app.rs // 192 lines | Owns mutable application state, traffic collection, and device navigation.
│   ├── cli.rs // 434 lines | Parses localized command-line arguments and produces a validated RunConfig.
│   ├── collector.rs // 238 lines | 📡 Collects network interface counters and prepares traffic snapshots for the TUI.
│   ├── config.rs // 194 lines | Defines validated, strongly typed runtime configuration shared by the Rust modules.
│   ├── diagnostics.rs // 45 lines | Prints build, platform, and network-interface diagnostics outside the TUI.
│   ├── emoji.rs // 50 lines | ✨ Decorates CLI-facing labels with optional emoji icons.
│   ├── graph.rs // 279 lines | 📊 Renders incoming and outgoing traffic graphs for terminal display.
│   ├── loopback.rs // 265 lines | 🪟 Captures and counts Windows loopback traffic through Npcap when enabled.
│   ├── main.rs // 42 lines | Boots the Rust application and dispatches CLI actions to focused modules.
│   ├── netlink.rs // 231 lines | 🔗 Reads Linux and Android network counters directly through RTNETLINK.
│   ├── runtime.rs // 141 lines | Runs the terminal lifecycle, refresh loop, and semantic keyboard controls.
│   └── stats.rs // 244 lines | 📈 Calculates rolling traffic rates, totals, and adaptive graph scale values.
└── _build_info.rs // 51 lines | 🧾 Injects Git metadata and configures platform-specific linker behavior.
```
<!-- winload-source-tree:end -->

