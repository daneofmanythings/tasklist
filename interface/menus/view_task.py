from interface import utils
from interface.menu import ReplaceCurrent, NextMenu, PreviousMenu, BackToMain
from interface.menus.save_registry_confirmation import SaveRegistryConfirmation
from interface.menus.edit_task import EditTask


class ViewTask:

    TITLE = "VIEW TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = ViewTask(registry, header_list, optionals['task'])
        return M.run_instance()

    def __init__(self, registry, header_list, task):
        self.registry = registry
        self.header_list = header_list
        self.task = task

    @property
    def sub_menu(self):
        result = [
            f"{utils.hotkey('s')}ave",
            f"{utils.hotkey('e')}dit",
        ]

        if self.task in self.registry.tasks:
            result.append(f"{utils.hotkey('d')}elete")

        result.extend([
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",
        ])

        return result

    @property
    def options(self):
        result = {
            's': ReplaceCurrent(SaveRegistryConfirmation, task_save=self.task),
            'e': NextMenu(EditTask, task=self.task),
            'g': PreviousMenu(task=self.task),
            'h': BackToMain()
        }
        if self.task in self.registry.tasks:
            result['d'] = ReplaceCurrent(
                SaveRegistryConfirmation, task_delete=self.task)

        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.task.listify())
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)
