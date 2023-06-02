from interface.menu import Menu
from interface.menus.manage_tasks.create_tasks.create_task import CreateTask
from interface.menus.manage_tasks.view_tasks.view_tasks import ViewTasks

__all__ = ["ManageTasks"]


class ManageTasks(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE_TASKS /',
    )
    MENU = (
        '',
        "1) Create task",
        "2) View/Edit tasks",
        "3) Go back",
        '',
    )
    OPTIONS = {
        "1": CreateTask,
        "2": ViewTasks,
        "3": 0,
    }
