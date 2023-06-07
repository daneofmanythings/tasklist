from interface.utils import color_text, SOFT_GREEN
from interface.menu import Menu
from interface.menus.single_task import SingleTask
from interface.menus.repeat_task import RepeatTask
from interface.menus.recurring_task import RecurringTask

__all__ = ["CreateTask"]


class CreateTask(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / ' +
        color_text('CREATE TASK', *SOFT_GREEN) + ' /',
    )
    MENU = (
        "1) Single Task",
        "2) Repeat Task",
        "3) Recurring Task",
        "4) Go Back",
        "5) Main Menu",
    )
    OPTIONS = {
        "1": SingleTask,
        "2": RepeatTask,
        "3": RecurringTask,
        "4": 0,
        "5": -1,
    }
