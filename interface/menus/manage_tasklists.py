from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state
from interface.menus.generate_tasklist import GenerateTasklist
from interface.menus.view_all_tasklists import ViewAllTasklists
from interface.utils import color_text, hotkey
from config.theme import MENU_HIGHLIGHT


class ManageTasklists(Menu):
    HEADER = (
        'MAIN / ' + color_text('MANAGE_TASKLISTS', *MENU_HIGHLIGHT),
    )
    MENU = (
        hotkey('1') + " Generate new list",
        hotkey('2') + " View all lists",
        hotkey('3') + " Go Back",
    )
    OPTIONS = {
        "1": MenuReturn(state.NEXT_MENU, GenerateTasklist),
        "2": MenuReturn(state.NEXT_MENU, ViewAllTasklists),
        "3": MenuReturn(state.PREVIOUS_MENU, None)
    }
