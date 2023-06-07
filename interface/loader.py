from datetime import date
from typing import Optional
from structs.tasks import Task
import interface.utils as utils


class Loader:

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

    def run(self) -> Optional[Task]:
        for attr in vars(self.task):
            while True:
                utils.clear_terminal()
                print(self.display_string())
                response = input(f'Enter value for {attr} > ')
                if response == '-c':
                    return
                try:
                    setattr(self.task, attr, response)
                    self.help_string = ''
                    break
                except ValueError as ex:
                    self.help_string = str(ex)
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
