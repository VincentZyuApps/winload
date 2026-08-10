# Verifies Python CLI parsing, validation, localization, and typed configuration.
import contextlib
import io
import unittest

from winload.cli import (
    build_parser,
    parse_args,
    parse_hex_color,
    parse_max_value,
    resolve_title,
)
from winload.config import BarStyle, MaxMode, TitleAlign, Unit


class CliTests(unittest.TestCase):
    def test_defaults_are_typed(self):
        config = parse_args([])
        self.assertEqual(config.interval, 500)
        self.assertEqual(config.unit, Unit.BIT)
        self.assertEqual(config.bar_style, BarStyle.PLAIN)
        self.assertEqual(config.title_align, TitleAlign.CENTER)
        self.assertEqual(config.max_mode, MaxMode.SMART)

    def test_fixed_scale_and_color_are_normalized(self):
        config = parse_args([
            "--max-mode", "fixed", "--max-y-value", "100M",
            "--in-color", "0x00d7ff", "--unit", "byte",
        ])
        self.assertEqual(config.max_y_value, 100 * 1024 * 1024)
        self.assertEqual(config.in_color, (0, 215, 255))
        self.assertEqual(config.unit, Unit.BYTE)

    def test_invalid_zero_interval_exits(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as caught:
                parse_args(["--interval", "0"])
        self.assertEqual(caught.exception.code, 2)

    def test_fixed_requires_value(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                parse_args(["--max-mode", "fixed"])

    def test_value_and_color_helpers(self):
        self.assertEqual(parse_max_value("1G"), 1024**3)
        self.assertEqual(parse_hex_color("ffffff"), (255, 255, 255))

    def test_title_resolution(self):
        self.assertIsNone(resolve_title(None))
        self.assertEqual(resolve_title("custom"), "custom")
        self.assertTrue(resolve_title("__WINLOAD_TITLE_FLAG_ONLY__").startswith("winload "))

    def test_help_lists_localized_keyboard_shortcuts_before_system_info(self):
        languages = {
            "en-us": (
                "Keyboard Shortcuts:",
                "System:",
                ("Previous network device", "Next network device",
                 "Toggle debug information", "Toggle separator line",
                 "Toggle colors", "Quit"),
            ),
            "zh-cn": (
                "快捷键：",
                "系统:",
                ("切换到上一个网络设备", "切换到下一个网络设备",
                 "切换调试信息", "切换分隔线", "切换颜色", "退出"),
            ),
            "zh-tw": (
                "快捷鍵：",
                "系統:",
                ("切換到上一個網路裝置", "切換到下一個網路裝置",
                 "切換除錯資訊", "切換分隔線", "切換顏色", "退出"),
            ),
        }
        expected_keys = (
            "Left / Up",
            "Right / Down",
            "Tab / Enter",
            "F3",
            "=",
            "c",
            "q / Q / Ctrl+C",
            "PageUp",
            "PageDown",
            "C",
        )

        for lang, (title, system_label, actions) in languages.items():
            with self.subTest(lang=lang):
                help_text = build_parser(["--lang", lang]).format_help()
                for keys in expected_keys:
                    self.assertIn(keys, help_text)
                for action in actions:
                    self.assertIn(action, help_text)
                self.assertNotIn("Esc", help_text)
                self.assertLess(help_text.index("Options:"), help_text.index(title))
                self.assertLess(help_text.index(title), help_text.index(system_label))


if __name__ == "__main__":
    unittest.main()
