// Runs the terminal lifecycle, refresh loop, and semantic keyboard controls.

use std::io;
use std::time::{Duration, Instant};

use crossterm::event::{self, Event, KeyCode, KeyEventKind, KeyModifiers};

use crate::app::App;
use crate::config::RunConfig;
use crate::loopback::{self, LoopbackCounters, LoopbackMode};
use crate::ui;

pub fn run(terminal: &mut ratatui::DefaultTerminal, config: RunConfig) -> io::Result<String> {
    let tick_rate = Duration::from_millis(config.interval);
    let mut app = App::new(config);
    start_loopback(&mut app)?;
    let mut last_tick = Instant::now();
    app.update();

    loop {
        terminal.draw(|frame| ui::draw(frame, &app))?;
        let timeout = tick_rate
            .checked_sub(last_tick.elapsed())
            .unwrap_or_default();
        if event::poll(timeout)? {
            if let Event::Key(key) = event::read()? {
                if key.kind == KeyEventKind::Press && handle_key(&mut app, key.code, key.modifiers)
                {
                    return Ok(app.exit_info());
                }
            }
        }
        if last_tick.elapsed() >= tick_rate {
            app.update();
            last_tick = Instant::now();
        }
    }
}

fn start_loopback(app: &mut App) -> io::Result<()> {
    if app.loopback_mode == LoopbackMode::None {
        return Ok(());
    }
    let counters = LoopbackCounters::new();
    let result = match app.loopback_mode {
        LoopbackMode::Npcap => loopback::platform::start_npcap(counters.clone()),
        LoopbackMode::None => unreachable!(),
    };
    match result {
        Ok((info, capture)) => {
            app.loopback_info = Some(info);
            app.loopback_counters = Some(counters);
            app.loopback_capture = Some(capture);
            Ok(())
        }
        Err(error) => Err(io::Error::other(format!(
            "Failed to start loopback capture:\n{error}"
        ))),
    }
}

fn handle_key(app: &mut App, code: KeyCode, modifiers: KeyModifiers) -> bool {
    match code {
        KeyCode::Char('q') | KeyCode::Char('Q') | KeyCode::Esc => true,
        KeyCode::Char('c') if modifiers.contains(KeyModifiers::CONTROL) => true,
        KeyCode::Char('=') => {
            app.hide_separator = !app.hide_separator;
            false
        }
        KeyCode::Char('c') | KeyCode::Char('C') => {
            app.no_color = !app.no_color;
            false
        }
        KeyCode::Char('g') | KeyCode::Char('G') => {
            app.cycle_graph_style();
            false
        }
        KeyCode::Char('x') | KeyCode::Char('X') => {
            app.toggle_x_axis();
            false
        }
        KeyCode::Char('y') | KeyCode::Char('Y') => {
            app.cycle_y_axis();
            false
        }
        KeyCode::F(3) => {
            app.show_debug = !app.show_debug;
            false
        }
        KeyCode::Right | KeyCode::Down | KeyCode::Tab | KeyCode::Enter | KeyCode::PageDown => {
            app.next_device();
            false
        }
        KeyCode::Left | KeyCode::Up | KeyCode::PageUp => {
            app.prev_device();
            false
        }
        _ => false,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use clap::Parser;

    use crate::app::DeviceView;
    use crate::cli::Args;
    use crate::collector::DeviceInfo;
    use crate::stats::StatisticsEngine;

    fn app_for_shortcut_tests() -> App {
        let config = Args::try_parse_from(["winload"]).unwrap().into_config();
        let mut app = App::new(config);
        app.views = ["first", "second"]
            .into_iter()
            .map(|name| DeviceView {
                info: DeviceInfo {
                    name: name.into(),
                    addrs: Vec::new(),
                },
                engine: StatisticsEngine::new(500, 300, Some(10.0)),
            })
            .collect();
        app.current_idx = 0;
        app
    }

    #[test]
    fn python_compatible_shortcuts_work_in_rust() {
        let mut app = app_for_shortcut_tests();

        assert!(!handle_key(&mut app, KeyCode::Char('C'), KeyModifiers::SHIFT));
        assert!(app.no_color);

        assert!(!handle_key(&mut app, KeyCode::PageDown, KeyModifiers::NONE));
        assert_eq!(app.current_idx, 1);
        assert!(!handle_key(&mut app, KeyCode::PageUp, KeyModifiers::NONE));
        assert_eq!(app.current_idx, 0);
    }
}
