//! 网络流量数据采集模块
//! 通过 sysinfo 采集各网卡的累计收发字节数，供上层统计和绘图使用。

use sysinfo::Networks;
use std::collections::HashMap;
use std::time::Instant;

/// 单次采样快照
#[derive(Clone, Debug)]
pub struct Snapshot {
    /// 自程序启动以来的秒数
    pub elapsed_secs: f64,
    /// 累计接收字节数
    pub bytes_recv: u64,
    /// 累计发送字节数
    pub bytes_sent: u64,
}

/// 网卡设备信息
#[derive(Clone, Debug)]
pub struct DeviceInfo {
    /// 设备名称
    pub name: String,
    /// IPv4 地址列表
    pub addrs: Vec<String>,
}

/// 网络流量采集器
pub struct Collector {
    networks: Networks,
    start: Instant,
}

impl Collector {
    pub fn new() -> Self {
        Self {
            networks: Networks::new_with_refreshed_list(),
            start: Instant::now(),
        }
    }

    /// 打印所有网络接口的调试信息
    pub fn print_debug_info(&self) {
        println!("\n=== Network Interfaces Debug Info ===");
        println!("Total interfaces detected by sysinfo: {}\n", self.networks.len());

        for (name, data) in self.networks.iter() {
            println!("Interface: {}", name);
            println!("  MAC address: {}", data.mac_address());
            println!("  Total received: {} bytes", data.total_received());
            println!("  Total transmitted: {} bytes", data.total_transmitted());
            println!("  IP networks:");
            
            let ip_networks = data.ip_networks();
            if ip_networks.is_empty() {
                println!("    (none)");
            } else {
                for ip in ip_networks {
                    println!("    - {} (prefix: {})", ip.addr, ip.prefix);
                }
            }
            println!();
        }

        println!("Filtered devices (IPv4 only, used in UI): {}\n", self.devices().len());
        for dev in self.devices() {
            println!("  - {} [{}]", dev.name, dev.addrs.join(", "));
        }

        // Windows loopback 说明
        #[cfg(target_os = "windows")]
        {
            println!("\nNote: Windows loopback (127.0.0.1) traffic is not visible via");
            println!("  standard network APIs. The Loopback device appears in the");
            println!("  list but may show zero traffic.");
        }
    }

    /// 获取所有可用设备信息（按名称排序）
    pub fn devices(&self) -> Vec<DeviceInfo> {
        let mut devs: Vec<DeviceInfo> = self
            .networks
            .iter()
            .map(|(name, data)| {
                let addrs: Vec<String> = data
                    .ip_networks()
                    .iter()
                    .filter(|n| n.addr.is_ipv4())
                    .map(|n| n.addr.to_string())
                    .collect();
                DeviceInfo {
                    name: name.to_string(),
                    addrs,
                }
            })
            .collect();
        
        // Windows 平台手动添加 Loopback 接口（sysinfo 不返回）
        #[cfg(target_os = "windows")]
        {
            let has_loopback = devs.iter().any(|d| {
                d.name.to_lowercase().contains("loopback") 
                || d.addrs.iter().any(|a| a.starts_with("127."))
            });
            
            if !has_loopback {
                devs.push(DeviceInfo {
                    name: "Loopback Pseudo-Interface 1".to_string(),
                    addrs: vec!["127.0.0.1".to_string()],
                });
            }
        }
        
        devs.sort_by(|a, b| a.name.cmp(&b.name));
        devs
    }

    /// 采集一次所有网卡的当前累计数据
    pub fn collect(&mut self) -> HashMap<String, Snapshot> {
        // refresh() 只刷新已有接口的数据，不重建列表，计数器不会丢失
        self.networks.refresh();
        let elapsed = self.start.elapsed().as_secs_f64();

        #[cfg(target_os = "windows")]
        let mut snapshots: HashMap<String, Snapshot> = self.networks
            .iter()
            .map(|(name, data)| {
                (
                    name.to_string(),
                    Snapshot {
                        elapsed_secs: elapsed,
                        bytes_recv: data.total_received(),
                        bytes_sent: data.total_transmitted(),
                    },
                )
            })
            .collect();
        
        #[cfg(not(target_os = "windows"))]
        let snapshots: HashMap<String, Snapshot> = self.networks
            .iter()
            .map(|(name, data)| {
                (
                    name.to_string(),
                    Snapshot {
                        elapsed_secs: elapsed,
                        bytes_recv: data.total_received(),
                        bytes_sent: data.total_transmitted(),
                    },
                )
            })
            .collect();
        
        // Windows 平台为 Loopback 添加快照（暂无法获取真实流量）
        #[cfg(target_os = "windows")]
        {
            let has_loopback_snapshot = snapshots.keys().any(|k| {
                k.to_lowercase().contains("loopback")
            });

            if !has_loopback_snapshot {
                snapshots.insert(
                    "Loopback Pseudo-Interface 1".to_string(),
                    Snapshot {
                        elapsed_secs: elapsed,
                        bytes_recv: 0,
                        bytes_sent: 0,
                    },
                );
            }
        }
        
        snapshots
    }
}
