// Draws traffic histories in classic, line, scatter, and bar styles with optional axes.

use std::collections::VecDeque;

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    symbols::Marker,
    text::{Line, Span},
    widgets::{Axis, Chart, Dataset, GraphType, Paragraph, Sparkline},
    Frame,
};

use super::{color, display_width, pad};
use crate::app::App;
use crate::config::{BarStyle, GraphStyle, MaxMode, YAxis};
use crate::graph;
use crate::i18n::t;
use crate::stats::{self, TrafficStats};

pub fn draw(frame: &mut Frame, area: Rect, app: &App) {
    let halves = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Percentage(50), Constraint::Percentage(50)])
        .split(area);
    let Some(view) = app.current_view() else {
        return;
    };
    let labels = if app.emoji {
        (t("incoming_emoji"), t("outgoing_emoji"))
    } else {
        (t("incoming"), t("outgoing"))
    };
    draw_panel(
        frame,
        halves[0],
        app,
        labels.0,
        &view.engine.incoming,
        &view.engine.incoming_history,
        view.engine.incoming_smooth_peak,
        view.engine.incoming_smooth_peak_rising,
        app.in_color,
    );
    draw_panel(
        frame,
        halves[1],
        app,
        labels.1,
        &view.engine.outgoing,
        &view.engine.outgoing_history,
        view.engine.outgoing_smooth_peak,
        view.engine.outgoing_smooth_peak_rising,
        app.out_color,
    );
}

fn draw_panel(
    frame: &mut Frame,
    area: Rect,
    app: &App,
    label: &str,
    stats_value: &TrafficStats,
    history: &VecDeque<f64>,
    smooth_peak: f64,
    rising: bool,
    accent: Color,
) {
    if area.height < 2 || area.width < 20 {
        return;
    }
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Length(1), Constraint::Min(1)])
        .split(area);
    let history_peak = history.iter().copied().fold(0.0_f64, f64::max);
    let scale = match app.max_mode {
        MaxMode::Fixed => app
            .max_y_value
            .unwrap_or_else(|| graph::next_power_of_2_scaled(history_peak)),
        MaxMode::Smart => graph::next_power_of_2_scaled(smooth_peak),
        MaxMode::Legacy => graph::next_power_of_2_scaled(history_peak),
    };
    let mode = match app.max_mode {
        MaxMode::Fixed => format!(
            " [{}: {}]",
            t("tag_fixed"),
            stats::format_speed_unit(scale, app.unit)
        ),
        MaxMode::Smart => format!(
            " [{} {}s] {}",
            t("tag_smart_max"),
            app.max_half_life,
            if rising {
                t("arrow_up")
            } else {
                t("arrow_down")
            }
        ),
        MaxMode::Legacy => format!(" [{}]", t("tag_legacy")),
    };
    let text = format!(
        "{label} ({}){mode}:",
        graph::get_graph_scale_label_unit(scale, app.unit)
    );
    let style = color(
        match app.bar_style {
            BarStyle::Fill | BarStyle::Color => Style::default()
                .bg(accent)
                .fg(Color::Black)
                .add_modifier(Modifier::BOLD),
            BarStyle::Plain => Style::default().fg(accent).add_modifier(Modifier::BOLD),
        },
        app.no_color,
    );
    frame.render_widget(
        Paragraph::new(Span::styled(
            if app.bar_style == BarStyle::Fill {
                pad(&text, area.width as usize)
            } else {
                text
            },
            style,
        )),
        chunks[0],
    );
    if app.no_graph {
        draw_stats(frame, chunks[1], stats_value, app);
        return;
    }
    let stat_width = if app.emoji { 28 } else { 24 };
    let body = Layout::default()
        .direction(Direction::Horizontal)
        .constraints([Constraint::Min(10), Constraint::Length(stat_width)])
        .split(chunks[1]);
    draw_graph(frame, body[0], history, scale, accent, app);
    draw_stats(frame, body[1], stats_value, app);
}

fn draw_graph(
    frame: &mut Frame,
    area: Rect,
    history: &VecDeque<f64>,
    max_value: f64,
    accent: Color,
    app: &App,
) {
    let y_labels = match app.y_axis {
        YAxis::None => Vec::new(),
        YAxis::Percent => vec!["100%".into(), "50%".into(), "0%".into()],
        YAxis::Unit => vec![
            stats::format_speed_unit(max_value, app.unit),
            stats::format_speed_unit(max_value / 2.0, app.unit),
            "0".into(),
        ],
    };
    let axes = graph::axes_layout(area, app.interval, app.x_axis.interval(), y_labels);
    if axes.plot.is_empty() {
        return;
    }
    match app.graph_style {
        GraphStyle::Classic => draw_classic(
            frame,
            axes.plot,
            history,
            max_value,
            accent,
            app.unicode,
            app.no_color,
        ),
        GraphStyle::Bar => draw_bar(frame, axes.plot, history, max_value, accent, app.no_color),
        GraphStyle::Line | GraphStyle::Scatter => draw_chart(
            frame,
            axes.plot,
            history,
            max_value,
            axes.duration_seconds,
            accent,
            app.graph_style,
            app.interval,
            app.no_color,
        ),
    }
    draw_axes(frame, &axes, app.unicode, app.no_color, app.graph_style);
}

fn draw_axes(
    frame: &mut Frame,
    axes: &graph::AxesLayout,
    unicode: bool,
    no_color: bool,
    graph_style: GraphStyle,
) {
    let grid_style = color(Style::default().fg(Color::DarkGray), no_color);
    let (vertical, horizontal) = if unicode { ("│", "─") } else { ("|", "-") };
    let buffer = frame.buffer_mut();
    for tick in &axes.y_ticks {
        let y = axes.plot.y.saturating_add(tick.position);
        for x in axes.plot.x..axes.plot.right() {
            let cell = &mut buffer[(x, y)];
            if grid_replaceable(cell.symbol(), graph_style) {
                cell.set_symbol(horizontal).set_style(grid_style);
            }
        }
    }
    for tick in &axes.x_ticks {
        let x = axes.plot.x.saturating_add(tick.position);
        for y in axes.plot.y..axes.plot.bottom() {
            let cell = &mut buffer[(x, y)];
            if grid_replaceable(cell.symbol(), graph_style) {
                cell.set_symbol(vertical).set_style(grid_style);
            }
        }
    }
    for tick in &axes.y_ticks {
        if axes.y_label_width > 0 {
            frame.render_widget(
                Paragraph::new(tick.label.as_str()),
                Rect::new(
                    axes.plot.x - axes.y_label_width,
                    axes.plot.y + tick.position,
                    axes.y_label_width,
                    1,
                ),
            );
        }
    }
    if axes.plot.bottom() < frame.area().bottom() {
        for tick in &axes.x_ticks {
            let width = display_width(&tick.label).min(axes.plot.width as usize) as u16;
            let center = axes.plot.x.saturating_add(tick.position);
            let start = center
                .saturating_sub(width / 2)
                .clamp(axes.plot.x, axes.plot.right().saturating_sub(width));
            frame.render_widget(
                Paragraph::new(tick.label.as_str()),
                Rect::new(start, axes.plot.bottom(), width, 1),
            );
        }
    }
}

fn grid_replaceable(symbol: &str, style: GraphStyle) -> bool {
    symbol == " " || (style == GraphStyle::Classic && matches!(symbol, "." | "░" | "·"))
}

fn draw_classic(
    frame: &mut Frame,
    area: Rect,
    history: &VecDeque<f64>,
    max_value: f64,
    accent: Color,
    unicode: bool,
    no_color: bool,
) {
    let lines = graph::render_graph(
        history,
        area.width as usize,
        area.height as usize,
        max_value,
        unicode,
    );
    let rendered: Vec<Line> = lines
        .into_iter()
        .map(|line| {
            Line::from(
                line.chars()
                    .map(|character| {
                        let foreground = if matches!(character, '#' | '|' | '█' | '▓') {
                            accent
                        } else {
                            Color::DarkGray
                        };
                        Span::styled(
                            character.to_string(),
                            color(Style::default().fg(foreground), no_color),
                        )
                    })
                    .collect::<Vec<_>>(),
            )
        })
        .collect();
    frame.render_widget(Paragraph::new(rendered), area);
}

fn draw_bar(
    frame: &mut Frame,
    area: Rect,
    history: &VecDeque<f64>,
    max_value: f64,
    accent: Color,
    no_color: bool,
) {
    const SPARKLINE_MAX: u64 = 1_000_000;
    let visible = history.len().min(area.width as usize);
    let mut values = vec![0; area.width as usize - visible];
    values.extend(
        history.iter().take(visible).copied().rev().map(|value| {
            ((value / max_value.max(1.0)).clamp(0.0, 1.0) * SPARKLINE_MAX as f64) as u64
        }),
    );
    frame.render_widget(
        Sparkline::default()
            .data(&values)
            .max(SPARKLINE_MAX)
            .style(color(Style::default().fg(accent), no_color)),
        area,
    );
}

fn draw_chart(
    frame: &mut Frame,
    area: Rect,
    history: &VecDeque<f64>,
    max_value: f64,
    duration: f64,
    accent: Color,
    graph_style: GraphStyle,
    interval: u64,
    no_color: bool,
) {
    let count = area.width.max(1) as usize;
    let values: Vec<f64> = history.iter().take(count).copied().rev().collect();
    let step = interval as f64 / 1000.0;
    let history_duration = values.len().saturating_sub(1) as f64 * step;
    let points: Vec<(f64, f64)> = values
        .iter()
        .enumerate()
        .map(|(index, value)| {
            (
                -history_duration + index as f64 * step,
                value.clamp(0.0, max_value),
            )
        })
        .collect();
    let dataset = Dataset::default()
        .marker(Marker::Braille)
        .graph_type(if graph_style == GraphStyle::Line {
            GraphType::Line
        } else {
            GraphType::Scatter
        })
        .style(color(Style::default().fg(accent), no_color))
        .data(&points);
    frame.render_widget(
        Chart::new(vec![dataset])
            .x_axis(Axis::default().bounds([-duration, 0.0]))
            .y_axis(Axis::default().bounds([0.0, max_value])),
        area,
    );
}

fn draw_stats(frame: &mut Frame, area: Rect, value: &TrafficStats, app: &App) {
    let keys = if app.emoji {
        [
            "stat_curr_emoji",
            "stat_avg_emoji",
            "stat_min_emoji",
            "stat_max_emoji",
            "stat_ttl_emoji",
        ]
    } else {
        ["stat_curr", "stat_avg", "stat_min", "stat_max", "stat_ttl"]
    };
    let labels: Vec<&str> = keys.iter().map(|key| t(key)).collect();
    let width = labels
        .iter()
        .map(|label| display_width(label))
        .max()
        .unwrap_or(0);
    let values = [
        stats::format_speed_unit(value.current, app.unit),
        stats::format_speed_unit(value.average, app.unit),
        stats::format_speed_unit(value.minimum, app.unit),
        stats::format_speed_unit(value.maximum, app.unit),
        stats::format_bytes(value.total),
    ];
    let lines: Vec<Line> = labels
        .into_iter()
        .zip(values)
        .map(|(label, value)| {
            Line::from(vec![
                Span::styled(
                    format!(
                        "{}{}: ",
                        " ".repeat(width.saturating_sub(display_width(label))),
                        label
                    ),
                    color(
                        Style::default()
                            .fg(Color::Cyan)
                            .add_modifier(Modifier::BOLD),
                        app.no_color,
                    ),
                ),
                Span::styled(
                    value,
                    color(Style::default().fg(Color::White), app.no_color),
                ),
            ])
        })
        .collect();
    let target = if area.height >= lines.len() as u16 {
        Layout::default()
            .direction(Direction::Vertical)
            .constraints([Constraint::Min(0), Constraint::Length(lines.len() as u16)])
            .split(area)[1]
    } else {
        area
    };
    frame.render_widget(Paragraph::new(lines), target);
}

#[cfg(test)]
mod tests {
    use super::*;
    use ratatui::{backend::TestBackend, Terminal};
    use GraphStyle::{Bar, Classic, Line as LineGraph, Scatter};

    fn render_style(style: GraphStyle, width: u16, height: u16) -> String {
        let mut terminal = Terminal::new(TestBackend::new(width, height)).unwrap();
        let history = VecDeque::from([2048.0, 1024.0, 512.0, 256.0]);
        terminal
            .draw(|frame| {
                let axes = graph::axes_layout(
                    frame.area(),
                    500,
                    Some(1),
                    vec!["100%".into(), "50%".into(), "0%".into()],
                );
                match style {
                    GraphStyle::Classic => draw_classic(
                        frame,
                        axes.plot,
                        &history,
                        2048.0,
                        Color::Cyan,
                        false,
                        false,
                    ),
                    GraphStyle::Bar => {
                        draw_bar(frame, axes.plot, &history, 2048.0, Color::Cyan, false)
                    }
                    GraphStyle::Line | GraphStyle::Scatter => draw_chart(
                        frame,
                        axes.plot,
                        &history,
                        2048.0,
                        axes.duration_seconds,
                        Color::Cyan,
                        style,
                        500,
                        false,
                    ),
                }
                draw_axes(frame, &axes, false, false, style);
            })
            .unwrap();
        terminal
            .backend()
            .buffer()
            .content
            .iter()
            .map(|cell| cell.symbol())
            .collect()
    }

    #[test]
    fn every_style_renders_with_axes_and_survives_tiny_areas() {
        for style in [Classic, LineGraph, Scatter, Bar] {
            let rendered = render_style(style, 24, 6);
            assert!(!rendered.trim().is_empty(), "{style:?}");
            assert!(rendered.contains('-'), "{style:?}");
            assert!(rendered.contains('|'), "{style:?}");
            assert_eq!(render_style(style, 1, 1).chars().count(), 1);
        }
    }

    #[test]
    fn classic_grid_only_replaces_background_symbols() {
        for symbol in [" ", ".", "░", "·"] {
            assert!(grid_replaceable(symbol, GraphStyle::Classic));
        }
        for symbol in ["#", "|", "█", "▓"] {
            assert!(!grid_replaceable(symbol, GraphStyle::Classic));
        }
    }
}
