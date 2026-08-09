# Draws the interactive F3 diagnostics overlay.
"""Debug overlay rendering methods for the main curses UI."""

import curses

from ..i18n import get_lang, t
from ..stats import format_bytes, format_speed_unit


class DebugMixin:
    def _draw_debug_overlay(self, max_y: int, max_x: int) -> None:
        """Draw F3 debug overlay (Minecraft-style runtime info)"""
        import platform
        from ..i18n import get_lang

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
