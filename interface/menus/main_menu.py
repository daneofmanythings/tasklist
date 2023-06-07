from interface.utils import color_text, SOFT_GREEN
from interface.menu import Menu
from interface.menus.manage_tasks import ManageTasks
from interface.menus.manage_tasklists import ManageTasklists

__all__ = ['Main']


class Main(Menu):
    HEADER = (
        color_text('MAIN', *SOFT_GREEN) + ' /',
    )
    MENU = (
        '1) Manage Tasks.',
        '2) Manage Tasklists.',
    )

    OPTIONS = {
        "1": ManageTasks,
        "2": ManageTasklists,
    }
