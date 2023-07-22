from interface import utils
from interface.menu import PreviousMenu, NextMenu
from interface.menus.view_all_tasks import ViewAllTasks
from interface.menus.search_task_titles_parameters import SearchTaskTitlesParameters


__all__ = ['FindTasks']


class FindTasks:
    TITLE = "FIND TASKS"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = FindTasks(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.menu = [
            f"{utils.hotkey('1')} View All",
            f"{utils.hotkey('2')} Search Titles",
        ]

        self.sub_menu = [
            f"{utils.hotkey('g')}o back",
        ]

        self.options = {
            '1': NextMenu(ViewAllTasks),
            '2': NextMenu(SearchTaskTitlesParameters),
            'g': PreviousMenu(),
        }

    def display_string(self):
        result = "\n"
        result += utils.header_string(utils.paint_header(self.header_list))
        result += "\n"
        result += utils.menu_string(self.menu)
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        result = utils.get_menu_input(self.options)
        return result
