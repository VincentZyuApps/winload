# Builds, localizes, parses, and validates the Python command-line interface.
"""Command-line parsing that produces a validated :class:`RunConfig`."""

import argparse
import sys
from typing import Optional, Sequence

from .config import BarStyle, MaxMode, RgbColor, RunConfig, TitleAlign, Unit
from .diagnostics import format_build_info, get_help_system_info, get_system_info, get_version
from .emoji import decorate
from .i18n import set_lang, t

TITLE_FLAG_ONLY = "__WINLOAD_TITLE_FLAG_ONLY__"
SHORTCUT_KEY_WIDTH = 28


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
        return formatter.format_help().replace("usage:", "Usage:", 1).replace(
            "\noptions:", "\nOptions:"
        )


def parse_max_value(value: str) -> float:
    """Parse a positive byte value with an optional binary K/M/G suffix."""
    value = value.strip()
    multipliers = {"G": 1024**3, "g": 1024**3, "M": 1024**2, "m": 1024**2,
                   "K": 1024, "k": 1024}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            result = float(value[:-1]) * multiplier
            if result <= 0:
                raise ValueError("value must be greater than 0")
            return result
    result = float(value)
    if result <= 0:
        raise ValueError("value must be greater than 0")
    return result


def parse_hex_color(value: str) -> RgbColor:
    """Parse an RGB value written as six hexadecimal digits."""
    value = value.strip()
    if value.startswith(("0x", "0X")):
        value = value[2:]
    if len(value) != 6:
        raise argparse.ArgumentTypeError(
            f"expected 6 hex digits (e.g. 0x3399ff), got: {value}"
        )
    try:
        return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid hex color: {exc}") from exc


def resolve_title(raw_title: Optional[str]) -> Optional[str]:
    if raw_title is None or raw_title == "":
        return None
    if raw_title == TITLE_FLAG_ONLY:
        return f"winload {get_version()}"
    return raw_title


def format_keyboard_shortcuts(emoji_enabled: bool) -> str:
    """Format localized runtime controls with optional emoji decorations."""
    shortcuts = (
        ("Left / Up", "shortcut_previous_device"),
        ("Right / Down", "shortcut_next_device"),
        ("Tab / Enter", "shortcut_next_device"),
        ("F3", "shortcut_toggle_debug"),
        ("=", "shortcut_toggle_separator"),
        ("c", "shortcut_toggle_color"),
        ("q / Q / Ctrl+C", "shortcut_quit"),
        ("PageUp", "shortcut_previous_device"),
        ("PageDown", "shortcut_next_device"),
        ("C", "shortcut_toggle_color"),
    )
    lines = [decorate(emoji_enabled, "help_shortcuts_title", t("help_shortcuts_title"))]
    lines.extend(
        f"  {keys:<{SHORTCUT_KEY_WIDTH}}{decorate(emoji_enabled, action_key, t(action_key))}"
        for keys, action_key in shortcuts
    )
    return "\n".join(lines)


def build_parser(argv: Optional[Sequence[str]] = None) -> WinloadArgumentParser:
    """Build a parser after pre-reading options that affect localized help."""
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--lang", type=str, default="en-us")
    pre_parser.add_argument("-e", "--emoji", action="store_true", default=False)
    pre_args, _ = pre_parser.parse_known_args(argv)
    set_lang(pre_args.lang)

    def help_text(key: str) -> str:
        return decorate(pre_args.emoji, key, t(key))

    parser = WinloadArgumentParser(
        prog="winload",
        usage="%(prog)s [OPTIONS]",
        description=help_text("description"),
        epilog=(
            f"\n{format_keyboard_shortcuts(pre_args.emoji)}\n\n"
            f"{get_help_system_info(pre_args.emoji)}"
        ),
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-t", "--interval", type=int, default=500, metavar="INTERVAL",
                        help=help_text("help_interval"))
    parser.add_argument("-a", "--average", type=int, default=300, metavar="AVERAGE",
                        help=help_text("help_average"))
    parser.add_argument("-d", "--device", default=None, metavar="DEVICE",
                        help=help_text("help_device"))
    parser.add_argument("--title", nargs="?", const=TITLE_FLAG_ONLY, default=None,
                        metavar="TITLE", help=help_text("help_title"))
    parser.add_argument("--title-align", choices=[item.value for item in TitleAlign],
                        default=TitleAlign.CENTER.value, metavar="TITLE_ALIGN",
                        help=help_text("help_title_align"))
    parser.add_argument("--debug-info", action="store_true", help=help_text("help_debug_info"))
    parser.add_argument("-e", "--emoji", action="store_true", help=help_text("help_emoji"))
    parser.add_argument("-U", "--unicode", action="store_true", help=help_text("help_unicode"))
    parser.add_argument("-u", "--unit", choices=[item.value for item in Unit], default=Unit.BIT.value,
                        metavar="UNIT", help=help_text("help_unit"))
    parser.add_argument("-b", "--bar-style", choices=[item.value for item in BarStyle],
                        default=BarStyle.PLAIN.value, metavar="BAR_STYLE",
                        help=help_text("help_bar_style"))
    parser.add_argument("--in-color", type=parse_hex_color, default=None, metavar="IN_COLOR",
                        help=help_text("help_in_color"))
    parser.add_argument("--out-color", type=parse_hex_color, default=None, metavar="OUT_COLOR",
                        help=help_text("help_out_color"))
    parser.add_argument("--max-mode", choices=[item.value for item in MaxMode],
                        default=MaxMode.SMART.value, metavar="MAX_MODE",
                        help=help_text("help_max_mode"))
    parser.add_argument("--max-half-life", type=float, default=10.0, metavar="SECS",
                        help=help_text("help_max_half_life"))
    parser.add_argument("--max-y-value", default=None, metavar="VALUE",
                        help=help_text("help_max_y_value"))
    parser.add_argument("-n", "--no-graph", action="store_true", help=help_text("help_no_graph"))
    parser.add_argument("--hide-separator", action="store_true",
                        help=help_text("help_hide_separator"))
    parser.add_argument("--no-color", action="store_true", help=help_text("help_no_color"))
    parser.add_argument("--netlink", action="store_true", help=help_text("help_netlink"))
    parser.add_argument("--lang", choices=["en-us", "zh-cn", "zh-tw"], default="en-us",
                        metavar="LANG", help=help_text("help_lang"))
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS,
                        help=help_text("help_help"))
    parser.add_argument(
        "-V", "--version", action="version",
        version=(f"winload {get_version()} (Python edition)\n{format_build_info()}\n"
                 f"{get_system_info()}"),
        help=help_text("help_version"),
    )
    return parser


def parse_args(argv: Optional[Sequence[str]] = None) -> RunConfig:
    parser = build_parser(argv)
    args = parser.parse_args(argv)
    raw_args = list(sys.argv[1:] if argv is None else argv)
    if args.netlink and sys.platform not in ("linux", "android"):
        parser.error("--netlink is only available on Linux/Android")
    if args.interval <= 0:
        parser.error("--interval must be greater than 0")
    if args.average <= 0:
        parser.error("--average must be greater than 0")
    if args.max_half_life <= 0:
        parser.error("--max-half-life must be greater than 0")
    has_half_life = any(
        item == "--max-half-life" or item.startswith("--max-half-life=")
        for item in raw_args
    )
    if args.max_mode == MaxMode.FIXED:
        if args.max_y_value is None:
            parser.error("--max-mode fixed requires --max-y-value <VALUE>")
        try:
            args.max_y_value = parse_max_value(args.max_y_value)
        except (ValueError, IndexError) as exc:
            parser.error(f"invalid --max-y-value: {exc}")
        if has_half_life:
            parser.error("--max-half-life can only be used with --max-mode smart")
    else:
        if args.max_y_value is not None:
            parser.error("--max-y-value can only be used with --max-mode fixed")
        if args.max_mode == MaxMode.LEGACY and has_half_life:
            parser.error("--max-half-life can only be used with --max-mode smart")
    return RunConfig(
        interval=args.interval, average=args.average, device=args.device,
        title=resolve_title(args.title), title_align=TitleAlign(args.title_align),
        debug_info=args.debug_info, emoji=args.emoji, unicode=args.unicode,
        unit=Unit(args.unit), bar_style=BarStyle(args.bar_style), in_color=args.in_color,
        out_color=args.out_color, max_mode=MaxMode(args.max_mode),
        max_half_life=args.max_half_life, max_y_value=args.max_y_value,
        no_graph=args.no_graph, hide_separator=args.hide_separator,
        no_color=args.no_color, netlink=args.netlink, lang=args.lang,
    )
