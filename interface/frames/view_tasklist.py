from interface import utils

from interface.returns import ReplaceCurrent, NextFrame, PreviousFrame, BackToMain
from interface.frames.view_task import ViewTask


class ViewTasklist:

    TITLE = "VIEW TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = ViewTasklist(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, tasklist):
        self.registry = registry
        self.header_list = header_list
        self.tasklist = tasklist

    @property
    def sub_menu(self):
        result = list()

        if not self.registry.current_tasklist or self.registry.current_tasklist != self.tasklist:
            result.append(f"{utils.hotkey('s')}et to current")

        result.extend([
            f"{utils.hotkey('d')}elete",
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",

        ])
        return result

    @property
    def optionals(self):
        result = {f"{i + 1}": NextFrame(ViewTask, task=self.registry._tasks[task_name])
                  for i, task_name in enumerate(self.tasklist.tasks)
                  if task_name in self.registry._tasks}
        result.update({
            'd': PreviousFrame(execute=Deleter(self.registry, self.tasklist)),
            'g': PreviousFrame(),
            'h': BackToMain()
        })
        if not self.registry.current_tasklist or self.registry.current_tasklist != self.tasklist:
            result.update({
                's': ReplaceCurrent(
                    ViewTasklist,
                    tasklist=self.tasklist,
                    execute=Setter(self.registry, self.tasklist)
                )
            })
        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.tasklist.listify_numbered())
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())

        return utils.get_menu_input(self.optionals)


class Deleter:
    def __init__(self, registry, tasklist):
        self.registry = registry
        self.tasklist = tasklist

    def __call__(self):
        return self.registry.w_tasklist_delete(self.tasklist)


class Setter:
    def __init__(self, registry, tasklist):
        self.registry = registry
        self.tasklist = tasklist

    def __call__(self):
        return self.registry.w_current_tasklist_set(self.tasklist)
