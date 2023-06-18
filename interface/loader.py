from datetime import date
from typing import Optional
from structs.task import Task
import interface.utils as utils
from config.theme import EDITING_HIGHLIGHT, GREYED_OUT, ERROR
from config.globals import MENU_PADDING, PROMPT


class Loader:

    def __init__(self, header, task):

        self.header = header
        self.task = task
        self.help_string = ''

    def display_string(self):
        result = str()
        result += self.header
        result += utils.table_to_string(
            self.task.public_listify(), MENU_PADDING)
        result += self.help_string
        return result

    def run(self) -> Optional[Task]:
        space = " "
        cancel_text = utils.color_text(' [-c]ancel', *GREYED_OUT)
        for attr in self.task.public_vars():
            # Accesses properties correctly
            attr_trimmed = attr.removeprefix('_')
            attr_colored = utils.color_text(attr_trimmed, *EDITING_HIGHLIGHT)
            while True:
                utils.clear_terminal()
                print(self.display_string().replace(
                    f'{space * MENU_PADDING}{attr_trimmed}:', f'{space*MENU_PADDING}{attr_colored}:'))
                print(' ' * MENU_PADDING +
                      f'Enter value for {attr_colored}' + cancel_text)

                response = input(PROMPT)
                if response == '-c':
                    return None

                try:
                    setattr(self.task, attr_trimmed, response)
                    self.help_string = ''
                    break
                except ValueError as ex:
                    self.help_string = utils.color_text(str(ex), *ERROR)
                    continue
        return self.task


def main():
    HEADER = ('test',)
    L = Loader(HEADER, Task())
    t = L.run()
    print(t)
    print(date.today())


if __name__ == "__main__":
    main()
