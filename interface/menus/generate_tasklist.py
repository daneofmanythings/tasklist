from random import shuffle
from interface import utils
from structs.tasklist import Tasklist
from interface.menu import ReplaceCurrent
from interface.menus.current_tasklist import CurrentTasklist


__all__ = ['GenerateTasklist']


class GenerateTasklist:

    TITLE = "GENERATE TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = GenerateTasklist(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, parameters):
        self.registry = registry
        self.header_list = header_list
        self.parameters = parameters

        self.tasklist = Tasklist(self.parameters.title)

        duration = self.parameters.duration
        due_tasks = [t for t in self.registry.tasks if t.is_due]
        shuffle(due_tasks)

        for task in due_tasks:
            if duration >= int(task.length):
                self.tasklist.add_task(task.title)
                duration -= int(task.length)

    #     self.sub_menu = [
    #         f"{utils.hotkey('s')}ave",
    #         f"{utils.hotkey('r')}edo",
    #         f"{utils.hotkey('-c')}ancel",
    #     ]
    #
    # @property
    # def options(self):
    #     return {
    #         's': ReplaceCurrent(SaveRegistryConfirmation, tasklist_save=self.tasklist, current_tasklist_set=self.tasklist),
    #         'r': StayCurrent(parameters=self.parameters),
    #         '-c': PreviousMenu(),
    #     }
    #
    # def display_string(self):
    #     result = "\n"
    #     result += utils.header_string(self.header_list)
    #     result += "\n"
    #     result += utils.menu_string(self.tasklist.listify_numbered())
    #     result += "\n"
    #     result += utils.sub_menu_string(self.sub_menu)
    #     return result
    #
    def run_instance(self):
        # utils.clear_terminal()
        # print(self.display_string())
        self.registry.save(current_tasklist_set=self.tasklist)

        return ReplaceCurrent(CurrentTasklist)
