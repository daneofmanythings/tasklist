from interface import utils
from interface.menu import ReplaceCurrent, NextMenu, PreviousMenu, BackToMain, StayCurrent
from interface.menus.edit_task import EditTask


class ViewTask:

    TITLE = "VIEW TASK"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = ViewTask(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, task, refresh=None):
        self.registry = registry
        self.header_list = header_list
        self.task = task
        self.refresh = refresh
        if self.refresh:
            self.task.last_completed = None

            # saving registry
            self.registry.save(task_save=self.task)

    @property
    def sub_menu(self):
        result = [
            f"{utils.hotkey('e')}dit",
            f"{utils.hotkey('d')}elete",
        ]

        if self.task.last_completed:
            result.append(f"{utils.hotkey('r')}efresh")

        result.extend([
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",
        ])

        return result

    @property
    def options(self):
        result = {
            'e': NextMenu(EditTask, task=self.task),
            'd': PreviousMenu(execute=lambda: self.registry.save(task_delete=self.task)),
            'g': PreviousMenu(),
            'h': BackToMain()
        }

        if self.task.last_completed:
            result['r'] = StayCurrent(
                execute=lambda: self.registry.save(task_refresh=self.task.title))

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
