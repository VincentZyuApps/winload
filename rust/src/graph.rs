// 📊 Renders incoming and outgoing traffic graphs for terminal display.
//! 流量图形渲染
//! 仿 nload 的柱状图效果
//! - ASCII 模式 (默认): 使用 4 级字符: ' ', '.', '|', '#'
//! - Unicode 模式 (-U): 使用 Unicode block 字符: ' ', '·', '░', '▓', '█'

use std::collections::VecDeque;

/// 返回 >= value 的最近的 2 的幂次方，最小 2048 (2 KiB/s)
pub fn next_power_of_2_scaled(value: f64) -> f64 {
    if value <= 2048.0 {
        return 2048.0;
    }
    let mut result = 2048.0;
    while result < value {
        result *= 2.0;
    }
    result
}

/// 渲染柱状图
///
/// - `history`: 速率历史 (front = 最新值，越往后越旧)
/// - `width`:   图形宽度（字符列数）
/// - `height`:  图形高度（字符行数）
/// - `max_value`: 缩放上限，0.0 表示自动
/// - `unicode`:  true 使用 Unicode block 字符，false 使用 ASCII 字符
///
/// 返回 `height` 行的字符串列表，每行 `width` 个字符
pub fn render_graph(
    history: &VecDeque<f64>,
    width: usize,
    height: usize,
    max_value: f64,
    unicode: bool,
) -> Vec<String> {
    if width == 0 || height == 0 {
        return vec![];
    }

    // 取数据切片（最多 width 个值）
    let mut values: Vec<f64> = history
        .iter()
        .take(width)
        .copied()
        .map(|v| v.max(0.0))
        .collect();

    // 补齐不足 width 的部分
    values.resize(width, 0.0);

    // 自动缩放
    let max_val = if max_value <= 0.0 {
        let peak = values.iter().cloned().fold(0.0_f64, f64::max);
        next_power_of_2_scaled(peak)
    } else {
        max_value
    };
    let max_val = if max_val <= 0.0 { 2048.0 } else { max_val };

    // 字符集: (full, high, low, dot)
    let (ch_full, ch_high, ch_low, ch_dot) = if unicode {
        ('█', '▓', '░', '·')
    } else {
        ('#', '|', '.', '.')
    };

    // 逐行渲染 (第 0 行 = 最顶部)
    let mut lines = Vec::with_capacity(height);
    for row in 0..height {
        let mut chars = String::with_capacity(width);
        for col in 0..width {
            // values[0] 是最新值，显示在最右边
            let val_idx = width - 1 - col;
            let value = values[val_idx];

            let lower_limit = max_val * (height - row - 1) as f64 / height as f64;
            let traffic_per_line = max_val / height as f64;

            if value <= lower_limit {
                chars.push(' ');
            } else {
                let rest = value - lower_limit;
                if rest >= traffic_per_line {
                    chars.push(ch_full);
                } else if rest >= traffic_per_line * 0.7 {
                    chars.push(ch_high);
                } else if rest >= traffic_per_line * 0.3 {
                    chars.push(ch_low);
                } else {
                    chars.push(ch_dot);
                }
            }
        }
        lines.push(chars);
    }
    lines
}

/// 返回带单位选择的图形缩放标签
pub fn get_graph_scale_label_unit(max_value: f64, unit: crate::Unit) -> String {
    use crate::stats::format_speed_unit;
    format!("100% @ {}", format_speed_unit(max_value, unit))
}
