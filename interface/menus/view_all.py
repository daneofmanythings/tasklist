import interface.utils as utils
from interface.utils import color_text
from interface.editor import Editor
from structs.registry import save_registry, SAVE_PATH
from config.theme import MENU_HIGHLIGHT
from interface.menu import Menu


__all__ = ["ViewAll"]


class ViewAll(Menu):
    HEADER = (
        'MAIN / MANAGE TASKS / VIEW TASKS / ' +
        color_text('VIEW ALL', *MENU_HIGHLIGHT),
    )
    MENU = ()
    OPTIONS = {}

    @classmethod
    def display_string(self):
        return utils.table_to_string(self.HEADER, 10)

    @classmethod
    def run(self, registry):
        tasks = list(registry._ledger)
        tasks.sort()
        tasks_header = [f'{i + 1}) {t.title}' for i, t in enumerate(tasks)]

        utils.clear_terminal()
        print(self.display_string())
        print(utils.table_to_string(tasks_header, 3))

        response = input('Choose a task to edit > ')
        task = tasks[int(response) - 1]

        while True:
            utils.clear_terminal()
            print(self.display_string(), end='')
            print(utils.table_to_string(task.listify(), 3))
            will_edit = input('Save (s) | Edit (e) | Cancel (-c) > ')
            if will_edit == 's':
                registry.add_task(task)
                #####################
                save_registry(registry, SAVE_PATH)
                #####################
                return 0
            elif will_edit == 'e':
                E = Editor(self.display_string(), task)
                task = E.run()
            else:
                return 0
