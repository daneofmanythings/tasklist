from interface.utils import color_text, SOFT_GREEN
from interface.menu import Menu

__all__ = ["RecurringTask"]


class RecurringTask(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / CREATE TASK / ' +
        color_text('RECURRING TASK', *SOFT_GREEN),
    )
    MENU = (
        "1) Go Back",
    )
    OPTIONS = {
        "1": 0,
    }
