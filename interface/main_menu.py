from interface import utils
import shutil
from interface.menu import Menu
from interface.create_task import CreateTask
from interface.edit_task import EditTask
from interface.show_all import ViewAllTasks
from registry import Registry

__all__ = ['Main']


class Main(Menu):
    HEADER = (
        '',
        ' _______        _    _ _     _   ',
        '|__   __|      | |  | (_)   | |  ',
        '   | | __ _ ___| | _| |_ ___| |_ ',
        '   | |/ _` / __| |/ / | / __| __|',
        '   | | (_| \\__ \\   <| | \\__ \\ |_ ',
        '   |_|\\__,_|___/_|\\_\\_|_|___/\\__|',
    )

    MENU = (
        '',
        '1) Create new task.',
        '2) Edit existing task.',
        '3) View all tasks.'
    )

    OPTIONS = {
        "1": CreateTask,
        "2": EditTask,
        "3": ViewAllTasks,
    }

    @classmethod
    def show(self):
        x, y = shutil.get_terminal_size()
        padding = '\n' + ' ' * (y - 14)
        print(padding.join(s for s in self.HEADER))
        print('\n'.join(s for s in self.MENU))

    @classmethod
    def run(self, registry: Registry) -> Menu:
        self.show()
        return utils.get_menu_input("select from above", self.OPTIONS)
