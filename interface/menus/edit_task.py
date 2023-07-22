from datetime import date
from copy import copy
from config.theme import ERROR, EDITING_HIGHLIGHT, GREYED_OUT, CONFIRMATION
from config.globals import PROMPT, MENU_PADDING
from interface import utils
from interface.menu import PreviousMenu, BackToMain

__all__ = ['EditTask']


class EditTask:

    TITLE = "EDIT TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = EditTask(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, task):

        self.registry = registry
        self.header_list = header_list
        self.help_string = ''
        self.task = task
        self.pre_edit_task = copy(task)
        self.task_attributes = list(self.task.public_vars().keys())

        self.sub_menu = [
            f"{utils.hotkey('f')}inished",
            f"{utils.hotkey('m')}ark completion date",
            f"{utils.hotkey('c')}ancel edits",
            f"{utils.hotkey('h')}ome",
        ]

    @property
    def options(self):
        return {
            'f': PreviousMenu(task=self.task),
            'c': PreviousMenu(task=self.pre_edit_task),
            'h': BackToMain()
        }

    def display_string(self):
        menu = [utils.hotkey(str(i + 1)) + ' ' + t.removeprefix('_')
                for i, t in enumerate(self.task.public_listify())]
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(menu)
        result += MENU_PADDING + self.help_string
        return result

    # TODO : Fix this madness maybe. its a little better.
    def run_instance(self):

        while True:
            utils.clear_terminal()
            print(self.display_string())
            print(utils.sub_menu_string(self.sub_menu))
            response = input(PROMPT)

            if response in self.options:
                return self.options[response]

            # TODO: FIX THIS IT IS ANNOYING. Try to incorperate it into options
            if response == 't':
                if self.task.last_completed is None:
                    self.task.last_completed = date.today()
                    self.help_string = utils.paint_text(
                        "last completed set to today", CONFIRMATION)
                    continue
                else:
                    self.task.last_completed = None
                    self.help_string = utils.paint_text(
                        "last completed removed", CONFIRMATION)
                    continue

            try:
                field = self.task_attributes[int(response) - 1]
            except (IndexError, TypeError, ValueError):
                continue

            field_trimmed = field.removeprefix('_')
            field_colored = utils.paint_text(field_trimmed, EDITING_HIGHLIGHT)

            field_prompt = MENU_PADDING + \
                "Enter new value for {0} " + \
                utils.paint_text("[-c]ancel", GREYED_OUT)

            while True:
                utils.clear_terminal()
                print(self.display_string().replace(
                    f'] {field}:',
                    f'] {field_colored}:'))

                print(field_prompt.format(field_colored))

                response = input(PROMPT)

                if response == "-c":
                    break

                try:
                    setattr(self.task, field_trimmed, response)
                    self.help_string = ''
                    break
                except ValueError as e:
                    self.help_string = utils.paint_text(str(e), ERROR)
