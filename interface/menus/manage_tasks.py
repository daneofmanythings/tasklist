from interface.utils import color_text
from interface.menus.create_task import CreateTask
from interface.menus.view_tasks import ViewTasks
from interface.menu import MenuReturnState as state
from interface.menu import Menu, MenuReturn
from config.theme import MENU_HIGHLIGHT


class ManageTasks(Menu):
    HEADER = (
        'MAIN / ' + color_text('MANAGE_TASKS', *MENU_HIGHLIGHT) + ' /',
    )
    MENU = (
        "1) Create task",
        "2) View/Edit tasks",
        "3) Go back",
    )
    OPTIONS = {
        "1": MenuReturn(state.NEXT_MENU, CreateTask),
        "2": MenuReturn(state.NEXT_MENU, ViewTasks),
        "3": MenuReturn(state.PREVIOUS_MENU, None)
    }
