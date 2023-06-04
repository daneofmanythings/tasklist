from typing import Optional
from tasks import Task
import interface.utils as utils


class Editor:

    def __init__(self, header, task):

        self.header = header
        self.task = task
        self.help_string = ''

    def display_string(self):
        result = str()
        result += self.header
        result += utils.table_to_string(self.task.listify(), 4)
        result += self.help_string
        return result

    def run(self):

        while True:
            utils.clear_terminal()
            print(self.display_string())
            field_to_edit = input('Enter the name of the field to edit > ')
            if field_to_edit in vars(self.task):
                self.help_string = ''
                break
            self.help_string = '\'-c\' to cancel'

        while True:
            utils.clear_terminal()
            print(self.display_string())
            value_to_set = input(f'Enter new value for {field_to_edit} > ')
            try:
                setattr(self.task, field_to_edit, value_to_set)
                self.help_string = ''
                break
            except TypeError as e:
                self.help_string = str(e)

        return self.task
