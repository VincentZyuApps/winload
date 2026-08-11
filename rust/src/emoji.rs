// ✨ Decorates CLI-facing labels with optional emoji icons.
pub fn decorate(enabled: bool, key: &str, text: impl Into<String>) -> String {
    let text = text.into();
    if !enabled {
        return text;
    }

    icon(key)
        .map(|icon| format!("{icon} {text}"))
        .unwrap_or(text)
}

pub fn icon(key: &str) -> Option<&'static str> {
    match key {
        "description" => Some("🌐"),
        "help_interval" => Some("⏱️"),
        "help_average" => Some("📊"),
        "help_device" => Some("🖧"),
        "help_title" => Some("🏷️"),
        "help_title_align" => Some("↔️"),
        "help_debug_info" => Some("🔍"),
        "help_emoji" => Some("✨"),
        "help_unicode" => Some("█"),
        "help_unit" => Some("🧮"),
        "help_bar_style" => Some("🎛️"),
        "help_in_color" => Some("⬇️"),
        "help_out_color" => Some("⬆️"),
        "help_max_mode" => Some("📈"),
        "help_max_half_life" => Some("⏳"),
        "help_max_y_value" => Some("📏"),
        "help_no_graph" => Some("🚫"),
        "help_hide_separator" => Some("➖"),
        "help_no_color" => Some("⚫"),
        "help_npcap" => Some("🪟"),
        "help_netlink" => Some("🔗"),
        "help_lang" => Some("🌐"),
        "help_shortcuts_title" => Some("⌨️"),
        "shortcut_previous_device" => Some("⬅️"),
        "shortcut_next_device" => Some("➡️"),
        "shortcut_toggle_debug" => Some("🔧"),
        "shortcut_toggle_separator" => Some("➖"),
        "shortcut_toggle_color" => Some("🎨"),
        "shortcut_cycle_graph_style" => Some("📈"),
        "shortcut_toggle_x_axis" => Some("⏱️"),
        "shortcut_cycle_y_axis" => Some("📏"),
        "shortcut_quit" => Some("🚪"),
        "help_system_info" => Some("🖥️"),
        _ => None,
    }
}
