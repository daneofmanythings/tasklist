from interface.menu import Menu

__all__ = ["ManageTasklists"]


class ManageTasklists(Menu):
    HEADER = (
        'MAIN / MANAGE_TASKLISTS /',
    )
    MENU = (
        "1) Go Back",
    )
    OPTIONS = {
        "1": 0,
    }
