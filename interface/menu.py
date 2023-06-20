from enum import Enum, auto
from collections import namedtuple
from structs.registry import Registry
import interface.utils as utils
from config.globals import HEADER_OFFSET, MENU_OFFSET


class MenuReturnState(Enum):
    NEXT_MENU = auto()
    REPLACE_CURRENT = auto()
    PREVIOUS_MENU = auto()
    STAY_CURRENT = auto()
    BACK_TO_MAIN = auto()


# Mimicing rust enums
MenuReturn = namedtuple('MenuReturn', 'return_state returned_menu')


def NextMenu(menu):
    return MenuReturn(MenuReturnState.NEXT_MENU, menu)


def ReplaceCurrent(menu):
    return MenuReturn(MenuReturnState.REPLACE_CURRENT, menu)


def PreviousMenu():
    return MenuReturn(MenuReturnState.PREVIOUS_MENU, None)


def StayCurrent():
    return MenuReturn(MenuReturnState.STAY_CURRENT, None)


def BackToMain():
    return MenuReturn(MenuReturnState.BACK_TO_MAIN, None)


def work_in_progress(cls):
    cls.HEADER = (f"{cls.__name__} / (WIP)",)
    cls.MENU = ("[1] Go Back",)
    cls.OPTIONS = {"1": MenuReturn(MenuReturnState.PREVIOUS_MENU, None)}
    return cls


class Menu:

    HEADER = (
        ' _______        _    _ _     _   ',
        '|__   __|      | |  | (_)   | |  ',
        '   | | __ _ ___| | _| |_ ___| |_ ',
        '   | |/ _` / __| |/ / | / __| __|',
        '   | | (_| \\__ \\   <| | \\__ \\ |_ ',
        '   |_|\\__,_|___/_|\\_\\_|_|___/\\__|',
    )

    MENU = (
    )

    @classmethod
    def display_string(self):
        result = str()
        result += utils.table_to_string(self.HEADER, HEADER_OFFSET)
        result += utils.table_to_string(self.MENU, MENU_OFFSET)
        return result

    @classmethod
    def run(self, registry: Registry) -> MenuReturn:
        with utils.NoCursor():
            utils.clear_terminal()
            print(self.display_string())
        return utils.get_menu_input("", self.OPTIONS)
