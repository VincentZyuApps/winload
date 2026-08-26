// 🪟 Captures and counts Windows loopback traffic through Npcap when enabled.
//! Windows 本地回环流量捕获模块
//!
//! 通过 Npcap (pcap crate) 捕获 \Device\NPF_Loopback 上的数据包。
//!
//! 此模块仅在 Windows 平台编译。非 Windows 平台下提供空实现。

use std::sync::atomic::{AtomicBool, AtomicU64, Ordering};
use std::sync::Arc;

/// Npcap 下载地址 (仅 Windows)
#[cfg(target_os = "windows")]
pub const NPCAP_URL: &str = "https://npcap.com/#download";

/// 回环流量计数器 (线程安全，可在采集线程和主线程之间共享)
#[derive(Clone)]
pub struct LoopbackCounters {
    pub bytes_recv: Arc<AtomicU64>,
    pub bytes_sent: Arc<AtomicU64>,
}

impl LoopbackCounters {
    pub fn new() -> Self {
        Self {
            bytes_recv: Arc::new(AtomicU64::new(0)),
            bytes_sent: Arc::new(AtomicU64::new(0)),
        }
    }

    pub fn get_recv(&self) -> u64 {
        self.bytes_recv.load(Ordering::Relaxed)
    }

    pub fn get_sent(&self) -> u64 {
        self.bytes_sent.load(Ordering::Relaxed)
    }
}

/// Owns the Npcap capture thread and releases it when the application exits.
pub struct LoopbackCapture {
    stop: Arc<AtomicBool>,
    #[cfg(target_os = "windows")]
    worker: Option<std::thread::JoinHandle<()>>,
}

impl LoopbackCapture {
    #[cfg(target_os = "windows")]
    fn new(stop: Arc<AtomicBool>, worker: std::thread::JoinHandle<()>) -> Self {
        Self {
            stop,
            worker: Some(worker),
        }
    }

    pub fn stop(&self) {
        self.stop.store(true, Ordering::Relaxed);
    }
}

impl Drop for LoopbackCapture {
    fn drop(&mut self) {
        self.stop();
        #[cfg(target_os = "windows")]
        if let Some(worker) = self.worker.take() {
            let _ = worker.join();
        }
    }
}

/// 回环捕获模式
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum LoopbackMode {
    /// 不捕获回环流量 (默认)
    None,
    /// 使用 Npcap (pcap) 捕获
    Npcap,
}

// ═══════════════════════════════════════════════════════════
//  Windows 实现
// ═══════════════════════════════════════════════════════════

#[cfg(target_os = "windows")]
pub mod platform {
    use super::*;
    #[cfg(feature = "npcap")]
    use std::thread;

    /// Check if wpcap.dll (Npcap) is available on this system.
    /// Must be called before any pcap API calls when using /DELAYLOAD,
    /// otherwise the delay-load helper will raise a fatal exception.
    #[cfg(feature = "npcap")]
    fn is_npcap_installed() -> bool {
        extern "system" {
            fn LoadLibraryA(name: *const u8) -> *mut std::ffi::c_void;
            fn FreeLibrary(handle: *mut std::ffi::c_void) -> i32;
        }
        unsafe {
            let handle = LoadLibraryA(b"wpcap.dll\0".as_ptr());
            if handle.is_null() {
                false
            } else {
                FreeLibrary(handle);
                true
            }
        }
    }

    /// 启动 Npcap 回环捕获线程
    ///
    /// 返回 Ok(info_msg) 成功时，后台线程会持续累加计数器。
    /// 返回 Err(msg) 如果 Npcap 不可用或打开设备失败。
    #[cfg(feature = "npcap")]
    pub fn start_npcap(counters: LoopbackCounters) -> Result<(String, LoopbackCapture), String> {
        // Pre-flight: verify wpcap.dll is loadable before calling any pcap functions.
        // The binary uses /DELAYLOAD:wpcap.dll, so pcap functions are not resolved
        // until first call. If the DLL is missing, that first call would crash.
        if !is_npcap_installed() {
            return Err(format!(
                "Npcap is not installed on this system.\n\n\
                 The --npcap flag requires Npcap to capture loopback traffic.\n\
                 Please install Npcap from: {NPCAP_URL}\n\
                 (Enable 'Support loopback traffic capture' during installation)\n\n\
                 Or run without the --npcap flag."
            ));
        }

        // 尝试查找 Npcap Loopback 适配器
        let devices = pcap::Device::list().map_err(|e| {
            format!(
                "Failed to list pcap devices: {e}\n\n\
                 Npcap is not installed or not working.\n\
                 Please install Npcap from: {NPCAP_URL}\n\
                 (Enable 'Support loopback traffic capture' during installation)\n\n\
                 Or try running without --npcap flag, or use --etw instead."
            )
        })?;

        // Npcap 的回环设备通常包含 "Loopback" 或 "NPF_Loopback"
        let loopback_dev = devices
            .iter()
            .find(|d| {
                let name_lower = d.name.to_lowercase();
                let desc_lower = d.desc.as_deref().unwrap_or("").to_lowercase();
                name_lower.contains("loopback")
                    || name_lower.contains("npf_loopback")
                    || desc_lower.contains("adapter for loopback traffic capture")
                    || desc_lower.contains("npcap loopback")
            })
            .ok_or_else(|| {
                let available: Vec<String> = devices
                    .iter()
                    .map(|d| {
                        format!(
                            "  {} ({})",
                            d.name,
                            d.desc.as_deref().unwrap_or("no description")
                        )
                    })
                    .collect();
                format!(
                    "Npcap loopback adapter not found.\n\n\
                     Make sure Npcap is installed with 'Support loopback traffic' enabled.\n\
                     Download Npcap: {NPCAP_URL}\n\n\
                     Or try running without --npcap flag, or use --etw instead.\n\n\
                     Available devices:\n{}",
                    available.join("\n")
                )
            })?;

        let dev_name = loopback_dev.name.clone();
        let info_msg = format!("[npcap] Found loopback device: {dev_name}");

        // 在后台线程中持续捕获，并在应用退出时停止并回收线程。
        let stop = Arc::new(AtomicBool::new(false));
        let thread_stop = Arc::clone(&stop);
        let worker = thread::Builder::new()
            .name("npcap-loopback".to_string())
            .spawn(move || {
                if let Err(e) = npcap_capture_loop(&dev_name, &counters, &thread_stop) {
                    eprintln!("[npcap] Capture error: {e}");
                }
            })
            .map_err(|e| format!("Failed to spawn npcap thread: {e}"))?;

        Ok((info_msg, LoopbackCapture::new(stop, worker)))
    }

    #[cfg(feature = "npcap")]
    fn npcap_capture_loop(
        device_name: &str,
        counters: &LoopbackCounters,
        stop: &AtomicBool,
    ) -> Result<(), String> {
        let mut cap = pcap::Capture::from_device(device_name)
            .map_err(|e| format!("Cannot open device: {e}"))?
            .promisc(false)
            .snaplen(96) // 只需要 IP 头来获取包长度
            .timeout(100) // 100ms 超时，避免阻塞
            .open()
            .map_err(|e| format!("Cannot start capture: {e}"))?;

        while !stop.load(Ordering::Relaxed) {
            match cap.next_packet() {
                Ok(packet) => {
                    // Npcap loopback 使用 DLT_NULL 格式:
                    // 前 4 字节是地址族 (AF_INET=2, AF_INET6=23/30)
                    // 之后是完整的 IP 包
                    let data = packet.data;
                    if data.len() < 4 {
                        continue;
                    }

                    // 获取 IP 包长度 (跳过 4 字节的 DLT_NULL 头)
                    let ip_payload = &data[4..];
                    let pkt_len = ip_payload.len() as u64;

                    if ip_payload.is_empty() {
                        continue;
                    }

                    // 判断是 incoming 还是 outgoing:
                    // 对于 loopback，发送和接收的包都会被捕获。
                    // 简单方法: 所有包同时计入 recv 和 sent (因为回环流量
                    // 是自己发给自己的，收发对等)
                    counters.bytes_recv.fetch_add(pkt_len, Ordering::Relaxed);
                    counters.bytes_sent.fetch_add(pkt_len, Ordering::Relaxed);
                }
                Err(pcap::Error::TimeoutExpired) => {
                    // 正常超时，继续循环
                    continue;
                }
                Err(e) => {
                    return Err(format!("Packet capture error: {e}"));
                }
            }
        }
        Ok(())
    }

    #[cfg(not(feature = "npcap"))]
    pub fn start_npcap(_counters: LoopbackCounters) -> Result<(String, LoopbackCapture), String> {
        Err(format!(
            "winload was compiled without Npcap support (feature 'npcap' disabled).\n\
             Recompile with: cargo build --features npcap\n\n\
             Or download a pre-built release that includes Npcap support.\n\
             Npcap download: {NPCAP_URL}"
        ))
    }
}

// ═══════════════════════════════════════════════════════════
//  非 Windows 平台 — 空实现 (Linux/macOS 不需要特殊处理)
// ═══════════════════════════════════════════════════════════

#[cfg(not(target_os = "windows"))]
pub mod platform {
    use super::*;

    pub fn start_npcap(_counters: LoopbackCounters) -> Result<(String, LoopbackCapture), String> {
        Err("--npcap is only supported on Windows. \
             On Linux/macOS, loopback traffic is natively available."
            .to_string())
    }
}
