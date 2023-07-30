from interface import utils

from interface.returns import ReplaceCurrent, NextMenu, PreviousMenu, BackToMain
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
        result = {f"{i + 1}": NextMenu(ViewTask, task=self.registry._tasks[task_name])
                  for i, task_name in enumerate(self.tasklist.tasks.keys())
                  if task_name in self.registry._tasks}
        result.update({
            'd': PreviousMenu(execute=lambda: self.registry.save(tasklist_delete=self.tasklist)),
            'g': PreviousMenu(),
            'h': BackToMain()
        })
        if not self.registry.current_tasklist or self.registry.current_tasklist != self.tasklist:
            result.update({
                's': ReplaceCurrent(
                    ViewTasklist,
                    tasklist=self.tasklist,
                    execute=lambda: self.registry.save(
                        current_tasklist_set=self.tasklist
                    )
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
