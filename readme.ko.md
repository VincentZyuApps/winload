![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> Linux의 `nload`에서 영감을 받은, 네트워크 대역폭 및 트래픽을 실시간으로 모니터링하는 경량 CLI 도구입니다.

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

> **[📖 빌드 문서](.github/workflows/build.md)**

## 🚀 소개
`Winload`는 현대적인 터미널 환경에서 직관적이고 시각적인 네트워크 모니터링 기능을 제공합니다. 처음에는 Windows 환경에서 `nload`의 공백을 메우기 위한 도구로 시작되었으나, 현재는 Linux와 macOS까지 지원 범위를 확장했습니다.

## 🙏 감사의 말
Winload는 Roland Riegel의 고전적인 프로젝트인 「[nload](https://github.com/rolandriegel/nload)」에서 영감을 얻었습니다. 독창적인 아이디어와 훌륭한 사용자 경험을 제공해 준 원작자에게 깊은 감사를 표합니다.
https://github.com/rolandriegel/nload

## ✨ 주요 기능
- **두 가지 구현 방식 제공**
	- **Rust 버전**: 빠르고 메모리 안전하며, 단일 정적 바이너리로 제공되어 일상적인 모니터링에 최적화되어 있습니다.
	- **Python 버전**: 구조가 단순하여 프로토타이핑이나 기능 확장, 통합이 용이합니다.
- **교차 플랫폼 지원**: Windows, Linux, macOS (x64 및 ARM64)를 모두 지원합니다.
- **실시간 시각화**: 실시간으로 유입(Incoming) 및 유출(Outgoing) 트래픽 그래프와 처리량 통계를 보여줍니다.
- **미니멀한 UI**: `nload`의 사용성을 계승한 깔끔한 TUI(텍스트 사용자 인터페이스)를 제공합니다.

## 📊 성능 벤치마크
> ⚡ Winload (Rust)는 **~10ms의 시작 시간**과 **2MB 미만의 바이너리 크기**를 달성하여, Python 버전을 크게 능가하며 C++ nload와 대등한 효율성을 보여줍니다.

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 소스에서 실행

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# 또는 Gitee에서 클론 (중국 본토에서 더 빠름):
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv run python -m winload
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # 도움말 표시
cargo run --release -- --version # 버전 표시
```

## 🐍 Python 버전 설치
> 💡 **구현 참고사항**: PyPI 및 GitHub/Gitee 소스 코드만 Python 버전입니다.  
> Cargo만 Rust 소스 코드 로컬 빌드를 제공합니다.  
> 모든 다른 패키지 관리자(Scoop, AUR, npm, APT, RPM) 및 GitHub Releases는 **Rust 바이너리**를 제공합니다.
### Python (pip)
```bash
pip install winload
# uv 사용을 권장합니다:
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run python -c "import shutil; print(shutil.which('winload'))"
uv run winload
```

## 📥 Rust 버전 설치 (권장)
### npm (크로스 플래트폼)
```bash
# 권장（scoped）
npm install -g @vincentzyuapps/winload
# 대체（unscoped）
npm install -g winload-rust-bin
# 대체（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# Windows에서는 System32\winload.exe와의 충돌을 피하기 위해 win-nload 사용
# Linux/macOS에서는 winload 또는 win-nload 모두 사용 가능
# 또는 npx 를 직접 사용
npx @vincentzyuapps/winload
```

> 4가지 사전 컴파일된 바이너리 포함: x86_64 & ARM64, Windows·Linux·macOS 대응.

### Cargo (소스 코드 빌드)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop 이용)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# 또는 Gitee에서：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # optional: 설치 전에 수동으로 bucket 목록 업데이트
scoop install winload
# 바이너리 파일 실행
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 기존 Windows Console 대신 [Windows Terminal](https://github.com/microsoft/terminal) 사용을 권장합니다. CJK 문자 렌더링과 TUI 환경이 더 우수합니다.
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **모든 빌드는 Windows 10+가 필요합니다**（Rust 1.77+에서 Windows 7/8 지원이 중단되었습니다）。Scoop은 **x86_64** 및 **ARM64**용 **MSVC + Npcap** 빌드만 제공합니다.

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 계열 배포판 / Termux (간편 설치 스크립트)
> Debian/Ubuntu 및 파생 버전(Linux Mint, Pop!_OS, Deepin, UOS 등) 지원 (apt)

> Fedora/RHEL 및 파생 버전(Rocky Linux, AlmaLinux, CentOS Stream 등) 지원 (dnf)

> Android의 Termux (aarch64)도 지원

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [설치 스크립트 소스 보기](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Gitee 미러 (중국 본토 내 빠른 다운로드):**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [Gitee 설치 스크립트 소스 보기](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ 위의 두 `curl ... | bash` 설치 스크립트는 **x86_64 / aarch64** 아키텍처에서 **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）또는 **Termux**（Android）를 사용하는 시스템을 지원합니다. 다른 플랫폼에서는 **npm**（`npm install -g @vincentzyuapps/winload`）또는 **Cargo**（`cargo install winload`）를 사용하세요.

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> 최신 Homebrew에서는 설치 전에 서드파티 tap formula를 신뢰해야 할 수 있습니다.
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# 또는 Gitee에서（수동 탭 클론）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew는 **macOS**(Intel 및 Apple Silicon)와 **Linux**(x86_64 및 ARM64)를 지원합니다.

<details>
<summary>수동 설치</summary>

**DEB (Debian/Ubuntu):**
```bash
# GitHub Releases에서 최신 .deb 파일을 다운로드합니다.
sudo dpkg -i ./winload*.deb
# 또는 apt를 사용하여 의존성을 자동으로 해결하며 설치합니다.
sudo apt install ./winload*.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**또는 [GitHub Releases](https://github.com/VincentZyuApps/winload/releases)에서 바이너리를 직접 다운로드할 수 있습니다.**

</details>

## ⌨️ 사용법

```bash
winload              # 활성화된 모든 네트워크 인터페이스 모니터링
winload -t 200       # 새로고침 간격을 200ms로 설정
winload -d "Wi-Fi"   # 특정 장치 이름으로 시작 (부분 일치 가능)
winload --title "My Monitor" # 사용자 지정 헤더 제목 사용
winload -e           # TUI에 이모지 장식 활성화 🎉
winload --max-mode smart --max-half-life 10 # 부드러운 적응형 Y축 (기본값)
winload --max-mode legacy # nload 스타일 표시 히스토리 피크 스케일링
winload --max-mode fixed --max-y-value 10M # Y축 상한 고정
winload --graph-style line --x-axis 5s --y-axis unit # Rust: 시간축과 트래픽축을 표시하는 선 그래프
winload --npcap      # 127.0.0.1 루프백 트래픽 캡처 (Windows, Npcap 필요)
winload --netlink    # RTNETLINK 수동 활성화（Linux/Android, 기본 꺼짐）
```

### Rust 버전 추가 기능

Rust 버전은 `C`, `PageUp`, `PageDown`을 포함한 Python 버전의 모든 사용자 조작을 지원하며, 다음을 추가로 제공합니다.

- `Esc` 종료, 네 가지 그래프 스타일, 선택적 X/Y축, 실행 중 `g`/`x`/`y` 그래프 제어.
- Npcap 설치 후 Windows에서 사용할 수 있는 `--npcap` 루프백 캡처.

### 옵션 상세

| 플래그 | 설명 | 기본값 |
|------|-------------|---------|
| `-t`, `--interval <MS>` | 새로고침 간격 (밀리초 단위) | `500` |
| `-a`, `--average <SEC>` | 평균 계산을 위한 윈도우 시간 (초 단위) | `300` |
| `-d`, `--device <NAME>` | 기본 장치 이름 (부분 일치 가능) | — |
| `--title [TITLE]` | 장치 헤더 위에 제목 줄 추가. 값이 없으면 `winload <version>`을 표시하고, 빈 문자열(또는 생략)이면 기본 장치 헤더만 표시 | — |
| `-e`, `--emoji` | TUI에서 이모지 장식 활성화 🎉 | 비활성 |
| `-U`, `--unicode` | `classic` 그래프에 Unicode 블록 문자 사용 (█▓░·) | 비활성 |
| `--graph-style <STYLE>` | **[Rust 전용]** 그래프 형식: `classic`, `line`, `scatter`, `bar` | `classic` |
| `--x-axis <MODE>` | **[Rust 전용]** X축 격자: `none` 또는 `5s` 같은 양의 정수 초 간격 | `none` |
| `--y-axis <MODE>` | **[Rust 전용]** Y축 레이블과 격자: `none`, `percent`, `unit` | `none` |
| `-u`, `--unit <UNIT>` | 표시 단위: `bit` 또는 `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | 바 스타일: `fill`, `color`, 또는 `plain` | `plain` |
| `--in-color <HEX>` | 수신 그래프 색상, 16진수 RGB (예: `0x00d7ff`) | Cyan |
| `--out-color <HEX>` | 송신 그래프 색상, 16진수 RGB (예: `0xffaf00`) | Gold |
| `--max-mode <MODE>` | Y축 스케일링 모드: `smart`, `legacy`, `fixed` | `smart` |
| `--max-half-life <SECS>` | smart 모드 지수 감쇠 반감기 | `10` |
| `--max-y-value <VALUE>` | fixed 모드 Y축 상한 (예: `10M`, `1G`, `500K`) | — |
| `-n`, `--no-graph` | 그래프를 숨기고 통계만 표시 | 비활성 |
| `--hide-separator` | 구분선(등호 행) 숨기기 | 비활성 |
| `--no-color` | 모든 TUI 색상 비활성화 (흑백 모드) | 비활성 |
| `--npcap` | **[Windows Rust Only]** Npcap을 통해 루프백 트래픽 캡처 | 비활성 |
| `--netlink` | **[Linux/Android Only]** 기본 백엔드 대신 RTNETLINK 사용 (Termux proot distro 또는 제한된 환경용) | 비활성 |
| `--debug-info` | 네트워크 인터페이스 디버그 정보 출력 후 종료 | — |
| `-h`, `--help` | 도움말 출력 (`--help --emoji`로 이모지 버전 확인 가능!) | — |
| `-V`, `--version` | 버전 정보 출력 | — |

> **Y축 스케일링 모드** — 다음 세 가지 시나리오는 상호 배타적입니다:
>
> | 모드 | 플래그 | 동작 |
> |------|--------|------|
> | **smart** | `--max-mode smart --max-half-life 10` | 기본값. 트래픽 급증 시 상승한 뒤 부드럽게 지수 감쇠합니다. |
> | **legacy** | `--max-mode legacy` | nload 스타일로 표시 중인 그래프 히스토리 피크에 따라 자동 스케일링합니다. |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Y축을 지정한 값으로 고정합니다. |
>
> `--max-y-value`는 `--max-mode fixed`에서만, `--max-half-life`는 `--max-mode smart`에서만 사용할 수 있습니다.

### 키보드 단축키

| 키 | 동작 |
|-----|--------|
| `←` / `↑` | 이전 네트워크 장치로 전환 |
| `→` / `↓` | 다음 네트워크 장치로 전환 |
| `Tab` / `Enter` | 다음 네트워크 장치로 전환 |
| `PageUp` / `PageDown` | 이전/다음 네트워크 장치로 전환 |
| `F3` | 디버그 정보 오버레이 전환 (Minecraft 스타일) |
| `=` | 구분선 표시 여부 전환 |
| `c` | 색상 모드 켜기/끄기 전환 |
| `C` | 색상 모드 켜기/끄기 전환 |
| `g` / `G` | **[Rust 전용]** `classic` → `line` → `scatter` → `bar` 순환 |
| `x` / `X` | **[Rust 전용]** 시간축 전환. 간격을 지정하지 않았으면 `5s` 사용 |
| `y` / `Y` | **[Rust 전용]** Y축을 `none` → `percent` → `unit` 순으로 전환 |
| `q` / `Q` 또는 `Ctrl+C` | 프로그램 종료 |
| `Esc` | **[Rust 전용]** 프로그램 종료 |

> **구현 참고:** Rust는 `Esc`와 `g`/`x`/`y` 그래프 제어를 추가로 제공합니다. Rust의 기본 그래프 형식은 계속 `classic`이며 실행 중 변경은 현재 세션에만 적용됩니다. 네 가지 Rust 그래프 형식은 동일한 X/Y 격자와 스케일링 영역을 공유합니다. `--unicode`는 `classic`에만 적용되고 Ratatui 형식은 각각의 기본 마커를 사용합니다.

## 🪟 Windows 루프백 (127.0.0.1) 안내

Windows는 표준 API를 통해 루프백 트래픽을 보고하지 못하는 구조적 한계가 있습니다. 이는 [Windows 네트워크 스택의 기능적 결함](docs/win_loopback.md)에 기인합니다.

**Windows에서 루프백 트래픽을 모니터링하려면**, `--npcap` 플래그를 사용하십시오:

```bash
winload --npcap
```

이 기능을 사용하려면 [Npcap](https://npcap.com/#download)이 설치되어 있어야 하며, 설치 과정에서 "Support loopback traffic capture" 옵션이 활성화되어 있어야 합니다.

> 이전에는 Windows 자체의 `GetIfEntry` API를 직접 폴링하는 방식을 시도했으나, 루프백 인터페이스의 카운터는 항상 0으로 나타났습니다. 루프백 가상 인터페이스 뒤에는 데이터를 집계할 NDIS 드라이버가 존재하지 않기 때문입니다. 따라서 해당 코드 경로는 현재 제거되었습니다.

> 📖 Windows 루프백 문제에 대한 기술적인 상세 내용은 [docs/win_loopback.md](docs/win_loopback.md)를 참조하십시오.

## 🐧 Linux / Android / Termux Netlink

Linux 및 macOS에서는 별도의 설정 없이 루프백 트래픽 모니터링이 기본적으로 작동합니다.

**Linux/Android**에서 `/proc/net/dev`에 접근할 수 없는 경우（Termux proot distro 또는 기타 제한된 환경 등），`--netlink`를 사용하여 RTNETLINK를 통해 네트워크 통계를 직접 수집할 수 있습니다：

```bash
winload --netlink
```

> 참고：`--netlink`는 `--npcap`처럼 **수동으로 켜는 선택적 백엔드**이며, 플래그를 지정하지 않으면 활성화되지 않습니다. 일반 Linux/Android 실행은 기본 백엔드(Rust: sysinfo, Python: psutil)를 사용합니다. Python 에디션은 Linux/Android에서 `pyroute2`로 RTNETLINK를 사용합니다. macOS에서는 netlink를 사용할 수 없습니다.
>
> 📖 Linux/Android 네트워크 통계 수집 원리에 대한 자세한 내용은 [docs/linux_android_netlink.md](docs/linux_android_netlink.md)를 참조하십시오

## 🖼️ 미리보기
#### Python 버전 미리보기
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust 버전 미리보기
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust 버전 미리보기 GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### 터미널 녹화
[![asciicast](https://asciinema.org/a/1030894.svg)](https://asciinema.org/a/1030894?t=30)

> ↑ [asciinema](https://github.com/asciinema/asciinema) 로 녹화

## 📦 의존성

### Python 버전

| 패키지 | 버전 | 설명 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | 프로그래밍 언어 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | 프로세스 및 시스템 유틸리티 |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | Linux/Android RTNETLINK 백엔드 |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses 지원 |

### Rust 버전

| 패키지 | 버전 | 설명 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | 프로그래밍 언어 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | 터미널 UI 프레임워크 |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | 크로스 플랫폼 터미널 라이브러리 |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | 시스템 정보 라이브러리 |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | 명령줄 인자 파서 |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | 패킷 캡처 (선택 사항, Windows) |
## 🧭 맺음말

네트워크 트래픽은 무형으로 흐르고, 소리 없이 스쳐갑니다. 그러나 Winload는 그것에 형체를 부여하여, 터미널 위에서 수많은 패킷의 춤을 생생히 펼쳐 보입니다. 한 대의 기계가 숨 쉬는 그물의 맥박을 알고자 할 때, 이 도구는 책상 위의 작은 등불이 되어 주고, 밤바다를 항해하는 이에게 별이 되어 줍니다.

## 🧱 소스 구조

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

