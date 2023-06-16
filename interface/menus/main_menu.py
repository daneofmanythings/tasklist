from config.theme import MENU_HIGHLIGHT
from config.globals import MENU_PADDING, HEADER_PADDING
from interface.utils import color_text, hotkey
from interface.menus.manage_tasks import ManageTasks
from interface.menus.manage_tasklists import ManageTasklists
from interface.menus.current_tasklist import CurrentTasklist
from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state
from interface import utils


class Main(Menu):
    HEADER = (
        color_text('MAIN', *MENU_HIGHLIGHT) + ' /',
    )
    MENU = (
        hotkey("1") + ' Manage Tasks.',
        hotkey("2") + ' Manage Tasklists.',
    )

    OPTIONS = {
        "1": MenuReturn(state.NEXT_MENU, ManageTasks),
        "2": MenuReturn(state.NEXT_MENU, ManageTasklists),
    }

    @classmethod
    def run(self, registry):
        M = Main(registry)
        return M.run_instance()

    def __init__(self, registry):
        self.registry = registry
        self.MENU = list(Main.MENU)
        self.OPTIONS = dict(Main.OPTIONS)

    def run_instance(self):
        if self.registry._current_tasklist:
            self.MENU.append(f'{hotkey("3")} Open Current Tasklist')
            self.OPTIONS["3"] = MenuReturn(state.NEXT_MENU, CurrentTasklist)
        with utils.NoCursor():
            utils.clear_terminal()
            print(self.display_string_instance())
        return utils.get_menu_input("", self.OPTIONS)

    def display_string_instance(self):
        result = str()
        result += utils.table_to_string(self.HEADER, HEADER_PADDING)
        result += utils.table_to_string(self.MENU, MENU_PADDING)
        return result
