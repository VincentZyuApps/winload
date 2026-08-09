# Stores the Simplified Chinese localization catalog.

STRINGS = {
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
}
