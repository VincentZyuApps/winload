# 建置與發佈工作流

> **[📖 English](build.md)**
> **[📖 简体中文(大陆)](build.zh-cn.md)**
> **[📖 繁體中文(台灣)](build.zh-tw.md)**

## 📋 概述

CI/CD 流程完全由 **commit 資訊中的關鍵字** 驅動。推送至 `main` 分支時，只需在 commit message 中包含對應關鍵字，GitHub Actions 就會自動完成後續作業。

## 🔑 關鍵字

| Commit 資訊中的關鍵字 | 建置（8 平台） | GitHub Release | Scoop / AUR / npm | PyPI | crates.io | 基準測試 (Benchmark) |
|----------------------|:---:|:---:|:---:|:---:|:---:|:---:|
| `build action` | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| `build release` | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| `build publish` | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| `publish from release` | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| `pypi publish` | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| `crates publish` | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| `run benchmark` | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |


> **說明:** `publish from release` 從現有的 Release 抓取二進位檔發布，不會重新建置。`build publish` 則是完整的流程。

> **說明:** Pull Request 都會觸發建置（不會發布或推送套件管理工具）。PR 中 commit message 的關鍵字會被**忽略**——工作流程會無條件設定 `should_build=true`、`should_release=false`、`should_publish=false`，並跳過關鍵字解析。

> **發佈前檢查：** 修改 Rust 套件版本或相依套件後，請從包含 `winload` 儲存庫的目錄執行以下命令，以更新並驗證 `Cargo.lock`。

```bash
cd winload/rust

cargo metadata --format-version 1 > /dev/null
cargo check --locked --no-default-features

cd ..
git status
git diff HEAD --stat
git diff HEAD -- rust/Cargo.lock
```

> **說明：** 請先檢查鎖定檔差異，確認無誤後再將 `rust/Cargo.lock` 與其他變更一起暫存、提交並推送。

## 🚀 用法範例

```bash
# ============================================================
# 單個關鍵字
# ============================================================

# 僅建置，驗證所有平台的編譯
git commit --allow-empty -m "ci: test cross-compile (build action)"

# 僅運行基準測試
git commit --allow-empty -m "test: verify performance (run benchmark)"

# 建置 + 建立 GitHub Release（不發佈至套件管理工具）
git commit -m "release: v0.2.0 (build release)"

# 僅更新 Scoop bucket（從現有的最新 Release 抓取二進位檔，不重新建置）
git commit --allow-empty -m "ci: update scoop (publish from release)"

# 僅發布至 crates.io（不建置，不發布 Release）
git commit --allow-empty -m "release: v0.2.0 (crates publish)"

# 僅發布至 PyPI（不建置，不發布 Release）
git commit --allow-empty -m "release: v0.2.0 (pypi publish)"

# 完整流程：建置 + Release + 發布至 Scoop/AUR/npm
git commit -m "release: v0.2.0 (build publish)"

# ============================================================
# 兩個關鍵字組合
# ============================================================

# 建置 + Release + Scoop/AUR/npm + crates.io
git commit --allow-empty -m "release: v0.2.0 (build publish, crates publish)"

# PyPI + crates.io（不建置，不發布 Release）
git commit --allow-empty -m "release: v0.2.0 (pypi publish, crates publish)"

# 建置 + Release + Scoop/AUR/npm + PyPI
git commit --allow-empty -m "release: v0.2.0 (build publish, pypi publish)"

# ============================================================
# 三個關鍵字組合
# ============================================================

# 完整流程：建置 + Release + Scoop/AUR/npm + PyPI + crates.io
git commit --allow-empty -m "release: v0.2.0 (build publish, pypi publish, crates publish)"

# ============================================================
# 常規 commit（不需要建置和發布）
# ============================================================

# 僅更新文件
git commit -m "docs: update README"

# 修復錯誤
git commit -m "fix: resolve network interface detection issue"

# 新增功能
git commit -m "feat: add dark mode support"
```

## 🏗️ 建置目標 (Rust)

| 平台 | 架構 | Target | 說明 |
|------|:---:|--------|------|
| Windows | x64 (MSVC, npcap) | `x86_64-pc-windows-msvc` | 含 Npcap 抓包支援，原生 MSVC 編譯，Windows 7+ |
| Windows | x64 (MSVC, no-npcap) | `x86_64-pc-windows-msvc` | 無 Npcap 獨立二進位 (`--no-default-features`)，MSVC，Windows 7+ |
| Windows | ARM64 (MSVC, npcap) | `aarch64-pc-windows-msvc` | 含 Npcap 抓包，MSVC 交叉編譯，Windows 7+（驍龍 X / Surface Pro X） |
| Windows | ARM64 (MSVC, no-npcap) | `aarch64-pc-windows-msvc` | 無 Npcap 獨立二進位 (`--no-default-features`)，MSVC，Windows 7+ |
| Linux | x64 | `x86_64-unknown-linux-musl` | 在 Ubuntu runner 上用 musl 靜態連結編譯，主要用於所有 x64 Linux 發行版（大部分雲端伺服器） |
| Linux | ARM64 | `aarch64-unknown-linux-gnu` | 在 ubuntu-22.04 上用 gcc-aarch64 交叉編譯，主要用於 ARM64 伺服器 / 單板機（樹莓派等） |
| macOS | x64 | `x86_64-apple-darwin` | 在 Apple Silicon runner 上透過 Rosetta 編譯，主要用於 Intel Mac（2020 年及更早的舊款 Mac） |
| macOS | ARM64 | `aarch64-apple-darwin` | 在 Apple Silicon runner 上原生編譯，主要用於 M 系列 Mac（2020 年底至今的所有新款 Mac） |
| Android | ARM64 | `aarch64-linux-android` | 在 Ubuntu runner 上用 NDK（API 24）交叉編譯，主要用於 Termux（ARM 手機） |
| Android | x86_64 | `x86_64-linux-android` | 在 Ubuntu runner 上用 NDK（API 24）交叉編譯，主要用於模擬器 / Chromebook |

> **說明：** Linux 目標（x64 和 ARM64）除了生成獨立二進位檔外，還會額外生成 `.deb` 和 `.rpm` 套件。

## 📦 流程階段 (Rust)

```
check ──→ build ──→ release ──→ publish
  │         │         │           │
  │         │         │           ├─ Scoop: 從 Release 下載 Win 二進位檔
  │         │         │           │  生成 winload.json → 推送至 scoop-bucket
  │         │         │           │
  │         │         │           ├─ AUR: 從 Release 下載 Linux 二進位檔
  │         │         │           │  生成 PKGBUILD & .SRCINFO → 推送至 AUR
  │         │         │           │
  │         │         │           ├─ npm: 從 Release 下載 6 個平台二進位檔
  │         │         │           │  發佈平台套件 (os/cpu 限定)
  │         │         │           │  發佈主套件 (@vincentzyuapps/winload)
  │         │         │           │  同步至 GitHub Packages (npm.pkg.github.com)
  │         │         │           │
  │         │         │           └─ Gitee: 從 GitHub Release 下載附件
  │         │         │              透過 Gitee API 建立 Release
  │         │         │              上傳附件至 Gitee
  │         │         │              然後更新 Gitee Scoop/Homebrew
  │         │         │
  │         │         └─ 下載建置產物
  │         │            刪除舊的 release/tag
  │         │            生成 release notes
  │         │            建立 GitHub Release
  │         │
  │         └─ 編譯 8 個平台目標
  │            上傳建置產物
  │
  ├─→ sync-gitee-code（與 check 並行，每次 push 觸發）
  │    透過 hub-mirror-action 鏡像所有分支/標籤至 Gitee
  │
  ├─→ benchmark（獨立運行，'run benchmark' 觸發）
  │    運行 benchmark/benchmark.sh
  │    提交並推送 docs/benchmark/benchmark.svg
  │
  ├─→ publish-crates-io（建置成功後並行，與 Scoop/AUR/npm 同時）
  │    cargo publish --locked --allow-dirty
  │
  └─→ publish-pypi（獨立運行，不需要建置）
       uv build → uv publish
```

> **說明：** Release Notes 自動生成，包含下載表格（所有平台）、快速安裝指令（pip/npm/cargo/scoop/AUR）以及來自 git commits 的變更日誌。

```mermaid
flowchart TB
    subgraph check["check"]
        C1[解析 commit 資訊]
        C2[從 Cargo.toml 擷取版本號]
    end
    
    subgraph syncCode["sync-gitee-code"]
        SC1[鏡像至 Gitee]
    end
    
    subgraph build["build"]
        B1[編譯 8 個平台]
        B2[上傳建置產物]
    end
    
    subgraph release["release"]
        R1[下載建置產物]
        R2[刪除舊 release/tag]
        R3[生成 release notes]
        R4[建立 GitHub Release]
    end

    subgraph scoop["publish-scoop"]
        S1[下載 Win 二進位檔]
        S2[生成 winload.json]
        S3[推送至 scoop-bucket]
    end

    subgraph giteePackage["publish-scoop/homebrew-gitee"]
        G1[生成 Gitee manifest/formula]
        G2[推送至 Gitee bucket/tap]
    end
    
    subgraph aur["publish-aur-bin"]
        A1[下載 Linux 二進位檔]
        A2[生成 PKGBUILD & .SRCINFO]
        A3[推送至 AUR]
    end
    
    subgraph npm["publish-npm"]
        N1[下載 6 個平台二進位檔]
        N2[發佈平台套件]
        N3[發佈主套件]
        N4[同步至 GitHub Packages]
    end
    
    subgraph syncRelease["sync-gitee-release"]
        SR1[下載 GitHub Release]
        SR2[建立 Gitee Release]
        SR3[上傳附件]
    end
    
    subgraph benchmark["benchmark"]
        BM1[運行 benchmark.sh]
        BM2[提交並推送 SVG]
    end
    
    subgraph crates["publish-crates-io"]
        CR1[cargo publish --locked --allow-dirty]
    end
    
    subgraph pypi["publish-pypi"]
        PY1[uv build]
        PY2[uv publish]
    end

    C1 --> C2
    C1 -."每次 push".-> SC1
    C2 --> B1
    C2 --"run benchmark"--> BM1
    C2 --> PY1
    BM1 --> BM2
    PY1 --> PY2
    B1 --> B2
    B2 --> R1
    B2 --> CR1
    R1 --> R2 --> R3 --> R4
    R4 --> S1
    S1 --> S2 --> S3
    R4 --> A1
    A1 --> A2 --> A3
    R4 --> N1
    N1 --> N2 --> N3 --> N4
    R4 --> SR1
    SR1 --> SR2 --> SR3
    SR3 --"build publish"--> G1
    C2 --"publish from release：使用既有 Gitee Release"--> G1
    G1 --> G2
```

## 🍨 Scoop 發佈 (Rust)

`publish` 關鍵字會觸發 [scoop-bucket](https://github.com/VincentZyuApps/scoop-bucket) 儲存庫的更新：

1. 從最新的 GitHub Release 下載 Windows x64 和 ARM64 二進位檔案
2. 計算 SHA256 雜湊值
3. 生成 `winload.json` 清單檔案（包含 `64bit` 和 `arm64` 兩種架構）
4. 推送至 `VincentZyuApps/scoop-bucket` 儲存庫

## 🐧 AUR 發佈 (Rust)

`publish` 關鍵字也會觸發 AUR 套件 [winload-rust-bin](https://aur.archlinux.org/packages/winload-rust-bin) 的更新：

1. 從最新的 GitHub Release 下載 Linux x64 和 ARM64 二進位檔案
2. 計算 SHA256 雜湊值
3. 生成 `PKGBUILD` 和 `.SRCINFO`
4. 透過 SSH 推送至 AUR

### 前置條件

需在儲存庫的 **Settings → Secrets → Actions** 中設定 `AUR_SSH_KEY` 金鑰，值為 AUR 使用者的 SSH 私密金鑰。

## 📦 npm 發佈 (Rust)

`publish` 關鍵字也會觸發將 Rust 預編譯二進位檔發佈至 npm，套件名為 [`@vincentzyuapps/winload`](https://www.npmjs.com/package/@vincentzyuapps/winload)：

1. 從最新的 GitHub Release 下載 6 個平台的二進位檔案（Win/Linux/macOS × x64/ARM64）
2. 發佈 6 個平台專屬套件，每個套件帶有 `os`/`cpu` 欄位（npm 自動選擇匹配的套件）
3. 發佈主套件 `@vincentzyuapps/winload`，透過 `optionalDependencies` 引用各平台套件
4. 所有版本（包括預發佈如 `0.1.6-beta.4`）均以 `latest` 標籤發佈
5. 同步發佈至 [GitHub Packages](https://github.com/features/packages)（`npm.pkg.github.com`）

> 採用 [esbuild](https://github.com/evanw/esbuild) / [Biome](https://github.com/biomejs/biome) 模式：每個平台一個獨立套件，`optionalDependencies` 確保只下載匹配當前平台的二進位檔。

> 舊的非 scoped 套件名 `winload-rust-bin` 已棄用。改用 `@vincentzyuapps/winload` 是為了相容 GitHub Packages 規範。

### 前置條件

需在儲存庫的 **Settings → Secrets → Actions** 中設定 `NPM_TOKEN` 金鑰，值為 npm Automation Token。

> **注意：** GitHub Packages 發佈使用 `GITHUB_TOKEN`，由 GitHub Actions 自動提供，無需額外設定金鑰。

## 🐍 PyPI 發佈 (Python)

`pypi publish` 關鍵字會觸發將 Python 套件發佈至 PyPI：

1. 透過 [astral-sh/setup-uv](https://github.com/astral-sh/setup-uv) 安裝 `uv`
2. 在 `python/` 目錄下使用 `uv build` 建置套件
3. 使用 `uv publish` 發佈至 PyPI

### 前置條件

需在儲存庫的 **Settings → Secrets → Actions** 中設定 `PYPI_TOKEN` 金鑰，值為具備 "Entire account" 權限的 PyPI API Token。

## 📦 crates.io 發佈 (Rust)

`crates publish` 關鍵字會觸發將 Rust 套件發佈至 [crates.io](https://crates.io/crates/winload)：

1. 安裝 Rust stable 工具鏈
2. 執行 `cargo publish --locked --allow-dirty` 發佈至 crates.io
3. 使用者可以透過 `cargo install winload` 安裝

### 前置條件

需在儲存庫的 **Settings → Secrets → Actions** 中設定 `CARGO_REGISTRY_TOKEN` 金鑰，值為 crates.io API Token。

> **注意：** 此任務在建置成功後與 Scoop/AUR/npm 並行運行，確保編譯產物準備好後再發佈。

## 🔄 Gitee 同步

自動將程式碼和 Release 鏡像至 [Gitee](https://gitee.com/vincent-zyu/winload)（中國大陸 GitHub 替代）。

### sync-gitee-code — 程式碼鏡像

**每次 push 時運行**（與 `check` job 並行）：
- 使用 [Yikun/hub-mirror-action](https://github.com/Yikun/hub-mirror-action) 鏡像所有分支、標籤和提交
- 自動觸發，無需關鍵字

### sync-gitee-release — Release 鏡像

**在 `release` job 成功後運行**（與 GitHub 側套件發佈並行）：
1. 下載 GitHub Release 的所有附件
2. 透過 API 在 Gitee 上建立對應的 Release
3. 上傳所有二進位附件至 Gitee Release

當 `build publish` 建立全新的 Release 時，Gitee Scoop 和 Gitee Homebrew 會等待此鏡像任務成功後，再將 manifest/formula 指向 Gitee 附件。`publish from release` 會繼續直接使用既有的 Gitee Release，不強制先運行此鏡像任務。

### 前置條件

| 金鑰 | 取得方式 | 用途 |
|------|----------|------|
| `GITEE_PRIVATE_KEY` | SSH 金鑰對（參見 [設定指南](../../docs/dev/commit和release从github同步到gitee捏.md)） | 透過 hub-mirror-action 推送程式碼 |
| `GITEE_TOKEN` | [Gitee 個人存取權杖](https://gitee.com/profile/personal_access_tokens) | 透過 API 建立 Release 和上傳附件 |

> **注意：** 詳細設定步驟請參見 [commit和release从github同步到gitee捏.md](../../docs/dev/commit和release从github同步到gitee捏.md)。

## 📌 版本號

版本號自動從 `rust/Cargo.toml` (Rust) 或 `python/pyproject.toml` (Python) 中擷取，用於：
- Release 標籤名（如 `v0.1.5`）
- 產物檔名（如 `winload-windows-x86_64-msvc-npcap-v0.1.5.exe`）
- Scoop/AUR/npm/PyPI/crates.io 清單檔案中的版本欄位

> **注意：** npm 套件的版本號同樣來自 `rust/Cargo.toml`。CI 中 `publish-npm` 任務會在發佈前將版本號動態注入 `package.json` —— 儲存庫中的 `0.0.0` 佔位符不會被發佈。

## ⚙️ 前置條件彙總

| 金鑰 | 取得方式 | 用途 |
|------|----------|------|
| `SCOOP_BUCKET_TOKEN` | GitHub PAT（需 `repo` 權限） | 推送至 Scoop bucket |
| `AUR_SSH_KEY` | AUR 使用者 SSH 私密金鑰 | 推送至 AUR |
| `NPM_TOKEN` | npm Automation Token | 發佈至 npm |
| `PYPI_TOKEN` | PyPI API Token（Scope: "Entire account"） | 推送至 PyPI |
| `CARGO_REGISTRY_TOKEN` | crates.io API Token | 發佈至 crates.io |
| `GITEE_PRIVATE_KEY` | Gitee SSH 私密金鑰 | 鏡像程式碼至 Gitee |
| `GITEE_TOKEN` | Gitee 個人存取權杖 | 建立 Gitee releases |
