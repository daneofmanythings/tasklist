from interface import utils

from interface.menu import ReplaceCurrent, NextMenu
from interface.menus.view_tasklist import ViewTasklist
from interface.menus.save_registry import SaveRegistry


class CurrentTasklist:

    TITLE = "CURRENT TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = CurrentTasklist(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, task_name=None):
        self.registry = registry
        self.header_list = header_list
        self.tasklist = registry._current_tasklist

        if task_name:
            self.tasklist.toggle_completion(task_name)

        self.sub_menu = [
            f"{utils.hotkey('#')} toggle status",
            f"{utils.hotkey('v')}iew tasklist",
            # f"{utils.hotkey('p')}rocess",
            # f"process {utils.hotkey('a')}ll",
            f"{utils.hotkey('s')}ave",
        ]

    @property
    def optionals(self):
        result = {f"{i + 1}": ReplaceCurrent(CurrentTasklist, task_name=task_name)
                  for i, task_name in enumerate(self.tasklist.tasks.keys())}
        result.update({
            'v': NextMenu(ViewTasklist, tasklist=self.tasklist),
            # 'p': ReplaceCurrent(Sa)
            's': ReplaceCurrent(SaveRegistry, tasklist=self.tasklist)
        })
        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.tasklist.current_listify())
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())

        return utils.get_menu_input(self.optionals)
