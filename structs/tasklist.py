from structs.tasks import Task


class Tasklist:

    def __init__(self, tasks):
        self.tasks = tasks

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, val):
        pass
