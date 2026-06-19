![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> 輕若飛鴻，疾若奔雷；居終端之一隅，而觀網脈之往來。其意取自 Linux 之 `nload`，而為今世諸機所用。

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
[![Crates.io](https://img.shields.io/badge/Crates.io-000000?style=for-the-badge&logo=rust&logoColor=white)](https://crates.io/crates/winload)

[![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/@vincentzyuapps/winload)

[![Scoop.sh](https://img.shields.io/badge/Scoop.sh-7B4AE2?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSI4IiByPSI1IiBmaWxsPSIjRUM3MEExIi8+PGNpcmNsZSBjeD0iOCIgY3k9IjEyIiByPSI0LjUiIGZpbGw9IiNFQkYzQTEiLz48Y2lyY2xlIGN4PSIxNiIgY3k9IjEyIiByPSI0LjUiIGZpbGw9IiM4RTZFQzgiLz48cGF0aCBkPSJNMTYuNSA0bC0xLjUtMS41TDExLjUgNmwxLjUgMS41eiIgZmlsbD0iI2ZmZmZmZiIvPjxwYXRoIGQ9Ik0zIDEzaDE4YzAgNC40LTMuNiA4LTggOGgtNGMtNC40IDAtOC0zLjYtOC04eiIgZmlsbD0iIzRGNEI1MyIvPjwvc3ZnPg==)](https://scoop.sh/#/apps?q=%22https%3A%2F%2Fgithub.com%2FVincentZyuApps%2Fscoop-bucket%22&o=false)
[![AUR](https://img.shields.io/badge/AUR-1793D1?style=for-the-badge&logo=archlinux&logoColor=white)](https://aur.archlinux.org/packages/winload-rust-bin)
[![APT](https://img.shields.io/badge/APT-E95420?style=for-the-badge&logo=debian&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![RPM](https://img.shields.io/badge/RPM-CB1626?style=for-the-badge&logo=redhat&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Homebrew](https://img.shields.io/badge/Homebrew-FBB040?style=for-the-badge&logo=homebrew&logoColor=black)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)

> **[📖 構築之書](.github/workflows/build.zh-cn.md)**

## 🚀 序
`Winload` 者，終端中觀網流之器也。初生於 Windows，欲補 `nload` 不能行於其上之闕；今則兼濟 Linux、macOS，亦及諸架構。

## 🙏 謝
Winload 之靈感，承 Roland Riegel 之經典「[nload](https://github.com/rolandriegel/nload)」。前賢鑿井，後人飲水；其構想與體驗，皆為此器開山之石。
https://github.com/rolandriegel/nload

## ✨ 要義
- **雙本並行**
	- **Rust 本**：迅疾、安穩、內存無虞，且可成一靜態二進制，日常巡網最宜。
	- **Python 本**：易改易拓，若欲試新意、接旁器、作雛形，取之甚便。
- **橫行諸臺**：Windows、Linux、macOS（x64 & ARM64）皆可用。
- **即時成圖**：入流出流，頃刻見其高下；吞吐之數，如觀潮汐。
- **界面清簡**：承 `nload` 舊風，不事繁飾，而所需皆在。

## 📊 功力校驗
> ⚡ Winload（Rust）可得 **約 10ms 啟動**，二進制 **小於 2MB**。較 Python 本輕捷甚多，與 C++ nload 之效亦可相頡頏。

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 自源而行

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# 中土網路若遲，亦可取 Gitee：
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/py
pip install -r requirements.txt
python main.py
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # 示助
cargo run --release -- --version # 示版
```

## 🐍 Python 本安置
> 💡 **本末之辨**：PyPI 與 GitHub/Gitee 所得者，乃 Python 本。  
> 僅 Cargo 提供 Rust 原始碼供本地編譯。  
> 所有其他套件管理器（Scoop、AUR、npm、APT、RPM）及 GitHub Releases 均提供 **Rust 二進制**。
### Python (pip)
```bash
pip install winload
# uv 之用法亦佳：
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run winload
uv run python -c "import shutil; print(shutil.which('winload'))"
```

## 📥 Rust 本安置（薦）
### npm（跨平台）
```bash
# 主薦（scoped）
npm install -g @vincentzyuapps/winload
# 佐選（unscoped）
npm install -g winload-rust-bin
# 佐選（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# Windows 上以 win-nload 避 System32\winload.exe 之衝
# Linux/macOS 上 winload 與 win-nload 皆可用
# 或徑以 npx 行之
npx @vincentzyuapps/winload
```

> 內置 4 預編二進制：x86_64 & ARM64，遍及 Windows、Linux、macOS。

### Cargo（自源編鑄）
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# 或取諸 Gitee：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # 可先手動刷新 bucket
scoop install winload
# 行二進制
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 宜用 [Windows Terminal](https://github.com/microsoft/terminal)，其 CJK 字元之渲染較舊版精確，TUI 體驗亦佳。
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **諸構皆需 Windows 10+**（Rust 1.77+ 已棄 Windows 7/8）。Scoop 與 npm 預設供 **x86_64** 與 **ARM64** 之 **MSVC + Npcap** 構。今延後載入 `wpcap.dll`，可減未用 `--npcap` 時啟動失誤之虞，然回環抓包仍需系統已裝 Npcap。

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 系發行版 / Termux（一令而裝）
> 支援 Debian/Ubuntu 及其下游 —— Linux Mint、Pop!_OS、Deepin、統信 UOS 等（apt）

> 支援 Fedora/RHEL 及其下游 —— Rocky Linux、AlmaLinux、CentOS Stream 等（dnf）

> 亦支援 Android 之 Termux（aarch64）

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/install_scripts/install.sh | bash
which winload
```
> 📄 [觀安裝腳本之源](https://github.com/VincentZyuApps/winload/blob/main/docs/install_scripts/install.sh)

**🇨🇳 Gitee 鏡像（中土下載更速）：**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/install_scripts/install_gitee.sh | bash
which winload
```
> 📄 [觀 Gitee 安裝腳本之源](https://gitee.com/vincent-zyu/winload/blob/main/docs/install_scripts/install_gitee.sh)

> ⚠️ 上二 `curl ... | bash` 安裝腳本支援 **x86_64 / aarch64** 架構之 **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）或 **Termux**（Android）系統。他方平臺請以 **npm**（`npm install -g @vincentzyuapps/winload`）或 **Cargo**（`cargo install winload`）安裝。

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
```bash
brew tap vincentzyuapps/tap
# 或從 Gitee（手動克隆 tap）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew 支援 **macOS**（Intel 與 Apple Silicon）與 **Linux**（x86_64 與 ARM64）。

<details>
<summary>手動安裝</summary>

**DEB（Debian/Ubuntu）：**
```bash
# 從 GitHub Releases 下載最新 .deb 包
sudo dpkg -i ./winload*.deb
# 或以 apt（自動理依賴）
sudo apt install ./winload*.deb
which winload
```

**RPM（Fedora/RHEL）：**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**或逕自 [GitHub Releases](https://github.com/VincentZyuApps/winload/releases) 下載二進制。**

</details>

## ⌨️ 用法

```bash
winload              # 監所有活網口
winload -t 200       # 置刷新間隔 200ms
winload -d "Wi-Fi"   # 啟時徑定 Wi-Fi 網卡
winload --title      # 頂標題示 "winload <版號>"
winload --title "吾監" # 自訂頂標題
winload --title ""   # 守預設裝置標題
winload -e           # 啟 emoji 飾 🎉
winload --npcap      # 捕 127.0.0.1 回環流（Windows，需 Npcap）
winload --netlink    # 用 RTNETLINK（Linux/Android，Termux proot distro 等受限境）
```

### 參數

| 參數 | 說明 | 預設 |
|------|------|------|
| `-t`, `--interval <MS>` | 刷新間隔（毫秒） | `500` |
| `-a`, `--average <SEC>` | 均值計算窗（秒） | `300` |
| `-d`, `--device <NAME>` | 預設裝置名（模糊比對） | — |
| `--title [TITLE]` | 裝置標題上增一行：不帶值則示 `winload <版號>`；空字串（或略）則僅示預設裝置標題 | — |
| `-e`, `--emoji` | TUI 中啟 emoji 飾 🎉 | 關 |
| `-U`, `--unicode` | 用 Unicode 方塊字繪圖（█▓░·） | 關 |
| `-u`, `--unit <UNIT>` | 示單位：`bit` 或 `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | 條樣式：`fill`、`color` 或 `plain` | `fill` |
| `--in-color <HEX>` | 入图形色，十六進 RGB（如 `0x00d7ff`） | 青 |
| `--out-color <HEX>` | 出图形色，十六進 RGB（如 `0xffaf00`） | 金 |
| `-m`, `--max <VALUE>` | 固 Y 軸極值（如 `10M`、`1G`、`500K`）—— *與 `--smart-max` 相剋* | 自動 |
| `--smart-max [SECS]` | 智適 Y 軸：尖峰後自回落（半衰期，秒，預設 10s）—— *與 `--max` 相剋* | 關 |
| `-n`, `--no-graph` | 隱圖，僅示統計 | 關 |
| `--hide-separator` | 隱分隔線（等號一行） | 關 |
| `--no-color` | 禁 TUI 色（單色） | 關 |
| `--npcap` | **[Windows Rust Only]** 以 Npcap 捕回環流 | 關 |
| `--netlink` | **[Linux/Android Rust Only]** 以 RTNETLINK 代 sysinfo（Termux proot distro 或受限境中用） | 關 |
| `--debug-info` | 印網口除錯信息後退 | — |
| `-h`, `--help` | 示助（`--help --emoji` 可得 emoji 版！） | — |
| `-V`, `--version` | 示版號 | — |

> **Y 軸縮放模式** —— 以下三者互斥：
>
> | 模式 | 參數 | 行為 |
> |------|------|------|
> | **固定極值** | `--max <VALUE>` | Y 軸鎖定為指定值（如 `10M`、`1G`）。 |
> | **智適極值** | `--smart-max [SECS]` | Y 軸自適：突增即升，隨後平滑衰減（指數衰減，預設半衰期 10 秒）。 |
> | **歷史峰值** | *（皆不加）* | Y 軸隨各指標之歷史最大值 —— 預設行止。 |
>
> ⚠️ `--max` 與 `--smart-max` **相剋** —— 二者不可並用。

### 捷鍵

| 鍵 | 功 |
|----|----|
| `←` / `→` 或 `↑` / `↓` | 切網口 |
| `F3` | 切除錯信息層（Minecraft 風） |
| `=` | 切分隔線顯隱 |
| `c` | 切色開關 |
| `q` / `Esc` | 退 |

## 🪟 Windows 回環流（127.0.0.1）

Windows 不能以標準 API 報回環流——此 [Windows 網棧之缺](docs/win_loopback.zh-tw.md)。

**欲捕回環流於 Windows**，用 `--npcap` 參：

```bash
winload --npcap
```

需裝 [Npcap](https://npcap.com/#download)，裝時勾 "Support loopback traffic capture"。

> 嘗試輪詢 Windows 之 `GetIfEntry` API，然 loopback 計數恆零——loopback 虛口背後無 NDIS 驅以數之。今已去其徑。

> 📖 欲知其詳，請閱 [docs/win_loopback.zh-cn.md](docs/win_loopback.zh-cn.md)

Linux 及 macOS 上，回環流開箱即用，無需他參。

在 **Linux/Android** 上，若 `/proc/net/dev` 不可讀（如 Termux proot distro 或其他受限之境），可以 `--netlink` 參，逕以 RTNETLINK 取網絡之數：

```bash
winload --netlink
```

> 註：`--netlink` 惟 **Linux/Android** 可用。macOS 無 netlink — 默以 sysinfo 代之。
>
> 📖 欲知其詳，請閱 [docs/linux_android_netlink.zh-tw.md](docs/linux_android_netlink.zh-tw.md)

## 🖼️ 一覽
#### Python 本
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust 本
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust 本 GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### 終端錄
<a href="https://asciinema.org/a/1030894?startAt=30" target="_blank"><img src="https://asciinema.org/a/1030894.svg" alt="winload demo" width="100%" /></a>

> ↑ 以 [asciinema](https://github.com/asciinema/asciinema) 錄

## 📦 所賴

### Python 本

| 包 | 版 | 說 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | 編程言語 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | 進程及系統工具 |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses 支援 |

### Rust 本

| 包 | 版 | 說 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | 編程言語 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | 終端 UI 框架 |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | 跨平臺終端庫 |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | 系統信息庫 |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | 命令列參解析器 |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | 包捕（可選，Windows） |
## 🧭 結語

夫網流無形，而 Winload 使之有象；包行於終端，聲息不驚，卻能令千端萬緒之吞吐，盡呈目前。若欲知一機之網脈，是器可為案上小燈，亦可為夜航之星。

