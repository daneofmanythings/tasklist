from structs.tasks import Task, TaskEncoder, TaskDecoder
from structs.tasklist import Tasklist, TasklistEncoder, TasklistDecoder
import os
import json


class Registry:
    def __init__(self):
        self._tasks = set()
        self._tasklists = set()
        self._current_tasklist = None

    def add_task(self, task) -> None:
        if not isinstance(task, Task):
            raise TypeError(
                f"Tried to add a non-task object to the registry: {task}")
        self._tasks.add(task)

    def remove_task(self, task_title: str) -> None:
        self._tasks.remove(task_title)

    def task_complete(self, task_title):
        try:
            self.remove_task(task_title)
        except Exception:  # silently failing for now
            pass

    def add_tasklist(self, tasklist) -> None:
        if not isinstance(tasklist, Tasklist):
            raise TypeError(
                f"Tried to add a non-tasklist object to the registry: {tasklist}")
        self._tasklists.add(tasklist)

    def remove_tasklist(self, tasklist) -> None:
        self._tasklists.remove(tasklist)

    def set_current_tasklist(self, tasklist) -> None:
        if tasklist in self._tasklists or tasklist is None:
            self._current_tasklist = tasklist
        else:
            raise ValueError(
                f"Tasklist: {tasklist} not found in registry")

    def remove_current_tasklist(self):
        self._current_tasklist = None

    def __str__(self):
        result = ''

        for task in self._tasks:
            result += str(task)
            result += '\n'

        return result[:-1]

    def __repr__(self):
        result = str()
        for task in self._tasks:
            result += task.__repr__() + '\n'
        return result


class RegistryEncoder(TaskEncoder, TasklistEncoder):
    def default(self, arg):
        if isinstance(arg, Registry):
            return {
                'tasks': list(arg._tasks),
                'tasklists': list(arg._tasklists),
                'current_tasklist': arg._current_tasklist
            }

        return super().default(arg)


class RegistryDecoder(TaskDecoder, TasklistDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        result = Registry()

        for task in obj['tasks']:
            result.add_task(Task(**task))
        for tasklist in obj['tasklists']:
            result.add_tasklist(Tasklist(**tasklist))

        if obj['current_tasklist']:
            current_tasklist = Tasklist(**obj['current_tasklist'])
        else:
            current_tasklist = None

        result.set_current_tasklist(current_tasklist)

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
