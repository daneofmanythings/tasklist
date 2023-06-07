from __future__ import annotations
from interface import utils
from structs.registry import Registry

__all__ = ['Menu']


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
    def run(self, registry: Registry) -> Menu:
        with utils.NoCursor():
            utils.clear_terminal()
            print(self.display_string())
        return utils.get_menu_input("", self.OPTIONS)
