from datetime import date
from config.theme import ERROR, EDITING_HIGHLIGHT, GREYED_OUT, CONFIRMATION
from config.globals import PROMPT, MENU_PADDING
from interface import utils
from interface.menu import PreviousMenu, BackToMain, NextMenu

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

        self.sub_menu = [
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",
        ]

    @property
    def task_attributes(self):
        result = list(self.task.public_vars().keys())
        result.append('last_completetd')
        return result

    @property
    def options(self):
        return {
            'g': PreviousMenu(),
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
            # sub_menu is not in display_string because it changes when editing a field
            print(utils.sub_menu_string(self.sub_menu))

            response = input(PROMPT)

            if response in self.options:
                return self.options[response]

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
                    self.help_string = ''
                    break

                if field_trimmed == "title" and response in self.registry._tasks:
                    self.help_string = utils.paint_text(
                        "title already in registry", ERROR
                    )
                    continue

                try:
                    setattr(self.task, field_trimmed, response)
                    self.help_string = ''

                    # saving registry
                    self.registry.save(task_save=self.task)

                    break
                except ValueError as e:
                    self.help_string = utils.paint_text(str(e), ERROR)
