from tasks import Task, TaskEncoder


class LedgerEncoder(TaskEncoder):
    def default(self, arg):
        if isinstance(arg, Ledger):
            return {"ledger": list(arg._ledger)}
        if isinstance(arg, Task):
            return super().default(arg)

        return super().default(arg)


class Ledger:
    def __init__(self):
        self._ledger = set()

    # TODO: Verify kwargs for task object
    def add_task(self, **taskfields) -> None:
        keys = ('title', 'importance', 'duration', 'desc')
        for key in taskfields:
            if key not in keys:
                raise KeyError(
                    f'{key} is not a valid parameter (title, importance, duration, desc)')
        self._ledger.add(Task(**taskfields))

    def remove_task(self, task_title: str) -> None:
        self._ledger.remove(task_title)

    def __str__(self):
        result = ''

        for task in self._ledger:
            result += str(task)
            result += '\n'

        return result[:-1]
