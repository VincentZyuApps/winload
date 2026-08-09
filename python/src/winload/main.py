# Wires the Python CLI to diagnostics or the interactive terminal runtime.
"""winload Python command entry point."""

import sys

from .cli import parse_args
from .diagnostics import print_debug_info, print_system_info
from .i18n import t


def main() -> None:
    config = parse_args()
    if config.debug_info:
        try:
            print_debug_info(emoji=config.emoji, use_netlink=config.netlink)
        except RuntimeError as exc:
            if config.netlink:
                print(f"Error: {exc}", file=sys.stderr)
                raise SystemExit(1) from exc
            raise
        return

    try:
        import curses  # noqa: F401
    except ImportError:
        print(t("error_no_curses"))
        print("  pip install windows-curses")
        raise SystemExit(1)

    from .runtime import run

    try:
        run(config)
    except RuntimeError as exc:
        if config.netlink:
            print(f"Error: {exc}", file=sys.stderr)
            raise SystemExit(1) from exc
        raise
    except KeyboardInterrupt:
        pass
    finally:
        print_system_info()


if __name__ == "__main__":
    main()
