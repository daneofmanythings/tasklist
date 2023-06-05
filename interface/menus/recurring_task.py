from interface.menu import Menu

__all__ = ["RecurringTask"]


class RecurringTask(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / CREATE TASK / RECURRING TASK',
    )
    MENU = (
        "1) Go Back",
    )
    OPTIONS = {
        "1": 0,
    }
