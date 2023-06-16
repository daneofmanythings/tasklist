from interface.utils import color_text, hotkey
from interface.menus.create_task import CreateTask
from interface.menus.view_edit_tasks import ViewEditTasks
from interface.menu import MenuReturnState as state
from interface.menu import Menu, MenuReturn
from config.theme import MENU_HIGHLIGHT


class ManageTasks(Menu):
    HEADER = (
        'MAIN / ' + color_text('MANAGE_TASKS', *MENU_HIGHLIGHT) + ' /',
    )
    MENU = (
        hotkey('1') + " Create task",
        hotkey('2') + " View/Edit tasks",
        hotkey('3') + " Go back",
    )
    OPTIONS = {
        "1": MenuReturn(state.NEXT_MENU, CreateTask),
        "2": MenuReturn(state.NEXT_MENU, ViewEditTasks),
        "3": MenuReturn(state.PREVIOUS_MENU, None)
    }
