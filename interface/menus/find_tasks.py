from collections import ChainMap as cmap
from interface import utils
from interface.menu import PreviousMenu, NextMenu
from interface.menus import (
    ViewAllTasks,
    SearchTaskTitles,
)


__all__ = ['FindTasks']


class FindTasks:
    TITLE = "FIND TASKS"

    @classmethod
    def run(self, registry, header_list):
        M = FindTasks(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.menu = [
            f"{utils.hotkey('1')} View All",
            f"{utils.hotkey('2')} Search Titles",
        ]

        self.submenu = [
            f"{utils.hotkey('g')}o back",
        ]

        self.options = {
            '1': NextMenu(ViewAllTasks),
            '2': NextMenu(SearchTaskTitles),
            'g': PreviousMenu(),
        }

    def display_string(self):
        result = "\n"
        result += utils.header_string(utils.paint_header(self.header_list))
        result += "\n"
        result += utils.menu_string(self.menu)
        result += "\n"
        result += utils.submenu_string(self.submenu)

    def run_instance(self):
        print(self.display_string())
        result = utils.get_menu_input(self.options)
        return result
