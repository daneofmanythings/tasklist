# from typing import Optional
# from structs.tasks import Task
import interface.utils as utils
from interface.utils import color_text
from config.theme import ERROR_HINT, EDITING_HIGHLIGHT


class Editor:

    def __init__(self, header, task):

        self.header = header
        self.task = task
        self.help_string = ''

    def display_string(self):
        task_list = self.task.listify()
        result = str()
        result += self.header
        result += utils.table_to_string(task_list, 3)
        result += self.help_string
        return result

    def run(self):

        while True:
            utils.clear_terminal()
            print(self.display_string())
            field_to_edit = input('Enter the name of the field to edit > ')
            # replacing '_' to correctly use properties
            if field_to_edit in [s.replace('_', '') for s in vars(self.task)]:
                self.help_string = ''
                break
            self.help_string = color_text('\'-c\' to cancel', *ERROR_HINT)

        field_to_edit_colored = utils.color_text(
            field_to_edit, *EDITING_HIGHLIGHT)

        while True:
            utils.clear_terminal()
            print(self.display_string().replace(
                f'   {field_to_edit}:', f'   {field_to_edit_colored}:'))
            value_to_set = input(
                f'Enter new value for {field_to_edit_colored} > ')
            try:
                setattr(self.task, field_to_edit, value_to_set)
                self.help_string = ''
                break
            except ValueError as e:
                self.help_string = color_text(str(e), *ERROR_HINT)

        return self.task
