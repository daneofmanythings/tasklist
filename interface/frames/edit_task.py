from datetime import date
from config.theme import ERROR, HIGHLIGHT, GREYED_OUT, CONFIRMATION
from config.globals import PROMPT, MENU_PADDING
from interface import utils
from interface.returns import PreviousFrame, BackToMain, NextFrame, ReplaceCurrent

__all__ = ['EditTaskSelectField']


class EditTaskSelectField:

    TITLE = "EDIT TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = EditTaskSelectField(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, task):

        self.registry = registry
        self.header_list = header_list
        self.help_string = ''
        self.task = task

    @property
    def task_attributes(self):
        result = list(self.task.public_vars().keys())
        result.append('last_completed')
        return result

    @property
    def sub_menu(self):
        return [
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",
        ]

    @property
    def options(self):
        result = {str(i + 1): ReplaceCurrent(EditTaskReplaceField, task=self.task, field=f)
                  for i, f in enumerate(self.task_attributes)}
        result.update({
            'g': PreviousFrame(),
            'h': BackToMain()
        })
        return result

    def display_string(self):
        menu = [utils.hotkey(str(i + 1)) + ' ' + t.removeprefix('_')
                for i, t in enumerate(self.task.public_listify())]
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(menu)
        result += MENU_PADDING + self.help_string
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)


class EditTaskReplaceField:

    TITLE = "EDIT TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = EditTaskReplaceField(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, task, field):

        self.registry = registry
        self.header_list = header_list
        self.task = task
        self._field = field
        self.help_string = ''

    @property
    def field(self):
        return self._field.removeprefix("_")

    @property
    def field_colored(self):
        return utils.paint_text(self.field, HIGHLIGHT)

    @property
    def task_attributes(self):
        result = list(self.task.public_vars().keys())
        result.append('last_completed')
        return result

    @property
    def sub_menu(self):
        return "Enter new value for {0} " + utils.paint_text("[-c]ancel", GREYED_OUT)

    @property
    def options(self):
        result = {str(i + 1): ReplaceCurrent(EditTaskReplaceField, task=self.task, field=f)
                  for i, f in enumerate(self.task_attributes)}
        result.update({
            'g': PreviousFrame(),
            'h': BackToMain()
        })
        return result

    def display_string(self):
        menu = [t.removeprefix('_')
                for t in self.task.public_listify()]
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(menu)
        result += MENU_PADDING + self.help_string
        result += "\n"
        result += MENU_PADDING + self.sub_menu.format(self.field_colored)
        return result

    def run_instance(self):
        while True:
            utils.clear_terminal()
            print(self.display_string().replace(
                f'{MENU_PADDING}{self.field}:',
                f'{MENU_PADDING}{self.field_colored}:'))

            response = input(PROMPT)

            if response == "-c":
                self.help_string = ''
                return ReplaceCurrent(EditTaskSelectField, task=self.task)

            if self._field == "_title" and response in self.registry._tasks:
                self.help_string = utils.paint_text(
                    "title already in registry", ERROR
                )
                continue

            try:
                setattr(self.task, self.field, response)
                self.help_string = ''

                return ReplaceCurrent(EditTaskSelectField, task=self.task, execute=Saver(self.registry, self.task))
            except ValueError as e:
                self.help_string = utils.paint_text(str(e), ERROR)


class Saver:
    def __init__(self, registry, task):
        self.registry = registry
        self.task = task

    def __call__(self):
        return self.registry.w_task_save(self.task)
