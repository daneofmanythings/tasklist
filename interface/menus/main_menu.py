from interface.menu import Menu
from interface.menus.manage_tasks.manage_tasks import ManageTasks
from interface.menus.manage_tasklists.manage_tasklists import ManageTasklists

__all__ = ['Main']


class Main(Menu):
    HEADER = (
        'MAIN /',
    )
    MENU = (
        '1) Manage Tasks.',
        '2) Manage Tasklists.',
    )

    OPTIONS = {
        "1": ManageTasks,
        "2": ManageTasklists,
    }
