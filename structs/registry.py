from structs.tasks import Task, TaskEncoder, TaskDecoder
import os
import json

__all__ = ['Registry', 'RegistryEncoder', 'RegistryDecoder',
           'load_registry', 'save_registry', 'SAVE_PATH']

SAVE_PATH = './data/'


class Registry:
    def __init__(self):
        self._ledger = set()

    def add_task(self, task) -> None:
        if not isinstance(task, Task):
            raise TypeError(
                f"Tried to add a non-task object to the registry: {task}")
        self._ledger.add(task)

    def remove_task(self, task_title: str) -> None:
        self._ledger.remove(task_title)

    def __str__(self):
        result = ''

        for task in self._ledger:
            result += str(task)
            result += '\n'

        return result[:-1]

    def __repr__(self):
        result = str()
        for task in self._ledger:
            result += task.__repr__() + '\n'
        return result


class RegistryEncoder(TaskEncoder):
    def default(self, arg):
        if isinstance(arg, Registry):
            return list(arg._ledger)

        return super().default(arg)


class RegistryDecoder(TaskDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        result = Registry()
        for task in obj:
            result.add_task(Task(**task))
        return result


def load_registry(path):
    try:
        with open(path + 'data.json', 'r') as f:
            json_str = f.read()
        return json.loads(json_str, cls=RegistryDecoder)
    except FileNotFoundError:
        try:
            os.makedirs(path)
        except FileExistsError:
            pass
        return Registry()


def save_registry(registry, path):
    j_registry = json.dumps(registry, cls=RegistryEncoder, indent=2)
    with open(path + 'data.json', 'w') as f:
        f.write(j_registry)