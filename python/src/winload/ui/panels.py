# Draws classic traffic graphs and formatted statistics panels.
"""Reusable curses panel rendering methods for the main UI."""

import curses
from typing import List

from ..graph import get_graph_scale_label_unit, next_power_of_2_scaled, render_graph
from ..i18n import t
from ..stats import TrafficStats, format_bytes, format_speed_unit


class PanelMixin:
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
