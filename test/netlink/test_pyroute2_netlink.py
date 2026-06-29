#!/usr/bin/env python3
"""
Probe pyroute2 RTNETLINK support for winload.

Run on Linux / Android Termux / Termux proot:

    python test/netlink/probe_pyroute2_netlink.py

Install dependency if needed:

    python -m pip install pyroute2
"""

from __future__ import annotations

import json
import platform
import socket
import sys
import traceback
from typing import Any


def attr(attrs: list[tuple[str, Any]], name: str, default: Any = None) -> Any:
    for key, value in attrs:
        if key == name:
            return value
    return default


def compact(value: Any) -> Any:
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, dict):
        return {str(k): compact(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [compact(v) for v in value]
    return value


def print_header() -> None:
    print("== pyroute2 netlink probe ==")
    print(f"python: {sys.version.split()[0]} ({sys.executable})")
    print(f"platform.system: {platform.system()}")
    print(f"platform.release: {platform.release()}")
    print(f"platform.machine: {platform.machine()}")
    print(f"sys.platform: {sys.platform}")
    print()


def main() -> int:
    print_header()

    try:
        from pyroute2 import IPRoute  # type: ignore
    except Exception as exc:
        print("pyroute2 import: FAILED")
        print(f"{type(exc).__name__}: {exc}")
        print()
        print("Try: python -m pip install pyroute2")
        return 2

    print("pyroute2 import: OK")

    try:
        ipr = IPRoute()
    except Exception:
        print("IPRoute open: FAILED")
        traceback.print_exc()
        return 3

    try:
        links = ipr.get_links()
        addrs = ipr.get_addr(family=socket.AF_INET)
    except Exception:
        print("netlink query: FAILED")
        traceback.print_exc()
        ipr.close()
        return 4

    addr_map: dict[int, list[str]] = {}
    for addr_msg in addrs:
        index = addr_msg.get("index")
        if not isinstance(index, int):
            continue
        attrs = addr_msg.get("attrs", [])
        address = attr(attrs, "IFA_ADDRESS")
        if address:
            addr_map.setdefault(index, []).append(str(address))

    print(f"links: {len(links)}")
    print(f"ipv4 addr messages: {len(addrs)}")
    print()

    for link in links:
        index = link.get("index")
        attrs = link.get("attrs", [])
        name = attr(attrs, "IFLA_IFNAME", f"ifindex{index}")
        mtu = attr(attrs, "IFLA_MTU")
        operstate = attr(attrs, "IFLA_OPERSTATE")
        stats64 = attr(attrs, "IFLA_STATS64")
        stats = attr(attrs, "IFLA_STATS")

        chosen_stats = stats64 or stats or {}
        rx = chosen_stats.get("rx_bytes") if isinstance(chosen_stats, dict) else None
        tx = chosen_stats.get("tx_bytes") if isinstance(chosen_stats, dict) else None
        stat_source = "IFLA_STATS64" if stats64 else ("IFLA_STATS" if stats else "none")

        print(f"- {name} (index={index})")
        print(f"  state={operstate} mtu={mtu} ipv4={addr_map.get(index, [])}")
        print(f"  stats_source={stat_source} rx_bytes={rx} tx_bytes={tx}")

        if chosen_stats:
            keys = sorted(str(k) for k in chosen_stats.keys())
            print(f"  stats_keys={keys}")
        else:
            print("  raw_attrs=" + json.dumps(compact(attrs), ensure_ascii=False)[:1000])

    ipr.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
