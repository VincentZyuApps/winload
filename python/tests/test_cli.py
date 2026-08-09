# Verifies Python CLI parsing, validation, localization, and typed configuration.
import contextlib
import io
import unittest

from winload.cli import parse_args, parse_hex_color, parse_max_value, resolve_title
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


if __name__ == "__main__":
    unittest.main()
