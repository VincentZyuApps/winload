"""Emoji decoration helpers for CLI-facing labels."""

from __future__ import annotations


_ICONS = {
    "description": "🌐",
    "help_interval": "⏱️",
    "help_average": "📊",
    "help_device": "🖧",
    "help_title": "🏷️",
    "help_title_align": "↔️",
    "help_debug_info": "🔍",
    "help_emoji": "✨",
    "help_unicode": "█",
    "help_unit": "🧮",
    "help_bar_style": "🎛️",
    "help_in_color": "⬇️",
    "help_out_color": "⬆️",
    "help_max_mode": "📈",
    "help_max_half_life": "⏳",
    "help_max_y_value": "📏",
    "help_no_graph": "🚫",
    "help_hide_separator": "➖",
    "help_version": "🏷️",
    "help_no_color": "⚫",
    "help_npcap": "🪟",
    "help_netlink": "🔗",
    "help_lang": "🌐",
    "help_system_info": "🖥️",
}


def decorate(enabled: bool, key: str, text: str) -> str:
    """Prefix text with the icon for key when emoji output is enabled."""
    if not enabled:
        return text
    icon = _ICONS.get(key)
    if not icon:
        return text
    return f"{icon} {text}"
