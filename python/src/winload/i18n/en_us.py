# Stores the English localization catalog.

STRINGS = {
    # ── CLI help ──
    "description": "Network Load Monitor — nload-like TUI tool for Windows/Linux/macOS",
    "help_interval": (
        "Refresh interval in milliseconds\n\n"
        "[default: 500]"
    ),
    "help_average": (
        "Average window in seconds\n\n"
        "[default: 300]"
    ),
    "help_device": "Default device name (partial match)",
    "help_title": "Override header title: no value shows winload <version>; empty string keeps default device header",
    "help_title_align": (
        "Title alignment: left, center, right\n\n"
        "Possible values:\n"
        "- left:   Align title to the left\n"
        "- center: Center title (default)\n"
        "- right:  Align title to the right\n\n"
        "[default: center]"
    ),
    "help_emoji": "Enable emoji decorations in help, TUI, and output",
    "help_unit": (
        "Display unit: bit (default) or byte\n\n"
        "Possible values:\n"
        "- bit:  Display rates in Bit/s (default)\n"
        "- byte: Display rates in Byte/s\n\n"
        "[default: bit]"
    ),
    "help_max_mode": (
        "Y-axis scaling mode: smart (default), legacy, fixed\n\n"
        "Possible values:\n"
        "- smart:  Smart adaptive Y-axis with exponential decay (default)\n"
        "- legacy: nload-style auto scale based on the visible graph history\n"
        "- fixed:  Fixed Y-axis value from --max-y-value\n\n"
        "[default: smart]"
    ),
    "help_max_half_life": (
        "Half-life in seconds for smart Y-axis decay (default: 10)\n\n"
        "[default: 10]"
    ),
    "help_max_y_value": "Fixed Y-axis value for --max-mode fixed (e.g. 100M, 1G, 500K)",
    "help_no_graph": "Hide traffic graphs, show only statistics",
    "help_unicode": "Use Unicode block characters for graph (█▓░· instead of #|..)",
    "help_bar_style": (
        "Bar style for header/label/help: plain (default), fill, color\n\n"
        "Possible values:\n"
        "- fill:  Background color fills entire line\n"
        "- color: Background color only on text\n"
        "- plain: No background, text color only (default)\n\n"
        "[default: plain]"
    ),
    "help_in_color": "Incoming (download) graph color, hex RGB (e.g. 0x00d7ff). Default: cyan",
    "help_out_color": "Outgoing (upload) graph color, hex RGB (e.g. 0xffaf00). Default: gold",
    "help_hide_separator": "Hide separator line (the row of equals signs between header and panels)",
    "help_version": "Print version",
    "help_no_color": "Disable all TUI colors (monochrome mode). Press 'c' to toggle at runtime",
    "help_debug_info": "Print debug info about network interfaces and exit",
    "help_netlink": "[Linux/Android only] Use RTNETLINK via pyroute2 instead of psutil (useful in Termux proot distro or restricted environments without /proc/net/dev access)",
    "help_lang": (
        "Display language: en-us (default), zh-cn, zh-tw\n\n"
        "Possible values:\n"
        "- en-us: English (United States) — English (US)\n"
        "- zh-cn: Simplified Chinese (Mainland China) — 简体中文（大陆）\n"
        "- zh-tw: Traditional Chinese (Taiwan) — 繁體中文（台灣）\n\n"
        "[default: en-us]"
    ),
    "help_help": "Print help (see a summary with '-h')",
    "help_shortcuts_title": "Keyboard Shortcuts:",
    "shortcut_previous_device": "Previous network device",
    "shortcut_next_device": "Next network device",
    "shortcut_toggle_debug": "Toggle debug information",
    "shortcut_toggle_separator": "Toggle separator line",
    "shortcut_toggle_color": "Toggle colors",
    "shortcut_quit": "Quit",
    "help_system": "System",
    "help_arch": "Arch",
    # ── TUI strings ──
    "device": "Device",
    "device_emoji": "🖧 Device",
    "incoming": "Incoming",
    "incoming_emoji": "⬇️📥 Incoming",
    "outgoing": "Outgoing",
    "outgoing_emoji": "⬆️📤 Outgoing",
    "stat_curr": "Curr",
    "stat_avg": "Avg",
    "stat_min": "Min",
    "stat_max": "Max",
    "stat_ttl": "Ttl",
    "stat_curr_emoji": "⚡ Curr",
    "stat_avg_emoji": "📊  Avg",
    "stat_min_emoji": "📏  Min",
    "stat_max_emoji": "🚀  Max",
    "stat_ttl_emoji": "📦  Ttl",
    "help_bar": " ←/→ Switch Device | F3 Info | q Quit",
    "help_bar_emoji": " ⬅️/➡️ Switch Device | 🔧 F3 Info | 🚪 q Quit",
    "f3_help_bar": " F3 Return | ←/→ Switch Device | q Quit",
    "f3_help_bar_emoji": " 🔧 F3 Return | ⬅️/➡️ Switch | 🚪 q Quit",
    "f3_title": "═══ winload Debug Info (F3) ═══",
    "terminal_too_small": "Terminal too small!",
    "terminal_too_small_emoji": "😭 Terminal too small! 📌",
    "loopback_warning": " ⚠ Loopback: stats may be inaccurate on Windows",
    # ── Error messages ──
    "error_no_curses": "Error: please install windows-curses first",
    # ── F3 debug overlay section titles ──
    "debug_section_params": "═══ Parameters ═══",
    "debug_section_yaxis": "═══ Y-axis Scaling ═══",
    "debug_section_device": "═══ Device ═══",
    "debug_section_colors": "═══ Colors ═══",
    # ── F3 key-value labels ──
    "debug_version": "Version:",
    "debug_system": "System:",
    "debug_language": "Language:",
    "debug_interval": "Interval:",
    "debug_average": "Average:",
    "debug_unit": "Unit:",
    "debug_bar_style": "Bar Style:",
    "debug_emoji": "Emoji:",
    "debug_unicode": "Unicode:",
    "debug_no_graph": "No Graph:",
    "debug_no_color": "No Color:",
    "debug_hide_sep": "Hide Sep:",
    "debug_yaxis_mode": "Mode:",
    "debug_in_smooth": "In smooth:",
    "debug_out_smooth": "Out smooth:",
    "debug_device_name": "Name:",
    "debug_device_addr": "Address:",
    "debug_in_curr": "In Curr:",
    "debug_out_curr": "Out Curr:",
    "debug_in_total": "In Total:",
    "debug_out_total": "Out Total:",
    "debug_in_peak": "In Peak:",
    "debug_out_peak": "Out Peak:",
    "debug_in_color": "In Color:",
    "debug_out_color": "Out Color:",
    # ── Panel mode tags ──
    "tag_fixed": "fixed",
    "tag_smart_max": "smart",
    "tag_legacy": "legacy",
    "tag_auto": "auto",
    # ── Y-axis mode descriptions ──
    "yaxis_fixed": "fixed-max ({val})",
    "yaxis_smart": "smart (half-life: {sec}s)",
    "yaxis_legacy": "legacy (visible history peak)",
    # ── Misc ──
    "on": "on",
    "off": "off",
    "default_tag": "(default)",
    "addr_none": "(none)",
    "arrow_up": "↑",
    "arrow_down": "↓",
}
