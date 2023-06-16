from datetime import date
from typing import Optional
from structs.tasks import Task
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
        result += utils.table_to_string(self.task.listify(), MENU_PADDING)
        result += self.help_string
        return result

    def run(self) -> Optional[Task]:
        abort_prompt = utils.color_text(' [-c]ancel', *GREYED_OUT)
        for attr in vars(self.task):
            attr = attr.replace('_', '')  # Accesses properties correctly
            attr_colored = utils.color_text(attr, *EDITING_HIGHLIGHT)
            while True:
                utils.clear_terminal()
                print(self.display_string().replace(
                    f'   {attr}:', f'   {attr_colored}:'))
                print(' ' * MENU_PADDING +
                      f'Enter value for {attr_colored}' + abort_prompt)

                response = input(PROMPT)
                if response == '-c':
                    return None

                try:
                    setattr(self.task, attr, response)
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
