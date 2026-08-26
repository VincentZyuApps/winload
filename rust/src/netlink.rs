// 🔗 Reads Linux and Android network counters directly through RTNETLINK.
//! Linux/Android 网络接口枚举与流量统计模块
//!
#![cfg(any(target_os = "android", target_os = "linux"))]
//! 通过 RTNETLINK（RTM_GETLINK + IFLA_STATS64）获取各接口的 rx/tx 字节数，
//! 通过 getifaddrs() 枚举接口名称和 IPv4 地址。
//!
//! 此模块仅在 Android 平台编译，作为 sysinfo 的回退方案。
//! （Android SELinux 限制导致 /proc/net/dev 与 /sys/class/net/statistics 均不可访问）

use crate::collector::{DeviceInfo, Snapshot};
use libc;
use std::collections::HashMap;

pub(crate) fn netlink_collect(elapsed: f64) -> HashMap<String, Snapshot> {
    const RTM_GETLINK: u16 = 18;
    const RTM_NEWLINK: u16 = 16;
    const NLM_F_REQUEST: u16 = 1;
    const NLM_F_DUMP: u16 = 0x300;
    const NLMSG_ERROR: u16 = 2;
    const NLMSG_DONE: u16 = 3;
    const IFLA_IFNAME: u16 = 3;
    const IFLA_STATS64: u16 = 23;
    const NLMSG_HDR_LEN: usize = 16;
    const IFINFOMSG_LEN: usize = 16;
    const REQUEST_SEQUENCE: u32 = 1;

    #[repr(C)]
    struct SockaddrNl {
        family: u16,
        pad: u16,
        pid: u32,
        groups: u32,
    }

    let mut result = HashMap::new();
    unsafe {
        let fd = libc::socket(libc::AF_NETLINK, libc::SOCK_RAW, 0);
        if fd < 0 {
            return result;
        }

        let timeout = libc::timeval {
            tv_sec: 1,
            tv_usec: 0,
        };
        if libc::setsockopt(
            fd,
            libc::SOL_SOCKET,
            libc::SO_RCVTIMEO,
            &timeout as *const _ as *const libc::c_void,
            std::mem::size_of::<libc::timeval>() as libc::socklen_t,
        ) < 0
        {
            libc::close(fd);
            return result;
        }

        let mut req = [0u8; NLMSG_HDR_LEN + IFINFOMSG_LEN];
        req[0..4].copy_from_slice(&(req.len() as u32).to_ne_bytes());
        req[4..6].copy_from_slice(&RTM_GETLINK.to_ne_bytes());
        req[6..8].copy_from_slice(&(NLM_F_REQUEST | NLM_F_DUMP).to_ne_bytes());
        req[8..12].copy_from_slice(&REQUEST_SEQUENCE.to_ne_bytes());
        let sa = SockaddrNl {
            family: libc::AF_NETLINK as u16,
            pad: 0,
            pid: 0,
            groups: 0,
        };

        let sent = libc::sendto(
            fd,
            req.as_ptr() as *const libc::c_void,
            req.len(),
            0,
            &sa as *const _ as *const libc::sockaddr,
            std::mem::size_of::<SockaddrNl>() as libc::socklen_t,
        );
        if sent < 0 {
            libc::close(fd);
            return result;
        }

        let mut buf = vec![0u8; 32768];
        let mut completed = false;
        'outer: loop {
            let mut peer = SockaddrNl {
                family: 0,
                pad: 0,
                pid: 0,
                groups: 0,
            };
            let mut peer_len = std::mem::size_of::<SockaddrNl>() as libc::socklen_t;
            let n = libc::recvfrom(
                fd,
                buf.as_mut_ptr() as *mut libc::c_void,
                buf.len(),
                0,
                &mut peer as *mut _ as *mut libc::sockaddr,
                &mut peer_len,
            );
            if n <= 0 {
                break;
            }
            if peer_len != std::mem::size_of::<SockaddrNl>() as libc::socklen_t
                || peer.family != libc::AF_NETLINK as u16
                || peer.pid != 0
                || peer.groups != 0
            {
                continue;
            }
            let n = n as usize;
            let mut off = 0usize;
            while off + NLMSG_HDR_LEN <= n {
                let msg_len = u32::from_ne_bytes(buf[off..off + 4].try_into().unwrap()) as usize;
                let msg_type = u16::from_ne_bytes(buf[off + 4..off + 6].try_into().unwrap());
                let msg_seq = u32::from_ne_bytes(buf[off + 8..off + 12].try_into().unwrap());
                let msg_pid = u32::from_ne_bytes(buf[off + 12..off + 16].try_into().unwrap());
                let Some(end) = off.checked_add(msg_len) else {
                    break;
                };
                if msg_len < NLMSG_HDR_LEN || end > n {
                    break;
                }
                let Some(aligned_len) = msg_len.checked_add(3).map(|len| len & !3) else {
                    break;
                };
                let Some(next_off) = off.checked_add(aligned_len) else {
                    break;
                };
                if msg_seq != REQUEST_SEQUENCE || msg_pid != 0 {
                    off = next_off;
                    continue;
                }
                match msg_type {
                    NLMSG_DONE => {
                        completed = true;
                        break 'outer;
                    }
                    NLMSG_ERROR => break 'outer,
                    RTM_NEWLINK => {
                        let mut rta = off + NLMSG_HDR_LEN + IFINFOMSG_LEN;
                        let mut iface: Option<String> = None;
                        let mut rx = 0u64;
                        let mut tx = 0u64;
                        let mut has_stats = false;
                        while rta + 4 <= end {
                            let rlen = u16::from_ne_bytes([buf[rta], buf[rta + 1]]) as usize;
                            let rtyp = u16::from_ne_bytes([buf[rta + 2], buf[rta + 3]]);
                            if rlen < 4 || rta + rlen > end {
                                break;
                            }
                            match rtyp {
                                IFLA_IFNAME => {
                                    let s = &buf[rta + 4..rta + rlen];
                                    let nul = s.iter().position(|&b| b == 0).unwrap_or(s.len());
                                    iface = Some(String::from_utf8_lossy(&s[..nul]).into_owned());
                                }
                                IFLA_STATS64 => {
                                    let d = &buf[rta + 4..rta + rlen];
                                    if d.len() >= 32 {
                                        rx = u64::from_ne_bytes(d[16..24].try_into().unwrap());
                                        tx = u64::from_ne_bytes(d[24..32].try_into().unwrap());
                                        has_stats = true;
                                    }
                                }
                                _ => {}
                            }
                            rta += (rlen + 3) & !3;
                        }
                        if let (Some(name), true) = (iface, has_stats) {
                            result.insert(
                                name,
                                Snapshot {
                                    elapsed_secs: elapsed,
                                    bytes_recv: rx,
                                    bytes_sent: tx,
                                },
                            );
                        }
                    }
                    _ => {}
                }
                off = next_off;
            }
        }
        libc::close(fd);
    }
    if completed {
        result
    } else {
        HashMap::new()
    }
}

pub(crate) fn netlink_devices() -> Vec<DeviceInfo> {
    use std::ffi::CStr;

    let mut map: HashMap<String, Vec<String>> = HashMap::new();
    unsafe {
        let mut ifap: *mut libc::ifaddrs = std::ptr::null_mut();
        if libc::getifaddrs(&mut ifap) != 0 {
            return vec![];
        }
        let mut ifa = ifap;
        while !ifa.is_null() {
            let name = CStr::from_ptr((*ifa).ifa_name)
                .to_string_lossy()
                .into_owned();
            let sa = (*ifa).ifa_addr;
            if !sa.is_null() && (*sa).sa_family == libc::AF_INET as libc::sa_family_t {
                let sin = &*(sa as *const libc::sockaddr_in);
                let b = sin.sin_addr.s_addr.to_ne_bytes();
                map.entry(name)
                    .or_default()
                    .push(format!("{}.{}.{}.{}", b[0], b[1], b[2], b[3]));
            } else {
                map.entry(name).or_default();
            }
            ifa = (*ifa).ifa_next;
        }
        libc::freeifaddrs(ifap);
    }
    let mut devs: Vec<DeviceInfo> = map
        .into_iter()
        .map(|(name, addrs)| DeviceInfo { name, addrs })
        .collect();
    devs.sort_by(|a, b| a.name.cmp(&b.name));
    devs
}
