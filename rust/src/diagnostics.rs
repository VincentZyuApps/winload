// Prints build, platform, and network-interface diagnostics outside the TUI.

use crate::collector::Collector;

pub fn print_version() {
    println!(
        "\x1b[1mwinload {} (Rust edition)\x1b[0m",
        env!("CARGO_PKG_VERSION")
    );
    println!(
        "Commit Hash: {} | Commit Time: {}",
        env!("WINLOAD_GIT_COMMIT_HASH"),
        env!("WINLOAD_GIT_COMMIT_TIME")
    );
    println!(
        "System: {} | Arch: {} | Target: {}",
        std::env::consts::OS,
        std::env::consts::ARCH,
        env!("TARGET")
    );
}

pub fn print_system_info(extra: &str) {
    eprint!(
        "\nSystem: {} | Arch: {} | Target: {}",
        std::env::consts::OS,
        std::env::consts::ARCH,
        env!("TARGET")
    );
    if !extra.is_empty() {
        eprint!("\n\t{extra}");
    }
    eprintln!();
}

pub fn print_network_info(netlink: bool, emoji: bool) {
    let collector = Collector::new(netlink);
    if emoji {
        println!("\nNetwork Interfaces Debug Info");
    }
    collector.print_debug_info();
    if emoji {
        println!("Done.");
    }
}
