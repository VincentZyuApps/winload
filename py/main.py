"""
winload - Windows Network Load Monitor
仿 Linux nload 的终端网络流量监控工具

用法:
    python main.py              # 监控所有活跃网卡
    python main.py -t 200       # 设置刷新间隔 200ms
    python main.py -d "Wi-Fi"   # 指定默认设备

快捷键:
    ←/→  或 ↑/↓   切换网卡
    q              退出
"""

import argparse
import curses
import platform
import sys
import time
from importlib.metadata import version as get_pkg_version

from collector import Collector
from i18n import t, set_lang, get_lang
from ui import UI

TITLE_FLAG_ONLY = "__WINLOAD_TITLE_FLAG_ONLY__"


def get_version() -> str:
    try:
        return get_pkg_version("winload")
    except Exception:
        pass
    # Fallback: read version from pyproject.toml (for source runs)
    try:
        import re
        from pathlib import Path
        toml_path = Path(__file__).resolve().parent / "pyproject.toml"
        text = toml_path.read_text(encoding="utf-8")
        m = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
        if m:
            return m.group(1)
    except Exception:
        pass
    return "unknown"


def get_system_info() -> str:
    """Get system information string"""
    return f"System: {platform.system()} | Arch: {platform.machine()}"


def print_system_info() -> None:
    """Print system information to stderr"""
    print(f"\n{get_system_info()}", file=sys.stderr)


def print_debug_info(emoji: bool = False) -> None:
    """Print network interface debug info and exit"""
    import psutil

    if emoji:
        print("\n\U0001f50d\U0001f310 Network Interfaces Debug Info \U0001f5a7\u2728")

    print("\n=== Network Interfaces Debug Info ===")

    addrs = psutil.net_if_addrs()
    stats_map = psutil.net_if_stats()
    counters = psutil.net_io_counters(pernic=True)

    print(f"Total interfaces detected by psutil: {len(addrs)}\n")

    for name in sorted(addrs.keys()):
        print(f"Interface: {name}")

        if name in stats_map:
            s = stats_map[name]
            status = "UP" if s.isup else "DOWN"
            print(f"  Status: {status} | Speed: {s.speed} Mbps | MTU: {s.mtu}")

        print("  Addresses:")
        addr_list = addrs[name]
        if not addr_list:
            print("    (none)")
        else:
            for a in addr_list:
                family = a.family.name if hasattr(a.family, 'name') else str(a.family)
                print(f"    - [{family}] {a.address}")

        if name in counters:
            c = counters[name]
            print(f"  Total received: {c.bytes_recv} bytes")
            print(f"  Total transmitted: {c.bytes_sent} bytes")

        print()

    # Filtered devices (same logic as Collector)
    filtered = []
    for name in sorted(addrs.keys()):
        if name in stats_map and not stats_map[name].isup:
            continue
        ipv4 = [a.address for a in addrs[name] if a.family.value == 2 and a.address]
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


def parse_max_value(s: str) -> float:
    """解析人类可读的流量值，如 '100M' → 100*1024*1024"""
    s = s.strip()
    multipliers = {
        "G": 1024**3,
        "g": 1024**3,
        "M": 1024**2,
        "m": 1024**2,
        "K": 1024,
        "k": 1024,
    }
    for suffix, mul in multipliers.items():
        if s.endswith(suffix):
            return float(s[:-1]) * mul
    return float(s)


def parse_hex_color(s: str):
    """解析十六进制颜色码，如 '0x00d7ff' → (0, 215, 255)"""
    s = s.strip()
    if s.startswith(("0x", "0X")):
        s = s[2:]
    if len(s) != 6:
        raise argparse.ArgumentTypeError(
            f"expected 6 hex digits (e.g. 0x3399ff), got: {s}"
        )
    try:
        r = int(s[0:2], 16)
        g = int(s[2:4], 16)
        b = int(s[4:6], 16)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"invalid hex color: {e}")
    return (r, g, b)


def parse_args() -> argparse.Namespace:
    # First pass: extract --lang early so we can set language before building help texts
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--lang", type=str, default="en-us")
    pre_args, _ = pre_parser.parse_known_args()
    set_lang(pre_args.lang)

    parser = argparse.ArgumentParser(
        prog="winload",
        description=f"winload {get_version()} (Python edition)\n{t('description')}",
        epilog=f"\n{get_system_info()}",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-t",
        "--interval",
        type=int,
        default=500,
        metavar="INTERVAL",
        help=t("help_interval"),
    )
    parser.add_argument(
        "-a",
        "--average",
        type=int,
        default=300,
        metavar="SEC",
        help=t("help_average"),
    )
    parser.add_argument(
        "-d",
        "--device",
        type=str,
        default=None,
        metavar="NAME",
        help=t("help_device"),
    )
    parser.add_argument(
        "--title",
        type=str,
        nargs="?",
        const=TITLE_FLAG_ONLY,
        default=None,
        metavar="TITLE",
        help=t("help_title"),
    )
    parser.add_argument(
        "--title-align",
        type=str,
        choices=["left", "center", "right"],
        default="center",
        metavar="ALIGN",
        help="Title alignment: left, center, right\n\n[default: center]",
    )
    parser.add_argument(
        "-e",
        "--emoji",
        action="store_true",
        default=False,
        help=t("help_emoji"),
    )
    parser.add_argument(
        "-u",
        "--unit",
        type=str,
        choices=["bit", "byte"],
        default="bit",
        help=t("help_unit"),
    )
    max_group = parser.add_mutually_exclusive_group()
    max_group.add_argument(
        "-m",
        "--max",
        type=str,
        default=None,
        metavar="VALUE",
        help=t("help_max"),
    )
    max_group.add_argument(
        "--smart-max",
        type=float,
        nargs="?",
        const=10.0,
        default=None,
        metavar="SECS",
        help=t("help_smart_max"),
    )
    parser.add_argument(
        "-n",
        "--no-graph",
        action="store_true",
        default=False,
        help=t("help_no_graph"),
    )
    parser.add_argument(
        "-U",
        "--unicode",
        action="store_true",
        default=False,
        help=t("help_unicode"),
    )
    parser.add_argument(
        "-b",
        "--bar-style",
        type=str,
        choices=["fill", "color", "plain"],
        default="fill",
        help=t("help_bar_style"),
    )
    parser.add_argument(
        "--in-color",
        type=parse_hex_color,
        default=None,
        metavar="HEX",
        help=t("help_in_color"),
    )
    parser.add_argument(
        "--out-color",
        type=parse_hex_color,
        default=None,
        metavar="HEX",
        help=t("help_out_color"),
    )
    parser.add_argument(
        "--hide-separator",
        action="store_true",
        default=False,
        help=t("help_hide_separator"),
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"winload {get_version()} (Python edition)",
        help=t("help_version"),
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help=t("help_no_color"),
    )
    parser.add_argument(
        "--debug-info",
        action="store_true",
        default=False,
        help=t("help_debug_info"),
    )
    parser.add_argument(
        "--lang",
        type=str,
        choices=["en-us", "zh-cn", "zh-tw"],
        default="en-us",
        metavar="LANG",
        help=t("help_lang"),
    )
    return parser.parse_args()


def resolve_title(raw_title: str | None) -> str | None:
    if raw_title is None or raw_title == "":
        return None
    if raw_title == TITLE_FLAG_ONLY:
        return f"winload {get_version()}"
    return raw_title


def main_loop(stdscr: "curses.window", args: argparse.Namespace) -> None:
    """curses 主循环"""
    collector = Collector()

    # 解析 --max 参数
    fixed_max = None
    if args.max:
        try:
            fixed_max = parse_max_value(args.max)
        except (ValueError, IndexError):
            pass

    ui = UI(
        stdscr,
        collector,
        title=resolve_title(args.title),
        title_align=args.title_align,
        emoji=args.emoji,
        unit=args.unit,
        fixed_max=fixed_max,
        no_graph=args.no_graph,
        unicode=args.unicode,
        bar_style=args.bar_style,
        in_color=args.in_color,
        out_color=args.out_color,
        hide_separator=args.hide_separator,
        no_color=args.no_color,
        smart_max_half_life=args.smart_max,
        interval=args.interval,
        average=args.average,
    )

    # 如果指定了默认设备，切换到对应索引
    if args.device:
        for i, v in enumerate(ui.views):
            if args.device.lower() in v.name.lower():
                ui.current_device_idx = i
                break

    # 设置 stdin 非阻塞
    stdscr.nodelay(True)
    stdscr.timeout(100)  # getch 超时 100ms

    refresh_interval_sec = args.interval / 1000.0
    last_update = 0.0

    while True:
        now = time.time()

        # 处理键盘输入
        try:
            key = stdscr.getch()
            if key != -1:
                if not ui.handle_key(key):
                    break
        except curses.error:
            pass

        # 按刷新间隔采样 + 重绘
        if now - last_update >= refresh_interval_sec:
            ui.update()
            ui.draw()
            curses.doupdate()
            last_update = now


def main() -> None:
    args = parse_args()

    # --debug-info: print and exit
    if args.debug_info:
        print_debug_info(emoji=args.emoji)
        return

    # Windows 需要 windows-curses
    try:
        import curses as _curses  # noqa: F401
    except ImportError:
        print(t("error_no_curses"))
        print("  pip install windows-curses")
        sys.exit(1)

    try:
        curses.wrapper(lambda stdscr: main_loop(stdscr, args))
    except KeyboardInterrupt:
        pass
    finally:
        print_system_info()


if __name__ == "__main__":
    main()
