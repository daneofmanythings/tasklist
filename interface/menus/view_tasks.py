from config.theme import MENU_HIGHLIGHT
from interface.utils import color_text
from interface.menu import Menu
from interface.menus.view_all import ViewAll


__all__ = ["ViewTasks"]


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
        "1": ViewAll,
        "2": 1,
        "3": 0,
        "4": -1,
    }
