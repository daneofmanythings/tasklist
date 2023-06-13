from config.theme import MENU_HIGHLIGHT
from interface.utils import color_text
from interface.menus.view_all import ViewAll
from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state


class ViewTasks(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / ' + color_text('VIEW TASKS', *MENU_HIGHLIGHT),
    )
    MENU = (
        "1) View All",
        "2) Search All",
        "3) Go Back",
        "4) Main Menu",
    )
    OPTIONS = {
        "1": MenuReturn(state.NEXT_MENU, ViewAll),
        "2": MenuReturn(state.STAY_CURRENT, None),
        "3": MenuReturn(state.PREVIOUS_MENU, None),
        "4": MenuReturn(state.BACK_TO_MAIN, None),
    }
