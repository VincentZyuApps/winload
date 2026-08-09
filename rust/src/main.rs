// Boots the Rust application and dispatches CLI actions to focused modules.

mod app;
mod cli;
mod collector;
mod config;
mod diagnostics;
mod emoji;
mod graph;
mod i18n;
mod loopback;
#[cfg(any(target_os = "android", target_os = "linux"))]
mod netlink;
mod runtime;
mod stats;
mod ui;

use std::io;

fn main() -> io::Result<()> {
    let raw: Vec<String> = std::env::args().collect();
    if raw.iter().any(|arg| arg == "--version" || arg == "-V") {
        diagnostics::print_version();
        return Ok(());
    }
    let args = cli::parse().unwrap_or_else(|error| error.exit());
    if let Err(error) = args.validate() {
        eprintln!("error: {error}");
        std::process::exit(2);
    }
    let debug_info = args.debug_info;
    let config = args.into_config();
    if debug_info {
        diagnostics::print_network_info(config.netlink, config.emoji);
        return Ok(());
    }
    let mut terminal = ratatui::init();
    let result = runtime::run(&mut terminal, config);
    ratatui::restore();
    diagnostics::print_system_info(result.as_deref().unwrap_or(""));
    result.map(|_| ())
}
