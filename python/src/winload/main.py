# 🚦 Wires the Python CLI, argument parsing, runtime loop, and version output.
"""
winload - Windows Network Load Monitor
"""

import argparse
import importlib.util
import platform
import sys
import time
from importlib.metadata import version as get_pkg_version
from pathlib import Path

from .emoji import decorate
from .i18n import t, set_lang, get_lang

TITLE_FLAG_ONLY = "__WINLOAD_TITLE_FLAG_ONLY__"


def _load_format_build_info():
    """Load build metadata from the installed package or Python project root."""
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


class WinloadArgumentParser(argparse.ArgumentParser):
    """Render help closer to clap's description -> usage -> options layout."""

    def format_help(self) -> str:
        formatter = self._get_formatter()

        formatter.add_text(self.description)
        formatter.add_usage(self.usage, self._actions, self._mutually_exclusive_groups)

        for action_group in self._action_groups:
            formatter.start_section(action_group.title)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()

        formatter.add_text(self.epilog)
        return (
            formatter.format_help()
            .replace("usage:", "Usage:", 1)
            .replace("\noptions:", "\nOptions:")
        )


def get_version() -> str:
    try:
        return get_pkg_version("winload")
    except Exception:
        pass
    # Fallback: read version from pyproject.toml (for source runs)
    try:
        import re
        toml_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
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


def get_help_system_info(emoji: bool = False) -> str:
    """Get localized system information for CLI help epilog."""
    text = f"{t('help_system')}: {platform.system()} | {t('help_arch')}: {platform.machine()}"
    return decorate(emoji, "help_system_info", text)


def print_system_info() -> None:
    """Print system information to stderr"""
    print(f"\n{get_system_info()}", file=sys.stderr)


def print_debug_info(emoji: bool = False, use_netlink: bool = False) -> None:
    """Print network interface debug info and exit"""
    if use_netlink:
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
                c = counters[dev.name]
                print(f"  Total received: {c.bytes_recv} bytes")
                print(f"  Total transmitted: {c.bytes_sent} bytes")
            print()

        print(f"Filtered devices (netlink): {len(devices)}\n")
        for dev in devices:
            print(f"  - {dev.name} [{', '.join(dev.addrs)}]")

        print(f"\n{get_system_info()}")
        return

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
            value = float(s[:-1]) * mul
            if value <= 0:
                raise ValueError("value must be greater than 0")
            return value
    value = float(s)
    if value <= 0:
        raise ValueError("value must be greater than 0")
    return value


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
    # First pass: extract display options before building localized help texts.
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--lang", type=str, default="en-us")
    pre_parser.add_argument("-e", "--emoji", action="store_true", default=False)
    pre_args, _ = pre_parser.parse_known_args()
    set_lang(pre_args.lang)
    emoji_enabled = pre_args.emoji

    def help_text(key: str) -> str:
        return decorate(emoji_enabled, key, t(key))

    parser = WinloadArgumentParser(
        prog="winload",
        usage="%(prog)s [OPTIONS]",
        description=help_text("description"),
        epilog=f"\n{get_help_system_info(emoji_enabled)}",
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-t",
        "--interval",
        type=int,
        default=500,
        metavar="INTERVAL",
        help=help_text("help_interval"),
    )
    parser.add_argument(
        "-a",
        "--average",
        type=int,
        default=300,
        metavar="AVERAGE",
        help=help_text("help_average"),
    )
    parser.add_argument(
        "-d",
        "--device",
        type=str,
        default=None,
        metavar="DEVICE",
        help=help_text("help_device"),
    )
    parser.add_argument(
        "--title",
        type=str,
        nargs="?",
        const=TITLE_FLAG_ONLY,
        default=None,
        metavar="TITLE",
        help=help_text("help_title"),
    )
    parser.add_argument(
        "--title-align",
        type=str,
        choices=["left", "center", "right"],
        default="center",
        metavar="TITLE_ALIGN",
        help=help_text("help_title_align"),
    )
    parser.add_argument(
        "--debug-info",
        action="store_true",
        default=False,
        help=help_text("help_debug_info"),
    )
    parser.add_argument(
        "-e",
        "--emoji",
        action="store_true",
        default=False,
        help=help_text("help_emoji"),
    )
    parser.add_argument(
        "-U",
        "--unicode",
        action="store_true",
        default=False,
        help=help_text("help_unicode"),
    )
    parser.add_argument(
        "-u",
        "--unit",
        type=str,
        choices=["bit", "byte"],
        default="bit",
        metavar="UNIT",
        help=help_text("help_unit"),
    )
    parser.add_argument(
        "-b",
        "--bar-style",
        type=str,
        choices=["fill", "color", "plain"],
        default="plain",
        metavar="BAR_STYLE",
        help=help_text("help_bar_style"),
    )
    parser.add_argument(
        "--in-color",
        type=parse_hex_color,
        default=None,
        metavar="IN_COLOR",
        help=help_text("help_in_color"),
    )
    parser.add_argument(
        "--out-color",
        type=parse_hex_color,
        default=None,
        metavar="OUT_COLOR",
        help=help_text("help_out_color"),
    )
    parser.add_argument(
        "--max-mode",
        type=str,
        choices=["smart", "legacy", "fixed"],
        default="smart",
        metavar="MAX_MODE",
        help=help_text("help_max_mode"),
    )
    parser.add_argument(
        "--max-half-life",
        type=float,
        default=10.0,
        metavar="SECS",
        help=help_text("help_max_half_life"),
    )
    parser.add_argument(
        "--max-y-value",
        type=str,
        default=None,
        metavar="VALUE",
        help=help_text("help_max_y_value"),
    )
    parser.add_argument(
        "-n",
        "--no-graph",
        action="store_true",
        default=False,
        help=help_text("help_no_graph"),
    )
    parser.add_argument(
        "--hide-separator",
        action="store_true",
        default=False,
        help=help_text("help_hide_separator"),
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help=help_text("help_no_color"),
    )
    parser.add_argument(
        "--netlink",
        action="store_true",
        default=False,
        help=help_text("help_netlink"),
    )
    parser.add_argument(
        "--lang",
        type=str,
        choices=["en-us", "zh-cn", "zh-tw"],
        default="en-us",
        metavar="LANG",
        help=help_text("help_lang"),
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help=help_text("help_help"),
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=(
            f"winload {get_version()} (Python edition)\n"
            f"{format_build_info()}\n"
            f"{get_system_info()}"
        ),
        help=help_text("help_version"),
    )
    args = parser.parse_args()
    if args.netlink and sys.platform not in ("linux", "android"):
        parser.error("--netlink is only available on Linux/Android")
    if args.max_half_life <= 0:
        parser.error("--max-half-life must be greater than 0")
    if args.max_mode == "fixed":
        if args.max_y_value is None:
            parser.error("--max-mode fixed requires --max-y-value <VALUE>")
        try:
            args.max_y_value = parse_max_value(args.max_y_value)
        except (ValueError, IndexError) as e:
            parser.error(f"invalid --max-y-value: {e}")
        raw_args = sys.argv[1:]
        if any(a == "--max-half-life" or a.startswith("--max-half-life=") for a in raw_args):
            parser.error("--max-half-life can only be used with --max-mode smart")
    else:
        if args.max_y_value is not None:
            parser.error("--max-y-value can only be used with --max-mode fixed")
        if args.max_mode == "legacy":
            raw_args = sys.argv[1:]
            if any(a == "--max-half-life" or a.startswith("--max-half-life=") for a in raw_args):
                parser.error("--max-half-life can only be used with --max-mode smart")
    return args


def resolve_title(raw_title: str | None) -> str | None:
    if raw_title is None or raw_title == "":
        return None
    if raw_title == TITLE_FLAG_ONLY:
        return f"winload {get_version()}"
    return raw_title


def main_loop(stdscr: "curses.window", args: argparse.Namespace) -> None:
    """curses 主循环"""
    import curses

    from .collector import Collector
    from .ui import UI

    collector = Collector(use_netlink=args.netlink)

    ui = UI(
        stdscr,
        collector,
        title=resolve_title(args.title),
        title_align=args.title_align,
        emoji=args.emoji,
        unit=args.unit,
        max_mode=args.max_mode,
        max_half_life=args.max_half_life,
        max_y_value=args.max_y_value,
        no_graph=args.no_graph,
        unicode=args.unicode,
        bar_style=args.bar_style,
        in_color=args.in_color,
        out_color=args.out_color,
        hide_separator=args.hide_separator,
        no_color=args.no_color,
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
        try:
            print_debug_info(emoji=args.emoji, use_netlink=args.netlink)
        except RuntimeError as e:
            if args.netlink:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)
            raise
        return

    # Windows 需要 windows-curses
    try:
        import curses as curses_module
    except ImportError:
        print(t("error_no_curses"))
        print("  pip install windows-curses")
        sys.exit(1)

    try:
        curses_module.wrapper(lambda stdscr: main_loop(stdscr, args))
    except RuntimeError as e:
        if args.netlink:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        raise
    except KeyboardInterrupt:
        pass
    finally:
        print_system_info()


if __name__ == "__main__":
    main()
