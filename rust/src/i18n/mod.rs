// 🌐 Provides localized UI, help, and debug strings for supported languages.
//! i18n — Internationalization support
//! Supported languages: en-us, zh-cn, zh-tw

mod en_us;
mod zh_cn;
mod zh_tw;

use std::sync::atomic::{AtomicU8, Ordering};

/// Display language
#[derive(Clone, Copy, Debug, PartialEq, Eq, clap::ValueEnum)]
pub enum Lang {
    /// English (United States) — English (US)
    #[value(name = "en-us")]
    EnUs,
    /// Simplified Chinese (Mainland China) — 简体中文（大陆）
    #[value(name = "zh-cn")]
    ZhCn,
    /// Traditional Chinese (Taiwan) — 繁體中文（台灣）
    #[value(name = "zh-tw")]
    ZhTw,
}

static LANG: AtomicU8 = AtomicU8::new(0);

pub fn set_lang(lang: Lang) {
    LANG.store(lang as u8, Ordering::Relaxed);
}

pub fn get_lang() -> Lang {
    match LANG.load(Ordering::Relaxed) {
        1 => Lang::ZhCn,
        2 => Lang::ZhTw,
        _ => Lang::EnUs,
    }
}

pub fn language_name() -> &'static str {
    match get_lang() {
        Lang::EnUs => en_us::LANGUAGE_NAME,
        Lang::ZhCn => zh_cn::LANGUAGE_NAME,
        Lang::ZhTw => zh_tw::LANGUAGE_NAME,
    }
}

/// Look up a translated string by key. Falls back to en-us.
pub fn t(key: &str) -> &'static str {
    match get_lang() {
        Lang::EnUs => en_us::t(key),
        Lang::ZhCn => zh_cn::t(key),
        Lang::ZhTw => zh_tw::t(key),
    }
}
