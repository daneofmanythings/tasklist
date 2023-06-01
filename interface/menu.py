from __future__ import annotations
from interface import utils
from registry import Registry

__all__ = ['Menu']


class Menu:

    HEADER = (
        '',
        ' _______        _    _ _     _   ',
        '|__   __|      | |  | (_)   | |  ',
        '   | | __ _ ___| | _| |_ ___| |_ ',
        '   | |/ _` / __| |/ / | / __| __|',
        '   | | (_| \\__ \\   <| | \\__ \\ |_ ',
        '   |_|\\__,_|___/_|\\_\\_|_|___/\\__|',
    )

    @classmethod
    def show(self):
        padding = '\n' + ' ' * 10
        print(padding.join(s for s in self.HEADER))
        print('\n'.join(s for s in self.MENU))

    @classmethod
    def run(self, registry: Registry) -> Menu:
        with utils.NoCursor():
            utils.clear_terminal()
            self.show()
        return utils.get_menu_input("select from above", self.OPTIONS)
