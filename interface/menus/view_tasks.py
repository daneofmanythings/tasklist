from interface.utils import color_text, SOFT_GREEN
from interface.menu import Menu


__all__ = ["ViewTasks"]


class ViewTasks(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / ' + color_text('VIEW TASKS', *SOFT_GREEN),
    )
    MENU = (
        "1) Go Back",
        "2) Main Menu",
    )
    OPTIONS = {
        "1": 0,
        "2": -1,
    }
