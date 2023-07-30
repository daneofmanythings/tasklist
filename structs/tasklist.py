import json
from datetime import date
from functools import total_ordering

from interface import utils
# TODO: put these colors into the theming file
from config.themes.rosepine import PINE, ROSE, HIGHLIGHT_HIGH
from config.theme import HIGHLIGHT


@total_ordering
class Tasklist:

    # This is linked in main.py
    REGISTRY = None

    def __init__(self, title, tasks=None):
        self.title = title
        # self.tasks is a dict holding the task name and date of completion
        if tasks is None:
            self.tasks = dict()
        else:
            self.tasks = tasks

    def add_task(self, task_name: str):
        if task_name not in self.REGISTRY._tasks:
            raise ValueError(f'task: {task_name} not found in registry')
        self.tasks[task_name] = None

    def toggle_completion(self, task_name: str):
        # letting potential key errors leak. Should always be fed valid task
        if self.tasks[task_name]:
            self.tasks[task_name] = None
        else:
            self.tasks[task_name] = date.today()

    def current_listify(self):
        result = list()
        result.append(utils.paint_title(self.title))
        for task_name in self.tasks:
            if task_name in Tasklist.REGISTRY.tasks:
                if self.tasks[task_name]:
                    result.append(
                        f"{task_completed(task_name)}")
                else:
                    result.append(
                        f"{task_in_progress(task_name)}")
            else:
                result.append(
                    f"{task_not_found(task_name)}")

        return result

    def current_listify_numbered(self):
        result = list()
        result.append(utils.paint_title(self.title))
        for i, task_name in enumerate(self.tasks):
            if task_name in Tasklist.REGISTRY.tasks:
                if self.tasks[task_name]:
                    result.append(
                        f"{utils.hotkey(i + 1)} {task_completed(task_name)}")
                else:
                    result.append(
                        f"{utils.hotkey(i + 1)} {task_in_progress(task_name)}")
            else:
                result.append(
                    f"{utils.hotkey(i + 1)} {task_not_found(task_name)}")

        return result

    def listify_numbered(self):
        result = list()
        result.append(utils.paint_title(self.title))
        for i, task_name in enumerate(self.tasks):
            if task_name in Tasklist.REGISTRY._tasks:
                result.append(f"{utils.hotkey(i + 1)} {task_name}")
        return result

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.title == other
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


class TasklistDecoder(json.JSONDecoder):
    def decode(self, arg):
        if isinstance(arg, str):
            obj = json.loads(arg)
        else:
            obj = arg

        result = Tasklist(obj['title'])
        result.tasks = obj['tasks']

        return result


####################
# HELPER FUNCTIONS #
####################


def task_completed(task_name: str):
    result = task_name + " (COMPLETE)"
    return utils.paint_text(result, HIGHLIGHT_HIGH)


def task_in_progress(task_name: str):
    return task_name + utils.paint_text(" (in progress)", HIGHLIGHT)


def task_not_found(task_name: str):
    result = task_name + " (NOT FOUND)"
    return utils.paint_text(result, ROSE)


def task_not_due(task_name: str):
    return task_name + utils.paint_text(" (not due)", PINE)
