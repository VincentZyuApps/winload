// Defines validated, strongly typed runtime configuration shared by the Rust modules.

use ratatui::style::Color;

#[derive(Clone, Copy, Debug, PartialEq, Eq, clap::ValueEnum)]
pub enum Unit {
    Bit,
    Byte,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, clap::ValueEnum)]
pub enum BarStyle {
    Fill,
    Color,
    Plain,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, clap::ValueEnum)]
pub enum TitleAlign {
    Left,
    Center,
    Right,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, clap::ValueEnum)]
pub enum MaxMode {
    Smart,
    Legacy,
    Fixed,
}

#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, clap::ValueEnum)]
pub enum GraphStyle {
    #[default]
    Classic,
    Line,
    Scatter,
    Bar,
}

impl GraphStyle {
    pub fn next(self) -> Self {
        match self {
            Self::Classic => Self::Line,
            Self::Line => Self::Scatter,
            Self::Scatter => Self::Bar,
            Self::Bar => Self::Classic,
        }
    }
}

#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub enum XAxis {
    #[default]
    None,
    Seconds(u64),
}

impl XAxis {
    pub fn interval(self) -> Option<u64> {
        match self {
            Self::None => None,
            Self::Seconds(value) => Some(value),
        }
    }
}

#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, clap::ValueEnum)]
pub enum YAxis {
    #[default]
    None,
    Percent,
    Unit,
}

impl YAxis {
    pub fn next(self) -> Self {
        match self {
            Self::None => Self::Percent,
            Self::Percent => Self::Unit,
            Self::Unit => Self::None,
        }
    }
}

#[derive(Clone, Debug)]
pub struct RunConfig {
    pub interval: u64,
    pub average: u64,
    pub device: Option<String>,
    pub title: Option<String>,
    pub title_align: TitleAlign,
    pub emoji: bool,
    pub unicode: bool,
    pub unit: Unit,
    pub bar_style: BarStyle,
    pub in_color: Color,
    pub out_color: Color,
    pub max_mode: MaxMode,
    pub max_half_life: f64,
    pub max_y_value: Option<f64>,
    pub no_graph: bool,
    pub hide_separator: bool,
    pub no_color: bool,
    pub npcap: bool,
    pub netlink: bool,
    pub graph_style: GraphStyle,
    pub x_axis: XAxis,
    pub y_axis: YAxis,
}

pub fn parse_max_value(value: &str) -> Result<f64, String> {
    let value = value.trim();
    if value.is_empty() {
        return Err("empty value".into());
    }
    let (number, multiplier) = if let Some(n) = value.strip_suffix(['G', 'g']) {
        (n, 1024.0 * 1024.0 * 1024.0)
    } else if let Some(n) = value.strip_suffix(['M', 'm']) {
        (n, 1024.0 * 1024.0)
    } else if let Some(n) = value.strip_suffix(['K', 'k']) {
        (n, 1024.0)
    } else {
        (value, 1.0)
    };
    let parsed: f64 = number.parse().map_err(|e| format!("invalid number: {e}"))?;
    if !parsed.is_finite() || parsed <= 0.0 {
        return Err("value must be greater than 0".into());
    }
    Ok(parsed * multiplier)
}

pub fn parse_hex_color(value: &str) -> Result<Color, String> {
    let hex = value
        .trim()
        .strip_prefix("0x")
        .or_else(|| value.trim().strip_prefix("0X"))
        .unwrap_or(value.trim());
    if hex.len() != 6 {
        return Err(format!(
            "expected 6 hex digits (e.g. 0x3399ff), got: {value}"
        ));
    }
    let r = u8::from_str_radix(&hex[0..2], 16).map_err(|e| format!("bad red: {e}"))?;
    let g = u8::from_str_radix(&hex[2..4], 16).map_err(|e| format!("bad green: {e}"))?;
    let b = u8::from_str_radix(&hex[4..6], 16).map_err(|e| format!("bad blue: {e}"))?;
    Ok(Color::Rgb(r, g, b))
}

pub fn parse_x_axis(value: &str) -> Result<XAxis, String> {
    if value.eq_ignore_ascii_case("none") {
        return Ok(XAxis::None);
    }
    let seconds = value
        .strip_suffix('s')
        .ok_or("expected none or a positive integer with an s suffix (for example 5s)")?;
    let seconds: u64 = seconds.parse().map_err(|_| {
        "expected none or a positive integer with an s suffix (for example 5s)".to_string()
    })?;
    if seconds == 0 {
        return Err("--x-axis interval must be greater than 0s".into());
    }
    Ok(XAxis::Seconds(seconds))
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn graph_styles_cycle() {
        assert_eq!(GraphStyle::Bar.next(), GraphStyle::Classic);
    }
    #[test]
    fn x_axis_accepts_seconds() {
        assert_eq!(parse_x_axis("5s"), Ok(XAxis::Seconds(5)));
    }
    #[test]
    fn x_axis_rejects_invalid_values() {
        for value in ["0s", "5", "1.5s", "-5s"] {
            assert!(parse_x_axis(value).is_err());
        }
    }
}
