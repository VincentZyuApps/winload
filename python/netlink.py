"""
netlink.py - RTNETLINK backend for Linux/Android.

Uses pyroute2 to read interface addresses and traffic counters without
depending on /proc/net/dev.
"""

from __future__ import annotations

import socket
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class NetlinkDevice:
    name: str
    addrs: List[str] = field(default_factory=list)


@dataclass
class NetlinkStats:
    bytes_recv: int
    bytes_sent: int
    packets_recv: int = 0
    packets_sent: int = 0


def _import_iproute():
    try:
        from pyroute2 import IPRoute
    except Exception as e:
        raise RuntimeError(
            "failed to import pyroute2 for --netlink; install pyroute2 on Linux/Android"
        ) from e
    return IPRoute


def _attrs_to_dict(msg) -> dict:
    return dict(msg.get("attrs", []))


def _stats_from_attrs(attrs: dict) -> Optional[NetlinkStats]:
    stats = attrs.get("IFLA_STATS64") or attrs.get("IFLA_STATS")
    if not stats:
        return None
    return NetlinkStats(
        bytes_recv=int(stats.get("rx_bytes", 0)),
        bytes_sent=int(stats.get("tx_bytes", 0)),
        packets_recv=int(stats.get("rx_packets", 0)),
        packets_sent=int(stats.get("tx_packets", 0)),
    )


def _read_netlink():
    IPRoute = _import_iproute()
    ipr = None
    try:
        ipr = IPRoute()
        links = ipr.get_links()
        addrs = ipr.get_addr(family=socket.AF_INET)
    except Exception as e:
        raise RuntimeError(f"failed to read RTNETLINK data: {e}") from e
    finally:
        if ipr is not None:
            ipr.close()
    return links, addrs


def _ipv4_by_index(addrs) -> Dict[int, List[str]]:
    result: Dict[int, List[str]] = {}
    for addr in addrs:
        index = addr.get("index")
        attrs = _attrs_to_dict(addr)
        local = attrs.get("IFA_LOCAL") or attrs.get("IFA_ADDRESS")
        if index is not None and local:
            result.setdefault(int(index), []).append(str(local))
    return result


def netlink_devices() -> List[NetlinkDevice]:
    links, addrs = _read_netlink()
    ipv4 = _ipv4_by_index(addrs)
    devices: List[NetlinkDevice] = []

    for link in links:
        index = int(link.get("index", 0))
        attrs = _attrs_to_dict(link)
        name = attrs.get("IFLA_IFNAME")
        if not name:
            continue
        state = str(attrs.get("IFLA_OPERSTATE", "")).upper()
        if state == "DOWN":
            continue
        devices.append(NetlinkDevice(name=str(name), addrs=ipv4.get(index, [])))

    devices.sort(key=lambda d: d.name)
    return devices


def netlink_collect() -> Dict[str, NetlinkStats]:
    links, _ = _read_netlink()
    snapshots: Dict[str, NetlinkStats] = {}

    for link in links:
        attrs = _attrs_to_dict(link)
        name = attrs.get("IFLA_IFNAME")
        if not name:
            continue
        state = str(attrs.get("IFLA_OPERSTATE", "")).upper()
        if state == "DOWN":
            continue
        stats = _stats_from_attrs(attrs)
        if stats is not None:
            snapshots[str(name)] = stats

    if not snapshots:
        raise RuntimeError("RTNETLINK returned no interface traffic counters")
    return snapshots
