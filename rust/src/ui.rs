//! 基于 ratatui 的 TUI 界面渲染
//! 仿 nload 的双面板布局：上半 Incoming / 下半 Outgoing

use std::collections::VecDeque;

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::Paragraph,
    Frame,
};

use crate::graph;
use crate::stats::{self, TrafficStats};
use crate::App;

/// 主绘制入口
pub fn draw(frame: &mut Frame, app: &App) {
    let area = frame.area();

    if area.height < 10 || area.width < 40 {
        draw_too_small(frame, area, app.emoji);
        return;
    }

    // 判断当前是否为 Windows 平台的 Loopback 设备，需要额外一行显示警告
    let show_loopback_warning = {
        #[cfg(target_os = "windows")]
        {
            app.current_view()
                .map(|v| v.info.name.to_lowercase().contains("loopback"))
                .unwrap_or(false)
        }
        #[cfg(not(target_os = "windows"))]
        { false }
    };

    let header_height = if show_loopback_warning { 3 } else { 2 };

    // 主布局: 头部(2或3行) + 内容 + 帮助栏(1行)
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(header_height), // Header + (warning) + separator
            Constraint::Min(6),               // Content (Incoming + Outgoing)
            Constraint::Length(1),             // Help bar
        ])
        .split(area);

    draw_header(frame, chunks[0], app, show_loopback_warning);
    draw_panels(frame, chunks[1], app);
    draw_help(frame, chunks[2], app.emoji);
}

// ─── Header ────────────────────────────────────────────────

fn draw_header(frame: &mut Frame, area: Rect, app: &App, show_loopback_warning: bool) {
    if let Some(view) = app.current_view() {
        let addr_str = if !view.info.addrs.is_empty() {
            format!(" [{}]", view.info.addrs[0])
        } else {
            String::new()
        };

        let header_text = if app.emoji {
            format!(
                "🖧 Device {}{} ({}/{}) 📡:",
                view.info.name,
                addr_str,
                app.current_idx + 1,
                app.views.len(),
            )
        } else {
            format!(
                "Device {}{} ({}/{}):",
                view.info.name,
                addr_str,
                app.current_idx + 1,
                app.views.len(),
            )
        };

        let header = Line::from(Span::styled(
            header_text,
            Style::default()
                .fg(Color::White)
                .add_modifier(Modifier::BOLD),
        ));

        let mut lines = vec![header];
        
        if show_loopback_warning {
            lines.push(Line::from(Span::styled(
                " \u{26a0} Loopback traffic stats are not available on Windows",
                Style::default().fg(Color::Yellow),
            )));
        }

        let text_height = lines.len() as u16;
        frame.render_widget(
            Paragraph::new(lines),
            Rect {
                height: text_height,
                ..area
            },
        );

        let sep_width = (area.width as usize).min(120);
        let separator = Line::from(Span::styled(
            "=".repeat(sep_width),
            Style::default().fg(Color::Cyan),
        ));
        frame.render_widget(
            Paragraph::new(vec![separator]),
            Rect {
                y: area.y + text_height,
                height: 1,
                ..area
            },
        );
    }
}

// ─── Panels ────────────────────────────────────────────────

fn draw_panels(frame: &mut Frame, area: Rect, app: &App) {
    let panels = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Percentage(50), Constraint::Percentage(50)])
        .split(area);

    if let Some(view) = app.current_view() {
        let (in_label, out_label) = if app.emoji {
            ("⬇️📥 Incoming", "⬆️📤 Outgoing")
        } else {
            ("Incoming", "Outgoing")
        };
        draw_traffic_panel(
            frame,
            panels[0],
            in_label,
            &view.engine.incoming,
            &view.engine.incoming_history,
            app.emoji,
        );
        draw_traffic_panel(
            frame,
            panels[1],
            out_label,
            &view.engine.outgoing,
            &view.engine.outgoing_history,
            app.emoji,
        );
    }
}

fn draw_traffic_panel(
    frame: &mut Frame,
    area: Rect,
    label: &str,
    stats: &TrafficStats,
    history: &VecDeque<f64>,
    emoji: bool,
) {
    if area.height < 2 || area.width < 20 {
        return;
    }

    // 面板内布局: 标签行(1) + 内容区
    let panel_chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Length(1), Constraint::Min(1)])
        .split(area);

    // ── 标签行 ──
    let peak = history.iter().cloned().fold(0.0_f64, f64::max);
    let scale_max = graph::next_power_of_2_scaled(peak);
    let scale_label = graph::get_graph_scale_label(scale_max);
    let label_line = Line::from(Span::styled(
        format!("{label} ({scale_label}):"),
        Style::default()
            .fg(Color::Green)
            .add_modifier(Modifier::BOLD),
    ));
    frame.render_widget(Paragraph::new(vec![label_line]), panel_chunks[0]);

    // ── 内容区: 左侧图形 + 右侧统计 ──
    let stat_width: u16 = if emoji { 28 } else { 24 };
    let content_chunks = Layout::default()
        .direction(Direction::Horizontal)
        .constraints([Constraint::Min(10), Constraint::Length(stat_width)])
        .split(panel_chunks[1]);

    draw_graph(frame, content_chunks[0], history, scale_max);
    draw_stats(frame, content_chunks[1], stats, emoji);
}

// ─── Graph ─────────────────────────────────────────────────

fn draw_graph(frame: &mut Frame, area: Rect, history: &VecDeque<f64>, max_value: f64) {
    let width = area.width as usize;
    let height = area.height as usize;

    let lines = graph::render_graph(history, width, height, max_value);

    let styled_lines: Vec<Line> = lines
        .iter()
        .map(|line| {
            let spans: Vec<Span> = line
                .chars()
                .map(|ch| match ch {
                    '#' => Span::styled("#", Style::default().fg(Color::Green)),
                    '|' => Span::styled("|", Style::default().fg(Color::Green)),
                    '.' => Span::styled(".", Style::default().fg(Color::DarkGray)),
                    _ => Span::raw(" "),
                })
                .collect();
            Line::from(spans)
        })
        .collect();

    frame.render_widget(Paragraph::new(styled_lines), area);
}

// ─── Stats ─────────────────────────────────────────────────

fn draw_stats(frame: &mut Frame, area: Rect, stats: &TrafficStats, emoji: bool) {
    let stat_lines = format_stats_lines(stats, emoji);
    let stat_count = stat_lines.len() as u16;

    // 底部对齐
    if area.height >= stat_count {
        let inner = Layout::default()
            .direction(Direction::Vertical)
            .constraints([Constraint::Min(0), Constraint::Length(stat_count)])
            .split(area);
        frame.render_widget(Paragraph::new(stat_lines), inner[1]);
    } else {
        frame.render_widget(Paragraph::new(stat_lines), area);
    }
}

fn format_stats_lines(st: &TrafficStats, emoji: bool) -> Vec<Line<'static>> {
    let label_style = Style::default()
        .fg(Color::Cyan)
        .add_modifier(Modifier::BOLD);
    let value_style = Style::default().fg(Color::White);

    if emoji {
        vec![
            Line::from(vec![
                Span::styled("⚡ Curr: ", label_style),
                Span::styled(stats::format_speed(st.current), value_style),
            ]),
            Line::from(vec![
                Span::styled("📊  Avg: ", label_style),
                Span::styled(stats::format_speed(st.average), value_style),
            ]),
            Line::from(vec![
                Span::styled("📏  Min: ", label_style),
                Span::styled(stats::format_speed(st.minimum), value_style),
            ]),
            Line::from(vec![
                Span::styled("🚀  Max: ", label_style),
                Span::styled(stats::format_speed(st.maximum), value_style),
            ]),
            Line::from(vec![
                Span::styled("📦  Ttl: ", label_style),
                Span::styled(stats::format_bytes(st.total), value_style),
            ]),
        ]
    } else {
        vec![
            Line::from(vec![
                Span::styled("Curr: ", label_style),
                Span::styled(stats::format_speed(st.current), value_style),
            ]),
            Line::from(vec![
                Span::styled(" Avg: ", label_style),
                Span::styled(stats::format_speed(st.average), value_style),
            ]),
            Line::from(vec![
                Span::styled(" Min: ", label_style),
                Span::styled(stats::format_speed(st.minimum), value_style),
            ]),
            Line::from(vec![
                Span::styled(" Max: ", label_style),
                Span::styled(stats::format_speed(st.maximum), value_style),
            ]),
            Line::from(vec![
                Span::styled(" Ttl: ", label_style),
                Span::styled(stats::format_bytes(st.total), value_style),
            ]),
        ]
    }
}

// ─── Help / Error ──────────────────────────────────────────

fn draw_help(frame: &mut Frame, area: Rect, emoji: bool) {
    let help_text = if emoji {
        " ⬅️/➡️ Switch Device | 🚪 q Quit"
    } else {
        " \u{2190}/\u{2192} Switch Device | q Quit"
    };
    let help = Line::from(Span::styled(
        help_text,
        Style::default().fg(Color::Yellow),
    ));
    frame.render_widget(Paragraph::new(vec![help]), area);
}

fn draw_too_small(frame: &mut Frame, area: Rect, emoji: bool) {
    let msg = if emoji {
        "😭 Terminal too small! 📌"
    } else {
        "Terminal too small!"
    };
    let x = area.width.saturating_sub(msg.len() as u16) / 2;
    let y = area.height / 2;
    let line = Line::from(Span::styled(
        msg,
        Style::default()
            .fg(Color::Red)
            .add_modifier(Modifier::BOLD),
    ));
    frame.render_widget(
        Paragraph::new(vec![line]),
        Rect {
            x: area.x + x,
            y: area.y + y,
            width: msg.len() as u16,
            height: 1,
        },
    );
}
