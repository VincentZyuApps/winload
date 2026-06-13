# commit 和 release 从 GitHub 同步到 Gitee

> 通过 GitHub Actions 自动将代码 commit 和 release 同步到 Gitee 镜像仓库
>
> - GitHub：https://github.com/VincentZyuApps/winload
> - Gitee：https://gitee.com/vincent-zyu/winload

> [!NOTE]
> 原来是单独的 `sync-to-gitee.yml` 工作流，现在已经合并到 `build.yml` 中捏 ✨

---

## 🤔 这个功能做了什么？

同步逻辑已经集成在主工作流文件：[`.github/workflows/build.yml`](../../.github/workflows/build.yml)

### 触发时机

| 事件 | 同步内容 | 说明 |
|------|----------|------|
| `push` 到 main | 代码 | 每次 push 代码时自动镜像到 Gitee |
| `build publish` / `build release` | 代码 + Release | 构建完成后同时同步 Release |

### Job：`sync-gitee-code` — 同步代码

与 `check` job 并行运行，在每次 push 时触发。

使用 [Yikun/hub-mirror-action](https://github.com/Yikun/hub-mirror-action) 这个开源 Action（696⭐，4000+ 用户在用），把 GitHub 上 winload 仓库的 **所有分支 + 所有 Tag + 所有 Commit** 镜像推送到 Gitee。

原理很简单：在 GitHub Actions 的 ubuntu runner 里 `git clone` 下来，然后 `git push --force` 到 Gitee。

### Job：`sync-gitee-release` — 同步 Release

在 `release` job 完成后运行，与 `publish-scoop`、`publish-aur-bin`、`publish-npm` 等发布任务并行。做了这几件事：

1. 从 GitHub API 获取 Release 信息（标题、Release Notes、附件下载地址）
2. 下载所有 Release 附件（exe、deb、rpm 等二进制文件）
3. 通过 Gitee API v5 在 Gitee 上创建对应的 Release
4. 把下载下来的附件上传到 Gitee Release

### 效果

配置好之后，你只需要 `git push github main`，Gitee 那边就会自动跟着更新。不用再双 push 了。

---

## 🔧 需要配置的东西

你需要在 GitHub 仓库里配置 **2 个 Secrets**：

| Secret 名称 | 用途 |
|---|---|
| `GITEE_PRIVATE_KEY` | SSH 私钥，用于 `git push` 代码到 Gitee |
| `GITEE_TOKEN` | Gitee 个人访问令牌，用于调用 Gitee API 创建 Release |

下面一步一步来。

---

## 📝 步骤 1：生成 SSH 密钥对

这个密钥对专门用于 GitHub Actions 向 Gitee 推送代码。

### 1.1 生成密钥

**macOS / Linux / WSL：**

```bash
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -C "gitee-sync" -f ~/.ssh/gitee_sync_key
```

**Windows PowerShell：**

```powershell
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -C "gitee-sync" -f "$HOME\.ssh\gitee_sync_key"
```

> ⚠️ Windows 的 `ssh-keygen` 不认 `~`，必须用 `$HOME` 或写完整路径（如 `C:\Users\你的用户名\.ssh\gitee_sync_key`）。

- 提示 passphrase 时**直接回车**（不设密码），因为 GitHub Actions 里没法输密码
- 执行完后会生成两个文件：
  - `~/.ssh/gitee_sync_key` — **私钥**（待会放到 GitHub Secrets）
  - `~/.ssh/gitee_sync_key.pub` — **公钥**（待会放到 Gitee）

### 1.2 查看生成的密钥内容

**macOS / Linux / WSL：**

```bash
# 查看私钥（待会要复制到 GitHub）
cat ~/.ssh/gitee_sync_key

# 查看公钥（待会要复制到 Gitee）
cat ~/.ssh/gitee_sync_key.pub
```

**Windows PowerShell：**

```powershell
# 查看私钥（待会要复制到 GitHub）
Get-Content "$HOME\.ssh\gitee_sync_key"

# 查看公钥（待会要复制到 Gitee）
Get-Content "$HOME\.ssh\gitee_sync_key.pub"
```

> ⚠️ 私钥内容要**完整复制**，包括开头的 `-----BEGIN OPENSSH PRIVATE KEY-----` 和结尾的 `-----END OPENSSH PRIVATE KEY-----`，一个字符都不能少！

---

## 📝 步骤 2：把公钥添加到 Gitee

### 2.1 打开 Gitee SSH 公钥设置页面

浏览器打开：https://gitee.com/profile/sshkeys

### 2.2 添加公钥

1. 点击 **「添加公钥」**
2. **标题**：填一个你认得出来的名字，比如 `github-actions-sync-gitee`
3. **公钥**：粘贴 `~/.ssh/gitee_sync_key.pub` 的内容
4. 点击 **「确定」**

### 2.3 验证公钥是否生效

```bash
ssh -i ~/.ssh/gitee_sync_key -T git@gitee.com
```

如果看到类似 `Hi vincent-zyu! You've successfully authenticated` 就说明配好了。

---

## 📝 步骤 3：创建 Gitee 个人访问令牌

### 3.1 打开 Gitee 令牌设置页面

浏览器打开：https://gitee.com/profile/personal_access_tokens

### 3.2 生成令牌

1. 点击 **「生成新令牌」**
2. **私人令牌描述**：填 `github-actions-sync-gitee`（随便写）
3. **权限**：勾选 **`projects`**（必须，用于创建/更新 Release）
4. 点击 **「提交」**
5. 页面会显示生成的令牌，**立刻复制保存**（只显示一次！关了就看不到了）

---

## 📝 步骤 4：把私钥和令牌添加到 GitHub Secrets

### 4.1 打开 GitHub 仓库 Secrets 设置页面

浏览器打开：https://github.com/VincentZyuApps/winload/settings/secrets/actions

### 4.2 添加 `GITEE_PRIVATE_KEY`

1. 点击 **「New repository secret」**
2. **Name**：`GITEE_PRIVATE_KEY`
3. **Secret**：粘贴 `~/.ssh/gitee_sync_key` 私钥的**完整内容**
4. 点击 **「Add secret」**

> ⚠️ 注意是添加在 **Repository secrets** 下面，不是 Dependabot secrets 也不是 Environment secrets！

### 4.3 添加 `GITEE_TOKEN`

1. 点击 **「New repository secret」**
2. **Name**：`GITEE_TOKEN`
3. **Secret**：粘贴步骤 3 中复制的 Gitee 个人访问令牌
4. 点击 **「Add secret」**

### 4.4 确认配置

配置完后，Secrets 页面应该能看到这两个：

```
GITEE_PRIVATE_KEY    Updated just now
GITEE_TOKEN          Updated just now
```

---

## ✅ 验证

### 方法 1：推送代码触发

随便改个文件，push 到 GitHub：

```bash
git add .
git commit -m "test: verify gitee sync"
git push github main
```

然后去 https://github.com/VincentZyuApps/winload/actions 看 **「Sync to Gitee」** 这个 workflow 是否执行成功。

### 方法 2：手动触发

1. 打开 https://github.com/VincentZyuApps/winload/actions
2. 左侧选择 **「Sync to Gitee」**
3. 点击 **「Run workflow」**
4. 如果想同时同步最新 Release，勾选 **「是否同步最新 Release 到 Gitee？」**
5. 点击 **「Run workflow」** 按钮

### 验证同步结果

- 代码同步：看 https://gitee.com/vincent-zyu/winload 的 commit 记录是否和 GitHub 一致
- Release 同步：看 https://gitee.com/vincent-zyu/winload/releases 是否有对应的 Release 和附件

---

## ❓ 常见问题

### Q：同步失败报 `Permission denied (publickey)`

检查：
1. Gitee SSH 公钥是否添加了（步骤 2）
2. GitHub Secret `GITEE_PRIVATE_KEY` 的内容是否完整（包括 BEGIN/END 那两行）
3. 公钥和私钥是否是同一对（不要搞混了）

### Q：Release 同步失败报 `无效的私人令牌`

检查：
1. `GITEE_TOKEN` 是否过期了（Gitee 令牌有有效期，过期了重新生成一个）
2. 令牌权限是否勾选了 `projects`

### Q：以后还需要双 push 吗？

不需要了。你只需要 push 到 GitHub，Gitee 会自动同步。

之前 git remote 里配的 origin（Gitee）可以保留，不影响。但以后不用手动 `git push origin` 了。

### Q：workflow 报错了但 Gitee 上代码已经同步了？

`sync-code` 成功就说明代码同步没问题。如果是 `sync-release` 失败，可能是 Gitee API 偶尔抽风，可以在 Actions 页面手动 Re-run 那个 job。
