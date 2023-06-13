from config.theme import MENU_HIGHLIGHT
from interface.utils import color_text
from interface.menus.manage_tasks import ManageTasks
from interface.menus.manage_tasklists import ManageTasklists
from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state


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
