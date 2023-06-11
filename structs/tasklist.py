from structs.tasks import Task

__all__ = ['Tasklist']


class Tasklist:

    REGISTRY = None

    def __init__(self):
        self._tasks = dict()

    def add_task(self, task_name: str):
        self._tasks[task_name] = 0

    def toggle_status(self, task_name: str):
        # letting potential key errors leak
        self._tasks[task_name] = (self._tasks[task_name] + 1) % 2
