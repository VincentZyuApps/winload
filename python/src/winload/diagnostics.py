# Reports version, build, system, and network-interface diagnostic information.
"""Non-interactive diagnostic and version helpers."""

import importlib.util
import platform
import re
import sys
from importlib.metadata import version as get_pkg_version
from pathlib import Path

from .emoji import decorate
from .i18n import t


def _load_format_build_info():
    module_name = f"{__package__}._build_info"
    try:
        from ._build_info import format_build_info as formatter
    except ModuleNotFoundError as exc:
        if exc.name != module_name:
            raise
    else:
        return formatter

    source_path = Path(__file__).resolve().parents[2] / "_build_info.py"
    if not source_path.is_file():
        raise ImportError(f"Build info module not found: {source_path}")
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load build info module: {source_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(module_name, None)
        raise
    formatter = getattr(module, "format_build_info", None)
    if not callable(formatter):
        raise ImportError(f"format_build_info is missing from: {source_path}")
    return formatter


format_build_info = _load_format_build_info()


def _display_version(version: str) -> str:
    """Restore the project's cross-language prerelease spelling after PEP 440 normalization."""
    match = re.fullmatch(r"(\d+(?:\.\d+)*)(a|b|rc)(\d+)", version)
    if not match:
        return version
    base, stage, number = match.groups()
    stage = {"a": "alpha", "b": "beta", "rc": "rc"}[stage]
    return f"{base}-{stage}.{number}"


def get_version() -> str:
    try:
        return _display_version(get_pkg_version("winload"))
    except Exception:
        pass
    try:
        text = (Path(__file__).resolve().parents[2] / "pyproject.toml").read_text(
            encoding="utf-8"
        )
        match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
        if match:
            return match.group(1)
    except Exception:
        pass
    return "unknown"


def get_system_info() -> str:
    return f"System: {platform.system()} | Arch: {platform.machine()}"


def get_help_system_info(emoji: bool = False) -> str:
    text = f"{t('help_system')}: {platform.system()} | {t('help_arch')}: {platform.machine()}"
    return decorate(emoji, "help_system_info", text)


def print_system_info() -> None:
    print(f"\n{get_system_info()}", file=sys.stderr)


def print_debug_info(emoji: bool = False, use_netlink: bool = False) -> None:
    if use_netlink:
        _print_netlink_debug(emoji)
    else:
        _print_psutil_debug(emoji)


def _print_netlink_debug(emoji: bool) -> None:
    from .netlink import netlink_collect, netlink_devices

    if emoji:
        print("\n\U0001f50d\U0001f310 Network Interfaces Debug Info (netlink) \U0001f5a7\u2728")
    print("\n=== Network Interfaces Debug Info (netlink) ===")
    print("Using RTNETLINK via pyroute2.\n")
    devices = netlink_devices()
    counters = netlink_collect()
    print(f"Total interfaces detected by netlink: {len(devices)}\n")
    for dev in devices:
        print(f"Interface: {dev.name}")
        print(f"  IPv4: {', '.join(dev.addrs) if dev.addrs else '(none)'}")
        if dev.name in counters:
            counter = counters[dev.name]
            print(f"  Total received: {counter.bytes_recv} bytes")
            print(f"  Total transmitted: {counter.bytes_sent} bytes")
        print()
    print(f"Filtered devices (netlink): {len(devices)}\n")
    for dev in devices:
        print(f"  - {dev.name} [{', '.join(dev.addrs)}]")
    print(f"\n{get_system_info()}")


def _print_psutil_debug(emoji: bool) -> None:
    import psutil

    if emoji:
        print("\n\U0001f50d\U0001f310 Network Interfaces Debug Info \U0001f5a7\u2728")
    print("\n=== Network Interfaces Debug Info ===")
    addrs = psutil.net_if_addrs()
    stats_map = psutil.net_if_stats()
    counters = psutil.net_io_counters(pernic=True)
    print(f"Total interfaces detected by psutil: {len(addrs)}\n")
    for name in sorted(addrs):
        print(f"Interface: {name}")
        if name in stats_map:
            info = stats_map[name]
            status = "UP" if info.isup else "DOWN"
            print(f"  Status: {status} | Speed: {info.speed} Mbps | MTU: {info.mtu}")
        print("  Addresses:")
        if not addrs[name]:
            print("    (none)")
        else:
            for addr in addrs[name]:
                family = addr.family.name if hasattr(addr.family, "name") else str(addr.family)
                print(f"    - [{family}] {addr.address}")
        if name in counters:
            counter = counters[name]
            print(f"  Total received: {counter.bytes_recv} bytes")
            print(f"  Total transmitted: {counter.bytes_sent} bytes")
        print()
    filtered = []
    for name in sorted(addrs):
        if name in stats_map and not stats_map[name].isup:
            continue
        ipv4 = [addr.address for addr in addrs[name] if addr.family.value == 2 and addr.address]
        if ipv4:
            filtered.append((name, ipv4))
    print(f"Filtered devices (IPv4, UP): {len(filtered)}\n")
    for name, ips in filtered:
        print(f"  - {name} [{', '.join(ips)}]")
    if sys.platform == "win32":
        print("\nNote: Windows loopback (127.0.0.1) traffic is not visible via")
        print("  standard network APIs. The Loopback device appears in the")
        print("  list but may show zero traffic.")
    print(f"\n{get_system_info()}")
    if emoji:
        print("\n\U0001f3c1 Done! Happy debugging! \U0001f389\U0001f41b")
