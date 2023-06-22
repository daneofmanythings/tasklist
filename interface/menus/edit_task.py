from copy import copy
from config.theme import ERROR, EDITING_HIGHLIGHT
from config.globals import PROMPT, MENU_PADDING
from interface import utils
from interface.menu import PreviousMenu

__all__ = ['EditTask']


class EditTask:

    TITLE = "EDIT TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = EditTask(registry, header_list, optionals['task'])
        return M.run_instance()

    def __init__(self, registry, header_list, task):

        self.registry = registry
        self.header_list = header_list
        self.help_string = ''
        self.task = task
        self.pre_edit_task = copy(task)
        self.task_attributes = list(self.task.public_vars().keys())

        self.sub_menu = [
            f"{utils.hotkey('-f')}inished",
            f"{utils.hotkey('-c')}ancel edits",
        ]

    @property
    def options(self):
        return {
            '-f': PreviousMenu(task=self.task),
            '-c': PreviousMenu(task=self.pre_edit_task),
        }

    # TODO: this is displaying weirdly. fix it
    def display_string(self):
        menu = [utils.hotkey(str(i + 1)) + ' ' + t.removeprefix('_')
                for i, t in enumerate(self.task.public_listify())]
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(menu)
        result += "\n"
        result += self.help_string
        result += utils.sub_menu_string(self.sub_menu)
        return result

    # TODO : Fix this madness maybe. its a little better.
    def run_instance(self):

        while True:
            utils.clear_terminal()
            print(self.display_string())
            response = input(PROMPT)

            if response in self.options:
                return self.options[response]

            try:
                field = self.task_attributes[int(response) - 1]
            except (IndexError, TypeError, ValueError):
                continue

            field_trimmed = field.removeprefix('_')
            field_colored = utils.paint_text(field_trimmed, EDITING_HIGHLIGHT)

            while True:
                utils.clear_terminal()
                print(self.display_string().replace(
                    f'] {field}:',
                    f'] {field_colored}:'))

                print(MENU_PADDING + f'Enter new value for {field_colored}')

                response = input(PROMPT)

                if response in self.options:
                    return self.options[response]

                try:
                    setattr(self.task, field_trimmed, response)
                    self.help_string = ''
                    break
                except ValueError as e:
                    self.help_string = utils.paint_text(str(e), ERROR)
