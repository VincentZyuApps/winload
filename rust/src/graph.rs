// 📊 Renders incoming and outgoing traffic graphs for terminal display.
//! 流量图形渲染
//! 仿 nload 的柱状图效果
//! - ASCII 模式 (默认): 使用 4 级字符: ' ', '.', '|', '#'
//! - Unicode 模式 (-U): 使用 Unicode block 字符: ' ', '·', '░', '▓', '█'

use std::collections::VecDeque;

use ratatui::layout::Rect;

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct AxisTick {
    pub position: u16,
    pub label: String,
}

#[derive(Debug)]
pub struct AxesLayout {
    pub plot: Rect,
    pub y_label_width: u16,
    pub x_ticks: Vec<AxisTick>,
    pub y_ticks: Vec<AxisTick>,
    pub duration_seconds: f64,
}

pub fn axes_layout(
    area: Rect,
    history_len: usize,
    sample_interval_ms: u64,
    x_interval_seconds: Option<u64>,
    y_labels: Vec<String>,
) -> AxesLayout {
    let label_width = y_labels
        .iter()
        .map(|label| label.chars().count())
        .max()
        .unwrap_or(0) as u16;
    let y_width = if label_width > 0 && area.width >= label_width.saturating_add(4) {
        label_width.saturating_add(1)
    } else {
        0
    };
    let x_height = u16::from(x_interval_seconds.is_some() && area.height >= 2);
    let plot = Rect::new(
        area.x.saturating_add(y_width),
        area.y,
        area.width.saturating_sub(y_width),
        area.height.saturating_sub(x_height),
    );
    let visible = history_len.min(plot.width as usize);
    let duration_ms = (visible.saturating_sub(1) as u64).saturating_mul(sample_interval_ms);
    let x_ticks = x_interval_seconds
        .map(|seconds| time_ticks(plot.width, duration_ms, seconds))
        .unwrap_or_default();
    let y_ticks = y_labels
        .into_iter()
        .enumerate()
        .filter(|_| !plot.is_empty())
        .map(|(index, label)| AxisTick {
            position: match index {
                0 => 0,
                1 => plot.height / 2,
                _ => plot.height.saturating_sub(1),
            },
            label,
        })
        .collect();
    AxesLayout {
        plot,
        y_label_width: y_width,
        x_ticks,
        y_ticks,
        duration_seconds: (duration_ms as f64 / 1000.0).max(sample_interval_ms as f64 / 1000.0),
    }
}

/// Builds right-to-left elapsed-time ticks, thinning dense intervals by an integer multiple.
pub fn time_ticks(width: u16, duration_ms: u64, interval_seconds: u64) -> Vec<AxisTick> {
    if width == 0 {
        return Vec::new();
    }
    if duration_ms == 0 || width == 1 {
        return vec![AxisTick {
            position: width - 1,
            label: "0s".into(),
        }];
    }
    let base_ms = interval_seconds.max(1).saturating_mul(1000);
    let columns = u64::from(width - 1);
    let minimum_ms = (6_u64
        .saturating_mul(duration_ms)
        .saturating_add(columns - 1))
        / columns;
    let multiple = minimum_ms.saturating_add(base_ms - 1) / base_ms;
    let step_ms = base_ms.saturating_mul(multiple.max(1));
    let mut ticks = Vec::new();
    let mut elapsed = 0_u64;
    while elapsed <= duration_ms {
        ticks.push(AxisTick {
            position: (duration_ms.saturating_sub(elapsed).saturating_mul(columns) / duration_ms)
                as u16,
            label: if elapsed == 0 {
                "0s".into()
            } else {
                format!("-{}s", elapsed / 1000)
            },
        });
        let Some(next) = elapsed.checked_add(step_ms) else {
            break;
        };
        elapsed = next;
    }
    ticks
}

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
pub fn get_graph_scale_label_unit(max_value: f64, unit: crate::config::Unit) -> String {
    use crate::stats::format_speed_unit;
    format!("100% @ {}", format_speed_unit(max_value, unit))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn classic_keeps_latest_sample_on_the_right() {
        let history = VecDeque::from([2048.0, 0.0]);
        assert_eq!(render_graph(&history, 2, 1, 2048.0, false), vec![" #"]);
    }

    #[test]
    fn empty_dimensions_are_safe() {
        assert!(render_graph(&VecDeque::new(), 0, 5, 0.0, false).is_empty());
    }

    #[test]
    fn time_ticks_use_history_span_and_thin_by_integer_multiples() {
        let regular = time_ticks(61, 30_000, 5);
        assert_eq!(regular.first().unwrap().label, "0s");
        assert_eq!(regular.last().unwrap().label, "-30s");
        assert_eq!(regular.len(), 7);

        let dense = time_ticks(20, 9_500, 1);
        assert!(dense.iter().all(|tick| {
            tick.label == "0s"
                || tick.label[1..tick.label.len() - 1].parse::<u64>().unwrap() % 3 == 0
        }));
    }
}
