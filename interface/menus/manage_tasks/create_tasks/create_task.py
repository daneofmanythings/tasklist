from interface.menu import Menu
from interface.menus.manage_tasks.create_tasks.single_task.single_task import SingleTask

__all__ = ["CreateTask"]


class CreateTask(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / CREATE TASK',
    )
    MENU = (
        "1) Single Task",
        "2) Repeat Task",
        "3) Recurring Task",
    )
    OPTIONS = {
        "1": SingleTask,
    }
