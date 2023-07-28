from interface import utils
from interface.menu import PreviousMenu, ReplaceCurrent


class ProcessTasklist:

    TITLE = "PROCESS TASKLIST"

    @classmethod
    def run(self, registry, header, **optionals):
        M = ProcessTasklist(registry, header, **optionals)
        return M.run_instance()

    def __init__(self, registry, header):
        self.registry = registry
        self.header = header
        self.tasklist = registry.current_tasklist

        self.sub_menu = [
            f"Process and {utils.hotkey('d')}elete",
            f"Process and {utils.hotkey('s')}ave",
            f"{utils.hotkey('g')}o back",
        ]

        self.options = {
            # 'd': ReplaceCurrent(SaveRegistryConfirmation, current_tasklist_process_delete=self.tasklist),
            # 's': ReplaceCurrent(SaveRegistryConfirmation, current_tasklist_process_save=self.tasklist),
            'g': PreviousMenu()
        }

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header)
        result += "\n"
        result += utils.menu_string(self.tasklist.current_listify())
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)
