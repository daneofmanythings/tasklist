from config.theme import CURRENT_MENU
from interface.utils import color_text, hotkey
from interface.menus.view_all_tasks import ViewAll
from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state


class FindTasks(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / ' + color_text('VIEW TASKS', CURRENT_MENU),
    )
    MENU = (
        hotkey('1') + " View All",
        hotkey('2') + " Search All",
        hotkey('3') + " Go Back",
        hotkey('4') + " Main Menu",
    )
    OPTIONS = {
        "1": MenuReturn(state.NEXT_MENU, ViewAll),
        "2": MenuReturn(state.STAY_CURRENT, None),
        "3": MenuReturn(state.PREVIOUS_MENU, None),
        "4": MenuReturn(state.BACK_TO_MAIN, None),
    }
