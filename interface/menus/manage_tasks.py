from interface.utils import color_text, SOFT_GREEN
from interface.menu import Menu
from interface.menus.create_task import CreateTask
from interface.menus.view_tasks import ViewTasks

__all__ = ["ManageTasks"]


class ManageTasks(Menu):
    HEADER = (
        'MAIN / ' + color_text('MANAGE_TASKS', *SOFT_GREEN) + ' /',
    )
    MENU = (
        "1) Create task",
        "2) View/Edit tasks",
        "3) Go back",
    )
    OPTIONS = {
        "1": CreateTask,
        "2": ViewTasks,
        "3": 0,
    }
