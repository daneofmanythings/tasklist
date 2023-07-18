from interface import utils

from interface.menu import ReplaceCurrent, NextMenu, PreviousMenu
from interface.menus.view_task import ViewTask
from interface.menus.save_registry import SaveRegistry


class ViewTasklist:

    TITLE = "VIEW TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = ViewTasklist(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, tasklist):
        self.registry = registry
        self.header_list = header_list
        self.tasklist = registry._current_tasklist

        self.sub_menu = [
            f"{utils.hotkey('#')} view task",
            f"{utils.hotkey('s')}ave",
            f"{utils.hotkey('g')}o back",
        ]

    @property
    def optionals(self):
        result = {f"{i + 1}": NextMenu(ViewTask, task=self.registry._tasks[task_name])
                  for i, task_name in enumerate(self.tasklist.tasks.keys())}
        result.update({
            's': ReplaceCurrent(SaveRegistry, tasklist=self.tasklist),
            'g': PreviousMenu(),
        })
        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.tasklist.listify())
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())

        return utils.get_menu_input(self.optionals)
    pass
