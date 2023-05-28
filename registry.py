from tasks import Task, TaskEncoder, TaskDecoder
import json


class Registry:
    def __init__(self):
        self._ledger = set()

    # TODO: Verify kwargs for task object
    def add_task(self, task) -> None:
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
