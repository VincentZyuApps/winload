//! winload — Network Load Monitor
//! 仿 Linux nload 的终端网络流量监控工具 (Rust 版)
//!
//! 用法:
//!     winload              # 监控所有活跃网卡
//!     winload -t 200       # 设置刷新间隔 200ms
//!     winload -d "Wi-Fi"   # 指定默认设备
//!
//! 快捷键:
//!     ←/→ 或 ↑/↓   切换网卡
//!     q / Esc       退出

mod collector;
mod graph;
mod stats;
mod ui;

use std::io;
use std::time::{Duration, Instant};

use clap::Parser;
use crossterm::event::{self, Event, KeyCode, KeyEventKind, KeyModifiers};

use collector::{Collector, DeviceInfo};
use stats::StatisticsEngine;

// ─── CLI 参数 ──────────────────────────────────────────────

/// Network Load Monitor — nload-like TUI tool
#[derive(Parser)]
#[command(name = "winload", version, about)]
struct Args {
    /// Refresh interval in milliseconds
    #[arg(short = 't', long = "interval", default_value = "500")]
    interval: u64,

    /// Average window in seconds
    #[arg(short = 'a', long = "average", default_value = "300")]
    average: u64,

    /// Default device name (partial match)
    #[arg(short = 'd', long = "device")]
    device: Option<String>,

    /// Print debug info about network interfaces and exit
    #[arg(long = "debug-info")]
    debug_info: bool,

    /// Enable emoji decorations in TUI and output
    #[arg(short = 'e', long = "emoji")]
    emoji: bool,
}

// ─── App 状态 ──────────────────────────────────────────────

/// 单个网卡的视图状态
pub struct DeviceView {
    pub info: DeviceInfo,
    pub engine: StatisticsEngine,
}

/// 应用主状态
pub struct App {
    pub views: Vec<DeviceView>,
    pub current_idx: usize,
    pub emoji: bool,
    collector: Collector,
}

impl App {
    fn new(args: &Args) -> Self {
        let collector = Collector::new();
        let devices = collector.devices();

        let views: Vec<DeviceView> = devices
            .into_iter()
            .map(|info| DeviceView {
                info,
                engine: StatisticsEngine::new(args.interval, args.average),
            })
            .collect();

        // 如果指定了默认设备，定位到对应索引
        let mut current_idx = 0;
        if let Some(ref name) = args.device {
            let lower = name.to_lowercase();
            if let Some(idx) = views
                .iter()
                .position(|v| v.info.name.to_lowercase().contains(&lower))
            {
                current_idx = idx;
            }
        }

        Self {
            views,
            current_idx,
            emoji: args.emoji,
            collector,
        }
    }

    pub fn current_view(&self) -> Option<&DeviceView> {
        self.views.get(self.current_idx)
    }

    fn update(&mut self) {
        let snapshots = self.collector.collect();
        for view in &mut self.views {
            if let Some(snap) = snapshots.get(&view.info.name) {
                view.engine.update(snap.clone());
            }
        }
    }

    fn next_device(&mut self) {
        if !self.views.is_empty() {
            self.current_idx = (self.current_idx + 1) % self.views.len();
        }
    }

    fn prev_device(&mut self) {
        if !self.views.is_empty() {
            self.current_idx = (self.current_idx + self.views.len() - 1) % self.views.len();
        }
    }
}

// ─── 主循环 ────────────────────────────────────────────────

fn run(terminal: &mut ratatui::DefaultTerminal, args: Args) -> io::Result<()> {
    let mut app = App::new(&args);
    let tick_rate = Duration::from_millis(args.interval);
    let mut last_tick = Instant::now();

    // 初始采集
    app.update();

    loop {
        terminal.draw(|frame| ui::draw(frame, &app))?;

        let timeout = tick_rate
            .checked_sub(last_tick.elapsed())
            .unwrap_or_default();

        if crossterm::event::poll(timeout)? {
            if let Event::Key(key) = event::read()? {
                // Windows 下 crossterm 会产生 Press + Release，只处理 Press
                if key.kind == KeyEventKind::Press {
                    match key.code {
                        KeyCode::Char('q') | KeyCode::Char('Q') | KeyCode::Esc => {
                            return Ok(());
                        }
                        KeyCode::Char('c')
                            if key.modifiers.contains(KeyModifiers::CONTROL) =>
                        {
                            return Ok(());
                        }
                        KeyCode::Right | KeyCode::Down | KeyCode::Tab | KeyCode::Enter => {
                            app.next_device();
                        }
                        KeyCode::Left | KeyCode::Up => {
                            app.prev_device();
                        }
                        _ => {}
                    }
                }
            }
        }

        if last_tick.elapsed() >= tick_rate {
            app.update();
            last_tick = Instant::now();
        }
    }
}

// ─── 入口 ──────────────────────────────────────────────────

fn main() -> io::Result<()> {
    let args = Args::parse();

    // 如果传入 --debug-info，打印接口信息后退出
    if args.debug_info {
        let collector = Collector::new();
        if args.emoji {
            println!("\n🔍🌐 Network Interfaces Debug Info 🖧✨");
        }
        collector.print_debug_info();
        if args.emoji {
            println!("🏁 Done! Happy debugging! 🎉🐛");
        }
        return Ok(());
    }
    let mut terminal = ratatui::init();
    let result = run(&mut terminal, args);
    ratatui::restore();
    result
}
