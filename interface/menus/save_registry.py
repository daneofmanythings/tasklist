from interface import utils
from interface.menu import PreviousMenu
from structs.registry import save_registry
from config.globals import SAVE_PATH, PROMPT


class SaveRegistry:

    TITLE = "SAVING REGISTRY"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = SaveRegistry(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, task=None, tasklist=None, current_tasklist=None):
        self.registry = registry
        self.header_list = header_list
        self.task = task
        self.tasklist = tasklist
        self.current_tasklist = current_tasklist
        self.menu = []

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.menu)
        return result

    def run_instance(self):
        if self.task:
            self.registry.add_task(self.task)
            self.menu.append("Task saved")
        if self.tasklist:
            self.registry.add_tasklist(self.tasklist)
            self.menu.append("Tasklist saved")
        if self.current_tasklist:
            self.registry.set_current_tasklist(self.current_tasklist)
            self.menu.append("Current tasklist updated")

        self.menu.append("Registry Saved!")
        save_registry(self.registry, SAVE_PATH)

        utils.clear_terminal()
        print(self.display_string())
        input(PROMPT)
        return PreviousMenu(task=self.task, tasklist=self.tasklist, current_tasklist=self.current_tasklist)
