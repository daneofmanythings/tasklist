from interface.frames.main_menu import MainMenu
from structs.app import App
from structs.tasklist import Tasklist
from structs.registry import load_registry
from config.globals import SAVE_PATH


def main():
    registry = load_registry(SAVE_PATH)
    Tasklist.REGISTRY = registry
    app = App(registry, MainMenu)

    try:
        while True:
            app.run_current()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
