from config.theme import MENU_HIGHLIGHT
from interface.utils import color_text
from interface.menu import Menu

__all__ = ["RepeatTask"]


class RepeatTask(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / CREATE TASK / ' +
        color_text('RECURRING TASK', *MENU_HIGHLIGHT),
    )
    MENU = (
        "1) Go Back",
    )
    OPTIONS = {
        "1": 0,
    }
