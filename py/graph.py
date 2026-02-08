"""
graph.py - ASCII 流量图形渲染
仿 nload 的柱状图效果，使用 4 级 ASCII 字符: ' ', '.', '|', '#'
"""

from collections import deque
from typing import List


def next_power_of_2_scaled(value: float) -> float:
    """
    返回 >= value 的最近的 2 的幂次方。
    用于图形的自动缩放上限。最小返回 2048 (2 KiB/s)。
    """
    if value <= 2048:
        return 2048.0
    result = 2048.0
    while result < value:
        result *= 2
    return result


def render_graph(
    history: deque,
    width: int,
    height: int,
    max_value: float = 0.0,
) -> List[str]:
    """
    渲染 ASCII 柱状图。

    参数:
        history: 速率历史 deque（[0] 是最新值，越往后越旧）
        width:   图形宽度（字符列数）
        height:  图形高度（字符行数）
        max_value: 缩放上限，0 表示自动

    返回:
        包含 height 行的字符串列表，每行 width 个字符
    """
    if width <= 0 or height <= 0:
        return []

    # 取实际需要的数据切片（最多 width 个值）
    values = []
    for i, v in enumerate(history):
        if i >= width:
            break
        values.append(max(v, 0.0))

    # 补齐不足 width 的部分
    while len(values) < width:
        values.append(0.0)

    # 自动缩放
    if max_value <= 0:
        peak = max(values) if values else 0.0
        max_value = next_power_of_2_scaled(peak)

    if max_value <= 0:
        max_value = 2048.0

    # 逐行渲染 (第 0 行 = 最顶部)
    lines: List[str] = []
    for row in range(height):
        chars = []
        for col in range(width):
            # values 是从新到旧，显示时最新在右边
            val_idx = width - 1 - col
            value = values[val_idx] if val_idx < len(values) else 0.0

            # 该行代表的区间
            lower_limit = max_value * (height - row - 1) / height
            traffic_per_line = max_value / height

            if value <= lower_limit:
                chars.append(" ")
            else:
                rest = value - lower_limit
                if rest >= traffic_per_line:
                    chars.append("#")
                elif rest >= traffic_per_line * 0.7:
                    chars.append("|")
                elif rest >= traffic_per_line * 0.3:
                    chars.append(".")
                else:
                    chars.append(" ")

        lines.append("".join(chars))

    return lines


def get_graph_scale_label(max_value: float) -> str:
    """返回图形缩放比例的标签文字，例如 '100% @ 1.25 MBit/s'"""
    from stats import format_speed
    return f"100% @ {format_speed(max_value)}"
