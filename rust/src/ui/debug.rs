// Draws the F3 runtime diagnostics overlay.

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::Paragraph,
    Frame,
};

use super::{color, pad};
use crate::app::App;
use crate::i18n::{language_name, t};
use crate::stats;

pub fn draw(frame: &mut Frame, area: Rect, app: &App) {
    let title = color(
        Style::default()
            .fg(Color::Cyan)
            .add_modifier(Modifier::BOLD),
        app.no_color,
    );
    let label = color(Style::default().fg(Color::Yellow), app.no_color);
    let mut lines = vec![
        Line::from(Span::styled(t("f3_title"), title)),
        Line::from(""),
    ];
    let mut row = |name: &str, value: String| {
        lines.push(Line::from(vec![
            Span::styled(format!("  {:<16}", name), label),
            Span::raw(value),
        ]))
    };
    row(
        t("debug_version"),
        format!("{} (Rust edition)", env!("CARGO_PKG_VERSION")),
    );
    row(
        t("debug_system"),
        format!(
            "{} | {} | {}",
            std::env::consts::OS,
            std::env::consts::ARCH,
            env!("TARGET")
        ),
    );
    row(t("debug_language"), language_name().into());
    row(t("debug_interval"), format!("{} ms", app.interval));
    row(t("debug_average"), format!("{} s", app.average));
    row(
        &format!("{}:", t("graph_style")),
        format!("{:?}", app.graph_style).to_lowercase(),
    );
    row(
        &format!("{}:", t("x_axis")),
        format!("{:?}", app.x_axis).to_lowercase(),
    );
    row(
        &format!("{}:", t("y_axis")),
        format!("{:?}", app.y_axis).to_lowercase(),
    );
    row(t("debug_no_graph"), on_off(app.no_graph).into());
    row(t("debug_no_color"), on_off(app.no_color).into());
    if let Some(view) = app.current_view() {
        row(
            t("debug_device_name"),
            format!(
                "{} ({}/{})",
                view.info.name,
                app.current_idx + 1,
                app.views.len()
            ),
        );
        row(
            t("debug_in_curr"),
            stats::format_speed_unit(view.engine.incoming.current, app.unit),
        );
        row(
            t("debug_out_curr"),
            stats::format_speed_unit(view.engine.outgoing.current, app.unit),
        );
    }
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Min(1), Constraint::Length(1)])
        .split(area);
    frame.render_widget(Paragraph::new(lines), chunks[0]);
    let help = if app.emoji {
        t("f3_help_bar_emoji")
    } else {
        t("f3_help_bar")
    };
    frame.render_widget(
        Paragraph::new(pad(help, chunks[1].width as usize)),
        chunks[1],
    );
}

fn on_off(value: bool) -> &'static str {
    if value {
        t("on")
    } else {
        t("off")
    }
}
