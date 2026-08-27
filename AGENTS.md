# winload Agent Guide

## 项目边界

- `python/` 是 Python 包，`rust/` 是 Rust crate；两套实现面向相同的终端网络监控体验。
- 修改共有能力时，优先同时评估 Python 与 Rust 的行为、帮助文本、i18n 和测试。
- 保持语言惯用写法，不复制另一种语言的源码结构或实现细节。

## 双实现对称

- 共有职责应优先使用对称的文件名和目录：`app`、`cli`、`collector`、`config`、`diagnostics`、`emoji`、`graph`、`i18n`、`netlink`、`runtime`、`stats`、`ui`。
- 新增跨实现功能前，先确定两侧对应模块及公共 CLI/配置行为；不能保持一致时，在代码或变更说明中写明原因。
- 新增或修改用户可见选项时，同步检查默认值、校验、帮助文本、三语翻译和回归测试。
- Rust 的用户体验应覆盖 Python；新增 Python 可见功能默认同步到 Rust，例外必须记录理由和作用域。
- 允许的非对称项包括 Python 的 `__init__.py`/`__main__.py`、Rust 的 `main.rs`，以及 Rust Windows Npcap 专属的 `loopback.rs`。
- Rust 的额外用户能力是 `Esc`、`--graph-style`、`--x-axis`、`--y-axis`、`g`/`x`/`y` 图表控制和 Windows `--npcap`；Python 保留基础 `classic` 图形。
- 平台专属能力不要求伪造另一实现；保留清晰的作用域，例如 Rust `--npcap` 与 Linux/Android 的 `--netlink`。

## 版本与发布

- Python `pyproject.toml`、Rust `Cargo.toml`、`Cargo.lock` 和 Python 入口版本断言必须保持同一版本。
- 版本升级后运行 `cargo metadata --format-version 1 > /dev/null` 更新锁文件，再执行 locked 检查。
- changelog 直接记录本地当前最新版本和实际日期；不要创建或保留版本级 `Unreleased` 条目。
- 发布触发词和发布路由以 `.github/workflows/build.yml` 为准；修改工作流时同步三份 `build*.md`，保持语义、格式和总行数一致。

## 验证命令

从仓库根目录使用 Bash/WSL 和 `uv` 创建本地环境：

```bash
uv venv
uv pip install --python .venv/bin/python -e ./python
.venv/bin/python -m unittest discover -s python/tests
.venv/bin/python -m unittest discover -s test/readme
```

版本升级或 Rust 依赖变更前，按以下顺序更新、检查并审阅生成 README：

```bash
cd rust
cargo metadata --format-version 1 > /dev/null
cargo test --locked --no-default-features
cargo check --locked --no-default-features
../.venv/bin/python ../scripts/update_readme_tree.py --dry-run
# 审阅 dry-run 后才写入六份根 README。
../.venv/bin/python ../scripts/update_readme_tree.py
cd ..
git status
git diff HEAD --stat
git diff HEAD -- rust/Cargo.lock
```

- README 的源码树由 `scripts/update_readme_tree.py` 生成；不要手工修改生成区。
- 提交前运行 `git diff --check`；版本、CLI、i18n、图表或工作流改动按影响范围补充定向测试。
