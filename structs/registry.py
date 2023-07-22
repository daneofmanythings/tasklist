from structs.task import Task, TaskEncoder, TaskDecoder
from structs.tasklist import Tasklist, TasklistEncoder, TasklistDecoder
import os
import json
from datetime import date


class Registry:
    def __init__(self):
        self._tasks = dict()
        self._tasklists = dict()
        self._current_tasklist = None

    @property
    def tasks(self):
        return self._tasks.values()

    @property
    def tasklists(self):
        return self._tasklists.values()

    def add_task(self, task) -> None:
        if not isinstance(task, Task):
            raise TypeError(
                f"Tried to add a non-task object to the registry: {task}")
        self._tasks[task.title] = task

    def remove_task(self, task):
        del self._tasks[task.title]

    def process_current_tasklist(self):
        task_list = self._current_tasklist.tasks
        for task_name in task_list:
            if task_list[task_name] and task_name in self._tasks:
                self._tasks[task_name].last_completed = task_list[task_name]

    def add_tasklist(self, tasklist) -> None:
        if not isinstance(tasklist, Tasklist):
            raise TypeError(
                f"Tried to add a non-tasklist object to the registry: {tasklist}")
        self._tasklists[tasklist.title] = tasklist

    def remove_tasklist(self, tasklist) -> None:
        del self._tasklists[tasklist.title]

    def set_current_tasklist(self, tasklist) -> None:
        if tasklist is None or tasklist in self._tasklists.values():
            self._current_tasklist = tasklist
        else:
            raise ValueError(
                f"Tasklist: {tasklist} not found in registry")

    def remove_current_tasklist(self):
        self.remove_tasklist(self._current_tasklist)
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
                'tasks': list(arg.tasks),
                'tasklists': list(arg._tasklists.values()),
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
