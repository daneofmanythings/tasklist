from config.theme import MENU_HIGHLIGHT
from interface.utils import color_text
from interface.menu import Menu
from interface.loader import Loader
from interface.editor import Editor
import interface.utils as utils
from structs.tasks import Task
from structs.registry import save_registry, SAVE_PATH

__all__ = ["SingleTask"]


class SingleTask(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / CREATE TASK / ' +
        color_text('SINGLE TASK', *MENU_HIGHLIGHT),
    )
    MENU = ()
    OPTIONS = {}

    @classmethod
    def display_string(self):
        return utils.table_to_string(SingleTask.HEADER, 10)

    @classmethod
    def run(self, registry):
        t = Task()
        L = Loader(utils.table_to_string(SingleTask.HEADER, 10), t)
        result = L.run()
        if result is None:
            return 0
        while True:
            utils.clear_terminal()
            print(self.display_string(), end='')
            print(utils.table_to_string(result.listify(), 3))
            will_edit = input('Save (s) | Edit (e) | Cancel (-c) > ')
            if will_edit == 's':
                registry.add_task(result)
                #####################
                save_registry(registry, SAVE_PATH)
                #####################
                return 0
            elif will_edit == 'e':
                E = Editor(self.display_string(), result)
                result = E.run()
            else:
                return 0
