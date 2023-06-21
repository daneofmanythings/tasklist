# from typing import Optional
# from structs.task import Task
import interface.utils as utils
from interface.utils import paint_text, hotkey
from config.theme import ERROR, EDITING_HIGHLIGHT, GREYED_OUT
from config.globals import MENU_OFFSET, PROMPT


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
        result += utils.table_to_string(numbered_task, MENU_OFFSET)
        result += self.help_string
        return result

    def run(self):

        task_attrs = list(self.task.public_vars().keys())

        # TODO : Fix this madness
        while True:
            listed_task = self.task.public_listify()
            utils.clear_terminal()
            print(self.display_string(listed_task))
            print(' ' * MENU_OFFSET + f"{hotkey('g')}o back")
            field_num = input(PROMPT)
            if field_num == 'g':
                return self.task

            try:
                field_to_edit = task_attrs[int(field_num) - 1]
            except:  # DEAL WITH IT
                continue

            field_to_edit_trimmed = field_to_edit.removeprefix('_')
            field_to_edit_colored = utils.paint_text(
                field_to_edit_trimmed, EDITING_HIGHLIGHT)

            while True:
                utils.clear_terminal()
                print(self.display_string(listed_task).replace(
                    f'] {field_to_edit}:', f'] {field_to_edit_colored}:'))
                print(' ' * MENU_OFFSET +
                      paint_text('[-g]o back', GREYED_OUT))
                print(' ' * MENU_OFFSET +
                      f'Enter new value for {field_to_edit_colored}')

                value_to_set = input(PROMPT)
                if value_to_set == '-g':
                    break
                try:
                    setattr(self.task, field_to_edit_trimmed, value_to_set)
                    self.help_string = ''
                    break
                except ValueError as e:
                    self.help_string = paint_text(str(e), ERROR)

        return self.task
