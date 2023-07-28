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
def NextMenu(menu, **optionals):
    return MenuReturn(MenuReturnState.NextMenu, menu), optionals


def ReplaceCurrent(menu, **optionals):
    return MenuReturn(MenuReturnState.ReplaceCurrent, menu), optionals


def PreviousMenu(**optionals):
    return MenuReturn(MenuReturnState.PreviousMenu, None), optionals


def StayCurrent(**optionals):
    return MenuReturn(MenuReturnState.StayCurrent, None), optionals


def BackToMain(**optionals):
    return MenuReturn(MenuReturnState.BackToMain, None), optionals
