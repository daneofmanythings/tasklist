from datetime import date
from typing import Optional
from structs.task import Task
import interface.utils as utils
from config.theme import EDITING_HIGHLIGHT, GREYED_OUT, ERROR
from config.globals import MENU_OFFSET, PROMPT, MENU_PADDING


class Loader:

    def __init__(self, header, task):

        self.header = header
        self.task = task
        self.help_string = ''

    def display_string(self):
        result = str()
        result += "\n"
        result += self.header
        result += "\n"
        result += utils.table_to_string(
            self.task.public_listify(), MENU_OFFSET)
        result += self.help_string
        return result

    def run(self) -> Optional[Task]:
        cancel_text = utils.paint_text(' [-c]ancel', GREYED_OUT)
        for attr in self.task.public_vars():
            # Accesses properties correctly
            attr_trimmed = attr.removeprefix('_')
            attr_colored = utils.paint_text(attr_trimmed, EDITING_HIGHLIGHT)
            while True:
                utils.clear_terminal()
                print(self.display_string().replace(
                    f'{MENU_PADDING}{attr_trimmed}:', f'{MENU_PADDING}{attr_colored}:'))
                print(MENU_PADDING +
                      f'Enter value for {attr_colored}' + cancel_text)

                response = input(PROMPT)
                if response == '-c':
                    return None

                try:
                    setattr(self.task, attr_trimmed, response)
                    self.help_string = ''
                    break
                except ValueError as ex:
                    self.help_string = utils.paint_text(str(ex), ERROR)
                    continue
        return self.task
