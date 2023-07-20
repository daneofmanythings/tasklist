from interface import utils

from interface.menu import ReplaceCurrent, NextMenu, PreviousMenu
from interface.menus.view_tasklist import ViewTasklist
from interface.menus.save_registry_confirmation import SaveRegistryConfirmation
from interface.menus.process_tasklist import ProcessTasklist


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
            f"{utils.hotkey('v')}iew tasklist",
            f"{utils.hotkey('p')}rocess tasklist",
            f"{utils.hotkey('s')}ave",
            f"{utils.hotkey('g')}o back",
        ]

    @property
    def optionals(self):
        result = {f"{i + 1}": ReplaceCurrent(CurrentTasklist, task_name=task_name)
                  for i, task_name in enumerate(self.tasklist.tasks.keys())}
        result.update({
            'v': NextMenu(ViewTasklist, tasklist=self.tasklist),
            'p': NextMenu(ProcessTasklist),
            's': ReplaceCurrent(SaveRegistryConfirmation, tasklist_save=self.tasklist),
            'g': PreviousMenu(),
        })
        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.tasklist.current_listify_numbered())
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())

        return utils.get_menu_input(self.optionals)
