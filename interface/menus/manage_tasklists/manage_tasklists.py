from interface.menu import Menu

__all__ = ["ManageTasklists"]


class ManageTasklists(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE_TASKLISTS /',
        '',
    )
    MENU = (
        "1) Generate tasklist",
        "2) View/Edit taskslists",
        "3) Go back",
        '',
    )
    OPTIONS = {
        "1": CreateTask,
        "2": EditTask,
        "3": 0,
    }
