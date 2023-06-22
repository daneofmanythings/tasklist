from interface import utils
from config.globals import PROMPT
from interface.menu import ReplaceCurrent, NextMenu, PreviousMenu
from interface.menus.save_registry import SaveRegistry
from interface.menus.edit_task import EditTask
from interface.menus.delete_task import DeleteTask


class ViewTask:

    TITLE = "VIEW TASK"

    @classmethod
    def run(self, registry, header_list, task, tasklist):
        M = ViewTask(registry, header_list, task)
        return M.run_instance()

    def __init__(self, registry, header_list, task):
        self.registry = registry
        self.header_list = header_list
        self.task = task

        self.sub_menu = [
            f"{utils.hotkey('s')}ave to registry",
            f"{utils.hotkey('e')}dit",
            f"{utils.hotkey('d')}elete task",
            f"{utils.hotkey('g')}o back",
        ]

    @property
    def options(self):
        return {
            's': ReplaceCurrent(SaveRegistry, task=self.task),
            'e': NextMenu(EditTask, task=self.task),
            'd': ReplaceCurrent(DeleteTask, task=self.task),
            'g': PreviousMenu(task=self.task),
        }

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.task.public_listify())
        return result

    def run_instance(self):
        while True:
            utils.clear_terminal()
            print(self.display_string())
            print(utils.submenu_string(self.sub_menu))

            try:
                return utils.get_menu_input(self.options)
            except KeyError:
                continue
