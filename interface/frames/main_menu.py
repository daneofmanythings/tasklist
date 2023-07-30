from interface import utils
from interface.returns import NextFrame
from interface.frames.create_task import CreateTask
from interface.frames.find_tasks import FindTasks
from interface.frames.generate_tl_parameters import GenerateTasklistParameters
from interface.frames.current_tasklist import CurrentTasklist
from interface.frames.find_tasklist import FindTasklist


__all__ = ['MainMenu']


class MainMenu:
    TITLE = "TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = MainMenu(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.menu = [
            f"{utils.hotkey('1')} Create Task",
            f"{utils.hotkey('2')} Find Task",
            f"{utils.hotkey('3')} Find Tasklist",
            f"{utils.hotkey('4')} Generate Tasklist",
        ]

        self.options = {
            '1': NextFrame(CreateTask),
            '2': NextFrame(FindTasks),
            '3': NextFrame(FindTasklist),
            '4': NextFrame(GenerateTasklistParameters),
        }

        if self.registry.current_tasklist:
            self.menu.append(f"{utils.hotkey('5')} Open Current Tasklist")
            self.options['5'] = NextFrame(CurrentTasklist)

    def display_string(self):
        result = "\n"
        painted_header = utils.paint_header(self.header_list)
        result += utils.header_string(painted_header)
        result += "\n"
        result += utils.menu_string(self.menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)
