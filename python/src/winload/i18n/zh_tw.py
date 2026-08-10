# Stores the Traditional Chinese localization catalog.

STRINGS = {
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
    "help_shortcuts_title": "快捷鍵：",
    "shortcut_previous_device": "切換到上一個網路裝置",
    "shortcut_next_device": "切換到下一個網路裝置",
    "shortcut_toggle_debug": "切換除錯資訊",
    "shortcut_toggle_separator": "切換分隔線",
    "shortcut_toggle_color": "切換顏色",
    "shortcut_quit": "退出",
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
}
