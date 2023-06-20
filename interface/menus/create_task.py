from interface import utils
from interface.utils import color_text, hotkey
from interface.loader import Loader
from interface.editor import Editor
from config.theme import CURRENT_MENU
from config.globals import HEADER_OFFSET, MENU_OFFSET, SAVE_PATH, PROMPT, MENU_PADDING
from structs.task import Task
from structs.registry import save_registry
from interface.menu import MenuReturnState as state
from interface.menu import Menu, MenuReturn


class CreateTask(Menu):
    TITLE = "CREATE TASK"

    HEADER = (
        'MAIN / MANAGE TASKS / ' +
        color_text('CREATE TASK', CURRENT_MENU),
    )
    MENU = ()
    OPTIONS = {}

    @classmethod
    def display_string(self):
        return utils.table_to_string(self.HEADER, HEADER_OFFSET)

    @classmethod
    def run(self, registry):
        T = Task()
        L = Loader(utils.table_to_string(self.HEADER, HEADER_OFFSET), T)

        result = L.run()

        if result is None:
            return MenuReturn(state.PREVIOUS_MENU, None)

        while True:
            utils.clear_terminal()
            print(self.display_string(), end='')
            print(utils.table_to_string(result.public_listify(), MENU_OFFSET))
            print(MENU_PADDING +
                  f"{hotkey('s')}ave | {hotkey('e')}dit | {hotkey('-c')}ancel")

            will_edit = input(PROMPT)
            if will_edit == 's':
                registry.add_task(result)
                save_registry(registry, SAVE_PATH)
                return MenuReturn(state.PREVIOUS_MENU, None)
            elif will_edit == 'e':
                E = Editor(self.display_string(), result)
                result = E.run()
            elif will_edit == '-c':
                return MenuReturn(state.PREVIOUS_MENU, None)
            else:
                continue
