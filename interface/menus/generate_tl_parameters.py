from datetime import datetime
from typing import Optional
from interface import utils
from structs.tasklist_parameters import TasklistParameters
from interface.menus.generate_tasklist import GenerateTasklist
from interface.menu import ReplaceCurrent, PreviousMenu
from config.theme import GREYED_OUT, EDITING_HIGHLIGHT, ERROR
from config.globals import MENU_PADDING, PROMPT


class GenerateTasklistParameters:

    TITLE = "GENERATE TASKLIST > PARAMETERS"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = GenerateTasklistParameters(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.help_string = ''
        self.parameters = TasklistParameters()

    def display_string(self, parameters):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(parameters.public_listify())
        result += self.help_string
        return result

    def run_instance(self):
        self.parameters = self.parameter_creation(self.parameters)

        if self.parameters is None:
            return PreviousMenu()

        return ReplaceCurrent(GenerateTasklist, parameters=self.parameters)

    def parameter_creation(self, parameters) -> Optional[TasklistParameters]:
        cancel_text = utils.paint_text(' [-c]ancel', GREYED_OUT)

        for attr in parameters.public_vars():
            # Accesses properties correctly
            attr_trimmed = attr.removeprefix('_')
            attr_painted = utils.paint_text(attr_trimmed, EDITING_HIGHLIGHT)

            while True:
                utils.clear_terminal()
                print(self.display_string(parameters).replace(
                    f'{MENU_PADDING}{attr_trimmed}:',
                    f'{MENU_PADDING}{attr_painted}:'))

                print(MENU_PADDING +
                      f'Enter value for {attr_painted}' + cancel_text)

                response = input(PROMPT)
                if response == '-c':
                    return None

                if attr_trimmed == "title" and response in self.registry._tasklists:
                    self.help_string == utils.paint_text(
                        "title already in registry", ERROR
                    )
                    continue

                try:
                    setattr(parameters, attr_trimmed, response)
                    self.help_string = ''
                    break
                except ValueError as ex:
                    self.help_string = MENU_PADDING + \
                        utils.paint_text(str(ex), ERROR)
                    continue
        return parameters
