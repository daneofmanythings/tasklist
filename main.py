from structs import (
    App,
    # Registry,
    # RegistryEncoder,
    # RegistryDecoder,
    load_registry,
    SAVE_PATH,
)


def main():
    registry = load_registry(SAVE_PATH)
    app = App(registry)
    # add_data_sample(registry)
    # save_registry(registry, SAVE_PATH)
    while True:
        app.run_current()

    # print(eegistry)


if __name__ == "__main__":
    main()
