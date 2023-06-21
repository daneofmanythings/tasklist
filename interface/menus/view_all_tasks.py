from collections import ChainMap as cmap
from interface import utils
from interface.menu import PreviousMenu
from interface.utils import paint_text, hotkey
from interface.editor import Editor
from structs.registry import save_registry
from config.theme import CURRENT_MENU
from config.globals import MENU_OFFSET, HEADER_OFFSET, SAVE_PATH, PROMPT


__all__ = ['ViewAllTasks']


class ViewAllTasks:

    TITLE = "View All Tasks"

    @classmethod
    def run(self, registry, header_list):
        M = ViewAllTasks(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list

        tasks = list(self.registry.tasks)
        tasks.sort()
        self.task_menu = [f"{hotkey(i + 1)} {t.title}"
                          for i, t in enumerate(tasks)]

        self.submenu = [
            f"{utils.hotkey('g')}o back",
        ]
        self.options = dict(cmap(self.task_menu, self.submenu)).values()

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.task_menu)
        result += "\n"
        result += utils.submenu_string()
        return result

    # TODO: clean up this method. separate and validate
    def run_instance(self):

        while True:
            utils.clear_terminal()
            print(self.display_string())

            response = input(PROMPT)
            # the following check should be done the other direction with a try
            if response in [str(i + 1) for i in range(len(tasks_header))]:
                task = tasks[int(response) - 1]
            elif response == 'g':
                return PreviousMenu()
            else:
                continue

            while True:
                utils.clear_terminal()
                print(self.display_string(), end='')
                print(utils.table_to_string(task.listify(), MENU_OFFSET))
                print(' ' * MENU_OFFSET +
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
