from enum import Enum, auto
from collections import namedtuple
from structs.registry import Registry
import interface.utils as utils

__all__ = ['Menu', 'MenuReturnState', 'MenuReturn']


class MenuReturnState(Enum):
    NEXT_MENU = auto()
    PREVIOUS_MENU = auto()
    STAY_CURRENT = auto()
    REPLACE_CURRENT = auto()
    BACK_TO_MAIN = auto()


MenuReturn = namedtuple('MenuReturn', 'return_state returned_menu')


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
        result += utils.table_to_string(self.HEADER, 10)
        result += utils.table_to_string(self.MENU, 3)
        return result

    @classmethod
    def run(self, registry: Registry) -> MenuReturn:
        with utils.NoCursor():
            utils.clear_terminal()
            print(self.display_string())
        return utils.get_menu_input("", self.OPTIONS)
