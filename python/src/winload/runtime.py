# Manages the curses lifecycle, input mapping, refresh cadence, and UI rendering loop.
"""Interactive terminal runtime for the Python implementation."""

import time

from .app import Action, App
from .collector import Collector
from .config import RunConfig


def map_key(key: int) -> Action:
    """Translate curses key codes to UI-independent application actions."""
    import curses

    if key in (ord("q"), ord("Q")):
        return Action.QUIT
    if key == curses.KEY_F0 + 3:
        return Action.TOGGLE_DEBUG
    if key == ord("="):
        return Action.TOGGLE_SEPARATOR
    if key in (ord("c"), ord("C")):
        return Action.TOGGLE_COLOR
    if key in (curses.KEY_RIGHT, curses.KEY_DOWN, ord("\t"), curses.KEY_NPAGE, 10):
        return Action.NEXT_DEVICE
    if key in (curses.KEY_LEFT, curses.KEY_UP, curses.KEY_PPAGE):
        return Action.PREVIOUS_DEVICE
    return Action.NONE


def main_loop(stdscr: "curses.window", config: RunConfig) -> None:
    """Run collection, input handling, and rendering until quit."""
    import curses

    from .ui import UI

    collector = Collector(use_netlink=config.netlink)
    app = App(collector, config)
    ui = UI(stdscr, app)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    refresh_interval_sec = config.interval / 1000.0
    last_update = 0.0
    while True:
        now = time.time()
        try:
            key = stdscr.getch()
            if key != -1 and not app.handle_action(map_key(key)):
                break
        except curses.error:
            pass
        if now - last_update >= refresh_interval_sec:
            app.update()
            ui.draw()
            curses.doupdate()
            last_update = now


def run(config: RunConfig) -> None:
    """Initialize curses and execute the interactive application."""
    import curses

    curses.wrapper(lambda stdscr: main_loop(stdscr, config))
