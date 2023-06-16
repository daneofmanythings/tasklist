from interface import utils
from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state
from interface.utils import color_text, hotkey
from interface.editor import Editor
from structs.registry import save_registry
from config.theme import MENU_HIGHLIGHT
from config.globals import MENU_PADDING, HEADER_PADDING, SAVE_PATH, PROMPT


class ViewAll(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / VIEW TASKS / ' +
        color_text('VIEW ALL', *MENU_HIGHLIGHT),
    )
    MENU = ()
    OPTIONS = {}

    @classmethod
    def display_string(self):
        return utils.table_to_string(self.HEADER, HEADER_PADDING)

    # TODO: clean up this method. separate and validate
    @classmethod
    def run(self, registry):
        tasks = list(registry._tasks)
        tasks.sort()
        tasks_header = [
            f'{hotkey(i + 1)} {t.title}' for i, t in enumerate(tasks)]

        utils.clear_terminal()
        print(self.display_string())
        print(utils.table_to_string(tasks_header, MENU_PADDING))

        response = input(PROMPT)
        task = tasks[int(response) - 1]

        while True:
            utils.clear_terminal()
            print(self.display_string(), end='')
            print(utils.table_to_string(task.listify(), MENU_PADDING))
            print(' ' * MENU_PADDING +
                  f'{hotkey("s")}ave | {hotkey("e")}dit | {hotkey("-c")}ancel')

            will_edit = input(PROMPT)
            if will_edit == 's':
                registry.add_task(task)
                save_registry(registry, SAVE_PATH)
                return MenuReturn(state.PREVIOUS_MENU, None)
            elif will_edit == 'e':
                E = Editor(self.display_string(), task)
                task = E.run()
            elif will_edit == "-c":
                return MenuReturn(state.PREVIOUS_MENU, None)
            else:
                continue
