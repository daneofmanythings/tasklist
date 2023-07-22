from interface import utils
from interface.menu import PreviousMenu, ReplaceCurrent
from interface.menus.save_registry import SaveRegistry
from config.theme import ERROR


class SaveRegistryConfirmation:

    TITLE = "SAVING REGISTRY > CONFIRMATION"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = SaveRegistryConfirmation(registry, header_list, **optionals)
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

        self.menu = []

        self.sub_menu = [
            f"{utils.hotkey('c')}onfirm",
            f"{utils.hotkey('g')}o back",
        ]

    # TODO: Make this less bad.
    @property
    def attrs_to_hand_off(self):
        return {k: v for k, v in vars(self).items() if "task" in k}

    @property
    def options(self):
        return {
            'c': ReplaceCurrent(SaveRegistry, **self.attrs_to_hand_off),
            'g': PreviousMenu(),
        }

    # TODO: This is brute force. Make it prettier.
    def populate_changes(self):
        if self.task_save:
            self.menu.append(f"Saving task: {self.task_save.title}")
            if self.task_save in self.registry.tasks:
                self.menu.append(
                    utils.paint_text(
                        f"This will overwrite task of the same name in registry.",
                        ERROR
                    )
                )
        if self.task_delete:
            self.menu.append(f"Deleting task: {self.task_delete.title}")
        if self.tasklist_save:
            self.menu.append(f"Saving tasklist: {self.tasklist_save.title}")
            if self.tasklist_save in self.registry.tasklists:
                self.menu.append(
                    utils.paint_text(
                        f"This will overwrite tasklist of the same name in registry.",
                        ERROR
                    )
                )
        if self.tasklist_delete:
            self.menu.append(
                f"Deleting tasklist: {self.tasklist_delete.title}")
        if self.current_tasklist_set:
            self.menu.append(
                f"Setting current tasklist: {self.current_tasklist_set.title}")
        if self.current_tasklist_process_save:
            self.menu.append(
                f"Processing current tasklist: {self.current_tasklist_process_save.title}")
        if self.current_tasklist_process_delete:
            self.menu.append(
                f"Processing and deleting current tasklist: {self.current_tasklist_process_delete.title}")

    def display_string(self):
        self.populate_changes()
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.menu)
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)
