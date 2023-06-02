from interface.menu import Menu

__all__ = ["SingleTask"]


class SingleTask(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE TASKS / CREATE TASK / SINGLE TASK',
    )
    MENU = (
        '',
        '(type \'-q\' to cancel)'
        '',
    )
    OPTIONS = {
        "-q": 0,
    }

    def __init__(self, registry):
        pass
