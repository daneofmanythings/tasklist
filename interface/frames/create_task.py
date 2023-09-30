from interface import utils
from typing import Optional
from config.theme import GREYED_OUT, HIGHLIGHT, ERROR
from config.globals import PROMPT, MENU_PADDING
from structs.task import Task
from interface.returns import ReplaceCurrent, PreviousFrame
from interface.frames.view_task import ViewTask

__all__ = ['CreateTask']


class CreateTask:
    TITLE = "CREATE TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = CreateTask(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.help_string = str()
        self.task = Task()

    def display_string(self, attr):
        if not self.help_string:
            self.help_string = MENU_PADDING + \
                utils.paint_text(Task.help_strings[attr], GREYED_OUT)

        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.task.public_listify())
        result += self.help_string
        return result

    def run_instance(self):
        # TODO: incorporate get_user_inputs into the options paradigm
        self.task = self.get_user_inputs(self.task)

        if self.task is None:
            return PreviousFrame()

        return ReplaceCurrent(ViewTask, task=self.task, execute=Saver(self.registry, self.task))

    def get_user_inputs(self, task):
        cancel_text = utils.paint_text(' [-c]ancel', GREYED_OUT)
        for attr in task.public_vars():
            # Accesses properties correctly
            attr_trimmed = attr.removeprefix('_')
            attr_painted = utils.paint_text(attr_trimmed, HIGHLIGHT)

            while True:
                utils.clear_terminal()
                print(self.display_string(attr_trimmed).replace(
                    f'{MENU_PADDING}{attr_trimmed}:',
                    f'{MENU_PADDING}{attr_painted}:'))

                print(MENU_PADDING +
                      f'Enter value for {attr_painted}' + cancel_text)

                response = input(PROMPT)
                if response == '-c':
                    return None

                if attr_trimmed == "title" and response in self.registry._tasks:
                    self.help_string = MENU_PADDING + utils.paint_text(
                        "title already exists in registry", ERROR
                    )
                    continue

                try:
                    setattr(task, attr_trimmed, response)
                    self.help_string = ''
                    break
                except ValueError as ex:
                    self.help_string = MENU_PADDING + \
                        utils.paint_text(str(ex), ERROR)
                    continue
        return task


class Saver:
    def __init__(self, registry, task):
        self.registry = registry
        self.task = task

    def __call__(self):
        return self.registry.w_task_save(self.task)
