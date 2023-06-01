from interface.menu import Menu
from interface.create_task import CreateTask
from interface.edit_task import EditTask

__all__ = ["ManageTasks"]


class ManageTasks(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE_TASKS /',
        '',
    )
    MENU = (
        "1) Create task",
        "2) View/Edit tasks",
        "3) Go back",
        '',
    )
    OPTIONS = {
        "1": CreateTask,
        "2": EditTask,
        "3": 0,
    }
