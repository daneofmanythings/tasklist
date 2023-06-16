from enum import Enum, auto
from collections import namedtuple
from structs.registry import Registry
import interface.utils as utils
from config.globals import HEADER_PADDING, MENU_PADDING


class MenuReturnState(Enum):
    NEXT_MENU = auto()
    PREVIOUS_MENU = auto()
    STAY_CURRENT = auto()
    REPLACE_CURRENT = auto()
    BACK_TO_MAIN = auto()


MenuReturn = namedtuple('MenuReturn', 'return_state returned_menu')


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
        result += utils.table_to_string(self.HEADER, HEADER_PADDING)
        result += utils.table_to_string(self.MENU, MENU_PADDING)
        return result

    @classmethod
    def run(self, registry: Registry) -> MenuReturn:
        with utils.NoCursor():
            utils.clear_terminal()
            print(self.display_string())
        return utils.get_menu_input("", self.OPTIONS)
