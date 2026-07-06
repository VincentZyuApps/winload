![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> 輕量級實時終端網路流量監控工具，靈感來自 Linux 的 nload。

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

> **[📖 建置文檔](.github/workflows/build.zh-tw.md)**

## 🚀 簡介
`Winload` 是一個直觀的終端網路流量監控工具。最初為 Windows 打造，彌補 `nload` 在 Windows 上的空白，現已支援 Linux 和 macOS。

## 🙏 致謝
Winload 的靈感來自 Roland Riegel 的經典 「[nload](https://github.com/rolandriegel/nload)」 項目，感謝原作者的創意與體驗。
https://github.com/rolandriegel/nload

## ✨ 主要特性
- **雙實現版本**
	- **Rust 版**: 快速、內存安全、單靜態二進製文件，適合日常監控。
	- **Python 版**: 易於修改和擴展，適合原型開發或集成。
- **跨平台**: Windows、Linux、macOS（x64 & ARM64）。
- **實時可視化**: 實時上行/下行流量圖和吞吐量統計。
- **簡潔界面**: 乾淨的 TUI，沿襲 nload 的人體工程學設計。

## 📊 效能基準測試
> ⚡ Winload (Rust) 實現 **~10ms 啟動速度** 和 **<2MB 二進位檔案體積**，在效率上顯著優於 Python 並與 C++ nload 相當。

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 從原始碼執行

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# 或從 Gitee 克隆（中國大陸更快）：
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv venv --python 3.13
uv pip install -r requirements.txt
uv run python main.py
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # 顯示說明
cargo run --release -- --version # 顯示版本
```

## 🐍 Python 版本安裝
> 💡 **實作說明**：僅 PyPI 和 GitHub/Gitee 源代碼是 Python 版本。  
> 僅 Cargo 提供 Rust 原始碼供本地編譯。  
> 所有其他套件管理器（Scoop、AUR、npm、APT、RPM）及 GitHub Releases 均提供 **Rust 二進制文件**。
### Python (pip)
```bash
pip install winload
# 推薦使用 uv：
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run winload
uv run python -c "import shutil; print(shutil.which('winload'))"
```

## 📥 Rust 版本安裝（推薦）
### npm (跨平台)
```bash
# 推薦（scoped）
npm install -g @vincentzyuapps/winload
# 備選（unscoped）
npm install -g winload-rust-bin
# 備選（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# 在 Windows 上使用 win-nload 以避免與 System32\winload.exe 衝突
# 在 Linux/macOS 上，winload 和 win-nload 均可使用
# 或直接使用 npx
npx @vincentzyuapps/winload
```

> 包含 4 個預編譯二進制文件：x86_64 & ARM64 版本，支援 Windows、Linux 和 macOS。

### Cargo (原始碼編譯)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# 或從 Gitee 克隆：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # optional: 提前手動更新 bucket 列表
scoop install winload
# 執行二進位檔案
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 建議使用 [Windows Terminal](https://github.com/microsoft/terminal) 而非舊版 Windows Console，以獲得正確的中文字元渲染和更好的 TUI 體驗。
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **所有構建均需 Windows 10+**（Rust 1.77+ 已放棄支援 Windows 7/8）。Scoop 和 npm 預設提供 **x86_64** 和 **ARM64** 的 **MSVC + Npcap** 構建。這些構建現在會延遲載入 `wpcap.dll`，可降低尚未使用 `--npcap` 前的啟動失敗風險，但回環擷取仍然需要系統已安裝 Npcap。

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 系發行版 / Termux（一鍵安裝指令稿）
> 支援 Debian/Ubuntu 及其衍生版 —— Linux Mint、Pop!_OS、Deepin、UnionTech OS 等 (apt)

> 支援 Fedora/RHEL 及其衍生版 —— Rocky Linux、AlmaLinux、CentOS Stream 等 (dnf)

> 也支援 Android 上的 Termux (aarch64)

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [查看安裝指令稿原始碼](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Gitee 鏡像（大陸地區下載更快）：**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [查看 Gitee 安裝指令稿原始碼](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ 以上兩個 `curl ... | bash` 安裝指令稿支援 **x86_64 / aarch64** 架構上使用 **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）或 **Termux**（Android）的系統。其他平台請使用 **npm**（`npm install -g @vincentzyuapps/winload`）或 **Cargo**（`cargo install winload`）安裝。

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> 較新的 Homebrew 可能要求先信任第三方 tap 的 formula 後再安裝。
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# 或從 Gitee（手動克隆 tap）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew 支援 **macOS**（Intel 和 Apple Silicon）和 **Linux**（x86_64 和 ARM64）。

<details>
<summary>手動安裝</summary>

**DEB (Debian/Ubuntu):**
```bash
# 從 GitHub Releases 下載最新 .deb 包
sudo dpkg -i ./winload*.deb
# 或使用 apt（自動處理依賴）
sudo apt install ./winload*.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**或者直接從 [GitHub Releases](https://github.com/VincentZyuApps/winload/releases) 下載二進制文件。**

</details>

## ⌨️ 用法

```bash
winload              # 監控所有活躍網路藉口
winload -t 200       # 設定刷新間隔為 200ms
winload -d "Wi-Fi"   # 啟動時定位到 Wi-Fi 網卡
winload --title "我的監視器" # 使用自訂頂部標題
winload -e           # 啟用 emoji 裝飾 🎉
winload --max-mode smart --max-half-life 10 # 平滑自適應 Y 軸（預設）
winload --max-mode legacy # nload 風格的可見歷史峰值縮放
winload --max-mode fixed --max-y-value 10M # 固定 Y 軸上限
winload --npcap      # 擷取 127.0.0.1 回環流量 (Windows，需安裝 Npcap)
winload --netlink    # 手動啟用 RTNETLINK（Linux/Android，預設關閉）
```

### 參數選項

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `-t`, `--interval <MS>` | 刷新間隔（毫秒） | `500` |
| `-a`, `--average <SEC>` | 平均值計算視窗（秒） | `300` |
| `-d`, `--device <NAME>` | 預設裝置名稱（模糊比對） | — |
| `--title [TITLE]` | 在裝置標題上方新增標題行：不帶值時顯示 `winload <版本號>`；空字串（或省略）時僅顯示預設裝置標題 | — |
| `-e`, `--emoji` | 啟用 emoji 裝飾 🎉 | 關閉 |
| `-U`, `--unicode` | 使用 Unicode 方塊字元繪圖（█▓░·） | 關閉 |
| `-u`, `--unit <UNIT>` | 顯示單位：`bit` 或 `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | 狀態列樣式：`fill`、`color` 或 `plain` | `fill` |
| `--in-color <HEX>` | 下行圖形顏色，十六進位 RGB（如 `0x00d7ff`） | 青色 |
| `--out-color <HEX>` | 上行圖形顏色，十六進位 RGB（如 `0xffaf00`） | 金色 |
| `--max-mode <MODE>` | Y 軸縮放模式：`smart`、`legacy` 或 `fixed` | `smart` |
| `--max-half-life <SECS>` | smart 模式指數衰減半衰期 | `10` |
| `--max-y-value <VALUE>` | fixed 模式固定 Y 軸上限（如 `10M`、`1G`、`500K`） | — |
| `-n`, `--no-graph` | 隱藏圖形，僅顯示統計資訊 | 關閉 |
| `--hide-separator` | 隱藏分隔線（等號一行） | 關閉 |
| `--no-color` | 停用所有 TUI 顏色（單色模式） | 關閉 |
| `--npcap` | **[Windows Rust Only]** 透過 Npcap 擷取回環流量（建議） | 關閉 |
| `--netlink` | **[Linux/Android Only]** 使用 RTNETLINK 替代預設後端（在 Termux proot distro 或受限環境中適用） | 關閉 |
| `--debug-info` | 列印網路介面除錯資訊後退出 | — |
| `-h`, `--help` | 列印說明（`--help --emoji` 可查看 emoji 版！） | — |
| `-V`, `--version` | 列印版本號 | — |

> **Y 軸縮放模式**
>
> | 模式 | 參數 | 行為 |
> |------|------|------|
> | **smart** | `--max-mode smart --max-half-life 10` | 預設。流量突增時立即跳升，隨後平滑指數回落。 |
> | **legacy** | `--max-mode legacy` | nload 風格，按目前可見圖形視窗峰值自動縮放。 |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Y 軸鎖定為指定值。 |
>
> `--max-y-value` 僅可用於 `--max-mode fixed`；`--max-half-life` 僅可用於 `--max-mode smart`。

### 快捷鍵

| 按鍵 | 功能 |
|------|------|
| `←` / `→` 或 `↑` / `↓` | 切換網路裝置 |
| `F3` | 切換除錯資訊介面（Minecraft 風格） |
| `=` | 切換分割線的顯示/隱藏 |
| `c` | 切換顏色開/關 |
| `q` / `Esc` | 退出 |

## 🪟 Windows 回環流量 (127.0.0.1)

Windows 無法透過標準 API 回報回環流量——這是 [Windows 網路堆疊的功能缺失](docs/win_loopback.zh-tw.md)。

**要在 Windows 上擷取回環流量**，使用 `--npcap` 參數：

```bash
winload --npcap
```

需要安裝 [Npcap](https://npcap.com/#download)，安裝時勾選 "Support loopback traffic capture"。

> 我之前嘗試過直接輪詢 Windows 自帶的 `GetIfEntry` API，但 loopback 的計數器始終為 0——loopback 虛擬介面背後根本沒有 NDIS 驅動程式在計數。該程式碼路徑已被移除。

> 📖 深入了解 Windows 回環為何失效，請閱讀 [docs/win_loopback.zh-tw.md](docs/win_loopback.zh-tw.md)

## 🐧 Linux / Android / Termux Netlink

在 Linux 和 macOS 上，回環流量開箱即用，無需額外參數。

在 **Linux/Android** 上，如果無法存取 `/proc/net/dev`（例如在 Termux proot distro 或其他受限環境中），可使用 `--netlink` 透過 RTNETLINK 直接收集網路統計資訊：

```bash
winload --netlink
```

> 注意：`--netlink` 和 `--npcap` 一樣是**手動啟用的可選後端**，預設不會啟用；一般 Linux/Android 仍使用預設後端（Rust：sysinfo，Python：psutil）。Python 版在 Linux/Android 上透過 `pyroute2` 使用 RTNETLINK。macOS 不支援 netlink。
>
> 📖 深入了解 Linux/Android 網路統計採集原理，請閱讀 [docs/linux_android_netlink.zh-tw.md](docs/linux_android_netlink.zh-tw.md)

## 🖼️ 預覽
#### Python 版預覽
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust 版預覽
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust 版預覽 GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### 終端錄製
<a href="https://asciinema.org/a/1030894?startAt=30" target="_blank"><img src="https://asciinema.org/a/1030894.svg" alt="winload demo" width="100%" /></a>

> ↑ 使用 [asciinema](https://github.com/asciinema/asciinema) 錄製

## 📦 依賴

### Python 版本

| 套件 | 版本 | 說明 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | 編程語言 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | 進程和系統工具 |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | Linux/Android 上的 RTNETLINK 後端 |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses 支援 |

### Rust 版本

| 套件 | 版本 | 說明 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | 編程語言 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | 終端 UI 框架 |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | 跨平台終端庫 |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | 系統信息庫 |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | 命令行參數解析器 |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | 數據包捕獲（可選，Windows） |
## 🧭 結語

網路流量本是無形無影之物，而 Winload 卻能讓它具象於眼前。資料包在終端中穿行，無聲無息，卻能將千絲萬縷的吞吐之狀盡數呈現。若你想讀懂一台機器的網路脈搏，此工具既可作案頭的一盞小燈，也可作夜航時的一顆星。

