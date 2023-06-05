from interface.menu import Menu


__all__ = ["ViewTasks"]


class ViewTasks(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE TASKS / VIEW TASKS',
    )
    MENU = (
        '',
        "1) Go Back",
        '',
    )
    OPTIONS = {
        "1": 0,
    }
