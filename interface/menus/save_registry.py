from interface import utils
from interface.menu import PreviousMenu
from structs.registry import save_registry
from config.globals import SAVE_PATH, PROMPT


class SaveRegistry:

    TITLE = "SAVING REGISTRY"

    @classmethod
    def run(self, registry, header_list, task, tasklist):
        M = SaveRegistry(registry, header_list, task, tasklist)
        return M.run_instance()

    def __init__(self, registry, header_list, task, tasklist):
        self.registry = registry
        self.header_list = header_list
        self.task = task
        self.tasklist = tasklist
        self.menu = ["Registry saved!",]

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.menu)
        return result

    def run_instance(self):
        if self.task:
            self.registry.add_task(self.task)
        if self.tasklist:
            self.registry.add_tasklist(self.tasklist)

        save_registry(self.registry, SAVE_PATH)

        utils.clear_terminal()
        print(self.display_string())
        input(PROMPT)
        return PreviousMenu(task=self.task, tasklist=self.tasklist)
