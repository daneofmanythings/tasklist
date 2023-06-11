from interface import utils
from interface.utils import color_text
from interface.loader import Loader
from interface.editor import Editor
from config.theme import MENU_HIGHLIGHT
from structs.tasks import Task
from structs.registry import save_registry, SAVE_PATH
from interface.menu import MenuReturnState as state
from interface.menu import Menu, MenuReturn


__all__ = ["CreateTask"]


class CreateTask(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / ' +
        color_text('CREATE TASK', *MENU_HIGHLIGHT),
    )
    MENU = ()
    OPTIONS = {}

    @classmethod
    def display_string(self):
        return utils.table_to_string(self.HEADER, 10)

    @classmethod
    def run(self, registry):
        t = Task()
        L = Loader(utils.table_to_string(self.HEADER, 10), t)

        result = L.run()

        if result is None:
            return MenuReturn(state.PREVIOUS_MENU, None)

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
                return MenuReturn(state.PREVIOUS_MENU, None)
            elif will_edit == 'e':
                E = Editor(self.display_string(), result)
                result = E.run()
            else:
                return MenuReturn(state.PREVIOUS_MENU, None)
