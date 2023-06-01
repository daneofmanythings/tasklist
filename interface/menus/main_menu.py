from interface.menu import Menu
from interface.manage_tasks import ManageTasks
from interface.manage_tasklists import ManageTasklists

__all__ = ['Main']


class Main(Menu):
    HEADER = (
        '',
        'MAIN /',
        '',
    )
    MENU = (
        '1) Manage Tasks.',
        '2) Manage Tasklists.',
        '',
    )

    OPTIONS = {
        "1": ManageTasks,
        "2": ManageTasklists,
    }
