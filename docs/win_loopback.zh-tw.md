# Windows Loopback 流量監控：為什麼標準 API 不行，Npcap 可以？

> **[📖 English](win_loopback.md)**
> **[📖 简体中文(大陆)](win_loopback.zh-cn.md)**
> **[📖 繁體中文(台灣)](win_loopback.zh-tw.md)**

## ⚡ TL;DR

Windows 的 loopback (`127.0.0.1`) 流量在 `tcpip.sys` 內部直接短路，**完全繞過了 NDIS 網路驅動層**，導致 `GetIfEntry` / `GetIfTable` 的計數器始終為 0。

這是 **Windows 網路棧的功能缺失**——loopback 介面從未被賦予一個完整的 NDIS miniport 驅動，標準的監控 API 對它根本不起作用。

Npcap 透過 WFP (Windows Filtering Platform) callout driver 在短路之前攔截資料包，因此能抓到。

---

## 🏗️ Windows 網路棧架構

```
App  →  Winsock  →  AFD.sys  →  tcpip.sys  →  NDIS  →  NIC driver  →  Hardware
```

### 正常網卡的流量路徑

```
tcpip.sys  →  NDIS (counter +1)  →  miniport driver  →  physical NIC
```

NDIS 驅動在這裡更新 `MIB_IFROW.dwInOctets` / `dwOutOctets`，所以 `GetIfEntry()` 能拿到正確的值。

### Loopback 的流量路徑

```
tcpip.sys  →  direct loopback (short-circuit)  →  receive path
                     ↑
              NDIS layer entirely skipped
              counters never updated
```

當資料發往 `127.0.0.1` 時，`tcpip.sys` 在**傳輸層就直接短路**了——資料包從發送路徑直接複製到接收路徑，**根本不經過 NDIS 層**。

Windows 的 "Loopback Pseudo-Interface 1" 其實是一個**虛擬佔位符**。它出現在 `GetIfTable` 的介面清單裡（`dwType = IF_TYPE_SOFTWARE_LOOPBACK = 24`），但背後沒有真正的 NDIS miniport 驅動在做計數，所以計數器永遠是 0。

**這不是什麼"效能最佳化"，而是一個不完整的實作。** Linux 和 macOS 的 loopback 都走完整的裝置路徑，額外開銷微乎其微。微軟只是從未投入精力把 loopback 介面做成一個真正的 NDIS 裝置，導致沒有標準 API 能報告 loopback 流量，只能靠第三方工具（Npcap）來填坑。

---

## 🪟 為什麼 Npcap 能抓到？

Npcap 註冊了一個 **WFP (Windows Filtering Platform) callout driver**，在 `tcpip.sys` 做環回**之前**攔截資料包，然後複製一份到使用者態：

```
tcpip.sys send path
    ↓
  WFP callout (Npcap intercepts and copies here)
    ↓
  short-circuit loopback to receive path
```

這不是透過 NDIS 層實現的，而是在更上層——WFP 是 `tcpip.sys` 內部的 hook 點。

這就是為什麼 Npcap 安裝時需要勾選 **"Support loopback traffic capture"**——這會啟用 WFP callout 驅動，並建立 `NPF_Loopback` 虛擬介面卡供 `pcap` 函式庫使用。

---

## ⚖️ 與 Linux / macOS 的對比

### Linux

Linux 的 `lo` 介面是一個**真正的網路裝置**，有完整的驅動實作（`drivers/net/loopback.c`）：

```
App → socket → TCP/IP stack → dev_queue_xmit() → lo driver → netif_rx() → receive path
                                    ↑
                              lo driver updates stats normally here
```

`loopback_xmit()` 函式會正常更新 `dev->stats`，所以 `/proc/net/dev` 裡 `lo` 的 `RX bytes` / `TX bytes` 是完全準確的。

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

macOS 的 `lo0` 介面與 Linux 類似，也是一個**真正具備 BPF 能力的網路介面**。loopback 流量會經過 `if_loop.c` 驅動，BPF tap 可以在那裡抓包，`netstat -I lo0` 能看到真實的計數器。

macOS 繼承了 BSD 的設計哲學——loopback 就是一個普通網路介面，只是沒有實體硬體。

---

## 🧠 設計哲學總結

|                          | Windows                              | Linux                            | macOS                        |
| ------------------------ | ------------------------------------ | -------------------------------- | ---------------------------- |
| Loopback 實作層          | `tcpip.sys` 內部短路                 | `lo` 裝置驅動                    | `lo0` 裝置驅動               |
| 經過網路裝置層？         | ❌ 不經過 NDIS                       | ✅ 完整走 `dev_queue_xmit` 路徑  | ✅ 完整走 `if_output` 路徑   |
| 計數器正確？             | ❌ 永遠為 0                          | ✅ 正確                          | ✅ 正確                      |
| 原生 BPF/pcap 抓包？     | ❌ 需要 Npcap WFP 補救               | ✅ 原生支援                      | ✅ 原生支援                  |
| 設計理念                 | 功能缺失，實作不完整                 | 一切皆裝置，統一抽象             | BSD 傳統，一切皆介面         |

**根本原因是 Windows 的 loopback 實作不完整**，並非刻意的設計取捨。Linux 的 `lo` 驅動在 loopback 路徑上只多了幾個函式呼叫——開銷微乎其微——卻換來了與所有標準監控與抓包工具的完全相容。微軟只是沒有把這項工作完成：loopback 虛擬介面有出現在介面清單中，但背後沒有真正的驅動支援。

---

## 🧭 winload 的解決方案

winload 使用 **Npcap** 作為 Windows loopback 擷取後端：

- **`--npcap` (建議)**: 透過 Npcap 的 WFP callout 擷取真實 loopback 封包，資料精準。
  需要安裝 [Npcap](https://npcap.com/#download)，安裝時勾選 "Support loopback traffic capture"。

> 我曾經嘗試過直接輪詢 `GetIfEntry` / `GetIfTable` 計數器，希望能繞過 Npcap 依賴。結果呢？在我測試的每個 Windows 版本上，計數器都紋絲不動地保持為 0。如上文所述，loopback 虛擬介面背後沒有 NDIS 驅動，根本沒有東西在計數。最終我刪除了那部分程式碼。感謝微軟一貫的 *穩定發揮*。

所以是的——在 Windows 上監控回環流量，必須安裝第三方驅動。而 Linux 和 macOS 上開箱即用，因為這些作業系統從一開始就把 loopback 當成真正的網路裝置來對待。Windows 上則靠 [Npcap](https://npcap.com/#download) 專案填了作業系統留下的坑。

在 Linux / macOS 上，loopback 流量透過 [`sysinfo`](https://crates.io/crates/sysinfo) crate 直接取得，不需額外參數。

## 📦 Windows 發佈矩陣

| Windows release / channel | OS / Arch | `--npcap` | Accurate Windows loopback capture | Uses system Npcap | Bundles Npcap | npm | Scoop | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `winload-windows-x86_64-msvc-npcap.exe` | Windows / x86_64 | Yes | Yes, when Npcap is installed and loopback capture is enabled | Yes | No | ✅ | ✅ | MSVC build with delay-loaded `wpcap.dll` |
| `winload-windows-x86_64-msvc-no-npcap.exe` | Windows / x86_64 | No | No | No | No | ❌ | ❌ | No Npcap support; normal NIC traffic still works |
| `winload-windows-aarch64-msvc-npcap.exe` | Windows / ARM64 | Yes | Yes, when Npcap is installed and loopback capture is enabled | Yes | No | ✅ | ✅ | ARM64 MSVC build with delay-loaded `wpcap.dll` |
| `winload-windows-aarch64-msvc-no-npcap.exe` | Windows / ARM64 | No | No | No | No | ❌ | ❌ | ARM64 build without Npcap support |

### 補充說明

- winload 從不把 Npcap 打包進程式；所有 `npcap` 構建都使用使用者系統裡安裝的 Npcap。
- 延遲載入 `wpcap.dll` 只能降低尚未使用 `--npcap` 前的啟動失敗風險，不能取代系統安裝 Npcap。
- `no-npcap` Windows 構建仍然能監控一般網卡流量，只是不能準確擷取 Windows 本地回環流量。
