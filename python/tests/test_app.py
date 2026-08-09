# Verifies UI-independent application updates, navigation, and runtime actions.
import sys
import types
import unittest

try:
    import psutil  # noqa: F401
except ModuleNotFoundError:
    sys.modules["psutil"] = types.ModuleType("psutil")

from winload.app import Action, App
from winload.collector import DeviceInfo, Snapshot
from winload.config import RunConfig


class FakeCollector:
    device_names = ["eth0", "wifi0"]

    def get_device_info(self, name):
        return DeviceInfo(name, ["127.0.0.1" if name == "eth0" else "10.0.0.2"])

    def collect(self):
        return {
            "eth0": Snapshot(1.0, 100, 50),
            "wifi0": Snapshot(1.0, 200, 75),
        }


class AppTests(unittest.TestCase):
    def test_initial_device_partial_match(self):
        app = App(FakeCollector(), RunConfig(device="wifi"))
        self.assertEqual(app.current_view.name, "wifi0")

    def test_navigation_wraps(self):
        app = App(FakeCollector(), RunConfig())
        app.previous_device()
        self.assertEqual(app.current_view.name, "wifi0")
        app.next_device()
        self.assertEqual(app.current_view.name, "eth0")

    def test_actions_toggle_mutable_runtime_state(self):
        app = App(FakeCollector(), RunConfig())
        self.assertTrue(app.handle_action(Action.TOGGLE_DEBUG))
        self.assertTrue(app.show_debug)
        self.assertTrue(app.handle_action(Action.TOGGLE_SEPARATOR))
        self.assertTrue(app.hide_separator)
        self.assertFalse(app.handle_action(Action.QUIT))

    def test_update_feeds_each_device_engine(self):
        app = App(FakeCollector(), RunConfig())
        app.update()
        self.assertEqual(len(app.current_view.engine._samples), 1)


if __name__ == "__main__":
    unittest.main()
