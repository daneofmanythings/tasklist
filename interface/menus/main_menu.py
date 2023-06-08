from config.theme import MENU_HIGHLIGHT
from interface.utils import color_text
from interface.menu import Menu
from interface.menus.manage_tasks import ManageTasks
from interface.menus.manage_tasklists import ManageTasklists

__all__ = ['Main']


class Main(Menu):
    HEADER = (
        color_text('MAIN', *MENU_HIGHLIGHT) + ' /',
    )
    MENU = (
        '1) Manage Tasks.',
        '2) Manage Tasklists.',
    )

    OPTIONS = {
        "1": ManageTasks,
        "2": ManageTasklists,
    }
