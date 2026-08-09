# Coordinates curses layout, colors, application state, and public UI access.
"""Curses user interface for the Python implementation."""

import curses
import sys

from ..app import App, DeviceView
from ..i18n import t
from .debug import DebugMixin
from .panels import PanelMixin


class UI(PanelMixin, DebugMixin):
    """Render an App without owning collection or navigation state."""

    COLOR_HEADER = 1
    COLOR_SEPARATOR = 2
    COLOR_LABEL = 3
    COLOR_GRAPH_FULL = 4
    COLOR_GRAPH_HIGH = 5
    COLOR_GRAPH_LOW = 6
    COLOR_STAT_LABEL = 7
    COLOR_STAT_VALUE = 8
    COLOR_HELP = 9
    COLOR_ERROR = 10

    def __init__(self, stdscr: "curses.window", app: App):
        self.stdscr = stdscr
        self.app = app
        config = app.config
        self.collector = app.collector
        self.title = config.title
        self.title_align = config.title_align
        self.emoji = config.emoji
        self.unit = config.unit
        self.max_mode = config.max_mode
        self.max_half_life = config.max_half_life
        self.max_y_value = config.max_y_value
        self.no_graph = config.no_graph
        self.unicode = config.unicode
        self.bar_style = config.bar_style
        self.in_color_rgb = config.in_color
        self.out_color_rgb = config.out_color
        self.interval = config.interval
        self.average = config.average
        curses.start_color()
        curses.use_default_colors()
        try:
            curses.init_pair(self.COLOR_HEADER, curses.COLOR_WHITE, -1)
            curses.init_pair(self.COLOR_SEPARATOR, curses.COLOR_CYAN, -1)
            curses.init_pair(self.COLOR_LABEL, curses.COLOR_GREEN, -1)
            curses.init_pair(self.COLOR_GRAPH_FULL, curses.COLOR_GREEN, -1)
            curses.init_pair(self.COLOR_GRAPH_HIGH, curses.COLOR_GREEN, -1)
            curses.init_pair(self.COLOR_GRAPH_LOW, curses.COLOR_WHITE, -1)
            curses.init_pair(self.COLOR_STAT_LABEL, curses.COLOR_CYAN, -1)
            curses.init_pair(self.COLOR_STAT_VALUE, curses.COLOR_WHITE, -1)
            curses.init_pair(self.COLOR_HELP, curses.COLOR_YELLOW, -1)
            curses.init_pair(self.COLOR_ERROR, curses.COLOR_RED, -1)
        except curses.error:
            pass
        self.COLOR_IN_GRAPH = self.COLOR_GRAPH_FULL
        self.COLOR_OUT_GRAPH = self.COLOR_GRAPH_FULL
        self.COLOR_IN_LABEL = self.COLOR_LABEL
        self.COLOR_OUT_LABEL = self.COLOR_LABEL
        self._can_change_color = curses.can_change_color()
        try:
            if self._can_change_color and self.in_color_rgb:
                red, green, blue = self.in_color_rgb
                curses.init_color(20, red * 1000 // 255, green * 1000 // 255, blue * 1000 // 255)
                curses.init_pair(11, 20, -1)
                self.COLOR_IN_GRAPH = self.COLOR_IN_LABEL = 11
            if self._can_change_color and self.out_color_rgb:
                red, green, blue = self.out_color_rgb
                curses.init_color(21, red * 1000 // 255, green * 1000 // 255, blue * 1000 // 255)
                curses.init_pair(12, 21, -1)
                self.COLOR_OUT_GRAPH = self.COLOR_OUT_LABEL = 12
        except curses.error:
            pass
        try:
            curses.curs_set(0)
        except curses.error:
            pass

    @property
    def views(self):
        return self.app.views

    @property
    def current_view(self) -> DeviceView:
        return self.app.current_view

    @property
    def current_device_idx(self) -> int:
        return self.app.current_device_idx

    @property
    def show_debug(self) -> bool:
        return self.app.show_debug

    @property
    def hide_separator(self) -> bool:
        return self.app.hide_separator

    @property
    def no_color(self) -> bool:
        return self.app.no_color

    def _color(self, attr: int) -> int:
        return 0 if self.no_color else attr

    def update(self) -> None:
        self.app.update()

    def next_device(self) -> None:
        self.app.next_device()

    def prev_device(self) -> None:
        self.app.previous_device()

    def draw(self) -> None:
        """绘制整个界面"""
        self.stdscr.erase()
        max_y, max_x = self.stdscr.getmaxyx()

        if max_y < 10 or max_x < 40:
            self._draw_too_small(max_y, max_x)
            self.stdscr.noutrefresh()
            return

        # F3 Debug overlay (Minecraft-style)
        if self.show_debug:
            self._draw_debug_overlay(max_y, max_x)
            return

        view = self.current_view
        device_idx = self.current_device_idx % len(self.views)

        row = 0

        # ── 头部: Device name [ip] (n/m): ──
        header_attr = self._color(self._get_bar_attr(self.COLOR_HEADER, bold=True))

        # Add title line if present
        if self.title is not None:
            title_len = len(self.title)
            pad_total = max(0, max_x - 1 - title_len)
            if self.title_align == "center":
                pad_l = pad_total // 2
            elif self.title_align == "right":
                pad_l = pad_total
            else:
                pad_l = 0
            if self.bar_style == "fill":
                title_line = (" " * pad_l + self.title).ljust(max_x - 1)
            else:
                title_line = " " * pad_l + self.title
            self._safe_addstr(row, 0, title_line, header_attr)
            row += 1

        # Always show device header
        addr = view.get_addr_str()
        addr_str = f" [{addr}]" if addr else ""
        if self.emoji:
            device_header = (
                f"{t('device_emoji')} {view.name}{addr_str} "
                f"({device_idx + 1}/{len(self.views)}) 📡:"
            )
        else:
            device_header = (
                f"{t('device')} {view.name}{addr_str} "
                f"({device_idx + 1}/{len(self.views)}):"
            )
        if self.bar_style == "fill":
            device_header = device_header.ljust(max_x - 1)
        self._safe_addstr(row, 0, device_header, header_attr)
        row += 1

        # ── Loopback 警告（仅 Windows）──
        if self._is_loopback_on_windows(view):
            warning = t("loopback_warning")
            warn_attr = self._color(self._get_bar_attr(self.COLOR_HELP))
            if self.bar_style == "fill":
                warning = warning.ljust(max_x - 1)
            self._safe_addstr(row, 0, warning, warn_attr)
            row += 1

        # ── 分隔线 ──
        if not self.hide_separator:
            sep = "=" * (max_x - 1)
            self._safe_addstr(row, 0, sep, self._color(curses.color_pair(self.COLOR_SEPARATOR)))
            row += 1

        # 可用于面板的高度
        usable_height = max_y - row - 1  # 留 1 行给底部帮助
        panel_height = usable_height // 2

        if panel_height < 3:
            self._safe_addstr(row, 0, "Terminal too small")
            self.stdscr.noutrefresh()
            return

        # ── Incoming 面板 ──
        in_label = t("incoming_emoji") if self.emoji else t("incoming")
        self._draw_panel(
            start_row=row,
            max_x=max_x,
            panel_height=panel_height,
            label=in_label,
            stats=view.engine.incoming,
            history=view.engine.incoming_history,
            is_incoming=True,
            smart_max_peak=view.engine.incoming_smooth_peak,
            smart_max_rising=view.engine.incoming_smooth_peak_rising,
        )
        row += panel_height

        # ── Outgoing 面板 ──
        out_label = t("outgoing_emoji") if self.emoji else t("outgoing")
        self._draw_panel(
            start_row=row,
            max_x=max_x,
            panel_height=panel_height,
            label=out_label,
            stats=view.engine.outgoing,
            history=view.engine.outgoing_history,
            is_incoming=False,
            smart_max_peak=view.engine.outgoing_smooth_peak,
            smart_max_rising=view.engine.outgoing_smooth_peak_rising,
        )
        row += panel_height

        # ── 底部帮助行 ──
        if self.emoji:
            help_text = t("help_bar_emoji")
        else:
            help_text = t("help_bar")
        help_attr = self._color(self._get_bar_attr(self.COLOR_HELP))
        if self.bar_style == "fill":
            help_text = help_text.ljust(max_x - 1)
        self._safe_addstr(
            max_y - 1, 0,
            help_text[:max_x - 1],
            help_attr,
        )

        self.stdscr.noutrefresh()


    def _is_loopback_on_windows(self, view: DeviceView) -> bool:
        """检测当前是否为 Windows 平台的 Loopback 设备"""
        if sys.platform != "win32":
            return False
        # 设备名包含 "loopback"（同 Rust 逻辑）
        if "loopback" in view.name.lower():
            return True
        # 地址为 127.0.0.1
        if view.info and any(a == "127.0.0.1" for a in view.info.addrs):
            return True
        return False


    def handle_key(self, key: int) -> bool:
        """Compatibility wrapper for callers that previously sent keys to UI."""
        from ..runtime import map_key

        return self.app.handle_action(map_key(key))
