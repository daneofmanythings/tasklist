import json
from registry import Registry, RegistryEncoder, RegistryDecoder
from tasks import Task
from app import App
import os


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


SAVE_PATH = './data/'


def load_registry(path):
    try:
        with open(path + 'data.json', 'r') as f:
            json_str = f.read()
        return json.loads(json_str, cls=RegistryDecoder)
    except FileNotFoundError:
        try:
            os.makedirs(SAVE_PATH)
        except FileExistsError:
            pass
        return Registry()


def save_registry(registry, path):
    j_registry = json.dumps(registry, cls=RegistryEncoder, indent=2)
    with open(path + 'data.json', 'w') as f:
        f.write(j_registry)


def main():
    registry = load_registry(SAVE_PATH)
    app = App(registry)
    # add_data_sample(registry)
    # save_registry(registry, SAVE_PATH)
    app.run_current()

    # print(registry)


if __name__ == "__main__":
    main()
