from interface import utils
from interface.returns import ReplaceCurrent, NextFrame, PreviousFrame, BackToMain, StayCurrent
from interface.frames.edit_task import EditTaskSelectField


class ViewTask:

    TITLE = "VIEW TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = ViewTask(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, task):
        self.registry = registry
        self.header_list = header_list
        self.task = task

    @property
    def sub_menu(self):
        result = [
            f"{utils.hotkey('e')}dit",
            f"{utils.hotkey('d')}elete",
        ]

        if self.task.last_completed:
            result.append(f"{utils.hotkey('r')}efresh")

        result.extend([
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",
        ])

        return result

    @property
    def options(self):
        result = {
            'e': NextFrame(EditTaskSelectField, task=self.task),
            'd': PreviousFrame(execute=Deleter(self.registry, self.task)),
            'g': PreviousFrame(),
            'h': BackToMain()
        }

        if self.task.last_completed:
            result['r'] = StayCurrent(
                execute=Refresher(self.registry, self.task))

        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.task.listify())
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)


class Deleter:
    def __init__(self, registry, task):
        self.registry = registry
        self.task = task

    def __call__(self):
        return self.registry.w_task_delete(self.task)


class Refresher:
    def __init__(self, registry, task):
        self.registry = registry
        self.task = task

    def __call__(self):
        return self.registry.w_task_refresh(self.task)
