# PyPI 手动发布流程指南

> 使用 uv 构建并发布 Python 包到 PyPI
>
> ⚠️ 本文档中 `$VERSION` 代表当前要发布的版本号（如 `0.1.6-beta.3`）。

---

## 📋 发布前准备

### 1. 确认版本号
```bash
# 从 pyproject.toml 读取版本
wsl
grep '^version' python/pyproject.toml
# 例: version = "0.1.6-beta.3"
```
> 🔔 以下所有操作都用这个版本号替换 `${VERSION}`。

### 2. 安装 uv（如果还没安装）
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy Bypass -c "irm https://gitee.com/wangnov/uv-custom/releases/download/0.10.5/uv-installer-custom.ps1 | iex"

# macOS / Linux
curl -LsSf https://gitee.com/wangnov/uv-custom/releases/download/0.10.5/uv-installer-custom.sh | sh

```

### 3. 安装构建依赖
```bash
cd python
uv sync
```

---

## 🔨 构建包

### 使用 uv 构建（推荐）
```bash
cd python

# 构建 wheel 和源码包
uv build

# 查看产物
ls dist/
```

---

## 📤 发布到 PyPI

### 方式 A: 使用 uv publish（推荐）

```bash
cd python

# 发布到 TestPyPI（测试）
# uv publish --index https://test.pypi.org/simple/
uv publish --publish-url https://test.pypi.org/legacy/

# 测试安装
cd D:\aaaStuffsaaa\from_git\test\20260224_test_winload
uv venv
uv pip install --index-url https://test.pypi.org/simple/ winload
uv run py winload --help

# 发布到正式 PyPI
uv publish
```

### 方式 B: 使用 twine

```bash
cd python

# 安装 twine
pip install twine

# 发布到 TestPyPI（测试）
twine upload --repository testpypi dist/*

# 测试安装
pip install --index-url https://test.pypi.org/simple/ winload

# 发布到正式 PyPI
twine upload dist/*
```

---

## 🧪 测试安装

### 从 TestPyPI 安装
```bash
pip install --index-url https://test.pypi.org/simple/ winload
winload --help
```

### 从正式 PyPI 安装
```bash
pip install winload
winload --help
```

---

## 📝 发布检查清单

每次发布新版本时：
- [ ] 更新 `python/pyproject.toml` 中的版本号
- [ ] 构建包：`cd python && uv build`
- [ ] 发布到 TestPyPI 并测试安装
- [ ] 发布到正式 PyPI
- [ ] 验证安装：`pip install winload && winload --version`

---

## 📌 用户安装方式

```bash
# 方式 1: pip
pip install winload

# 方式 2: uv
uv add winload
```

---

## ⚠️ 常见问题

| 问题 | 解决 |
|------|------|
| `ModuleNotFoundError: No module named 'hatchling'` | 确保使用 `uv build`，它会自动安装构建依赖 |
| `error: invalid command 'bdist_wheel'` | 使用 `uv build` 而不是 `python setup.py` |
| 发布失败，提示权限错误 | 检查 PyPI API Token 是否正确 |
| 包名已存在 | 更改 `pyproject.toml` 中的 `name` 字段 |
