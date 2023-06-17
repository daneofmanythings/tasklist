# from typing import Optional
# from structs.task import Task
import interface.utils as utils
from interface.utils import color_text, hotkey
from config.theme import ERROR, EDITING_HIGHLIGHT, GREYED_OUT
from config.globals import MENU_PADDING, PROMPT


class Editor:

    def __init__(self, header, task):

        self.header = header
        self.task = task
        self.help_string = ''

    def display_string(self, listed_task):
        numbered_task = [hotkey(str(i + 1)) + ' ' + t.removeprefix('_') for i,
                         t in enumerate(listed_task)]
        result = str()
        result += self.header
        result += utils.table_to_string(numbered_task, MENU_PADDING)
        result += self.help_string
        return result

    def run(self):

        listed_task = self.task.public_listify()
        task_attrs = list(self.task.public_vars().keys())

        # TODO : Fix this madness
        while True:
            utils.clear_terminal()
            print(self.display_string(listed_task))
            print(' ' * MENU_PADDING + color_text('[-c]ancel', *GREYED_OUT))
            field_num = input(PROMPT)
            if field_num == '-c':
                return self.task

            try:
                field_to_edit = task_attrs[int(field_num) - 1]
                break
            except:  # DEAL WITH IT
                continue

        field_to_edit_colored = utils.color_text(
            field_to_edit.removeprefix('_'), *EDITING_HIGHLIGHT)

        while True:
            utils.clear_terminal()
            print(self.display_string(listed_task).replace(
                f'] {field_to_edit}:', f'] {field_to_edit_colored}:'))
            print(' ' * MENU_PADDING + color_text('[-c]ancel', *GREYED_OUT))
            print(f'Enter new value for {field_to_edit_colored}')

            value_to_set = input(PROMPT)
            if value_to_set == '-c':
                return self.task
            try:
                setattr(self.task, field_to_edit, value_to_set)
                self.help_string = ''
                break
            except ValueError as e:
                self.help_string = color_text(str(e), *ERROR)

        return self.task
