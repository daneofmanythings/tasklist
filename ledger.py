from tasks import Task


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
