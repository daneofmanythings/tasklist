from interface import utils
from typing import Optional
from config.theme import GREYED_OUT, EDITING_HIGHLIGHT, ERROR
from config.globals import PROMPT, MENU_PADDING
from structs.task import Task
from interface.menu import ReplaceCurrent, PreviousMenu
from interface.menus.view_task import ViewTask

__all__ = ['CreateTask']


class CreateTask:
    TITLE = "CREATE TASK"

    @classmethod
    def run(self, registry, header_list, task, tasklist):
        M = CreateTask(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.help_string = str()
        self.task = None

    def display_string(self, task):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(task.public_listify())
        result += self.help_string
        return result

    def run_instance(self):
        blank_task = Task()

        self.task = self.task_creation(blank_task)

        if self.task is None:
            return PreviousMenu()

        return ReplaceCurrent(ViewTask, task=self.task)

    def task_creation(self, task) -> Optional[Task]:
        cancel_text = utils.paint_text(' [-c]ancel', GREYED_OUT)
        for attr in task.public_vars():
            # Accesses properties correctly
            attr_trimmed = attr.removeprefix('_')
            attr_painted = utils.paint_text(attr_trimmed, EDITING_HIGHLIGHT)

            while True:
                utils.clear_terminal()
                print(self.display_string(task).replace(
                    f'{MENU_PADDING}{attr_trimmed}:',
                    f'{MENU_PADDING}{attr_painted}:'))

                print(MENU_PADDING +
                      f'Enter value for {attr_painted}' + cancel_text)

                response = input(PROMPT)
                if response == '-c':
                    return None

                try:
                    setattr(task, attr_trimmed, response)
                    self.help_string = ''
                    break
                except ValueError as ex:
                    self.help_string = MENU_PADDING + \
                        utils.paint_text(str(ex), ERROR)
                    continue
        return task
