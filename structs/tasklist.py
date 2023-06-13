import json


class Tasklist:

    REGISTRY = None

    def __init__(self):
        self._tasks = dict()

    def add_task(self, task_name: str):
        if task_name not in self.REGISTRY:
            raise ValueError(f'task: {task_name} not found in registry')
        self._tasks[task_name] = 0

    def toggle_status(self, task_name: str):
        # letting potential key errors leak
        self._tasks[task_name] = (self._tasks[task_name] + 1) % 2


class TasklistEncoder(json.JSONEncoder):
    def default(self, arg):
        return vars(arg)
