from interface import utils

from interface.menu import ReplaceCurrent, NextMenu, PreviousMenu, StayCurrent
from interface.menus.view_tasklist import ViewTasklist


class CurrentTasklist:

    TITLE = "CURRENT TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = CurrentTasklist(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.tasklist = registry.current_tasklist

        self.sub_menu = [
            f"{utils.hotkey('v')}iew",
            f"{utils.hotkey('f')}inished",
            f"finished and {utils.hotkey('r')}etain list",
            f"{utils.hotkey('g')}o back",
        ]

    @property
    def optionals(self):
        result = {f"{i + 1}": StayCurrent(execute=lambda: self.registry.save(current_tasklist_toggle_task=task_name))
                  for i, task_name in enumerate(self.tasklist.tasks.keys())}
        result.update({
            'v': NextMenu(ViewTasklist, tasklist=self.tasklist),
            'f': PreviousMenu(execute=lambda: self.registry.save(current_tasklist_process_delete=self.tasklist)),
            'r': PreviousMenu(execute=lambda: self.registry.save(current_tasklist_process_save=self.tasklist)),
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
        if not self.tasklist:
            return PreviousMenu()
        utils.clear_terminal()
        print(self.display_string())

        return utils.get_menu_input(self.optionals)
