from interface.menus.main_menu import Main
from structs.app import App
from structs.tasklist import Tasklist
from structs.registry import load_registry
from config.globals import SAVE_PATH


def main():
    registry = load_registry(SAVE_PATH)
    Tasklist.REGISTRY = registry
    app = App(registry, Main)
    # add_data_sample(registry)
    # save_registry(registry, SAVE_PATH)
    while True:
        app.run_current()

    # print(eegistry)


if __name__ == "__main__":
    main()
