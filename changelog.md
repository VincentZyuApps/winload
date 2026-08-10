# Changelog 📜✨

All notable changes to **winload** are collected here.

This changelog is written in English and summarizes the project history from the Git tag timeline, release commits, and working-tree diffs.

The `v0.1.12` series is reconstructed from the release commits `03d80cc` through `be4afee`. The local tag timeline currently ends at `v0.1.11`, so the `v0.1.12` release commits are used as the authoritative source for dates and contents.

The project ships two implementations:

- 🦀 Rust edition: the primary packaged binary for most package managers.
- 🐍 Python edition: the PyPI/source-friendly implementation.
- 🪟 Windows support includes Npcap-assisted loopback capture in the Rust edition.
- 🐧 Linux and Android support include an opt-in Netlink path.
- 🍎 macOS support uses the default platform network counters.
- 📦 Distribution spans GitHub Releases, Gitee mirrors, PyPI, crates.io, npm, Scoop, AUR, Homebrew, DEB, RPM, and install scripts.

## Version Index 🧭

- [v0.2.0-alpha.4](#v020-alpha4---unreleased-) 🧪
- [v0.2.0-alpha.3](#v020-alpha3---2026-08-10-) 🧩
- [v0.1.12](#v0112---2026-08-09-) ✅
- [v0.1.12-rc.5](#v0112-rc5---2026-07-12-) 🧱
- [v0.1.12-rc.4](#v0112-rc4---2026-07-11-) 🔒
- [v0.1.12-rc.3](#v0112-rc3---2026-07-11-) 🧾
- [v0.1.12-rc.2](#v0112-rc2---2026-07-10-) 🚀
- [v0.1.12-rc.1](#v0112-rc1---2026-07-09-) 🇨🇳
- [v0.1.12-beta.2](#v0112-beta2---2026-07-09-) 🎨
- [v0.1.12-beta.1](#v0112-beta1---2026-07-09-) ✨
- [v0.1.11](#v0111---2026-06-29-) 🐍
- [v0.1.10-beta.1](#v0110-beta1---2026-06-29-) 📈
- [v0.1.9](#v019---2026-06-29-) 🔗
- [v0.1.8](#v018---2026-05-23-) 🖥️
- [v0.1.7](#v017---2026-03-08-) 🚢
- [v0.1.6-beta](#v016-beta-series---2026-02-16-to-2026-02-24-) 📦
- [v0.1.5-beta](#v015-beta-series---2026-02-16-) 🪣
- [v0.1.4-beta.1](#v014-beta1---2026-02-13-) 🎛️
- [v0.1.1-beta.1](#v011-beta1---2026-02-10-) 🛠️
- [v0.1.0](#v010---2026-02-09-) 🌱
- [Initial Development](#initial-development---2026-02-08-to-2026-02-09-) 🧪

## [v0.2.0-alpha.4] - Unreleased 🧪

### Release Focus 🎯

- 🐧 Repairs AUR publishing by replacing the malformed Arch Linux container digest with a verified immutable OCI index digest.
- 🔁 Adds the independent `aur-publish` trigger for retrying only the AUR package from an existing GitHub Release.
- 📦 Keeps `build-publish` and `publish-from-release` connected to AUR so full package-manager publishing remains unchanged.
- 🔖 Synchronizes the Python package, Rust crate, Cargo lockfile, and version tests at `0.2.0-alpha.4`.

### CI and Documentation 🛠️

- 🧮 Replaces the invalid 65-character SHA256 value with the verified 64-character `archlinux:latest` OCI index digest.
- 🧱 Replaces the ambiguous package-manager flag with independent Scoop, Homebrew, AUR, npm, PyPI, and crates.io outputs.
- 🔒 Preserves the Release success/skipped gate, preventing AUR publication when a requested GitHub Release fails.
- 🏷️ Marks only alpha versions as GitHub/Gitee prereleases and publishes their npm packages with the `alpha` dist-tag; beta, RC, and stable versions remain regular/latest releases.
- 🦀 Lets `crates-publish` run independently instead of waiting for an unrelated multi-platform build job.
- 📚 Documents the six release targets, trigger fan-out, and alpha-channel policy consistently across all three workflow guides.

## [v0.2.0-alpha.3] - 2026-08-10 🧩

### Release Focus 🎯

- 🧪 Opens the `v0.2.0` development line with the Python and Rust package versions synchronized at `0.2.0-alpha.3`.
- 🧭 Refactors both implementations toward a symmetric module layout while preserving their public command entry points.
- 🦀 Expands the Rust TUI with multiple graph styles and optional time/traffic axes.
- 📚 Adds generated source-layout sections to all six project READMEs.

### Symmetric Architecture 🧩

- 🧱 Breaks the oversized Python and Rust entry points into matching configuration, CLI, application-state, runtime, and diagnostics responsibilities.
- 🌐 Moves translations and UI rendering into parallel module directories, while retaining deliberate platform-specific differences such as Rust Npcap loopback capture.
- 🔒 Keeps application state independent from rendering to avoid circular dependencies and make runtime behavior easier to test.

### Rust Graphs and Axes 📈

- 📊 Adds Rust-only `classic`, `line`, `scatter`, and `bar` graph styles, with `classic` remaining the default.
- 🕒 Adds an optional X-axis based on seconds before the current sample and a Y-axis with `none`, `percent`, and traffic-unit modes.
- ⌨️ Adds `g`, `x`, and `y` runtime controls; an unconfigured X-axis falls back to a `5s` interval when toggled on.
- 🧮 Shares the same grid, viewport, history order, and Y-axis scaling rules across all four graph styles.
- 🔣 Limits `--unicode` to the classic character graph, leaving Ratatui styles to use their native markers.

### Documentation and Tooling 🛠️

- 🌳 Adds a standard-library README source-tree generator with localized end-of-file sections, deterministic ordering, source roles, and physical line counts.
- ✅ Adds `-d`, `--dry-run`, and `--dryrun` validation aliases plus CI enforcement for stale sections and malformed markers.
- 📏 Warns when a source file exceeds 400 lines and rejects files over the 500-line hard limit.
- ⌨️ Adds localized keyboard-shortcut sections to both CLI help screens and synchronizes all six READMEs with shared, Python-only, and Rust-only controls.

## [v0.1.12] - 2026-08-09 ✅

### Release Focus 🎯

- ✅ Promotes both the Python and Rust editions from `0.1.12-rc.5` to the stable `0.1.12` release.
- 🔧 Fixes Python runtime configuration propagation so the requested refresh interval and averaging window actually control traffic statistics.
- 🧭 Replaces space-separated CI trigger phrases with explicit hyphenated tokens and hardens their matching boundaries.
- 🔐 Reduces GitHub Actions permissions and pins third-party build dependencies for a more reproducible release pipeline.
- 📦 Requests the complete `build-publish`, `pypi-publish`, and `crates-publish` release path.

### Runtime Correctness 🐍

- 🔗 Changes Python Netlink imports to package-relative imports so installed wheels can load the backend correctly.
- ⏱️ Passes `interval` and `average` from the Python CLI through the UI layer into `StatisticsEngine`.
- 📈 Ensures both the refresh cadence and rolling average window follow the values selected by the user.
- ✅ Rejects non-positive Python `--interval` and `--average` values before entering the TUI.
- 🦀 Adds equivalent zero-value validation to the Rust CLI so both editions enforce the same basic timing constraints.

### CI Trigger Contract 🧭

- 🔑 Standardizes the supported tokens as `build-action`, `build-release`, `build-publish`, `publish-from-release`, `pypi-publish`, `crates-publish`, and `run-benchmark`.
- 🧱 Requires independent token boundaries so prefixes, suffixes, and similar prose do not accidentally start build or publishing jobs.
- 🔤 Keeps trigger matching case-insensitive while rejecting embedded lookalike strings.
- 📚 Synchronizes the trigger tables, command examples, ASCII flows, and Mermaid diagrams across the English, Simplified Chinese, and Traditional Chinese workflow guides.
- 📝 Updates the changelog, Gitee synchronization notes, and Rust binary publishing notes to use the new trigger spellings.

### CI Supply-Chain Hardening 🔐

- 🛡️ Removes workflow-wide write permissions and grants write access only to jobs that create releases or update external package metadata.
- 📌 Pins checkout, Rust toolchain/cache, artifact, Node.js, uv, and Gitee mirroring actions to immutable commit SHAs.
- 🧮 Verifies the downloaded Npcap SDK against a fixed SHA256 checksum before Windows builds consume it.
- 📦 Pins `cargo-deb` and `cargo-generate-rpm` versions to make Linux package generation repeatable.
- 🐧 Pins the Arch Linux publishing container to an immutable image digest instead of a floating `latest` tag.

### Verification and Release Metadata 🧪

- 🔒 Synchronizes `python/pyproject.toml`, `rust/Cargo.toml`, and the `winload` entry in `rust/Cargo.lock` at `0.1.12`.
- ✅ Verifies `cargo metadata` lockfile synchronization and `cargo check --locked --no-default-features` under WSL Debian.
- ✅ Exercises valid trigger tokens, case-insensitive matching, and rejection of prefix/suffix false positives.
- 📝 Adds an automated-testing plan and CI supply-chain review notes for subsequent hardening work.

### Commit Reference 🔎

- 🔖 Commit: `be4afee`
- 📅 Date: 2026-08-09
- 🧾 Subject: `release: 准备 v0.1.12 并修复参数传递与加固 CI 供应链`
- 📦 Version change: `0.1.12-rc.5` -> `0.1.12`
- 🚢 Pipeline intent: `build-publish`, `pypi-publish`, `crates-publish`

## [v0.1.12-rc.5] - 2026-07-12 🧱

### Release Focus 🎯

- 🧱 Aligns the Python and Rust build-information layouts before the stable release.
- 📦 Bumps both editions and the Rust lockfile from `0.1.12-rc.4` to `0.1.12-rc.5`.
- 🔒 Keeps packaged builds tied to the checked-in lockfile.

### Symmetric Build Metadata 🧾

- 🐍 Consolidates the Python build metadata implementation into `python/_build_info.py`.
- 🦀 Renames the Rust build script from `rust/build.rs` to `rust/_build_info.rs` and declares it explicitly in `Cargo.toml`.
- 🪞 Establishes the symmetric project-root pair `python/_build_info.py` and `rust/_build_info.rs`.
- 📦 Uses Hatchling `force-include` to install the Python metadata file as `winload/_build_info.py` inside wheels.
- 🔍 Makes Python prefer installed build metadata while retaining source-tree Git hash, commit time, and dirty-state fallback behavior.
- ⚙️ Updates CI to inject the triggering commit hash and time into the new Python metadata location.
- 🎯 Preserves Rust `TARGET` injection and the Windows MSVC Npcap delay-load linker configuration.

### Local Build Tooling 🛠️

- 📂 Moves the local Rust release helper from `rust/build.py` to `scripts/build_rust_bin.py`.
- 🧭 Updates project-root discovery so the relocated script can still find the Rust crate.
- 🔒 Adds `--locked` to local Rust release builds and updates the related build and publishing documentation.
- ✅ Verifies Python source, editable, wheel, and sdist metadata fallbacks plus Rust check, run, and package flows.

### Commit Reference 🔎

- 🔖 Commit: `a361241`
- 📅 Date: 2026-07-12
- 🧾 Subject: `release: 准备 v0.1.12-rc.5 并对齐构建信息文件结构`
- 📦 Version change: `0.1.12-rc.4` -> `0.1.12-rc.5`
- 🚢 Pipeline intent: `build-publish`, `pypi-publish`, `crates-publish`

## [v0.1.12-rc.4] - 2026-07-11 🔒

### Release Focus 🎯

- 🔒 Makes Cargo lockfile consistency a release requirement.
- 📦 Bumps both editions from `0.1.12-rc.3` to `0.1.12-rc.4` and repairs the stale `winload` lockfile version.
- 🧾 Simplifies Rust build metadata by removing local dirty-state injection from compiled binaries.

### Locked Rust Builds 📦

- 🔐 Adds `--locked` to every multi-platform Rust release build.
- 🚢 Adds `--locked` to `cargo publish` while retaining `--allow-dirty` for generated release documentation.
- 🧪 Documents the pre-release `cargo metadata`, `cargo check --locked`, `git status`, and lockfile-diff checks.
- 🌐 Keeps the English, Simplified Chinese, and Traditional Chinese workflow documentation structurally synchronized.

### Build Metadata and Planning 🧭

- 🧹 Removes `WINLOAD_GIT_DIRTY`, `.git/index` rebuild tracking, and build-time `git status --porcelain` checks from Rust.
- 🧾 Retains the seven-character commit hash, commit time, and target information in Rust `--version` output.
- 🐍 Leaves Python source-tree dirty detection unchanged.
- 🧩 Adds the initial Python/Rust module-splitting plan for `main`, `ui`, and `i18n` without performing the migration in this release.

### Commit Reference 🔎

- 🔖 Commit: `4e4b17e`
- 📅 Date: 2026-07-11
- 🧾 Subject: `release: 准备 v0.1.12-rc.4 并完善 Rust 锁文件与版本信息`
- 📦 Version change: `0.1.12-rc.3` -> `0.1.12-rc.4`
- 🚢 Pipeline intent: `build-publish`, `pypi-publish`, `crates-publish`

## [v0.1.12-rc.3] - 2026-07-11 🧾

### Release Focus 🎯

- 🧾 Adds reproducible build and source metadata to both editions' version output.
- 📦 Bumps Python and Rust from `0.1.12-rc.2` to `0.1.12-rc.3`.
- 📚 Introduces this changelog and records the earlier release history.

### Build and Version Information 🔎

- 🦀 Adds the short commit hash and commit time to Rust `--version`, injected by the Rust build script.
- 🐍 Adds commit hash, commit time, system, and architecture to Python `--version`.
- 🔍 Makes Python source runs prefer live Git metadata when a checkout is available.
- 📦 Adds generated Python metadata fallback so PyPI wheels and sdists retain release commit information without a `.git` directory.
- ⚙️ Generates Python build metadata in CI before the PyPI package is built.
- 🧹 Marks local Python source output dirty when Git reports staged, unstaged, or untracked changes.

### Documentation and Source Metadata 📚

- 🏷️ Changes the six README GitHub and Gitee badges to two-color platform/gray designs.
- 📝 Adds concise English responsibility comments to Python and Rust source files.
- 🎨 Keeps Rust `--version` emphasis on the first line while rendering commit and system details as normal text.

### Commit Reference 🔎

- 🔖 Commit: `0438ff4`
- 📅 Date: 2026-07-11
- 🧾 Subject: `release: 准备 v0.1.12-rc.3 并补充构建元数据与文档徽章`
- 📦 Version change: `0.1.12-rc.2` -> `0.1.12-rc.3`
- 🚢 Pipeline intent: `build-publish`, `pypi-publish`, `crates-publish`

## [v0.1.12-rc.2] - 2026-07-10 🚀

### Release Focus 🎯

- 🚀 Prepares `v0.1.12-rc.2` for the full build/publish pipeline.
- 🐍 Completes the Python help-output alignment work started in the earlier `v0.1.12` pre-releases.
- 🦀 Keeps Rust and Python package versions synchronized at `0.1.12-rc.2`.
- 🧾 Makes Python CLI help look much closer to the Rust/clap output.
- ✨ Keeps optional emoji decoration available in help output without forcing emojis into plain mode.
- 🌐 Improves help text consistency across `en-us`, `zh-cn`, and `zh-tw`.
- 📚 Updates README examples so the `uv` flow verifies the installed command before running it.
- 📦 Continues the `build-publish, pypi-publish, crates-publish` release path.

### Python CLI Help 🐍

- 🧾 Added a custom `WinloadArgumentParser`.
- 🧭 The custom parser renders help in a more Rust/clap-like order.
- 🧭 Help output now follows description, `Usage`, then `Options`.
- 🧩 The Python parser keeps the program name as `winload`.
- 🧩 Usage now prints as `winload [OPTIONS]`.
- 🧩 Option sections are normalized to `Options`.
- 🏷️ Argument metavars were adjusted to match the Rust CLI more closely.
- 🏷️ `--title-align` now uses `TITLE_ALIGN`.
- 🏷️ `--bar-style` now uses `BAR_STYLE`.
- 🏷️ `--max-mode` now uses `MAX_MODE`.
- 🏷️ `--max-half-life` now uses `SECS`.
- 🏷️ `--max-y-value` now uses `VALUE`.
- 🧾 `--help` and `--version` positions were aligned with the Rust command.
- 🔍 The help system avoids importing TUI-only runtime pieces just to print help.
- 🧪 `--version` prints `winload <version> (Python edition)`.
- 🧼 Emoji decoration was removed from Python `--version` help text to better match Rust's built-in line style.
- 🌐 Help epilog includes localized system information.
- 🖥️ System information includes platform and architecture.
- 🧭 Python help now pre-scans `--lang` before building localized help text.
- ✨ Python help now pre-scans `--emoji` before adding emoji decorations.
- ✅ Invalid `--netlink` use is still rejected outside Linux/Android.
- ✅ `--max-mode fixed` still requires `--max-y-value`.
- ✅ `--max-y-value` remains restricted to fixed mode.
- ✅ `--max-half-life` remains restricted to smart mode.

### Python i18n 🌐

- 🌐 Expanded `en-us` help text for value-heavy options.
- 🌐 Expanded `zh-cn` help text for value-heavy options.
- 🌐 Expanded `zh-tw` help text for value-heavy options.
- 🧾 Added `Possible values` blocks to Python help for `title-align`.
- 🧾 Added `Possible values` blocks to Python help for `unit`.
- 🧾 Added `Possible values` blocks to Python help for `bar-style`.
- 🧾 Added `Possible values` blocks to Python help for `max-mode`.
- 🧾 Added `Possible values` blocks to Python help for `lang`.
- ⚫ Clarified `--no-color` wording.
- 🔗 Clarified Python `--netlink` wording.
- 🎛️ Clarified `--bar-style` wording around `plain`, `fill`, and `color`.
- ⬇️ Clarified incoming color help text.
- ⬆️ Clarified outgoing color help text.
- 📌 Added explicit default-value text where useful.
- 🖥️ Added localized `System` label.
- 🧱 Added localized `Arch` label.
- 🪟 Kept Windows loopback warnings localized.
- 📏 Kept panel mode tags localized.
- 📊 Kept debug overlay labels localized.

### Python Packaging 📦

- 📦 Version bumped from `0.1.12-rc.1` to `0.1.12-rc.2`.
- 📦 Console script remains `winload = "winload.main:main"`.
- 📦 Wheel package path remains `src/winload`.
- ▶️ `python -m winload` remains supported.
- 🧩 `python/src/winload/__main__.py` continues to call `main`.
- 🧩 `python/src/winload/__init__.py` continues to expose package metadata.
- 🐍 The source layout stays package-native instead of top-level module based.
- ✅ `get_version()` still prefers installed package metadata.
- ✅ `get_version()` still falls back to reading `pyproject.toml` for source runs.
- 🧼 Python source execution docs now match the package layout.

### Rust CLI Alignment 🦀

- 🦀 Rust version remains aligned with Python at `0.1.12-rc.2`.
- ✨ Rust help decoration remains driven by the shared `emoji` module.
- 🧭 Rust pre-scans `--emoji` before constructing translated help.
- 🌐 Rust still pre-scans `--lang` before clap parsing.
- 🖥️ Rust help footer includes localized OS, arch, and target labels.
- 🎛️ Rust `--bar-style` default remains `plain`.
- 🏷️ Rust `--title-align` help is localized.
- 🔗 Rust `--netlink` help remains platform-scoped to Linux/Android.
- 🪟 Rust `--npcap` help remains platform-scoped to Windows.

### README Updates 📚

- 📚 Python `uv` examples now check the `winload` entry point before running it.
- 🧪 The command-order change helps users confirm the script path first.
- 🐍 Source-run examples continue to prefer `uv run python -m winload`.
- 📦 PyPI installation docs continue to separate Python edition from Rust binary packages.
- 🦀 Rust installation docs continue to identify most package managers as Rust binary channels.
- 🐧 Netlink docs remain linked from the README.
- 🪟 Windows loopback docs remain linked from the README.

### Compatibility Notes ⚠️

- ⚠️ This release does not make Netlink the default.
- ⚠️ This release does not make Npcap mandatory for normal startup.
- ⚠️ Python help output improvements do not change core sampling behavior.
- ⚠️ The default visual bar style remains changed from older releases: `plain` is now the default.
- ⚠️ Users expecting the old filled header/help bars can still pass `--bar-style fill`.
- ⚠️ Python `--netlink` still requires `pyroute2` on Linux/Android.
- ⚠️ Windows loopback capture still needs Npcap through the Rust `--npcap` path.

### Commit Reference 🔎

- 🔖 Commit: `3335833`
- 📅 Date: 2026-07-10
- 🧾 Subject: `release: 准备 v0.1.12-rc.2 并对齐 Python help 输出`
- 📦 Version change: `0.1.12-rc.1` -> `0.1.12-rc.2`
- 🚢 Pipeline intent: `build-publish, pypi-publish, crates-publish`

## [v0.1.12-rc.1] - 2026-07-09 🇨🇳

### Release Focus 🎯

- 🇨🇳 Prepared `v0.1.12-rc.1`.
- 🚢 Adjusted the Gitee publishing chain.
- 📦 Ensured Gitee package-manager manifests wait for mirrored release assets when needed.
- 🔁 Preserved the faster `publish-from-release` path for existing Gitee releases.
- 📚 Synchronized workflow documentation across languages.
- 🏷️ Reduced Homebrew badge payload size.
- 🧪 Kept `build-publish, pypi-publish, crates-publish` enabled for the release path.

### CI & Gitee Release Flow 🚢

- 🇨🇳 `publish-scoop-gitee` now depends on `sync-gitee-release`.
- 🇨🇳 `publish-homebrew-gitee` now depends on `sync-gitee-release`.
- ✅ Fresh release builds wait for Gitee Release sync before Gitee bucket/tap updates.
- ✅ `publish-from-release` can continue using an already existing Gitee Release.
- 🧭 The conditional logic now checks whether the current run is creating a release.
- 🧭 If a release is being created, the Gitee release sync must succeed first.
- 🧭 If a release is not being created, the existing mirrored release is treated as the source.
- 🪣 Scoop manifests avoid pointing to Gitee assets before those assets exist.
- 🍺 Homebrew formula updates avoid pointing to Gitee assets before those assets exist.
- 📚 English workflow docs were updated.
- 📚 Simplified Chinese workflow docs were updated.
- 📚 Traditional Chinese workflow docs were updated.
- 📊 Mermaid workflow diagrams were updated.
- 🔐 Gitee secret documentation remains tied to release mirroring.

### Badge & README Work 🏷️

- 🍺 Homebrew Shields.io custom logo payload was compressed.
- 🖼️ The embedded icon was reduced to a compact 32x32 asset.
- 🎨 The logo was quantized to reduce badge URL size.
- 🏷️ README Python Versions badge label was adjusted to `version`.
- 🍺 README Homebrew badge text was simplified.
- 🍺 The Homebrew badge keeps the Formula link.
- 🧪 The badge test markdown records compressed payload information.
- 📚 Six README variants received synchronized badge updates.

### Commit Reference 🔎

- 🔖 Commit: `c043429`
- 📅 Date: 2026-07-09
- 🧾 Subject: `release: 准备 v0.1.12-rc.1 并调整 Gitee 发布链路`
- 📦 Version change: `0.1.12-beta.2` -> `0.1.12-rc.1`
- 🚢 Pipeline intent: `build-publish, pypi-publish, crates-publish`

## [v0.1.12-beta.2] - 2026-07-09 🎨

### Release Focus 🎯

- 🎨 Prepared `v0.1.12-beta.2`.
- 🎛️ Changed the default bar style from `fill` to `plain`.
- 🏷️ Improved README badges.
- 🐍 Added richer Python package metadata.
- 🧪 Added local Homebrew badge generation test assets.
- 🧾 Kept Rust and Python help text consistent with the new default.
- 📦 Continued release metadata synchronization between Rust and Python.

### CLI Defaults 🎛️

- 🎛️ Rust `--bar-style` default changed to `plain`.
- 🎛️ Python `--bar-style` default changed to `plain`.
- 🧾 English help says `plain` is the default.
- 🧾 Simplified Chinese help says `plain` is the default.
- 🧾 Traditional Chinese help says `plain` is the default.
- 📚 README option tables were updated from `fill` to `plain`.
- 🧭 The available values remain `fill`, `color`, and `plain`.
- 🎨 Users can still opt into full-line background styling with `--bar-style fill`.
- 🎨 Users can still use text-only background styling with `--bar-style color`.
- 🎨 The default now favors a quieter terminal look.

### Python Metadata 🐍

- 🐍 Added PyPI classifiers.
- 📦 Marked development status as Beta.
- 🖥️ Marked console environment support.
- 📜 Marked MIT license metadata.
- 🌐 Marked operating system independence.
- 🐍 Declared Python 3 support.
- 🐍 Declared Python 3.9 support.
- 🐍 Declared Python 3.10 support.
- 🐍 Declared Python 3.11 support.
- 🐍 Declared Python 3.12 support.
- 🐍 Declared Python 3.13 support.
- 🏷️ README badges now show Python version support through PyPI.

### Badge Test Assets 🧪

- 🧪 Added `docs/test/test-shield-io-homebrew-logo/`.
- 🧪 Added a Pillow-based badge logo generator script.
- 🧪 Added a generated Homebrew logo PNG.
- 🧪 Added a test markdown file for Shields.io badge rendering.
- 🧹 Removed the older placeholder shield test document.
- 📊 Updated `.gitattributes` so test assets do not distort Linguist language stats.
- 📝 Explicitly kept Markdown visible to Linguist statistics where intended.

### Commit Reference 🔎

- 🔖 Commit: `b1b682d`
- 📅 Date: 2026-07-09
- 🧾 Subject: `release: 准备 v0.1.12-beta.2 并更新徽章与默认栏样式`
- 📦 Version change: `0.1.12-beta.1` -> `0.1.12-beta.2`
- 🚢 Pipeline intent: `build-publish, pypi-publish, crates-publish`

## [v0.1.12-beta.1] - 2026-07-09 ✨

### Release Focus 🎯

- ✨ Started the `v0.1.12` pre-release line.
- 🐍 Migrated Python code into a package-native `src/winload` layout.
- ▶️ Added `python -m winload` execution.
- 📦 Updated Python packaging paths.
- ✨ Added emoji-decorated help support.
- 🌐 Expanded localized help text across supported languages.
- 🧾 Avoided requiring TUI dependencies when printing Python help.
- 📚 Updated source-run docs to match the new Python layout.

### Python Layout Migration 🐍

- 📁 Moved `python/collector.py` to `python/src/winload/collector.py`.
- 📁 Moved `python/graph.py` to `python/src/winload/graph.py`.
- 📁 Moved `python/i18n.py` to `python/src/winload/i18n.py`.
- 📁 Moved `python/main.py` to `python/src/winload/main.py`.
- 📁 Moved `python/netlink.py` to `python/src/winload/netlink.py`.
- 📁 Moved `python/stats.py` to `python/src/winload/stats.py`.
- 📁 Moved `python/ui.py` to `python/src/winload/ui.py`.
- 🧩 Added package initialization.
- ▶️ Added module execution support.
- 📦 Changed wheel packaging from `packages = ["."]` to `packages = ["src/winload"]`.
- 📦 Changed the console entry point from `main:main` to `winload.main:main`.
- 🧭 Source execution now matches package import behavior.
- 🧹 The layout is less dependent on the current working directory.
- 🧪 The package layout is more suitable for PyPI installs and source runs.

### Emoji Help ✨

- ✨ Added Python emoji decoration helper.
- ✨ Added Rust emoji decoration helper.
- 🌐 Emoji support now covers help descriptions.
- 🧾 Emoji support now covers option help text.
- 🖥️ Emoji support now covers system information footers.
- 🧭 Emoji decoration remains opt-in through `--emoji`.
- 🧼 Plain help remains available without decorative prefixes.
- 🐍 Python help pre-scans emoji state.
- 🦀 Rust help pre-scans emoji state.
- 🔍 Debug information output can also use emoji decoration.
- 📊 TUI labels continue to support emoji mode.

### Documentation 📚

- 📚 Source-run docs now use `uv run python -m winload`.
- 📚 `python/uv.md` was updated.
- 📚 README files across languages were synchronized.
- 🇬🇧 English README was updated.
- 🇨🇳 Simplified Chinese README was updated.
- 🇹🇼 Traditional Chinese README was updated.
- 🇯🇵 Japanese README was updated.
- 🇰🇷 Korean README was updated.
- 🏛️ Classical Chinese README was updated.
- 🧪 A shield test placeholder was kept before being replaced in beta.2.

### Commit Reference 🔎

- 🔖 Commit: `03d80cc`
- 📅 Date: 2026-07-09
- 🧾 Subject: `release: 准备 v0.1.12-beta.1 并完善 help emoji`
- 📦 Version change: `0.1.11` -> `0.1.12-beta.1`
- 🚢 Pipeline intent: `build-publish, pypi-publish, crates-publish`

## Documentation Refresh Before v0.1.12 - 2026-06-30 to 2026-07-07 📚

### Onefetch & Metadata 🖼️

- 🖼️ Refreshed the docs onefetch screenshot after the `v0.1.11` release.
- 📦 Synchronized `Cargo.lock` package version metadata.
- 🧼 Normalized `rust/build.py` import ordering.
- 🔖 Commit reference: `c6643b4`.

### Netlink Documentation 🔗

- 🔗 Added clearer README entry points for Linux / Android / Termux Netlink.
- 📚 Updated multilingual README Netlink sections.
- 🪟 Synchronized Windows loopback heading style.
- 🐧 Synchronized Linux/Android Netlink heading style.
- 🏛️ Fixed a Classical Chinese README deep-dive link.
- 🧼 Added missing final newlines where needed.
- 🧪 Cleaned benchmark SVG generator imports and section comments.
- 🔖 Commit reference: `6745be8`.

### Install Script Relocation 📁

- 📁 Moved install scripts from `docs/install_scripts/` to `docs/scripts/install/`.
- 📥 Updated GitHub raw install commands.
- 🇨🇳 Updated Gitee raw install commands.
- 🔗 Updated source links for both install scripts.
- 🧾 Updated install script usage comments.
- 🧭 Updated fallback hints in the scripts.
- 🐧 Updated Termux debugging notes with the new path.
- 🔖 Commit reference: `583994d`.

## [v0.1.11] - 2026-06-29 🐍

### Release Focus 🎯

- 🐍 Finalized the `v0.1.11` release.
- 🔗 Added the Python Netlink backend in the beta line.
- 📁 Reorganized the Python project layout before the later `src/winload` migration.
- 📚 Updated Python `uv` workflow docs.
- 🏷️ Refined release download badges.
- 🧹 Ignored generated environment and cache paths.

### Python Netlink Backend 🔗

- 🔗 Added a Python RTNETLINK backend using `pyroute2`.
- 🐧 Targeted Linux and Android environments.
- 📱 Covered Termux/proot-style restricted environments.
- 🧭 Kept the backend opt-in behind `--netlink`.
- 🧪 Used Netlink as an alternative when `/proc/net/dev` is unavailable.
- 📊 Collected interface byte counters through Netlink data.
- 🧾 Listed filtered devices in debug output.
- ⚠️ Reported missing `pyroute2` as a clear runtime error.
- 🌐 Documented Linux/Android backend behavior.

### Release Polish 🧼

- 🧹 Ignored `.env` and generated Python cache paths.
- 📚 Updated `uv` usage docs.
- 🏷️ Refined release download badges.
- 🔖 `v0.1.11-rc.1` prepared the release line.
- 🔖 `v0.1.11` finalized it.

## [v0.1.10-beta.1] - 2026-06-29 📈

### Release Focus 🎯

- 📈 Redesigned Y-axis scaling options.
- 🧠 Continued the smart scaling work from earlier releases.
- 🧭 Made scaling behavior easier to reason about.
- 🛠️ Prepared the transition toward the later `max-mode` model.

### Scaling Notes 📊

- 📊 Scaling behavior became a named mode.
- 🧠 Smart adaptive scaling remained the default direction.
- 🧾 Documentation clarified scaling choices.
- 📏 Fixed scaling stayed available through explicit values.
- 🧪 Legacy behavior stayed available for users who preferred history-peak scaling.

## [v0.1.9] - 2026-06-29 🔗

### Release Focus 🎯

- 🔗 Added `--netlink` support for Linux and Android.
- 🪟 Improved Windows loopback capture guidance.
- 🧰 Fixed Linux build dependencies for Netlink.
- 📦 Trimmed Windows release targets to a simpler MSVC matrix.
- 📚 Expanded Netlink and loopback documentation.
- 🏛️ Added Classical Chinese README coverage.

### v0.1.9-beta.1 🏷️

- 🏷️ Added the `--title` option.
- 🧾 Allowed users to display a custom terminal UI title.
- 📚 Updated README files for the new title option.
- 📦 Bumped Rust and Python versions to `0.1.9-beta.1`.
- 🖼️ Moved preview images under `docs/images/`.
- 🖼️ Added a onefetch banner.

### v0.1.9-beta.2 🪟

- 🪟 Reverted default Windows packages to MSVC + Npcap with delay-load behavior.
- 🧩 Kept no-Npcap binaries available separately.
- 📚 Rewrote Windows loopback docs in English.
- 📚 Rewrote Windows loopback docs in Simplified Chinese.
- 📚 Rewrote Windows loopback docs in Traditional Chinese.
- 🧾 Updated README install notes around Npcap defaults.
- 🛡️ Kept startup safer by delay-loading `wpcap.dll`.

### v0.1.9-beta.3 to beta.7 🏷️

- 🏷️ Changed `--title` behavior to add a line above the device header.
- 🧾 Kept the device header visible even when a custom title is used.
- 🧭 Added `--title-align`.
- ↔️ Supported left title alignment.
- ↔️ Supported center title alignment.
- ↔️ Supported right title alignment.
- 🧼 Fixed indentation in header rendering.
- 🛠️ Fixed Rust header format strings.
- 🛠️ Fixed a missing format placeholder in a device header string.
- 📚 Updated README documentation across languages.

### v0.1.9-rc.1 to rc.3 📦

- 🏛️ Added Classical Chinese README.
- 🧾 Added concluding text across README variants.
- 🧪 Retried no-Npcap Windows builds.
- 🪣 Updated Scoop badge to the official icon.
- 📦 Refactored npm publishing workflow.
- 🪟 Trimmed Windows matrix entries.
- 🪟 Removed MinGW x64 from the supported release table.
- 🪟 Removed i686 MSVC from the supported release table.
- 🪟 Removed i686 MinGW from the supported release table.
- 🧾 Simplified Windows binary labels.
- 📚 Updated release template download tables.
- 📚 Updated loopback docs for the reduced Windows matrix.
- 📚 Updated all README files from six precompiled Windows variants to four.

### v0.1.9-rc.4 to rc.7 🔗

- 🤖 Added Android Netlink fallback for Rust network stats.
- 🖥️ Added platform-specific exit information with i18n and emoji support.
- 🛠️ Resolved Android build errors.
- 🌐 Added bilingual language labels in enum docs and section headers.
- 🇺🇸 Appended `(US)` to English language labels where helpful.
- 🧾 Added Termux support notes.
- 🔗 Added the `--netlink` flag.
- 🪟 Kept Npcap loopback support documented.
- 📚 Added Netlink docs.
- 🧰 Added `libc` dependency for Linux target builds.

### Stable v0.1.9 ✅

- ✅ Finalized the release after the Netlink and Windows-matrix work.
- ✅ Kept the project focused on supported release targets.
- ✅ Preserved opt-in behavior for platform-specific backends.
- ✅ Left normal Linux/Android runs on the default backend unless `--netlink` is passed.

## [v0.1.8] - 2026-05-23 🖥️

### Release Focus 🎯

- 🖥️ Added major TUI debugging and scaling improvements.
- 📈 Introduced smart adaptive Y-axis scaling.
- 🧪 Added the F3 debug overlay.
- 🌐 Improved i18n coverage.
- 📐 Fixed terminal display-width issues for CJK labels.
- 📦 Expanded release packaging and distribution docs.
- 🎬 Added visual preview assets.
- 📦 Stabilized `0.1.8` after a long RC line.

### v0.1.8-beta.1 to beta.4 📈

- 📈 Added `--smart-max` smart adaptive Y-axis scaling in Rust.
- ⏳ Adjusted smart max half-life from 5 seconds to 10 seconds.
- 🐍 Ported smart scaling and debug info to Python.
- 🧪 Added a Python local development README placeholder.
- ⚖️ Added mutual exclusion between `--max` and `--smart-max`.
- 📚 Added Y-axis scaling documentation.
- 🧪 Added the F3 debug overlay.
- 🏷️ Added mode tags for panel display.
- ↕️ Added smart-max direction arrows.

### v0.1.8-rc.0 to rc.3 📚

- 📚 Added dependency tables with shields to README files.
- 🎬 Added the Rust edition preview GIF.
- 🐍 Updated Python version references.
- 🦀 Updated Rust version references.
- 🎨 Adjusted dependency badge colors.
- 🪟 Added i686 Windows and Linux support during the RC experiments.
- 📦 Extracted release notes into `.github/release_template.md`.
- 🧾 Used shield.io badges in release notes.
- 📦 Skipped DEB/RPM packaging for i686.
- 🪣 Kept i686 packaging focused on npm/Scoop/AUR where applicable.

### v0.1.8-rc.4 to rc.12 🧰

- 📱 Added Termux support.
- 🪟 Iterated on Windows toolchain naming.
- 🪟 Documented MSVC versus MinGW.
- 🧰 Adjusted MinGW setup approaches in CI.
- 🧰 Added linker discovery fixes.
- 🧰 Added musl cross-toolchain handling.
- 🧰 Added fallback behavior for flaky musl downloads.
- 🧰 Skipped i686 builds when all musl download mirrors failed.
- 📦 Published an i686 musl cross-toolchain artifact tag.
- 📦 Used a project-hosted release as primary musl mirror.

### v0.1.8-rc.13 to rc.18 🌐

- 🌐 Localized F3 debug overlay labels.
- 🌐 Localized panel mode tags.
- 🌐 Added 30+ i18n keys.
- 🐍 Replaced hardcoded Python UI strings with translated strings.
- 🦀 Replaced hardcoded Rust UI strings with translated strings.
- 🇨🇳 Fixed Gitee clone URLs.
- 📚 Added source-run sections to README files.
- 🪟 Added Windows platform markers for `windows-curses`.
- 🍺 Added Homebrew badge and install instructions.
- 🇨🇳 Added Gitee alternatives for Scoop and Homebrew.
- 🍺 Fixed Homebrew formula directory creation.
- 🍺 Added Homebrew platform notes.
- 🪣 Added Scoop platform notes.
- 📦 Transposed release template download table.
- 🏷️ Standardized `nonpcap` to `no-npcap`.
- 📚 Added Scoop/Homebrew links to README files.

### v0.1.8-rc.20 to rc.26 🧪

- 🪟 Documented Windows 10+ requirements.
- 🧹 Removed dead XP shim code.
- 🛠️ Removed build references to deleted XP shim code.
- 🎬 Added asciinema terminal recording embeds.
- 📦 Fixed RPM pre-release version handling.
- 📦 Replaced hyphens with tildes for RPM version compatibility.
- 🧪 Added debug logging around RPM version rewriting.
- 🎬 Added recorded-by attribution lines.
- 📚 Simplified DEB/RPM install commands.
- 🧾 Updated release template wording.

### v0.1.8-rc.27 to rc.32 🌐

- 🌐 Replaced escaped Unicode sequences with real UTF-8 characters.
- 🧾 Fixed incorrect Simplified Chinese debug title text.
- 🧾 Fixed incorrect Traditional Chinese debug title text.
- 📡 Replaced escaped antenna emoji with a real glyph.
- 📐 Aligned debug panel values using `unicode-width`.
- 📐 Fixed CJK label width handling.
- 🍺 Removed redundant Homebrew formula link lines.
- 📱 Repositioned platform compatibility notes.
- 📱 Added Termux support to install script docs.
- 📦 Added npm provenance publishing.
- 🔐 Added OIDC permissions for npm provenance.
- 🔐 Added missing GitHub Packages permissions.

### Stable v0.1.8 ✅

- ✅ Finalized `0.1.8` from `0.1.8-rc.32`.
- 🐍 Updated README Python version references to 3.13.11.
- 🧰 Updated `uv venv` examples to Python 3.13.
- 🇨🇳 Fixed Gitee Scoop manifest heredoc variable expansion.
- 🇨🇳 Escaped Gitee autoupdate URLs correctly for Scoop templates.
- 🚢 Published with build, PyPI, and crates.io flow.

## [v0.1.7] - 2026-03-08 🚢

### Release Focus 🎯

- 🚢 Established much of the multi-channel publishing story.
- 🤖 Added Android release table coverage.
- 🇨🇳 Integrated Gitee code and release synchronization.
- 📥 Added Gitee install script support.
- 🦀 Added crates.io publishing support.
- 📦 Migrated npm package naming.
- 🪟 Improved Windows Npcap startup behavior.
- 📐 Improved CJK terminal width handling.

### v0.1.7-beta Series 🧪

- 🌐 Added `--lang` i18n support.
- 🌐 Supported `en-us`.
- 🌐 Supported `zh-cn`.
- 🌐 Supported `zh-tw`.
- 🦀 Implemented language selection in Rust.
- 🐍 Implemented language selection in Python.
- 🤖 Added Android build targets.
- 📦 Added npm publish job.
- 📚 Updated build docs for eight targets.
- 🤖 Added Android badges.
- 📚 Updated Alpine/Termux publishing guide.
- 🧾 Improved version management.
- 📚 Documented combined CI workflow.
- 📦 Fixed README path in npm publish workflow.
- 🖥️ Added system info on exit and in help.
- 📚 Enhanced npm package documentation.
- 📦 Triggered full release pipeline for beta.4.
- 📥 Improved install script hints.
- 🪣 Added AUR recommendation in install script output.

### crates.io and Cargo Publishing 🦀

- 🦀 Added Crates.io badge.
- 🦀 Added `cargo install winload` instructions.
- 📚 Clarified distribution channels.
- 📚 Documented that PyPI/GitHub/Gitee can provide Python edition paths.
- 📚 Documented that Cargo installs the Rust source build.
- 📚 Documented that package managers generally distribute Rust binaries.
- 🚢 Added crates.io publishing support in CI.
- 📦 Copied README into the Rust package before crates.io publish.
- 🧹 Standardized readme filename casing.
- 🐧 Fixed Linux CI path case sensitivity around `readme.md`.

### npm Migration 📦

- 📦 Prepared migration from `winload-rust-bin` to `@vincentzyuapps/winload`.
- 🧾 Added migration notices to README files.
- 🧭 Added `pm list -g` verification commands.
- 🦀 Added `cargo install --list` verification commands.
- 🧭 Added `which winload` verification commands.
- 🪟 Added `win-nload` bin alias to avoid Windows `winload.exe` name conflicts.
- 📦 Updated optional dependencies.
- 📦 Updated publish configuration.
- 🔐 Iterated on GitHub Packages authentication.
- 🔐 Moved `.npmrc` auth into the correct package location.
- 📜 Added the project license where packaging needed it.
- 📦 Migrated platform package names to `@vincentzyuapps/winload-*`.

### Windows & Npcap 🪟

- 🪟 Delay-loaded `wpcap.dll`.
- ✅ Windows binaries can start without Npcap installed.
- ⚠️ Loopback capture still requires Npcap when `--npcap` is used.
- 📚 Added richer release notes installation guidance.
- 📥 Added `WINLOAD_VERSION` support to install scripts.
- 🪟 Recommended Windows Terminal for better rendering.
- 📐 Fixed CJK padding using display-width-aware logic.

### Benchmark & Gitee Work 📊

- 📊 Added an automated benchmark suite.
- 🧪 Added Bash and Go benchmark tooling.
- 📚 Fixed CJK doc filename issues.
- 📊 Updated benchmark results.
- 📊 Cleaned benchmark scripts.
- 📊 Fixed SVG benchmark chart labels.
- 🎞️ Slowed benchmark SVG animation playback.
- 🇨🇳 Added Gitee sync workflow.
- 🇨🇳 Merged Gitee sync into the main build workflow.
- 🇨🇳 Added `sync-gitee-code`.
- 🇨🇳 Added `sync-gitee-release`.
- 🇨🇳 Added Gitee Release API upload handling.
- 🇨🇳 Added Gitee install script.
- 🇨🇳 Added verbose upload logging.
- 🇨🇳 Added upload timeout and retry behavior.
- 🇨🇳 Fixed Gitee release sync `404` behavior.
- 🇨🇳 Added `target_commitish` for Gitee release sync.
- 🇨🇳 Added JSON-safe request body handling.

### Stable v0.1.7 ✅

- ✅ Added Android binary URLs to the release table.
- ✅ Renamed Gitee jobs with a clear prefix for sidebar sorting.
- ✅ Added specific-version install command to the Gitee script docs.
- ✅ Fixed Chinese formatting in install script compatibility notes.
- ✅ Published with build, PyPI, and crates.io paths.

## [v0.1.6-beta Series] - 2026-02-16 to 2026-02-24 📦

### Packaging & CI 📦

- 📦 Added DEB build work.
- 📦 Added RPM build work.
- 🧾 Renamed DEB/RPM artifacts to a unified format.
- 📥 Added install script support.
- 🚢 Integrated DEB/RPM builds into the main job.
- 🧾 Enhanced release notes.
- 📚 Added installation sections.
- ⚫ Added `--no-color` documentation.
- ⌨️ Added `c` shortcut documentation.
- 🚢 Tested the full release pipeline for `0.1.6-beta.1`.
- 🚢 Repeated build release tests for beta.2 and beta.3.
- 🦀 Ran Rust edition build publishing for beta.4.

### Language & Docs 🌐

- 🇹🇼 Added Traditional Chinese support.
- 🪟 Improved Windows loopback implementation documentation.
- 📚 Translated build and release workflow docs.
- 🐧 Improved Linux install docs.
- 📥 Added apt install guidance.
- 🔗 Added install script source links.
- 🌐 Unified multilingual navigation links.
- 🇯🇵 Added Japanese README translation.
- 🇰🇷 Added Korean README translation.
- 📚 Added AUR and Homebrew dual-arch support docs.
- 🪟 Fixed Npcap descriptions.
- 🌐 Added bilingual English/Chinese CLI help text.

### PyPI Work 🐍

- 🐍 Added PyPI packaging.
- 🐍 Added `pyproject.toml` for uv-based packaging.
- 🐍 Added PyPI publishing documentation.
- 🐍 Added PyPI publish support to CI/CD.
- 🐍 Added PyPI badge to README files.
- 🐍 Separated Python edition install docs from Rust edition install docs.
- 🛠️ Fixed package build issues.
- 🧾 Added `-V` / `--version` argument.
- 📚 Updated PyPI publishing docs with working commands.
- 🧹 Simplified README section headers.
- 🧼 Cleaned virtual environment activation scripts.

## [v0.1.5-beta Series] - 2026-02-16 🪣

### Release Focus 🎯

- 🪣 Added Scoop publishing work.
- 🚩 Refactored build and publish flags.
- 🧪 Tested Scoop publish retries.
- 🪟 Avoided conflict with Windows `winload.exe` by using the `win-nload` shim.
- 🧾 Clarified PR build-only behavior in workflow docs.
- 🧪 Continued release automation experiments.

### UI & Runtime 🖥️

- ➖ Added separator line toggle feature.
- 📏 Fixed separator line width to follow terminal size dynamically.
- ⚫ Added `--no-color`.
- ⌨️ Added runtime `c` key toggle for monochrome mode.

## [v0.1.4-beta.1] - 2026-02-13 🎛️

### Release Focus 🎯

- 🎛️ Added more display customization options.
- 🪟 Explored Windows loopback capture approaches.
- 🧾 Improved Npcap error messages.
- 📚 Updated documentation for display flags and capture behavior.

### Added ➕

- 🧱 Added `--unicode`.
- 🎛️ Added `--bar-style`.
- ⬇️ Added `--in-color`.
- ⬆️ Added `--out-color`.
- 🐍 Added those display options to Python.
- 🦀 Added those display options to Rust.
- 🪟 Added early `--npcap`/`--etw` CI work.
- 🛠️ Tested Windows GetIfTable-based implementation ideas.

### Changed 🔧

- 🧾 Moved Npcap/ETW info from stderr to the TUI header bar in later follow-up.
- 🧹 Removed ineffective ETW loopback backend in later `0.1.6` work.
- 📚 Kept loopback docs updated with the reality of Windows counters.

## [v0.1.1-beta.1] - 2026-02-10 🛠️

### Release Focus 🎯

- 🛠️ Fixed Windows bash syntax in CI.
- 🧱 Improved cache isolation for `aarch64` builds.
- 🪟 Added Windows ARM64 build target work.
- 🐧 Added Linux ARM64 build target work.
- 📦 Improved platform build coverage.

### Features Leading Into This Release ✨

- 🎨 Enhanced Python TUI styling.
- 🏷️ Added platform badges.
- 📚 Added usage documentation.
- ✨ Added `-e` / `--emoji` for emoji-decorated TUI mode.
- 🧮 Added `--unit`.
- 📏 Added `--max`.
- 🚫 Added `--no-graph`.
- 🦀 Added those major flags to Rust.
- 🐍 Added those major flags to Python.
- 🐧 Switched Linux x86_64 builds toward musl static linking for GLIBC portability.
- 📚 Changed README presentation to show Rust as the primary language.

## [v0.1.0] - 2026-02-09 🌱

### Release Focus 🎯

- 🌱 Created the first tagged release.
- 🚢 Used an empty commit to test GitHub build/release behavior.
- 📦 Established the earliest release automation feedback loop.
- 🧪 Follow-up commits added auto-versioned artifacts.
- 🧪 Release workflow was rewritten for fresh releases and changelog commits.

### Project State 🧩

- 🐍 The Python implementation already existed.
- 🦀 The Rust port work had already started.
- 🧪 GitHub Actions multi-platform experiments were already underway.
- 📚 README presentation and badges were rapidly evolving.

## Initial Development - 2026-02-08 to 2026-02-09 🧪

### Project Initialization 🌱

- 🐍 Initialized `winload` as a Python network load monitor.
- 🧭 Focused on an `nload`-like terminal experience.
- 🦀 Added a Rust port with Ratatui TUI.
- 🚢 Added GitHub Actions workflow experiments.
- 🖼️ Added Rust implementation preview docs.
- 📚 Adjusted README headings and preview presentation.
- 🎨 Added early title formatting.
- 🧹 Ignored Rust build output directories.
- 🧹 Removed tracked build artifacts.
- 🖼️ Added a Socialify project banner.
- 🧪 Tested multi-platform build actions.
- 🍎 Fixed macOS runner behavior.
- 📦 Enabled cargo cache in CI.

## `v0.1.11..v0.1.12` Release Diff Summary 📊

### Files & Scale 📏

- 📊 59 files changed between `v0.1.11` (`1b630fa`) and the stable release commit `be4afee`.
- ➕ 3053 insertions.
- ➖ 500 deletions.
- 🐍 Python package layout changed significantly.
- 🦀 Rust CLI/help code changed moderately.
- 📚 README and docs were synchronized across languages.
- 🚢 GitHub Actions release flow changed for Gitee publishing.
- 🧪 Badge test assets were added.
- 🖼️ Onefetch image asset was refreshed.

### Key File Areas 🗂️

- 🧾 `.github/workflows/build.yml`
- 📚 `.github/workflows/build.md`
- 📚 `.github/workflows/build.zh-cn.md`
- 📚 `.github/workflows/build.zh-tw.md`
- 📊 `benchmark/main.go`
- 🐧 `docs/linux_android_netlink.md`
- 🐧 `docs/linux_android_netlink.zh-cn.md`
- 🐧 `docs/linux_android_netlink.zh-tw.md`
- 🪟 `docs/win_loopback.md`
- 🪟 `docs/win_loopback.zh-cn.md`
- 🪟 `docs/win_loopback.zh-tw.md`
- 📥 `docs/scripts/install/install.sh`
- 📥 `docs/scripts/install/install_gitee.sh`
- 🧪 `docs/test/test-shield-io-homebrew-logo/`
- 🐍 `python/pyproject.toml`
- 🧾 `python/_build_info.py`
- 🐍 `python/src/winload/main.py`
- 🐍 `python/src/winload/i18n.py`
- 🐍 `python/src/winload/emoji.py`
- 🐍 `python/src/winload/ui.py`
- 🦀 `rust/Cargo.toml`
- 🔒 `rust/Cargo.lock`
- 🧾 `rust/_build_info.rs`
- 🦀 `rust/src/main.rs`
- 🦀 `rust/src/i18n.rs`
- 🦀 `rust/src/emoji.rs`
- 🛠️ `scripts/build_rust_bin.py`
- 📚 `readme.md`
- 📚 `readme.zh-cn.md`
- 📚 `readme.zh-tw.md`
- 📚 `readme.jp.md`
- 📚 `readme.ko.md`
- 📚 `readme.lzh.md`

## Migration Notes 🧭

### For Python Users 🐍

- 🐍 Source runs should prefer `uv run python -m winload`.
- 📦 Installed command runs should continue to use `winload`.
- 🧭 The console script now points to `winload.main:main`.
- 🧩 Direct imports should use the `winload` package path.
- 🔗 `--netlink` remains Linux/Android-only.
- 🪟 Windows still requires `windows-curses` for the Python TUI.
- 🧾 Help can be shown without importing the full TUI runtime path.
- ✨ Use `--emoji` to decorate help and TUI text.
- 🌐 Use `--lang en-us`, `--lang zh-cn`, or `--lang zh-tw` for localized UI/help.

### For Rust Users 🦀

- 🦀 Normal `winload` binary usage is unchanged.
- 🎛️ The visual default changed to `--bar-style plain`.
- 🎨 Pass `--bar-style fill` to recover older filled-line styling.
- 🪟 Use `--npcap` for Windows loopback capture when Npcap is installed.
- 🔗 Use `--netlink` on Linux/Android when the default backend cannot access network counters.
- ✨ Use `--emoji` to decorate help, TUI labels, and output where supported.
- 🌐 Use `--lang` for localized output.

### For Package Maintainers 📦

- 📦 Python packages now build from `python/src/winload`.
- 📦 Python metadata includes explicit classifiers.
- 🦀 Rust crate metadata carries the same release version.
- 🇨🇳 Gitee package manager manifests should wait for release sync on fresh releases.
- 🍺 Homebrew badge and formula docs were refreshed.
- 🪣 Scoop Gitee publishing flow was refined.
- 📥 Install scripts moved to `docs/scripts/install/`.

## Platform Notes 🖥️

### Windows 🪟

- 🪟 Standard Windows APIs do not reliably expose loopback traffic counters.
- 🪟 Rust loopback capture uses Npcap when `--npcap` is enabled.
- 🧩 Npcap-enabled builds delay-load `wpcap.dll`.
- ✅ Delay loading lets the binary start without Npcap until capture is requested.
- ⚠️ Capturing loopback traffic still requires Npcap installation.
- 🧾 Windows release assets focus on supported MSVC variants.
- 📚 Windows loopback docs explain why normal counters are insufficient.

### Linux 🐧

- 🐧 Normal Linux runs use the default backend.
- 🔗 `--netlink` enables RTNETLINK collection.
- 📦 Linux release assets include binary, DEB, and RPM paths.
- 📦 RPM pre-release version handling uses tilde-compatible transformation.
- 🧰 Earlier i686 experiments were trimmed from the supported release matrix.
- 📚 Linux install docs cover apt, dnf, and manual releases.

### Android / Termux 🤖

- 🤖 Android builds are part of the release story.
- 📱 Termux install support was added to install scripts.
- 🔗 Netlink can help in restricted Android/Termux environments.
- 📚 Termux notes are included in README and install-script docs.
- ⚠️ Netlink remains opt-in.

### macOS 🍎

- 🍎 macOS release binaries are part of the release table.
- 🍺 Homebrew install paths were refined.
- 🍺 Homebrew formula generation supports macOS and Linux where applicable.
- 📚 Homebrew tap links exist for GitHub and Gitee flows.

## Distribution Notes 📦

### Python / PyPI 🐍

- 🐍 PyPI distributes the Python edition.
- 🐍 Python package support is declared for Python 3.9 through 3.13.
- 📦 The package uses Hatchling.
- 📦 The console script exposes `winload`.
- 📚 Python install docs include pip and uv examples.

### Rust / crates.io 🦀

- 🦀 crates.io distributes the Rust source package.
- 🦀 `cargo install winload` builds the Rust edition.
- 📚 Cargo install docs are included in README files.
- 📦 README path handling was fixed for crates.io publishing.

### npm 📦

- 📦 npm packaging moved to `@vincentzyuapps/winload`.
- 📦 Platform packages moved under matching scoped names.
- 🔐 GitHub Packages auth handling was iterated.
- 🧾 npm provenance support was added later.
- 📚 README docs explain npm distribution channels.

### Scoop / AUR / Homebrew 🪣

- 🪣 Scoop publishing was added and refined.
- 🪣 Scoop has GitHub and Gitee bucket options.
- 🐧 AUR binary package publishing was automated.
- 🍺 Homebrew tap publishing was added.
- 🇨🇳 Gitee mirrors exist for China-friendly install flows.
- 📚 README files include package-manager-specific notes.

### Direct Release Assets 🚢

- 🚢 GitHub Releases remain the primary binary asset source.
- 🇨🇳 Gitee Releases mirror assets for regional access.
- 📦 Release templates include platform download tables.
- 🏷️ Download badges were refined across multiple releases.
- 🧾 Release notes include quick install commands and changelog summaries.

## Compatibility Notes ⚠️

- ⚠️ `--netlink` is opt-in and platform-specific.
- ⚠️ `--npcap` is opt-in and Windows-specific.
- ⚠️ Python TUI on Windows still depends on `windows-curses`.
- ⚠️ The `plain` bar style is now the default.
- ⚠️ Older screenshots may show the previous filled bar style.
- ⚠️ Some old release notes mention i686 or MinGW variants that were later trimmed.
- ⚠️ Some early Windows loopback approaches were explored and then removed.
- ⚠️ ETW loopback capture references were removed after proving ineffective for the intended path.
- ⚠️ The current supported Windows release matrix is simpler than the large experimental matrix from the `v0.1.8` RC line.

## Git Log Coverage Notes 🔎

- 🔎 This changelog emphasizes tagged releases and major pre-release milestones.
- 🔎 Small CI retry commits are summarized when they only retried the same pipeline.
- 🔎 Documentation-only sync commits are grouped by affected area.
- 🔎 Release-trigger commits are listed when they changed packaging behavior or version metadata.
- 🔎 The `v0.1.12` series is intentionally more detailed because it is reconstructed from its release commits and the complete stable-release diff.
- 🔎 Earlier releases are summarized by behavior, platform support, packaging impact, and user-visible changes.

## Unreleased / Next Checklist 📝

- 🧪 Keep the Python and Rust test suites green throughout the `v0.2.0` pre-release cycle.
- 🌳 Run the README source-tree generator in dry-run mode before publishing each pre-release.
- 📈 Exercise all Rust graph styles and axis modes in narrow and wide terminals.
- 📦 Re-check wheel, sdist, Cargo package, and lockfile metadata before the next publish trigger.
- 📝 Verify README install commands and package-manager metadata after publishing new assets.
- 🇨🇳 Verify Gitee Release synchronization before updating the Gitee bucket and tap manifests.
- 🏷️ Fetch or confirm the remote `v0.1.12` tag separately if the local tag timeline needs to be completed.
