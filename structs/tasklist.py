import json
from functools import total_ordering


@total_ordering
class Tasklist:

    REGISTRY = None

    def __init__(self, title, tasks=None):
        self.title = title
        if tasks is None:
            self.tasks = dict()
        else:
            self.tasks = tasks

    def add_task(self, task_name: str):
        if task_name not in self.REGISTRY._tasks:
            raise ValueError(f'task: {task_name} not found in registry')
        self.tasks[task_name] = 0

    def toggle_status(self, task_name: str):
        # letting potential key errors leak
        self.tasks[task_name] = (self.tasks[task_name] + 1) % 2

    def listify(self):
        result = list()
        result.append(f"{self.title}\n----------")
        for attr, val in self.tasks.items():
            result.append(f"{attr}: {val}")
        return result

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        if not isinstance(other, Tasklist):
            raise NotImplementedError(
                "Equality only implemented on type Tasklist.")
        return self.title == other.title

    def __lt__(self, other):
        if not isinstance(other, Tasklist):
            raise NotImplementedError(
                "Comparison only implemented on type Task.")
        return self.title <= other.title


class TasklistEncoder(json.JSONEncoder):
    def default(self, arg):
        return vars(arg)
