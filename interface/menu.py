from enum import Enum, auto
from collections import namedtuple


class MenuReturnState(Enum):
    NextMenu = auto()
    ReplaceCurrent = auto()
    PreviousMenu = auto()
    StayCurrent = auto()
    BackToMain = auto()


# Mimicing rust enums
MenuReturn = namedtuple('MenuReturn', 'return_state returned_menu')


# The return 'types' for menus.
# TODO: optionals put into the 'rust enum'?
def NextMenu(menu, task=None, tasklist=None):
    optionals = {
        'task': task,
        'tasklist': tasklist,
    }
    return MenuReturn(MenuReturnState.NextMenu, menu), optionals


def ReplaceCurrent(menu, task=None, tasklist=None):
    optionals = {
        'task': task,
        'tasklist': tasklist,
    }
    return MenuReturn(MenuReturnState.ReplaceCurrent, menu), optionals


def PreviousMenu(menu=None, task=None, tasklist=None):
    optionals = {
        'task': task,
        'tasklist': tasklist,
    }
    return MenuReturn(MenuReturnState.PreviousMenu, None), optionals


def StayCurrent(menu=None, task=None, tasklist=None):
    optionals = {
        'task': task,
        'tasklist': tasklist,
    }
    return MenuReturn(MenuReturnState.StayCurrent, None), optionals


def BackToMain(menu, task=None, tasklist=None):
    optionals = {
        'task': task,
        'tasklist': tasklist,
    }
    return MenuReturn(MenuReturnState.BackToMain, None), optionals
