# 📡 Collects network interface counters with psutil or the optional Netlink backend.
"""
collector.py - 网络流量数据采集模块
通过 psutil 采集各网卡的累计收发字节数，供上层统计和绘图使用。
Linux/Android 可通过 --netlink 显式启用 RTNETLINK backend。
"""

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import psutil


@dataclass
class Snapshot:
    """单次采样快照"""
    timestamp: float          # time.time()
    bytes_recv: int           # 累计接收字节
    bytes_sent: int           # 累计发送字节
    packets_recv: int = 0
    packets_sent: int = 0


@dataclass
class DeviceInfo:
    """网卡设备信息"""
    name: str
    addrs: List[str] = field(default_factory=list)  # IP 地址列表


class Collector:
    """
    网络流量采集器。
    每次调用 collect() 会读取所有网卡的累计字节数并生成 Snapshot。
    """

    def __init__(self, ignored_interfaces: Optional[List[str]] = None, use_netlink: bool = False):
        self._ignored = set(ignored_interfaces or [])
        self._use_netlink = use_netlink
        self._devices: Dict[str, DeviceInfo] = {}
        self._refresh_devices()

    @property
    def using_netlink(self) -> bool:
        return self._use_netlink

    def _refresh_devices(self) -> None:
        """刷新可用网卡列表及其 IP 地址"""
        if self._use_netlink:
            from .netlink import netlink_devices

            self._devices.clear()
            for dev in netlink_devices():
                if dev.name in self._ignored:
                    continue
                self._devices[dev.name] = DeviceInfo(name=dev.name, addrs=dev.addrs)
            return

        addrs = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        self._devices.clear()
        for name, addr_list in addrs.items():
            if name in self._ignored:
                continue
            # 只保留 UP 状态的接口
            if name in stats and not stats[name].isup:
                continue
            ips = []
            for a in addr_list:
                # AF_INET = 2
                if a.family.value == 2 and a.address:
                    ips.append(a.address)
            self._devices[name] = DeviceInfo(name=name, addrs=ips)

    @property
    def device_names(self) -> List[str]:
        """返回所有可用设备名（排序后）"""
        return sorted(self._devices.keys())

    def get_device_info(self, name: str) -> Optional[DeviceInfo]:
        return self._devices.get(name)

    def collect(self) -> Dict[str, Snapshot]:
        """
        一次性采集所有网卡的当前累计数据。
        返回 {device_name: Snapshot}
        """
        ts = time.time()
        if self._use_netlink:
            from .netlink import netlink_collect

            counters = netlink_collect()
            result: Dict[str, Snapshot] = {}
            for name in self._devices:
                if name not in counters:
                    continue
                c = counters[name]
                result[name] = Snapshot(
                    timestamp=ts,
                    bytes_recv=c.bytes_recv,
                    bytes_sent=c.bytes_sent,
                    packets_recv=c.packets_recv,
                    packets_sent=c.packets_sent,
                )
            return result

        counters = psutil.net_io_counters(pernic=True)
        result: Dict[str, Snapshot] = {}
        for name in self._devices:
            if name not in counters:
                continue
            c = counters[name]
            result[name] = Snapshot(
                timestamp=ts,
                bytes_recv=c.bytes_recv,
                bytes_sent=c.bytes_sent,
                packets_recv=c.packets_recv,
                packets_sent=c.packets_sent,
            )
        return result
