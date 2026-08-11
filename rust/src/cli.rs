// Parses localized command-line arguments and produces a validated RunConfig.

use clap::{parser::ValueSource, ArgMatches, CommandFactory, FromArgMatches, Parser};
use ratatui::style::Color;

use crate::config::{
    parse_hex_color, parse_max_value, parse_x_axis, BarStyle, GraphStyle, MaxMode, RunConfig,
    TitleAlign, Unit, XAxis, YAxis,
};
use crate::emoji;
use crate::i18n::{set_lang, t, Lang};

#[derive(Parser, Debug)]
#[command(name = "winload", version = concat!(env!("CARGO_PKG_VERSION"), " (Rust edition)"))]
pub struct Args {
    #[arg(short = 't', long = "interval", default_value = "500")]
    interval: u64,
    #[arg(short = 'a', long = "average", default_value = "300")]
    average: u64,
    #[arg(short = 'd', long = "device")]
    device: Option<String>,
    #[arg(long = "title", num_args = 0..=1, default_missing_value = "__WINLOAD_TITLE_FLAG_ONLY__", value_name = "TITLE")]
    title: Option<Option<String>>,
    #[arg(long = "title-align", value_enum, default_value = "center")]
    title_align: TitleAlign,
    #[arg(long = "debug-info")]
    pub debug_info: bool,
    #[arg(short = 'e', long = "emoji")]
    emoji: bool,
    #[arg(short = 'U', long = "unicode")]
    unicode: bool,
    #[arg(short = 'u', long = "unit", value_enum, default_value = "bit")]
    unit: Unit,
    #[arg(short = 'b', long = "bar-style", value_enum, default_value = "plain")]
    bar_style: BarStyle,
    #[arg(long = "in-color", value_parser = parse_hex_color)]
    in_color: Option<Color>,
    #[arg(long = "out-color", value_parser = parse_hex_color)]
    out_color: Option<Color>,
    #[arg(long = "max-mode", value_enum, default_value = "smart")]
    max_mode: MaxMode,
    #[arg(long = "max-half-life", default_value = "10", value_name = "SECS")]
    max_half_life: f64,
    #[arg(skip)]
    max_half_life_explicit: bool,
    #[arg(long = "max-y-value", value_parser = parse_max_value, value_name = "VALUE")]
    max_y_value: Option<f64>,
    #[arg(short = 'n', long = "no-graph")]
    no_graph: bool,
    #[arg(long = "hide-separator")]
    hide_separator: bool,
    #[arg(long = "no-color")]
    no_color: bool,
    #[arg(long = "npcap")]
    npcap: bool,
    #[arg(long = "netlink")]
    netlink: bool,
    #[arg(long = "graph-style", value_enum, default_value = "classic")]
    graph_style: GraphStyle,
    #[arg(long = "x-axis", value_parser = parse_x_axis, default_value = "none", value_name = "none|Ns")]
    x_axis: XAxis,
    #[arg(long = "y-axis", value_enum, default_value = "none")]
    y_axis: YAxis,
    #[arg(long = "lang", value_enum, default_value = "en-us")]
    lang: Lang,
}

fn pre_scan_lang(raw: &[String]) -> Lang {
    for (index, value) in raw.iter().enumerate() {
        let selected = if value == "--lang" {
            raw.get(index + 1).map(String::as_str)
        } else {
            value.strip_prefix("--lang=")
        };
        if let Some(selected) = selected {
            return match selected {
                "zh-cn" => Lang::ZhCn,
                "zh-tw" => Lang::ZhTw,
                _ => Lang::EnUs,
            };
        }
    }
    Lang::EnUs
}

fn pre_scan_emoji(raw: &[String]) -> bool {
    raw.iter().skip(1).any(|arg| {
        arg == "--emoji"
            || arg == "-e"
            || (arg.starts_with('-')
                && !arg.starts_with("--")
                && arg.chars().skip(1).any(|ch| ch == 'e'))
    })
}

fn help(key: &str, emoji_enabled: bool) -> String {
    emoji::decorate(emoji_enabled, key, t(key))
}

fn keyboard_shortcuts(emoji_enabled: bool) -> String {
    let rows = [
        ("Left / Up", "shortcut_previous_device"),
        ("Right / Down", "shortcut_next_device"),
        ("Tab / Enter", "shortcut_next_device"),
        ("F3", "shortcut_toggle_debug"),
        ("=", "shortcut_toggle_separator"),
        ("c", "shortcut_toggle_color"),
        ("q / Q / Ctrl+C", "shortcut_quit"),
        ("Esc", "shortcut_quit"),
        ("g / G", "shortcut_cycle_graph_style"),
        ("x / X", "shortcut_toggle_x_axis"),
        ("y / Y", "shortcut_cycle_y_axis"),
    ];
    let mut output = format!("{}\n", help("help_shortcuts_title", emoji_enabled));
    for (keys, action) in rows {
        output.push_str(&format!("  {keys:<28}{}\n", help(action, emoji_enabled)));
    }
    output.pop();
    output
}

fn translated_command(emoji_enabled: bool) -> clap::Command {
    let system = emoji::decorate(
        emoji_enabled,
        "help_system_info",
        format!(
            "{}: {} | {}: {} | {}: {}",
            t("help_system"),
            std::env::consts::OS,
            t("help_arch"),
            std::env::consts::ARCH,
            t("help_target"),
            env!("TARGET")
        ),
    );
    let footer = format!("{}\n\n{}", keyboard_shortcuts(emoji_enabled), system);
    let mut command = Args::command()
        .about(help("description", emoji_enabled))
        .after_help(footer);
    for (id, key) in [
        ("interval", "help_interval"),
        ("average", "help_average"),
        ("device", "help_device"),
        ("title", "help_title"),
        ("title_align", "help_title_align"),
        ("debug_info", "help_debug_info"),
        ("emoji", "help_emoji"),
        ("unicode", "help_unicode"),
        ("unit", "help_unit"),
        ("bar_style", "help_bar_style"),
        ("in_color", "help_in_color"),
        ("out_color", "help_out_color"),
        ("max_mode", "help_max_mode"),
        ("max_half_life", "help_max_half_life"),
        ("max_y_value", "help_max_y_value"),
        ("no_graph", "help_no_graph"),
        ("hide_separator", "help_hide_separator"),
        ("no_color", "help_no_color"),
        ("npcap", "help_npcap"),
        ("netlink", "help_netlink"),
        ("lang", "help_lang"),
    ] {
        command = command.mut_arg(id, |arg| arg.help(help(key, emoji_enabled)));
    }
    command
        .mut_arg("graph_style", |arg| {
            arg.help(help("help_graph_style", emoji_enabled))
        })
        .mut_arg("x_axis", |arg| arg.help(help("help_x_axis", emoji_enabled)))
        .mut_arg("y_axis", |arg| arg.help(help("help_y_axis", emoji_enabled)))
}

pub fn parse() -> Result<Args, clap::Error> {
    let raw: Vec<String> = std::env::args().collect();
    set_lang(pre_scan_lang(&raw));
    let matches = translated_command(pre_scan_emoji(&raw)).try_get_matches_from(raw)?;
    args_from_matches(&matches)
}

fn args_from_matches(matches: &ArgMatches) -> Result<Args, clap::Error> {
    let max_half_life_explicit =
        matches.value_source("max_half_life") == Some(ValueSource::CommandLine);
    let mut args = Args::from_arg_matches(matches)?;
    args.max_half_life_explicit = max_half_life_explicit;
    Ok(args)
}

impl Args {
    pub fn validate(&self) -> Result<(), String> {
        if self.interval == 0 {
            return Err("--interval must be greater than 0".into());
        }
        if self.average == 0 {
            return Err("--average must be greater than 0".into());
        }
        if !self.max_half_life.is_finite() || self.max_half_life <= 0.0 {
            return Err("--max-half-life must be greater than 0".into());
        }
        match self.max_mode {
            MaxMode::Fixed if self.max_y_value.is_none() => {
                return Err("--max-mode fixed requires --max-y-value <VALUE>".into())
            }
            MaxMode::Smart | MaxMode::Legacy if self.max_y_value.is_some() => {
                return Err("--max-y-value can only be used with --max-mode fixed".into())
            }
            MaxMode::Fixed | MaxMode::Legacy if self.max_half_life_explicit => {
                return Err("--max-half-life can only be used with --max-mode smart".into())
            }
            _ => {}
        }
        Ok(())
    }

    pub fn into_config(self) -> RunConfig {
        let title = match self.title {
            None => None,
            Some(None) => Some(format!("winload {}", env!("CARGO_PKG_VERSION"))),
            Some(Some(value)) if value.is_empty() => None,
            Some(Some(value)) if value == "__WINLOAD_TITLE_FLAG_ONLY__" => {
                Some(format!("winload {}", env!("CARGO_PKG_VERSION")))
            }
            Some(Some(value)) => Some(value),
        };
        RunConfig {
            interval: self.interval,
            average: self.average,
            device: self.device,
            title,
            title_align: self.title_align,
            emoji: self.emoji,
            unicode: self.unicode,
            unit: self.unit,
            bar_style: self.bar_style,
            in_color: self.in_color.unwrap_or(Color::Rgb(0x00, 0xd7, 0xff)),
            out_color: self.out_color.unwrap_or(Color::Rgb(0xff, 0xaf, 0x00)),
            max_mode: self.max_mode,
            max_half_life: self.max_half_life,
            max_y_value: self.max_y_value,
            no_graph: self.no_graph,
            hide_separator: self.hide_separator,
            no_color: self.no_color,
            npcap: self.npcap,
            netlink: self.netlink,
            graph_style: self.graph_style,
            x_axis: self.x_axis,
            y_axis: self.y_axis,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn new_graph_arguments_parse() {
        let args = Args::try_parse_from([
            "winload",
            "--graph-style",
            "line",
            "--x-axis",
            "5s",
            "--y-axis",
            "unit",
        ])
        .unwrap();
        assert_eq!(args.graph_style, GraphStyle::Line);
        assert_eq!(args.x_axis, XAxis::Seconds(5));
        assert_eq!(args.y_axis, YAxis::Unit);
    }

    fn parsed(values: &[&str]) -> Args {
        let matches = Args::command().try_get_matches_from(values).unwrap();
        args_from_matches(&matches).unwrap()
    }

    #[test]
    fn default_half_life_is_allowed_outside_smart_mode() {
        assert!(parsed(&["winload", "--max-mode", "legacy"])
            .validate()
            .is_ok());
        assert!(
            parsed(&["winload", "--max-mode", "fixed", "--max-y-value", "100M",])
                .validate()
                .is_ok()
        );
    }

    #[test]
    fn explicit_half_life_is_rejected_in_legacy_and_fixed_modes() {
        for values in [
            vec!["winload", "--max-mode", "legacy", "--max-half-life", "5"],
            vec![
                "winload",
                "--max-mode",
                "fixed",
                "--max-y-value",
                "100M",
                "--max-half-life=5",
            ],
        ] {
            assert_eq!(
                parsed(&values).validate(),
                Err("--max-half-life can only be used with --max-mode smart".into())
            );
        }
    }

    #[test]
    fn explicit_half_life_is_allowed_in_smart_mode() {
        assert!(
            parsed(&["winload", "--max-mode", "smart", "--max-half-life", "5",])
                .validate()
                .is_ok()
        );
    }

    #[test]
    fn long_help_localizes_shortcuts_between_options_and_system_info() {
        for (lang, title, previous, graph, system) in [
            (
                Lang::EnUs,
                "Keyboard Shortcuts:",
                "Previous network device",
                "Cycle graph style",
                "System:",
            ),
            (
                Lang::ZhCn,
                "快捷键：",
                "切换到上一个网络设备",
                "循环切换图形风格",
                "系统:",
            ),
            (
                Lang::ZhTw,
                "快捷鍵：",
                "切換到上一個網路裝置",
                "循環切換圖形風格",
                "系統:",
            ),
        ] {
            set_lang(lang);
            let rendered = translated_command(false).render_long_help().to_string();

            for expected in [
                title,
                previous,
                graph,
                "Left / Up",
                "Right / Down",
                "Tab / Enter",
                "F3",
                "=",
                "c",
                "g / G",
                "x / X",
                "y / Y",
                "q / Q / Ctrl+C",
                "Esc",
            ] {
                assert!(
                    rendered.contains(expected),
                    "missing {expected:?} in:\n{rendered}"
                );
            }

            let options_index = rendered.find("Options:").unwrap();
            let shortcuts_index = rendered.find(title).unwrap();
            let system_index = rendered.find(system).unwrap();
            assert!(options_index < shortcuts_index);
            assert!(shortcuts_index < system_index);
        }
        set_lang(Lang::EnUs);
    }

    #[test]
    fn long_help_decorates_keyboard_shortcuts_with_emoji() {
        let plain = translated_command(false).render_long_help().to_string();
        let emoji = translated_command(true).render_long_help().to_string();

        assert!(!plain.contains("⌨️ Keyboard Shortcuts:"));
        assert!(!plain.contains("⬅️ Previous network device"));
        for expected in [
            "⌨️ Keyboard Shortcuts:",
            "⬅️ Previous network device",
            "➡️ Next network device",
            "🔧 Toggle debug information",
            "➖ Toggle separator line",
            "🎨 Toggle colors",
            "🚪 Quit",
            "📈 Cycle graph style",
            "⏱️ Toggle X-axis grid",
            "📏 Cycle Y-axis labels",
        ] {
            assert!(
                emoji.contains(expected),
                "missing {expected:?} in:\n{emoji}"
            );
        }
    }
}
