from typing import Optional
from tasks import Task
import interface.utils as utils


class Loader:

    def __init__(self, header, task):

        self.header = header
        self.task = task

    def display_info(self):
        return self.header + '\n' + str(self.task)

    def run(self) -> Optional[Task]:
        for attr in vars(self.task):
            if attr.startswith('_'):
                continue
            utils.clear_terminal()
            print(self.display_info())
            response = input(f'Enter value for {attr} > ')
            if response == '-c':
                return
            setattr(self.task, attr, response)
        return self.task


def main():
    header = 'Header'
    field_list = ['test', 'pls']
    loader = Loader(0, header, field_list)
    print(loader.display_info())


if __name__ == "__main__":
    main()
