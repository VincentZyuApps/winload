// Coordinates the ratatui layout, header, help bar, panels, and debug overlay.

mod debug;
mod panels;

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::Paragraph,
    Frame,
};

use crate::app::App;
use crate::config::{BarStyle, TitleAlign};
use crate::i18n::t;
#[cfg(target_os = "windows")]
use crate::loopback::LoopbackMode;

pub(super) fn color(style: Style, no_color: bool) -> Style {
    if no_color {
        Style::default()
    } else {
        style
    }
}

pub(super) fn display_width(value: &str) -> usize {
    unicode_width::UnicodeWidthStr::width(value)
}

pub(super) fn pad(value: &str, width: usize) -> String {
    format!(
        "{value}{}",
        " ".repeat(width.saturating_sub(display_width(value)))
    )
}

pub fn draw(frame: &mut Frame, app: &App) {
    let area = frame.area();
    if area.height < 10 || area.width < 40 {
        draw_too_small(frame, area, app);
        return;
    }
    if app.show_debug {
        debug::draw(frame, area, app);
        return;
    }

    let loopback = app
        .current_view()
        .map(|view| view.info.name.to_lowercase().contains("loopback"))
        .unwrap_or(false);
    #[cfg(target_os = "windows")]
    let warning = loopback && app.loopback_mode == LoopbackMode::None;
    #[cfg(not(target_os = "windows"))]
    let warning = false;
    let info = loopback && app.loopback_info.is_some();
    let header_height = 1
        + u16::from(app.title.is_some())
        + u16::from(warning || info)
        + u16::from(!app.hide_separator);
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(header_height),
            Constraint::Min(6),
            Constraint::Length(1),
        ])
        .split(area);
    draw_header(frame, chunks[0], app, warning, info);
    panels::draw(frame, chunks[1], app);
    draw_help(frame, chunks[2], app);
}

fn aligned(value: &str, width: usize, align: TitleAlign, fill: bool) -> String {
    let available = width.saturating_sub(display_width(value));
    let left = match align {
        TitleAlign::Left => 0,
        TitleAlign::Center => available / 2,
        TitleAlign::Right => available,
    };
    let right = if fill { available - left } else { 0 };
    format!("{}{value}{}", " ".repeat(left), " ".repeat(right))
}

fn bar_style(style: BarStyle, accent: Color, no_color: bool) -> Style {
    color(
        match style {
            BarStyle::Fill | BarStyle::Color => Style::default()
                .bg(accent)
                .fg(Color::Black)
                .add_modifier(Modifier::BOLD),
            BarStyle::Plain => Style::default().fg(accent).add_modifier(Modifier::BOLD),
        },
        no_color,
    )
}

fn draw_header(frame: &mut Frame, area: Rect, app: &App, warning: bool, info: bool) {
    let Some(view) = app.current_view() else {
        return;
    };
    let width = area.width as usize;
    let address = view
        .info
        .addrs
        .first()
        .map(|value| format!(" [{value}]"))
        .unwrap_or_default();
    let mode = if view.info.name.to_lowercase().contains("loopback") {
        #[cfg(target_os = "windows")]
        {
            if app.loopback_mode == LoopbackMode::Npcap {
                " [npcap]"
            } else {
                ""
            }
        }
        #[cfg(not(target_os = "windows"))]
        {
            ""
        }
    } else {
        ""
    };
    let label = if app.emoji {
        t("device_emoji")
    } else {
        t("device")
    };
    let device = format!(
        "{label} {}{address} ({}/{}){mode} :",
        view.info.name,
        app.current_idx + 1,
        app.views.len()
    );
    let style = bar_style(app.bar_style, Color::White, app.no_color);
    let mut lines = Vec::new();
    if let Some(title) = &app.title {
        lines.push(Line::from(Span::styled(
            aligned(
                title,
                width,
                app.title_align,
                app.bar_style == BarStyle::Fill,
            ),
            style,
        )));
    }
    lines.push(Line::from(Span::styled(
        if app.bar_style == BarStyle::Fill {
            pad(&device, width)
        } else {
            device
        },
        style,
    )));
    if warning {
        lines.push(Line::from(Span::styled(
            t("loopback_warning"),
            color(Style::default().fg(Color::Yellow), app.no_color),
        )));
    } else if info {
        lines.push(Line::from(Span::styled(
            format!(" {}", app.loopback_info.as_deref().unwrap_or_default()),
            color(Style::default().fg(Color::Green), app.no_color),
        )));
    }
    if !app.hide_separator {
        lines.push(Line::from(Span::styled(
            "=".repeat(width),
            color(Style::default().fg(Color::Cyan), app.no_color),
        )));
    }
    frame.render_widget(Paragraph::new(lines), area);
}

fn draw_help(frame: &mut Frame, area: Rect, app: &App) {
    let base = match (std::env::consts::OS, app.emoji) {
        ("windows", true) => t("help_bar_win_emoji"),
        ("windows", false) => t("help_bar_win"),
        ("linux", true) => t("help_bar_linux_emoji"),
        ("linux", false) => t("help_bar_linux"),
        (_, true) => t("help_bar_emoji"),
        (_, false) => t("help_bar"),
    };
    let text = format!("{base} | {}", graph_shortcut_help(app.emoji));
    let text = if app.bar_style == BarStyle::Fill {
        pad(&text, area.width as usize)
    } else {
        text
    };
    frame.render_widget(
        Paragraph::new(Line::from(Span::styled(
            text,
            bar_style(app.bar_style, Color::White, app.no_color),
        ))),
        area,
    );
}

fn graph_shortcut_help(emoji: bool) -> String {
    let icons = if emoji {
        ("📈 ", "⏱️ ", "📏 ")
    } else {
        ("", "", "")
    };
    format!(
        "{}g {} | {}x {} | {}y {}",
        icons.0,
        t("graph_style"),
        icons.1,
        t("x_axis"),
        icons.2,
        t("y_axis")
    )
}

#[cfg(test)]
mod tests {
    use super::graph_shortcut_help;

    #[test]
    fn graph_shortcut_icons_follow_emoji_mode() {
        let plain = graph_shortcut_help(false);
        assert!(!plain.contains('📈'));
        assert!(!plain.contains('⏱'));
        assert!(!plain.contains('📏'));

        let emoji = graph_shortcut_help(true);
        assert!(emoji.contains("📈 g "));
        assert!(emoji.contains("⏱️ x "));
        assert!(emoji.contains("📏 y "));
    }
}

fn draw_too_small(frame: &mut Frame, area: Rect, app: &App) {
    let message = if app.emoji {
        t("terminal_too_small_emoji")
    } else {
        t("terminal_too_small")
    };
    let width = display_width(message).min(area.width as usize) as u16;
    let rect = Rect::new(
        area.x + area.width.saturating_sub(width) / 2,
        area.y + area.height / 2,
        width,
        1,
    );
    frame.render_widget(
        Paragraph::new(Line::from(Span::styled(
            message,
            color(
                Style::default().fg(Color::Red).add_modifier(Modifier::BOLD),
                app.no_color,
            ),
        ))),
        rect,
    );
}
