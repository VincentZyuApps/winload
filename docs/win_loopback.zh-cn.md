# Windows Loopback 流量监控：为什么标准 API 不行，Npcap 可以？

> **[📖 English](win_loopback.md)**
> **[📖 简体中文(大陆)](win_loopback.zh-cn.md)**
> **[📖 繁體中文(台灣)](win_loopback.zh-tw.md)**

## ⚡ TL;DR

Windows 的 loopback (`127.0.0.1`) 流量在 `tcpip.sys` 内部直接短路，**完全绕过了 NDIS 网络驱动层**，导致 `GetIfEntry` / `GetIfTable` 的计数器始终为 0。

这是 **Windows 网络栈的功能缺失**——loopback 接口从未被赋予一个完整的 NDIS miniport 驱动，标准的监控 API 对它根本不起作用。

Npcap 通过 WFP (Windows Filtering Platform) callout driver 在短路之前拦截数据包，因此能抓到。

---

## 🏗️ Windows 网络栈架构

```
App  →  Winsock  →  AFD.sys  →  tcpip.sys  →  NDIS  →  NIC driver  →  Hardware
```

### 正常网卡的流量路径

```
tcpip.sys  →  NDIS (counter +1)  →  miniport driver  →  physical NIC
```

NDIS 驱动在这里更新 `MIB_IFROW.dwInOctets` / `dwOutOctets`，所以 `GetIfEntry()` 能拿到正确的值。

### Loopback 的流量路径

```
tcpip.sys  →  direct loopback (short-circuit)  →  receive path
                     ↑
              NDIS layer entirely skipped
              counters never updated
```

当数据发往 `127.0.0.1` 时，`tcpip.sys` 在**传输层就直接短路**了——数据包从发送路径直接复制到接收路径，**根本不经过 NDIS 层**。

Windows 的 "Loopback Pseudo-Interface 1" 其实是一个**虚拟占位符**。它出现在 `GetIfTable` 的接口列表里（`dwType = IF_TYPE_SOFTWARE_LOOPBACK = 24`），但背后没有真正的 NDIS miniport 驱动在做计数，所以计数器永远是 0。

**这不是什么"性能优化"，而是一个不完整的实现。** Linux 和 macOS 的 loopback 都走完整的设备路径，额外开销微乎其微。微软只是从未投入精力把 loopback 接口做成一个真正的 NDIS 设备，导致没有标准 API 能报告 loopback 流量，只能靠第三方工具（Npcap）来填坑。

---

## 🪟 为什么 Npcap 能抓到？

Npcap 注册了一个 **WFP (Windows Filtering Platform) callout driver**，在 `tcpip.sys` 做环回**之前**拦截数据包，然后复制一份到用户态：

```
tcpip.sys send path
    ↓
  WFP callout (Npcap intercepts and copies here)
    ↓
  short-circuit loopback to receive path
```

这不是通过 NDIS 层实现的，而是在更上层——WFP 是 `tcpip.sys` 内部的 hook 点。

这就是为什么 Npcap 安装时需要勾选 **"Support loopback traffic capture"**——这会启用 WFP callout 驱动，并创建 `NPF_Loopback` 虚拟适配器供 `pcap` 库使用。

---

## ⚖️ 与 Linux / macOS 的对比

### Linux

Linux 的 `lo` 接口是一个**真正的网络设备**，有完整的驱动实现（`drivers/net/loopback.c`）：

```
App → socket → TCP/IP stack → dev_queue_xmit() → lo driver → netif_rx() → receive path
                                    ↑
                              lo driver updates stats normally here
```

`loopback_xmit()` 函数会正常更新 `dev->stats`，所以 `/proc/net/dev` 里 `lo` 的 `RX bytes` / `TX bytes` 是完全准确的。

```c
// Simplified Linux kernel loopback_xmit()
static netdev_tx_t loopback_xmit(struct sk_buff *skb, struct net_device *dev) {
    len = skb->len;
    dev->stats.tx_bytes += len;   // ← actually updated!
    dev->stats.tx_packets++;
    dev->stats.rx_bytes += len;
    dev->stats.rx_packets++;
    netif_rx(skb);                // deliver to receive path
    return NETDEV_TX_OK;
}
```

### macOS

macOS 的 `lo0` 接口与 Linux 类似，也是一个**真正具备 BPF 能力的网络接口**。loopback 流量会经过 `if_loop.c` 驱动，BPF tap 可以在那里抓包，`netstat -I lo0` 能看到真实的计数器。

macOS 继承了 BSD 的设计哲学——loopback 就是一个普通网络接口，只是没有物理硬件。

---

## 🧠 设计哲学总结

|                          | Windows                              | Linux                            | macOS                        |
| ------------------------ | ------------------------------------ | -------------------------------- | ---------------------------- |
| Loopback 实现层          | `tcpip.sys` 内部短路                 | `lo` 设备驱动                    | `lo0` 设备驱动               |
| 经过网络设备层？         | ❌ 不经过 NDIS                       | ✅ 完整走 `dev_queue_xmit` 路径  | ✅ 完整走 `if_output` 路径   |
| 计数器正确？             | ❌ 始终为 0                          | ✅ 正确                          | ✅ 正确                      |
| 原生 BPF/pcap 抓包？     | ❌ 需要 Npcap WFP 补救               | ✅ 原生支持                      | ✅ 原生支持                  |
| 设计理念                 | 功能缺失，实现不完整                 | 一切皆设备，统一抽象             | BSD 传统，一切皆接口         |

**根本原因是 Windows 的 loopback 实现不完整**，不是什么刻意的设计权衡。Linux 的 `lo` 驱动在 loopback 路径上只多了几个函数调用——开销微乎其微——却换来了与所有标准监控和抓包工具的完全兼容。微软只是没有把这个活干完：loopback 伪接口出现在接口列表里，但背后没有真正的驱动支撑。

---

## 🧭 winload 的解决方案

winload 使用 **Npcap** 作为 Windows loopback 捕获后端：

- **`--npcap` (推荐)**: 通过 Npcap 的 WFP callout 捕获真实 loopback 数据包，数据准确。
  需要安装 [Npcap](https://npcap.com/#download)，安装时勾选 "Support loopback traffic capture"。

> 我曾经尝试过直接轮询 `GetIfEntry` / `GetIfTable` 计数器，希望能绕开 Npcap 依赖。结果呢？在我测试的每个 Windows 版本上，计数器都雷打不动地保持为 0。如上文所述，loopback 伪接口背后没有 NDIS 驱动，根本没有东西在计数。最终我删除了那部分代码。感谢微软一贯的 *稳定发挥*。

所以是的——在 Windows 上监控回环流量，必须安装第三方驱动。而 Linux 和 macOS 上开箱即用，因为这些操作系统从一开始就把 loopback 当成真正的网络设备来对待。Windows 上则靠 [Npcap](https://npcap.com/#download) 项目填了操作系统留下的坑。

在 Linux / macOS 上，loopback 流量通过 [`sysinfo`](https://crates.io/crates/sysinfo) crate 直接获取，无需额外参数。

## 📦 Windows 分发矩阵

| Windows release / channel | OS / Arch | `--npcap` | Accurate Windows loopback capture | Uses system Npcap | Bundles Npcap | npm | Scoop | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `winload-windows-x86_64-msvc-npcap.exe` | Windows / x86_64 | Yes | Yes, when Npcap is installed and loopback capture is enabled | Yes | No | ✅ | ✅ | MSVC build with delay-loaded `wpcap.dll` |
| `winload-windows-x86_64-msvc-no-npcap.exe` | Windows / x86_64 | No | No | No | No | ❌ | ❌ | No Npcap support; normal NIC traffic still works |
| `winload-windows-aarch64-msvc-npcap.exe` | Windows / ARM64 | Yes | Yes, when Npcap is installed and loopback capture is enabled | Yes | No | ✅ | ✅ | ARM64 MSVC build with delay-loaded `wpcap.dll` |
| `winload-windows-aarch64-msvc-no-npcap.exe` | Windows / ARM64 | No | No | No | No | ❌ | ❌ | ARM64 build without Npcap support |

### 补充说明

- winload 从不把 Npcap 打包进程序；所有 `npcap` 构建都使用用户系统里安装的 Npcap。
- 延迟加载 `wpcap.dll` 只能降低未使用 `--npcap` 前的启动失败风险，不能替代系统安装 Npcap。
- `no-npcap` Windows 构建仍然能监控普通网卡流量，只是不能准确捕获 Windows 本地回环流量。
