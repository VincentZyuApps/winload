# Verifies language selection, catalog completeness, and translation fallbacks.
import unittest

from winload.i18n import EN_US, ZH_CN, ZH_TW, get_lang, set_lang, t


class I18nTests(unittest.TestCase):
    def tearDown(self):
        set_lang("en-us")

    def test_catalogs_have_identical_keys(self):
        self.assertEqual(set(EN_US), set(ZH_CN))
        self.assertEqual(set(EN_US), set(ZH_TW))

    def test_selection_and_unknown_language_fallback(self):
        set_lang("zh-cn")
        self.assertEqual(get_lang(), "zh-cn")
        self.assertEqual(t("device"), "设备")
        set_lang("not-a-language")
        self.assertEqual(get_lang(), "en-us")

    def test_unknown_key_returns_key(self):
        self.assertEqual(t("missing.translation.key"), "missing.translation.key")


if __name__ == "__main__":
    unittest.main()
