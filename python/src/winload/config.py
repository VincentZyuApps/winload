# Defines immutable, strongly typed runtime configuration for the Python application.
"""Normalized configuration shared by the CLI, app, runtime, and UI layers."""

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple


class StringEnum(str, Enum):
    """A string-compatible enum suitable for argparse and rendering code."""

    def __str__(self) -> str:
        return self.value


class Unit(StringEnum):
    BIT = "bit"
    BYTE = "byte"


class BarStyle(StringEnum):
    FILL = "fill"
    COLOR = "color"
    PLAIN = "plain"


class TitleAlign(StringEnum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class MaxMode(StringEnum):
    SMART = "smart"
    LEGACY = "legacy"
    FIXED = "fixed"


RgbColor = Tuple[int, int, int]

MIN_SAMPLE_CAPACITY = 600
MAX_SAMPLE_CAPACITY = 60_000


def requested_sample_capacity(interval_ms: int, average_window_sec: int) -> int:
    """Return the number of snapshots required by a requested average window."""
    return max(1000 * average_window_sec // interval_ms, MIN_SAMPLE_CAPACITY)


@dataclass(frozen=True)
class RunConfig:
    """Validated runtime settings produced by the CLI boundary."""

    interval: int = 500
    average: int = 300
    device: Optional[str] = None
    title: Optional[str] = None
    title_align: TitleAlign = TitleAlign.CENTER
    debug_info: bool = False
    emoji: bool = False
    unicode: bool = False
    unit: Unit = Unit.BIT
    bar_style: BarStyle = BarStyle.PLAIN
    in_color: Optional[RgbColor] = None
    out_color: Optional[RgbColor] = None
    max_mode: MaxMode = MaxMode.SMART
    max_half_life: float = 10.0
    max_y_value: Optional[float] = None
    no_graph: bool = False
    hide_separator: bool = False
    no_color: bool = False
    netlink: bool = False
    lang: str = "en-us"
