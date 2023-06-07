# import json
from structs import Task
from structs import App
from structs import (
    # Registry,
    # RegistryEncoder,
    # RegistryDecoder,
    load_registry,
    SAVE_PATH,
)


def add_data_sample(registry):
    keys = ('title', 'importance', 'duration', 'desc')
    args1 = ('dishes', None, None, 'do them')
    args2 = ('vaccuum', 5, 15, 'do it')
    args3 = ('garbage', 2, 10, 'gross')

    d1 = dict(zip(keys, args1))
    d2 = dict(zip(keys, args2))
    d3 = dict(zip(keys, args3))

    registry.add_task(Task(**d1))
    registry.add_task(Task(**d2))
    registry.add_task(Task(**d3))


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
