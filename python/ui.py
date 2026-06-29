"""
ui.py - 基于 curses 的 TUI 界面渲染
仿 nload 的双面板布局：上半 Incoming / 下半 Outgoing
"""

import curses
import sys
from typing import List, Optional

from collector import Collector, DeviceInfo
from i18n import t
from stats import StatisticsEngine, TrafficStats, format_speed, format_speed_unit, format_bytes
from graph import render_graph, next_power_of_2_scaled, get_graph_scale_label_unit


class DeviceView:
    """单个网卡设备的视图，包含 Incoming 和 Outgoing 两个面板"""

    def __init__(self, name: str, info: Optional[DeviceInfo] = None,
                 smart_max_half_life: Optional[float] = None):
        self.name = name
        self.info = info
        self.engine = StatisticsEngine(smart_max_half_life=smart_max_half_life)

    def get_addr_str(self) -> str:
        if self.info and self.info.addrs:
            return self.info.addrs[0]
        return ""


class UI:
    """curses TUI 主控"""

    # 颜色对
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

    def __init__(self, stdscr: "curses.window", collector: Collector,
                 title: Optional[str] = None,
                 title_align: str = "center",
                 emoji: bool = False, unit: str = "bit",
                 max_mode: str = "smart",
                 max_half_life: float = 10.0,
                 max_y_value: Optional[float] = None,
                 no_graph: bool = False,
                 unicode: bool = False, bar_style: str = "fill",
                 in_color: Optional[tuple] = None, out_color: Optional[tuple] = None,
                 hide_separator: bool = False, no_color: bool = False,
                 interval: int = 500, average: int = 300):
        self.stdscr = stdscr
        self.collector = collector
        self.current_device_idx = 0
        self.views: List[DeviceView] = []
        self.title = title
        self.title_align = title_align
        self.emoji = emoji
        self.unit = unit
        self.max_mode = max_mode
        self.max_half_life = max_half_life
        self.max_y_value = max_y_value
        self.no_graph = no_graph
        self.unicode = unicode
        self.bar_style = bar_style
        self.in_color_rgb = in_color
        self.out_color_rgb = out_color
        self.hide_separator = hide_separator
        self.no_color = no_color
        self.smart_max_half_life = max_half_life if max_mode == "smart" else None
        self.interval = interval
        self.average = average
        self.show_debug = False

        # 初始化颜色
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

        # 自定义颜色 (in/out graph colors)
        # 颜色对 11-16 用于自定义 graph 颜色
        self.COLOR_IN_GRAPH = self.COLOR_GRAPH_FULL   # 默认复用绿色
        self.COLOR_OUT_GRAPH = self.COLOR_GRAPH_FULL
        self.COLOR_IN_LABEL = self.COLOR_LABEL
        self.COLOR_OUT_LABEL = self.COLOR_LABEL
        self._can_change_color = curses.can_change_color()
        try:
            if self._can_change_color and self.in_color_rgb:
                r, g, b = self.in_color_rgb
                curses.init_color(20, r * 1000 // 255, g * 1000 // 255, b * 1000 // 255)
                curses.init_pair(11, 20, -1)
                self.COLOR_IN_GRAPH = 11
                self.COLOR_IN_LABEL = 11
            if self._can_change_color and self.out_color_rgb:
                r, g, b = self.out_color_rgb
                curses.init_color(21, r * 1000 // 255, g * 1000 // 255, b * 1000 // 255)
                curses.init_pair(12, 21, -1)
                self.COLOR_OUT_GRAPH = 12
                self.COLOR_OUT_LABEL = 12
        except curses.error:
            pass

        # 隐藏光标
        try:
            curses.curs_set(0)
        except curses.error:
            pass

        self._init_views()

    def _color(self, attr: int) -> int:
        """If no_color mode is active, strip all color/style attributes and return 0."""
        return 0 if self.no_color else attr

    def _init_views(self) -> None:
        """根据 collector 的设备列表创建视图"""
        self.views.clear()
        for name in self.collector.device_names:
            info = self.collector.get_device_info(name)
            self.views.append(DeviceView(name, info,
                                         smart_max_half_life=self.smart_max_half_life))
        if not self.views:
            # fallback: 如果没有设备（不太可能），至少显示一个占位
            self.views.append(DeviceView("(no device)",
                                         smart_max_half_life=self.smart_max_half_life))

    @property
    def current_view(self) -> DeviceView:
        idx = self.current_device_idx % len(self.views)
        return self.views[idx]

    def next_device(self) -> None:
        if self.views:
            self.current_device_idx = (
                (self.current_device_idx + 1) % len(self.views)
            )

    def prev_device(self) -> None:
        if self.views:
            self.current_device_idx = (
                (self.current_device_idx - 1) % len(self.views)
            )

    def update(self) -> None:
        """采集一次数据并更新所有设备的统计"""
        snapshots = self.collector.collect()
        for view in self.views:
            snap = snapshots.get(view.name)
            if snap:
                view.engine.update(snap)

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

    def _draw_panel(
        self,
        start_row: int,
        max_x: int,
        panel_height: int,
        label: str,
        stats: TrafficStats,
        history,
        is_incoming: bool = True,
        smart_max_peak: float = 0.0,
        smart_max_rising: bool = False,
    ) -> None:
        """绘制一个流量面板（图形 + 统计）"""
        # 选择颜色
        graph_color = self.COLOR_IN_GRAPH if is_incoming else self.COLOR_OUT_GRAPH
        label_color = self.COLOR_IN_LABEL if is_incoming else self.COLOR_OUT_LABEL

        # 统计信息（5 行）
        stat_lines = self._format_stats(stats)
        stat_width = max(len(s) for s in stat_lines) + 2 if stat_lines else 20

        # 确定缩放上限
        if self.max_mode == "fixed":
            scale_max = self.max_y_value or next_power_of_2_scaled(max(history) if history else 0.0)
        elif self.max_mode == "smart":
            scale_max = next_power_of_2_scaled(smart_max_peak)
        else:
            peak = max(history) if history else 0.0
            scale_max = next_power_of_2_scaled(peak)

        # 标签行
        scale_label = get_graph_scale_label_unit(scale_max, self.unit)
        mode_tag = ""
        if self.max_mode == "fixed":
            mode_tag = f" [{t('tag_fixed')}: {format_speed_unit(self.max_y_value or scale_max, self.unit)}]"
        elif self.max_mode == "smart":
            arrow = t("arrow_up") if smart_max_rising else t("arrow_down")
            mode_tag = f" [{t('tag_smart_max')} {self.max_half_life}s] {arrow}"
        else:
            mode_tag = f" [{t('tag_legacy')}]"
        label_text = f"{label} ({scale_label}){mode_tag}:"
        label_attr = self._color(self._get_bar_attr(label_color, bold=True))
        if self.bar_style == "fill":
            label_text = label_text.ljust(max_x - 1)
        self._safe_addstr(
            start_row, 0, label_text, label_attr,
        )

        graph_rows = panel_height - 1  # 去掉标签行

        if graph_rows < 1:
            return

        if self.no_graph:
            # 不绘制图形，只绘制统计信息（左对齐）
            stat_start_row = start_row + 1 + graph_rows - len(stat_lines)
            stat_col = 2
            for i, s in enumerate(stat_lines):
                r = stat_start_row + i
                if r < start_row + 1:
                    continue
                parts = s.split(": ", 1)
                if len(parts) == 2:
                    lbl_part = parts[0] + ": "
                    val_part = parts[1]
                    self._safe_addstr(
                        r, stat_col, lbl_part,
                        self._color(curses.color_pair(self.COLOR_STAT_LABEL) | curses.A_BOLD),
                    )
                    self._safe_addstr(
                        r, stat_col + len(lbl_part), val_part,
                        self._color(curses.color_pair(self.COLOR_STAT_VALUE)),
                    )
                else:
                    self._safe_addstr(r, stat_col, s, self._color(curses.color_pair(self.COLOR_STAT_VALUE)))
            return

        # 图形区域尺寸
        graph_cols = max(max_x - stat_width - 2, 10)

        # 渲染图形
        lines = render_graph(
            history=history,
            width=graph_cols,
            height=graph_rows,
            max_value=scale_max,
            unicode=self.unicode,
        )

        # Unicode 和 ASCII 字符映射
        if self.unicode:
            full_chars = {"█", "▓"}
            dim_chars = {"░"}
        else:
            full_chars = {"#", "|"}
            dim_chars = {"."}

        # 绘制图形
        for i, line in enumerate(lines):
            row = start_row + 1 + i
            for col_idx, ch in enumerate(line):
                if ch in full_chars:
                    color = self._color(curses.color_pair(graph_color))
                elif ch in dim_chars:
                    color = self._color(curses.color_pair(self.COLOR_GRAPH_LOW) | curses.A_DIM)
                else:
                    continue  # 空格不画
                self._safe_addch(row, col_idx, ch, color)

        # 绘制统计信息（右侧，底部对齐）
        stat_start_row = start_row + 1 + graph_rows - len(stat_lines)
        stat_col = max_x - stat_width
        for i, s in enumerate(stat_lines):
            r = stat_start_row + i
            if r < start_row + 1:
                continue
            # 标签部分 (Cur: / Avg: / ...)
            parts = s.split(": ", 1)
            if len(parts) == 2:
                lbl_part = parts[0] + ": "
                val_part = parts[1]
                self._safe_addstr(
                    r, stat_col, lbl_part,
                    self._color(curses.color_pair(self.COLOR_STAT_LABEL) | curses.A_BOLD),
                )
                self._safe_addstr(
                    r, stat_col + len(lbl_part), val_part,
                    self._color(curses.color_pair(self.COLOR_STAT_VALUE)),
                )
            else:
                self._safe_addstr(r, stat_col, s, self._color(curses.color_pair(self.COLOR_STAT_VALUE)))

    def _get_bar_attr(self, color_pair_id: int, bold: bool = False) -> int:
        """根据 bar_style 返回对应的 curses 属性"""
        attr = curses.color_pair(color_pair_id)
        if bold:
            attr |= curses.A_BOLD
        if self.bar_style in ("fill", "color"):
            # fill: 背景色铺满整行 (文字会被 ljust 填充)
            # color: 背景色仅在文字上 (不 ljust)
            attr |= curses.A_REVERSE
        # plain: 无背景色，纯前景着色
        return attr

    @staticmethod
    def _str_display_width(s: str) -> int:
        """计算字符串在终端中的显示宽度（CJK 字符占 2 列）"""
        w = 0
        for ch in s:
            cp = ord(ch)
            if (0x1100 <= cp <= 0x115F or 0x2E80 <= cp <= 0x9FFF
                    or 0xAC00 <= cp <= 0xD7AF or 0xF900 <= cp <= 0xFAFF
                    or 0xFE30 <= cp <= 0xFE4F or 0xFF01 <= cp <= 0xFF60
                    or 0xFFE0 <= cp <= 0xFFE6 or 0x20000 <= cp <= 0x2FA1F
                    or 0x30000 <= cp <= 0x3134F):
                w += 2
            elif 0xFE00 <= cp <= 0xFE0F or 0xE0100 <= cp <= 0xE01EF:
                pass  # variation selectors, 0 width
            elif cp >= 0x1F000:
                w += 2  # emoji
            else:
                w += 1
        return w

    def _format_stats(self, stats: TrafficStats) -> List[str]:
        """格式化 5 行统计文本，冒号动态对齐"""
        fmt = lambda v: format_speed_unit(v, self.unit)
        suffix = "_emoji" if self.emoji else ""
        keys = ["stat_curr", "stat_avg", "stat_min", "stat_max", "stat_ttl"]
        labels = [t(k + suffix) for k in keys]
        values = [fmt(stats.current), fmt(stats.average),
                  fmt(stats.minimum), fmt(stats.maximum),
                  format_bytes(stats.total)]
        max_w = max(self._str_display_width(lb) for lb in labels)
        lines = []
        for lb, val in zip(labels, values):
            pad = max_w - self._str_display_width(lb)
            lines.append(f"{' ' * pad}{lb}: {val}")
        return lines

    def _draw_too_small(self, max_y: int, max_x: int) -> None:
        msg = t("terminal_too_small_emoji") if self.emoji else t("terminal_too_small")
        y = max_y // 2
        x = max(0, (max_x - len(msg)) // 2)
        self._safe_addstr(
            y, x, msg,
            self._color(curses.color_pair(self.COLOR_ERROR) | curses.A_BOLD),
        )

    def _safe_addstr(self, y: int, x: int, text: str, attr: int = 0) -> None:
        """安全写入字符串，忽略边界溢出"""
        max_y, max_x = self.stdscr.getmaxyx()
        if y < 0 or y >= max_y or x < 0 or x >= max_x:
            return
        try:
            self.stdscr.addnstr(y, x, text, max_x - x - 1, attr)
        except curses.error:
            pass

    def _safe_addch(self, y: int, x: int, ch: str, attr: int = 0) -> None:
        max_y, max_x = self.stdscr.getmaxyx()
        if y < 0 or y >= max_y or x < 0 or x >= max_x:
            return
        try:
            self.stdscr.addch(y, x, ch, attr)
        except curses.error:
            pass

    def _draw_debug_overlay(self, max_y: int, max_x: int) -> None:
        """Draw F3 debug overlay (Minecraft-style runtime info)"""
        import platform
        from i18n import get_lang

        title_attr = self._color(curses.color_pair(self.COLOR_SEPARATOR) | curses.A_BOLD)
        section_attr = self._color(curses.color_pair(self.COLOR_HELP) | curses.A_BOLD)
        label_attr = self._color(curses.color_pair(self.COLOR_STAT_LABEL) | curses.A_BOLD)
        value_attr = self._color(curses.color_pair(self.COLOR_STAT_VALUE))

        row = 0

        def kv(r: int, key: str, val: str) -> int:
            self._safe_addstr(r, 2, f"{key:<14}", label_attr)
            self._safe_addstr(r, 16, str(val), value_attr)
            return r + 1

        def section(r: int, title: str) -> int:
            self._safe_addstr(r, 0, title, section_attr)
            return r + 1

        on_off = lambda b: t("on") if b else t("off")

        # Title
        self._safe_addstr(row, 0, t("f3_title"), title_attr)
        row += 2

        # Version & System
        try:
            from importlib.metadata import version as _get_ver
            ver = _get_ver("winload")
        except Exception:
            ver = "unknown"
        row = kv(row, t("debug_version"), f"{ver} (Python edition)")
        row = kv(row, t("debug_system"), f"{platform.system()} | {platform.machine()}")
        row = kv(row, t("debug_language"), get_lang())
        row += 1

        # Parameters
        row = section(row, t("debug_section_params"))
        row = kv(row, t("debug_interval"), f"{self.interval} ms")
        row = kv(row, t("debug_average"), f"{self.average} s")
        row = kv(row, t("debug_unit"), self.unit)
        row = kv(row, t("debug_bar_style"), self.bar_style)
        row = kv(row, t("debug_emoji"), on_off(self.emoji))
        row = kv(row, t("debug_unicode"), on_off(self.unicode))
        row = kv(row, t("debug_no_graph"), on_off(self.no_graph))
        row = kv(row, t("debug_no_color"), on_off(self.no_color))
        row = kv(row, t("debug_hide_sep"), on_off(self.hide_separator))
        row += 1

        # Y-axis Scaling
        row = section(row, t("debug_section_yaxis"))
        if self.max_mode == "fixed":
            mode_str = t("yaxis_fixed").format(val=format_speed_unit(self.max_y_value or 0.0, self.unit))
        elif self.max_mode == "smart":
            mode_str = t("yaxis_smart").format(sec=self.max_half_life)
        else:
            mode_str = t("yaxis_legacy")
        row = kv(row, t("debug_yaxis_mode"), mode_str)

        view = self.current_view
        if self.max_mode == "smart":
            row = kv(row, t("debug_in_smooth"), format_speed_unit(
                view.engine.incoming_smooth_peak, self.unit))
            row = kv(row, t("debug_out_smooth"), format_speed_unit(
                view.engine.outgoing_smooth_peak, self.unit))
        row += 1

        # Device
        row = section(row, t("debug_section_device"))
        device_idx = self.current_device_idx % len(self.views)
        addr = view.get_addr_str() or t("addr_none")
        row = kv(row, t("debug_device_name"), f"{view.name} ({device_idx + 1}/{len(self.views)})")
        row = kv(row, t("debug_device_addr"), addr)
        row = kv(row, t("debug_in_curr"), format_speed_unit(view.engine.incoming.current, self.unit))
        row = kv(row, t("debug_out_curr"), format_speed_unit(view.engine.outgoing.current, self.unit))
        row = kv(row, t("debug_in_total"), format_bytes(view.engine.incoming.total))
        row = kv(row, t("debug_out_total"), format_bytes(view.engine.outgoing.total))
        row = kv(row, t("debug_in_peak"), format_speed_unit(view.engine.incoming.maximum, self.unit))
        row = kv(row, t("debug_out_peak"), format_speed_unit(view.engine.outgoing.maximum, self.unit))
        row += 1

        # Colors
        row = section(row, t("debug_section_colors"))
        def fmt_color(rgb_tuple, default_name):
            if rgb_tuple:
                r, g, b = rgb_tuple
                return f"#{r:02x}{g:02x}{b:02x}"
            return f"{default_name} {t('default_tag')}"
        row = kv(row, t("debug_in_color"), fmt_color(self.in_color_rgb, "cyan"))
        row = kv(row, t("debug_out_color"), fmt_color(self.out_color_rgb, "gold"))

        # Help bar (bottom)
        help_text = t("f3_help_bar_emoji") if self.emoji else t("f3_help_bar")
        help_attr = self._color(self._get_bar_attr(self.COLOR_HELP))
        if self.bar_style == "fill":
            help_text = help_text.ljust(max_x - 1)
        self._safe_addstr(max_y - 1, 0, help_text[:max_x - 1], help_attr)

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
        """
        处理按键输入。
        返回 False 表示退出。
        """
        if key in (ord("q"), ord("Q")):
            return False
        elif key == curses.KEY_F0 + 3:  # F3
            self.show_debug = not self.show_debug
        elif key == ord("="):
            self.hide_separator = not self.hide_separator
        elif key in (ord("c"), ord("C")):
            self.no_color = not self.no_color
        elif key in (curses.KEY_RIGHT, curses.KEY_DOWN, ord("\t"),
                     curses.KEY_NPAGE, 10):  # 10 = Enter
            self.next_device()
        elif key in (curses.KEY_LEFT, curses.KEY_UP, curses.KEY_PPAGE):
            self.prev_device()
        return True
