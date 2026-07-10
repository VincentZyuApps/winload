# 🌐 Provides localized UI, help, and debug strings for supported languages.
"""
i18n.py - Internationalization support
Supported languages: en-us, zh-cn, zh-tw
"""

_current_lang = "en-us"

_STRINGS: dict[str, dict[str, str]] = {
    # ── English (en-us) — English (US) ──
    "en-us": {
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
    },
    # ── Simplified Chinese (zh-cn) — 简体中文（大陆）──
    "zh-cn": {
        # ── CLI help ──
        "description": "网络负载监控工具 — 仿 Linux nload 的终端网络流量监控工具",
        "help_interval": (
            "刷新间隔（毫秒）\n\n"
            "[默认: 500]"
        ),
        "help_average": (
            "平均值计算窗口（秒）\n\n"
            "[默认: 300]"
        ),
        "help_device": "默认网卡名称（支持部分匹配）",
        "help_title": "覆盖顶部标题：不带值时显示 winload <版本号>；空字符串保持默认设备标题",
        "help_title_align": (
            "标题对齐方式：left、center、right\n\n"
            "Possible values:\n"
            "- left:   Align title to the left\n"
            "- center: Center title (default)\n"
            "- right:  Align title to the right\n\n"
            "[默认: center]"
        ),
        "help_emoji": "在帮助、TUI 和输出中启用 emoji 装饰",
        "help_unit": (
            "显示单位：bit（默认）或 byte\n\n"
            "Possible values:\n"
            "- bit:  Display rates in Bit/s (default)\n"
            "- byte: Display rates in Byte/s\n\n"
            "[默认: bit]"
        ),
        "help_max_mode": (
            "Y 轴缩放模式：smart（默认）、legacy、fixed\n\n"
            "Possible values:\n"
            "- smart:  Smart adaptive Y-axis with exponential decay (default)\n"
            "- legacy: nload-style auto scale based on the visible graph history\n"
            "- fixed:  Fixed Y-axis value from --max-y-value\n\n"
            "[默认: smart]"
        ),
        "help_max_half_life": (
            "smart 模式指数衰减半衰期，单位秒（默认：10）\n\n"
            "[默认: 10]"
        ),
        "help_max_y_value": "fixed 模式固定 Y 轴上限（如 100M、1G、500K）",
        "help_no_graph": "隐藏流量图形，仅显示统计信息",
        "help_unicode": "使用 Unicode 块字符绘制图形（█▓░· 代替 #|..）",
        "help_bar_style": (
            "状态栏/帮助栏样式：plain（默认），fill，color\n\n"
            "Possible values:\n"
            "- fill:  Background color fills entire line\n"
            "- color: Background color only on text\n"
            "- plain: No background, text color only (default)\n\n"
            "[默认: plain]"
        ),
        "help_in_color": "入站（下载）图形颜色，十六进制 RGB（如 0x00d7ff）。默认：青色",
        "help_out_color": "出站（上传）图形颜色，十六进制 RGB（如 0xffaf00）。默认：金色",
        "help_hide_separator": "隐藏分隔线（标题和面板之间的等号行）",
        "help_version": "打印版本号",
        "help_no_color": "禁用所有 TUI 颜色（单色模式）。运行时按 'c' 切换",
        "help_debug_info": "打印网卡调试信息并退出",
        "help_netlink": "[仅 Linux/Android] 使用 pyroute2 通过 RTNETLINK 替代 psutil（适用于 Termux proot distro 或无法访问 /proc/net/dev 的受限环境）",
        "help_lang": (
            "显示语言：en-us（默认），zh-cn，zh-tw\n\n"
            "Possible values:\n"
            "- en-us: English (United States) — English (US)\n"
            "- zh-cn: Simplified Chinese (Mainland China) — 简体中文（大陆）\n"
            "- zh-tw: Traditional Chinese (Taiwan) — 繁體中文（台灣）\n\n"
            "[默认: en-us]"
        ),
        "help_help": "打印帮助（使用 '-h' 查看简短摘要）",
        "help_system": "系统",
        "help_arch": "架构",
        # ── TUI strings ──
        "device": "设备",
        "device_emoji": "🖧 设备",
        "incoming": "入站",
        "incoming_emoji": "⬇️📥 入站",
        "outgoing": "出站",
        "outgoing_emoji": "⬆️📤 出站",
        "stat_curr": "当前",
        "stat_avg": "平均",
        "stat_min": "最小",
        "stat_max": "最大",
        "stat_ttl": "总计",
        "stat_curr_emoji": "⚡ 当前",
        "stat_avg_emoji": "📊 平均",
        "stat_min_emoji": "📏 最小",
        "stat_max_emoji": "🚀 最大",
        "stat_ttl_emoji": "📦 总计",
        "help_bar": " ←/→ 切换设备 | F3 信息 | q 退出",
        "help_bar_emoji": " ⬅️/➡️ 切换设备 | 🔧 F3 信息 | 🚪 q 退出",
        "f3_help_bar": " F3 返回 | ←/→ 切换设备 | q 退出",
        "f3_help_bar_emoji": " 🔧 F3 返回 | ⬅️/➡️ 切换 | 🚪 q 退出",
        "f3_title": "═══ winload 调试信息 (F3) ═══",
        "terminal_too_small": "终端窗口太小！",
        "terminal_too_small_emoji": "😭 终端窗口太小！📌",
        "loopback_warning": " ⚠ 回环设备：Windows 上统计可能不准确",
        # ── Error messages ──
        "error_no_curses": "错误：请先安装 windows-curses",
        # ── F3 debug overlay section titles ──
        "debug_section_params": "═══ 参数 ═══",
        "debug_section_yaxis": "═══ Y 轴缩放 ═══",
        "debug_section_device": "═══ 设备 ═══",
        "debug_section_colors": "═══ 颜色 ═══",
        # ── F3 key-value labels ──
        "debug_version": "版本：",
        "debug_system": "系统：",
        "debug_language": "语言：",
        "debug_interval": "刷新间隔：",
        "debug_average": "平均窗口：",
        "debug_unit": "单位：",
        "debug_bar_style": "状态栏样式：",
        "debug_emoji": "表情：",
        "debug_unicode": "Unicode：",
        "debug_no_graph": "隐藏图形：",
        "debug_no_color": "无颜色：",
        "debug_hide_sep": "隐藏分隔线：",
        "debug_yaxis_mode": "模式：",
        "debug_in_smooth": "入站平滑：",
        "debug_out_smooth": "出站平滑：",
        "debug_device_name": "名称：",
        "debug_device_addr": "地址：",
        "debug_in_curr": "入站当前：",
        "debug_out_curr": "出站当前：",
        "debug_in_total": "入站总计：",
        "debug_out_total": "出站总计：",
        "debug_in_peak": "入站峰值：",
        "debug_out_peak": "出站峰值：",
        "debug_in_color": "入站颜色：",
        "debug_out_color": "出站颜色：",
        # ── Panel mode tags ──
        "tag_fixed": "固定",
        "tag_smart_max": "智能",
        "tag_legacy": "传统",
        "tag_auto": "自动",
        # ── Y-axis mode descriptions ──
        "yaxis_fixed": "固定最大值（{val}）",
        "yaxis_smart": "智能自适应（半衰期：{sec}秒）",
        "yaxis_legacy": "传统模式（可见历史峰值）",
        # ── Misc ──
        "on": "开",
        "off": "关",
        "default_tag": "（默认）",
        "addr_none": "（无）",
        "arrow_up": "↑",
        "arrow_down": "↓",
    },
    # ── Traditional Chinese (zh-tw) — 繁體中文（台灣）──
    "zh-tw": {
        # ── CLI help ──
        "description": "網路負載監控工具 — 仿 Linux nload 的終端網路流量監控工具",
        "help_interval": (
            "重新整理間隔（毫秒）\n\n"
            "[預設: 500]"
        ),
        "help_average": (
            "平均值計算視窗（秒）\n\n"
            "[預設: 300]"
        ),
        "help_device": "預設網路卡名稱（支援部分匹配）",
        "help_title": "覆蓋頂部標題：不帶值時顯示 winload <版本號>；空字串保持預設裝置標題",
        "help_title_align": (
            "標題對齊方式：left、center、right\n\n"
            "Possible values:\n"
            "- left:   Align title to the left\n"
            "- center: Center title (default)\n"
            "- right:  Align title to the right\n\n"
            "[預設: center]"
        ),
        "help_emoji": "在說明、TUI 和輸出中啟用 emoji 裝飾",
        "help_unit": (
            "顯示單位：bit（預設）或 byte\n\n"
            "Possible values:\n"
            "- bit:  Display rates in Bit/s (default)\n"
            "- byte: Display rates in Byte/s\n\n"
            "[預設: bit]"
        ),
        "help_max_mode": (
            "Y 軸縮放模式：smart（預設）、legacy、fixed\n\n"
            "Possible values:\n"
            "- smart:  Smart adaptive Y-axis with exponential decay (default)\n"
            "- legacy: nload-style auto scale based on the visible graph history\n"
            "- fixed:  Fixed Y-axis value from --max-y-value\n\n"
            "[預設: smart]"
        ),
        "help_max_half_life": (
            "smart 模式指數衰減半衰期，單位秒（預設：10）\n\n"
            "[預設: 10]"
        ),
        "help_max_y_value": "fixed 模式固定 Y 軸上限（如 100M、1G、500K）",
        "help_no_graph": "隱藏流量圖形，僅顯示統計資訊",
        "help_unicode": "使用 Unicode 區塊字元繪製圖形（█▓░· 取代 #|..）",
        "help_bar_style": (
            "狀態列/說明列樣式：plain（預設），fill，color\n\n"
            "Possible values:\n"
            "- fill:  Background color fills entire line\n"
            "- color: Background color only on text\n"
            "- plain: No background, text color only (default)\n\n"
            "[預設: plain]"
        ),
        "help_in_color": "入站（下載）圖形顏色，十六進位 RGB（如 0x00d7ff）。預設：青色",
        "help_out_color": "出站（上傳）圖形顏色，十六進位 RGB（如 0xffaf00）。預設：金色",
        "help_hide_separator": "隱藏分隔線（標題和面板之間的等號行）",
        "help_version": "列印版本號",
        "help_no_color": "停用所有 TUI 顏色（單色模式）。執行時按 'c' 切換",
        "help_debug_info": "列印網路卡除錯資訊並退出",
        "help_netlink": "[僅 Linux/Android] 使用 pyroute2 透過 RTNETLINK 取代 psutil（適用於 Termux proot distro 或無法存取 /proc/net/dev 的受限環境）",
        "help_lang": (
            "顯示語言：en-us（預設），zh-cn，zh-tw\n\n"
            "Possible values:\n"
            "- en-us: English (United States) — English (US)\n"
            "- zh-cn: Simplified Chinese (Mainland China) — 简体中文（大陆）\n"
            "- zh-tw: Traditional Chinese (Taiwan) — 繁體中文（台灣）\n\n"
            "[預設: en-us]"
        ),
        "help_help": "列印說明（使用 '-h' 查看簡短摘要）",
        "help_system": "系統",
        "help_arch": "架構",
        # ── TUI strings ──
        "device": "裝置",
        "device_emoji": "🖧 裝置",
        "incoming": "入站",
        "incoming_emoji": "⬇️📥 入站",
        "outgoing": "出站",
        "outgoing_emoji": "⬆️📤 出站",
        "stat_curr": "目前",
        "stat_avg": "平均",
        "stat_min": "最小",
        "stat_max": "最大",
        "stat_ttl": "總計",
        "stat_curr_emoji": "⚡ 目前",
        "stat_avg_emoji": "📊 平均",
        "stat_min_emoji": "📏 最小",
        "stat_max_emoji": "🚀 最大",
        "stat_ttl_emoji": "📦 總計",
        "help_bar": " ←/→ 切換裝置 | F3 資訊 | q 退出",
        "help_bar_emoji": " ⬅️/➡️ 切換裝置 | 🔧 F3 資訊 | 🚪 q 退出",
        "f3_help_bar": " F3 返回 | ←/→ 切換裝置 | q 退出",
        "f3_help_bar_emoji": " 🔧 F3 返回 | ⬅️/➡️ 切換 | 🚪 q 退出",
        "f3_title": "═══ winload 除錯資訊 (F3) ═══",
        "terminal_too_small": "終端視窗太小！",
        "terminal_too_small_emoji": "😭 終端視窗太小！📌",
        "loopback_warning": " ⚠ 回環裝置：Windows 上統計可能不準確",
        # ── Error messages ──
        "error_no_curses": "錯誤：請先安裝 windows-curses",
        # ── F3 debug overlay section titles ──
        "debug_section_params": "═══ 參數 ═══",
        "debug_section_yaxis": "═══ Y 軸縮放 ═══",
        "debug_section_device": "═══ 裝置 ═══",
        "debug_section_colors": "═══ 顏色 ═══",
        # ── F3 key-value labels ──
        "debug_version": "版本：",
        "debug_system": "系統：",
        "debug_language": "語言：",
        "debug_interval": "刷新間隔：",
        "debug_average": "平均窗口：",
        "debug_unit": "單位：",
        "debug_bar_style": "狀態列樣式：",
        "debug_emoji": "表情：",
        "debug_unicode": "Unicode：",
        "debug_no_graph": "隱藏圖形：",
        "debug_no_color": "無顏色：",
        "debug_hide_sep": "隱藏分隔線：",
        "debug_yaxis_mode": "模式：",
        "debug_in_smooth": "入站平滑：",
        "debug_out_smooth": "出站平滑：",
        "debug_device_name": "名稱：",
        "debug_device_addr": "地址：",
        "debug_in_curr": "入站目前：",
        "debug_out_curr": "出站目前：",
        "debug_in_total": "入站總計：",
        "debug_out_total": "出站總計：",
        "debug_in_peak": "入站峰值：",
        "debug_out_peak": "出站峰值：",
        "debug_in_color": "入站顏色：",
        "debug_out_color": "出站顏色：",
        # ── Panel mode tags ──
        "tag_fixed": "固定",
        "tag_smart_max": "智能",
        "tag_legacy": "傳統",
        "tag_auto": "自動",
        # ── Y-axis mode descriptions ──
        "yaxis_fixed": "固定最大值（{val}）",
        "yaxis_smart": "智能自適應（半衰期：{sec}秒）",
        "yaxis_legacy": "傳統模式（可見歷史峰值）",
        # ── Misc ──
        "on": "開",
        "off": "關",
        "default_tag": "（預設）",
        "addr_none": "（無）",
        "arrow_up": "↑",
        "arrow_down": "↓",
    },
}


def set_lang(lang: str) -> None:
    """Set the current display language."""
    global _current_lang
    lang = lang.lower().strip()
    if lang in _STRINGS:
        _current_lang = lang
    else:
        _current_lang = "en-us"


def get_lang() -> str:
    """Get the current display language."""
    return _current_lang


def t(key: str) -> str:
    """Look up a translated string by key. Falls back to en-us, then to the key itself."""
    table = _STRINGS.get(_current_lang, _STRINGS["en-us"])
    result = table.get(key)
    if result is not None:
        return result
    # fallback to English
    result = _STRINGS["en-us"].get(key)
    if result is not None:
        return result
    return key
