import json
from display import HEADER
from registry import Registry, RegistryEncoder, RegistryDecoder
from tasks import Task
import shutil


def main():
    registry = Registry()
    x, y = shutil.get_terminal_size()
    keys = ('title', 'importance', 'duration', 'desc')
    args1 = ('dishes', None, None, 'do them')
    args2 = ('vaccuum', 5, 15, 'do it')
    args3 = ('garbage', 2, 10, 'gross')

    d1 = dict(zip(keys, args1))
    d2 = dict(zip(keys, args2))
    d3 = dict(zip(keys, args3))

    registry.add_task(Task(**d1))
    registry.add_task(Task(**d2))
    padding = '\n' + ' ' * (y - 14)
    print(padding.join(s for s in HEADER))

    j_registry = json.dumps(registry, cls=RegistryEncoder, indent=2)
    with open('./data/data.json', 'w') as f:
        f.write(j_registry)

    registry = json.loads(j_registry, cls=RegistryDecoder)

    registry.add_task(Task(**d3))

    j_registry = json.dumps(registry, cls=RegistryEncoder, indent=2)
    # print(j_registry)


if __name__ == "__main__":
    main()
