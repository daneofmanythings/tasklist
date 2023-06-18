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
        tasks = list(registry._tasks.values())
        tasks.sort()
        tasks_header = [
            f'{hotkey(i + 1)} {t.title}' for i, t in enumerate(tasks)]

        while True:
            utils.clear_terminal()
            print(self.display_string())
            print(utils.table_to_string(tasks_header,
                  MENU_PADDING)[1:])  # removing a '\n'
            print(' ' * MENU_PADDING + f"{hotkey('g')}o back")

            response = input(PROMPT)
            # the following check should be done the other direction with a try
            if response in [str(i + 1) for i in range(len(tasks_header))]:
                task = tasks[int(response) - 1]
            elif response == 'g':
                return MenuReturn(state.PREVIOUS_MENU, None)
            else:
                continue

            while True:
                utils.clear_terminal()
                print(self.display_string(), end='')
                print(utils.table_to_string(task.listify(), MENU_PADDING))
                print(' ' * MENU_PADDING +
                      f'{hotkey("s")}ave | {hotkey("e")}dit | {hotkey("g")}o back')

                will_edit = input(PROMPT)
                if will_edit == 's':
                    registry.add_task(task)
                    save_registry(registry, SAVE_PATH)
                    break
                elif will_edit == 'e':
                    E = Editor(self.display_string(), task)
                    task = E.run()
                elif will_edit == "g":
                    break
                else:
                    continue
