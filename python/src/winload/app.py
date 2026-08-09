# Owns mutable application state, traffic updates, and device navigation.
"""UI-independent application state for winload."""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

from .collector import Collector, DeviceInfo
from .config import RunConfig
from .stats import StatisticsEngine


class Action(Enum):
    QUIT = auto()
    NEXT_DEVICE = auto()
    PREVIOUS_DEVICE = auto()
    TOGGLE_DEBUG = auto()
    TOGGLE_SEPARATOR = auto()
    TOGGLE_COLOR = auto()
    NONE = auto()


@dataclass
class DeviceView:
    """Statistics and metadata for one network interface."""

    name: str
    info: Optional[DeviceInfo]
    engine: StatisticsEngine

    @classmethod
    def create(
        cls,
        name: str,
        info: Optional[DeviceInfo] = None,
        smart_max_half_life: Optional[float] = None,
        interval: int = 500,
        average: int = 300,
    ) -> "DeviceView":
        return cls(
            name=name,
            info=info,
            engine=StatisticsEngine(
                refresh_interval_ms=interval,
                average_window_sec=average,
                smart_max_half_life=smart_max_half_life,
            ),
        )

    def get_addr_str(self) -> str:
        if self.info and self.info.addrs:
            return self.info.addrs[0]
        return ""


class App:
    """Own collection and navigation without depending on curses rendering."""

    def __init__(self, collector: Collector, config: RunConfig):
        self.collector = collector
        self.config = config
        self.current_device_idx = 0
        self.views: List[DeviceView] = []
        self.show_debug = False
        self.hide_separator = config.hide_separator
        self.no_color = config.no_color
        self._init_views()
        self.select_device(config.device)

    @property
    def current_view(self) -> DeviceView:
        return self.views[self.current_device_idx % len(self.views)]

    def _init_views(self) -> None:
        smart_half_life = (
            self.config.max_half_life if self.config.max_mode == "smart" else None
        )
        self.views = [
            DeviceView.create(
                name,
                self.collector.get_device_info(name),
                smart_max_half_life=smart_half_life,
                interval=self.config.interval,
                average=self.config.average,
            )
            for name in self.collector.device_names
        ]
        if not self.views:
            self.views.append(
                DeviceView.create(
                    "(no device)",
                    smart_max_half_life=smart_half_life,
                    interval=self.config.interval,
                    average=self.config.average,
                )
            )

    def select_device(self, query: Optional[str]) -> None:
        if not query:
            return
        for index, view in enumerate(self.views):
            if query.lower() in view.name.lower():
                self.current_device_idx = index
                return

    def next_device(self) -> None:
        if self.views:
            self.current_device_idx = (self.current_device_idx + 1) % len(self.views)

    def previous_device(self) -> None:
        if self.views:
            self.current_device_idx = (self.current_device_idx - 1) % len(self.views)

    def update(self) -> None:
        snapshots = self.collector.collect()
        for view in self.views:
            snapshot = snapshots.get(view.name)
            if snapshot:
                view.engine.update(snapshot)

    def handle_action(self, action: Action) -> bool:
        """Apply an action and return whether the runtime should continue."""
        if action is Action.QUIT:
            return False
        if action is Action.NEXT_DEVICE:
            self.next_device()
        elif action is Action.PREVIOUS_DEVICE:
            self.previous_device()
        elif action is Action.TOGGLE_DEBUG:
            self.show_debug = not self.show_debug
        elif action is Action.TOGGLE_SEPARATOR:
            self.hide_separator = not self.hide_separator
        elif action is Action.TOGGLE_COLOR:
            self.no_color = not self.no_color
        return True
