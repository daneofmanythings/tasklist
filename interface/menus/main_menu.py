from config.theme import MENU_HIGHLIGHT
from interface.utils import color_text
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
        '1) Manage Tasks.',
        '2) Manage Tasklists.',
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

    # TODO: fix visibility bug related to display_string
    def run_instance(self):
        if self.registry._current_tasklist:
            self.MENU.append('3) Open Current Tasklist')
            self.OPTIONS["3"] = MenuReturn(state.NEXT_MENU, CurrentTasklist)
        with utils.NoCursor():
            utils.clear_terminal()
            print(self.display_string())
        return utils.get_menu_input("", self.OPTIONS)
