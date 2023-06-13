from structs.tasks import Task, TaskEncoder, TaskDecoder
from structs.tasklist import Tasklist, TasklistEncoder
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

    def add_tasklist(self, tasklist_title) -> None:
        if not isinstance(tasklist_title, Tasklist):
            raise TypeError(
                f"Tried to add a non-tasklist object to the registry: {tasklist_title}")
        self._tasks.add(tasklist_title)

    def remove_tasklist(self, tasklist_title) -> None:
        self._tasklists.remove(tasklist_title)

    def set_current_tasklist(self, tasklist_title) -> None:
        if tasklist_title in self._tasklists:
            self._current_task = tasklist_title
        else:
            raise ValueError(
                f"Tasklist: {tasklist_title} not found in registry")

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


class RegistryDecoder(TaskDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        result = Registry()

        for task in obj['tasks']:
            result.add_task(Task(**task))
        for tasklist in obj['tasklists']:
            result.add_task(Tasklist(**tasklist))
        result.set_current_tasklist(obj['current_tasklist'])

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
