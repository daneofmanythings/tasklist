from interface import utils
from interface.menu import BackToMain
from structs.registry import save_registry
from config.globals import SAVE_PATH, PROMPT


class SaveRegistry:

    TITLE = "SAVING REGISTRY"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = SaveRegistry(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(
        self,
        registry,
        header_list,
        task_save=None,
        task_delete=None,
        tasklist_save=None,
        tasklist_delete=None,
        current_tasklist_set=None,
        current_tasklist_process_save=None,
        current_tasklist_process_delete=None,
    ):
        self.registry = registry
        self.header_list = header_list
        self.task_save = task_save
        self.task_delete = task_delete
        self.tasklist_save = tasklist_save
        self.tasklist_delete = tasklist_delete
        self.current_tasklist_set = current_tasklist_set
        self.current_tasklist_process_save = current_tasklist_process_save
        self.current_tasklist_process_delete = current_tasklist_process_delete

        self.menu = ["Registry saved!",]

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.menu)
        return result

    def run_instance(self):
        if self.task_save:
            self.registry.add_task(self.task_save)
        if self.task_delete:
            self.registry.remove_task(self.task_delete)
        if self.tasklist_save:
            self.registry.add_tasklist(self.tasklist_save)
        if self.tasklist_delete:
            if self.registry._current_tasklist and self.tasklist_delete == self.registry._current_tasklist:
                self.registry.remove_current_tasklist()
            else:
                self.registry.remove_tasklist(self.tasklist_delete)
        if self.current_tasklist_set:
            self.registry.set_current_tasklist(self.current_tasklist_set)
        if self.current_tasklist_process_save:
            self.registry.process_current_tasklist()
        if self.current_tasklist_process_delete:
            self.registry.process_current_tasklist()
            self.registry.remove_current_tasklist()

        save_registry(self.registry, SAVE_PATH)

        utils.clear_terminal()
        print(self.display_string())
        input(PROMPT)
        return BackToMain()
