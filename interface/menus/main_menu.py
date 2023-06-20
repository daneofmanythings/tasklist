from interface.utils import hotkey
from interface.menus.manage_tasklists import ManageTasklists
from interface.menus.current_tasklist import CurrentTasklist
from interface.menus.create_task import CreateTask
from interface.menus.find_tasks import FindTasks
from interface.menus.generate_tasklist import GenerateTasklist
from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state
from interface import utils
from config.globals import MENU_OFFSET


class Main(Menu):
    TITLE = "TASKLIST"

    @classmethod
    def run(self, registry, header_list):
        M = Main(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.current_tasklist = False
        self.registry = registry
        self.header_list = header_list
        self.menu_contents = {
            f"{hotkey('1')} Create Task": MenuReturn(state.NEXT_MENU, CreateTask),
            f"{hotkey('2')} Find Task": MenuReturn(state.NEXT_MENU, FindTasks),
            f"{hotkey('3')} Generate Tasklist": MenuReturn(state.NEXT_MENU, GenerateTasklist),
            f"{hotkey('4')} Manage Tasklists": MenuReturn(state.NEXT_MENU, ManageTasklists)
        }

        if self.registry._current_tasklist:
            self.menu_contents["Open Current Tasklist"] = MenuReturn(
                state.NEXT_MENU, CurrentTasklist)
            self.current_tasklist = True

        self.options = {f"{i + 1}": mr
                        for i, mr in enumerate(self.menu_contents.values())}

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string_instance())
        return utils.get_menu_input("", self.options)

    def display_string_instance(self):
        result = str()
        result += "\n"
        result += utils.header_string(utils.current_menu(self.header_list))
        result += "\n"
        result += utils.table_to_string(self.menu_contents.keys(), MENU_OFFSET)
        return result
