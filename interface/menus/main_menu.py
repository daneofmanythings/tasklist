from interface import utils
from interface.menu import NextMenu
from interface.menus.create_task import CreateTask
from interface.menus.find_tasks import FindTasks
from interface.menus.generate_tasklist import GenerateTasklist
from interface.menus.current_tasklist import CurrentTasklist


__all__ = ['MainMenu']


class MainMenu:
    TITLE = "TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = MainMenu(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.menu = [
            f"{utils.hotkey('1')} Create Task",
            f"{utils.hotkey('2')} Find Task",
            f"{utils.hotkey('3')} Generate Tasklist",
        ]

        self.options = {
            '1': NextMenu(CreateTask),
            '2': NextMenu(FindTasks),
            '3': NextMenu(GenerateTasklist)
        }

        if self.registry._current_tasklist:
            self.menu.append(f"{utils.hotkey('4')}Open Current Tasklist")
            self.options['4'] = NextMenu(CurrentTasklist)

    def display_string_instance(self):
        result = "\n"
        painted_header = utils.paint_header(self.header_list)
        result += utils.header_string(painted_header)
        result += "\n"
        result += utils.menu_string(self.menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string_instance())
        return utils.get_menu_input(self.options)
