# Selects the active language and exposes stable translation helpers.
"""Internationalization support for all bundled language catalogs."""

from typing import Dict

from .en_us import STRINGS as EN_US
from .zh_cn import STRINGS as ZH_CN
from .zh_tw import STRINGS as ZH_TW

_current_lang = "en-us"
_STRINGS: Dict[str, Dict[str, str]] = {
    "en-us": EN_US,
    "zh-cn": ZH_CN,
    "zh-tw": ZH_TW,
}


def set_lang(lang: str) -> None:
    """Set the display language, falling back to English."""
    global _current_lang
    normalized = lang.lower().strip()
    _current_lang = normalized if normalized in _STRINGS else "en-us"


def get_lang() -> str:
    """Return the current display language."""
    return _current_lang


def t(key: str) -> str:
    """Look up a string with English and key fallbacks."""
    return _STRINGS.get(_current_lang, EN_US).get(key, EN_US.get(key, key))
