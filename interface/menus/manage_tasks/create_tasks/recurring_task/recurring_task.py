from interface.menu import Menu

__all__ = ["RecurringTask"]


class RecurringTask(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE TASKS / CREATE TASK / RECURRING TASK',
    )
    MENU = (
        '',
        "1) Single Task",
        "2) Repeat Task",
        "3) Recurring Task",
        '',
    )
    OPTIONS = {
        "1": 0,
    }
