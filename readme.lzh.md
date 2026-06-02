![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> 輕若飛鴻，疾若奔雷；居終端之一隅，而觀網脈之往來。其意取自 Linux 之 `nload`，而為今世諸機所用。

> **[📖 English](readme.md)**
> **[📖 简体中文(大陆)](readme.zh-cn.md)**
> **[📖 繁體中文(台灣)](readme.zh-tw.md)**
> **[📖 日本語](readme.jp.md)**
> **[📖 한국어](readme.ko.md)**
> **[📖 文言文](readme.lzh.md)**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VincentZyuApps/winload)
[![Gitee](https://img.shields.io/badge/Gitee-C71D23?style=for-the-badge&logo=gitee&logoColor=white)](https://gitee.com/vincent-zyu/winload)

[![Windows x64 | ARM64](https://img.shields.io/badge/Windows-x64_|_ARM64-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Linux x64 | ARM64](https://img.shields.io/badge/Linux-x64_|_ARM64-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/VincentZyuApps/winload/releases)
[![macOS x64 | ARM64](https://img.shields.io/badge/macOS-x64_|_ARM64-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Android x64 | ARM64](https://img.shields.io/badge/Android-x64_|_ARM64-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)

[![PyPI](https://img.shields.io/badge/PyPI-3776AB?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/winload/)
[![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/@vincentzyuapps/winload)
[![Crates.io](https://img.shields.io/badge/Crates.io-000000?style=for-the-badge&logo=rust&logoColor=white)](https://crates.io/crates/winload)

[![Scoop](https://img.shields.io/badge/Scoop-7B4AE2?style=for-the-badge&logo=scoop&logoColor=white)](https://scoop.sh/#/apps?q=%22https%3A%2F%2Fgithub.com%2FVincentZyuApps%2Fscoop-bucket%22&o=false)
[![AUR](https://img.shields.io/badge/AUR-1793D1?style=for-the-badge&logo=archlinux&logoColor=white)](https://aur.archlinux.org/packages/winload-rust-bin)
[![APT](https://img.shields.io/badge/APT-E95420?style=for-the-badge&logo=debian&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![RPM](https://img.shields.io/badge/RPM-CB1626?style=for-the-badge&logo=redhat&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Homebrew](https://img.shields.io/badge/Homebrew-FBB040?style=for-the-badge&logo=homebrew&logoColor=black)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)

> **[📖 構築之書](.github/workflows/build.zh-cn.md)**

## 🚀 序

`Winload` 者，終端中觀網流之器也。其初生於 Windows，欲補 `nload` 不能行於其上之闕；今則兼濟 Linux、macOS，亦及諸架構。其屏若素帛，其線若江河；上行下行，一覽而知。包裹之小，起勢之速，置於案頭，若佩玉在身，常用而不覺累。

## 🙏 謝

Winload 承 Roland Riegel 所作 「[nload](https://github.com/rolandriegel/nload)」 之意。前賢鑿井，後人飲水；其構想與體驗，皆為此器開山之石。

https://github.com/rolandriegel/nload

## ✨ 要義

- **雙本並行**
	- **Rust 本**：迅疾、安穩、內存無虞，且可成一靜態二進制，日常巡網最宜。
	- **Python 本**：易改易拓，若欲試新意、接旁器、作雛形，取之甚便。
- **橫行諸臺**：Windows、Linux、macOS 皆可用，x64 與 ARM64 亦俱備。
- **即時成圖**：入流出流，頃刻見其高下；吞吐之數，如觀潮汐。
- **界面清簡**：承 `nload` 舊風，不事繁飾，而所需皆在。

## 📊 功力校驗

> ⚡ Winload（Rust）可得 **約 10ms 啟動**，二進制 **小於 5MB**。較 Python 本輕捷甚多，與 C++ nload 之效亦可相頡頏。

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
> Cargo 所供者，乃 Rust 源碼，可於本地鑄成。  
> Scoop、AUR、npm、APT、RPM 及 GitHub Releases 所分發者，多為 **Rust 二進制**。

### Python (pip)

```bash
pip install winload
winload
```

若欲升之：

```bash
pip install -U winload
```

## 📥 Rust 本安置（薦）

Rust 本尤輕且疾，若但欲監看網流，宜先取之。

### npm（諸臺可用）

```bash
npm install -g @vincentzyuapps/winload
winload
```

或以 npx 一試：

```bash
npx @vincentzyuapps/winload
```

### Cargo（自源編鑄）

```bash
cargo install winload
winload
```

### Windows (Scoop)

若已備 Scoop，可引 VincentZyuApps 之桶而取：

```powershell
scoop bucket add VincentZyuApps https://github.com/VincentZyuApps/scoop-bucket
scoop install winload
winload
```

更新之：

```powershell
scoop update winload
```

### Arch Linux (AUR)

```bash
yay -S winload-rust-bin
```

或：

```bash
paru -S winload-rust-bin
```

### Linux（一令而裝）

若欲直取 Releases 中之成品，可行：

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/install_scripts/install.sh | bash
```

> 📄 [觀 GitHub 安裝腳本之源](https://github.com/VincentZyuApps/winload/blob/main/docs/install_scripts/install.sh)

若 GitHub 遲滯，亦可取 Gitee：

```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/install_scripts/install_gitee.sh | bash
```

> 📄 [觀 Gitee 安裝腳本之源](https://gitee.com/vincent-zyu/winload/blob/main/docs/install_scripts/install_gitee.sh)

### macOS / Linux（Homebrew）

```bash
brew tap VincentZyuApps/tap
brew install winload
```

更新之：

```bash
brew update
brew upgrade winload
```

### GitHub Releases

可往 Releases 擇其所需：

```text
https://github.com/VincentZyuApps/winload/releases
```

常見器類：

- Windows x64 / ARM64
- Linux x64 / ARM64
- macOS x64 / ARM64
- Android x64 / ARM64

下載既畢，賦予可行之權，置於 PATH 中，即可呼之。

## ⌨️ 用法

常用之法甚簡：

```bash
winload
```

示助：

```bash
winload --help
```

示版：

```bash
winload --version
```

### 參數

可用之參數，依版本而或有增益。大抵如下：

```bash
winload [OPTIONS]
```

常見用途：

- 選定網卡
- 調整刷新間隔
- 顯示版本
- 顯示幫助

若不知所措，行：

```bash
winload --help
```

則可見諸旗幟。

### 鍵法

於 TUI 中，可用常見按鍵操其界面。若版本支援，通常可：

- `q`：退
- `Ctrl+C`：止
- 方向鍵：移視圖或選項

具體仍以 `--help` 與當前版本之提示為準。

## 🪟 Windows 回環流量（127.0.0.1）

Windows 對回環流量之統計，與 Linux 等系統不同。若觀 `127.0.0.1` 或本機服務互通之流量，或有不顯、不全、難準之處。

相關詳說見：

- [Windows loopback docs](docs/win_loopback.md)
- [Windows 回環流量說明（簡體中文）](docs/win_loopback.zh-cn.md)
- [Windows 回環流量說明（繁體中文）](docs/win_loopback.zh-tw.md)

## 🖼️ 一覽

#### Python 本

![Python Preview](docs/images/preview-py.png)

#### Rust 本

![Rust Preview](docs/images/preview-rust.png)

![Rust Preview GIF](docs/images/preview-rust.gif)

## 📦 所賴

### Python 本

Python 本常賴下列物：

- `psutil`
- `rich`
- 其他列於 `py/requirements.txt` 者

### Rust 本

Rust 本以 Cargo 管其依賴，詳見：

```text
rust/Cargo.toml
```

## 🧭 結語

夫網流無形，而 Winload 使之有象；包行於終端，聲息不驚，卻能令千端萬緒之吞吐，盡呈目前。若欲知一機之網脈，是器可為案上小燈，亦可為夜航之星。
