from datetime import date
from structs.tasklist import Tasklist
from interface.returns import ReplaceCurrent
from interface.frames.current_tasklist import CurrentTasklist


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

        due_tasks = sorted(
            due_tasks, key=lambda task: task.deadline or date.max)

        for task in due_tasks:
            if duration >= int(task.length):
                self.tasklist.add_task(task.title)
                duration -= int(task.length)

    # def has_tags(self, task):
    #     # when no tags are specified for filtering
    #     if not self.parameters.tags:
    #         return True
    #
    #     for tag in task.tags:
    #         if tag not in self.parameters.tags:
    #             return False
    #     return True

    def run_instance(self):
        return ReplaceCurrent(CurrentTasklist, execute=Setter(self.registry, self.tasklist))


class Setter:
    def __init__(self, registry, tasklist):
        self.registry = registry
        self.tasklist = tasklist

    def __call__(self):
        return self.registry.w_current_tasklist_set(self.tasklist)
