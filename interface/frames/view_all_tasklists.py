from interface import utils
from interface.returns import PreviousMenu, ReplaceCurrent, BackToMain
from interface.frames.view_tasklist import ViewTasklist


__all__ = ['ViewAllTasklists']


class ViewAllTasklists:

    TITLE = "VIEW ALL TASKLISTS"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = ViewAllTasklists(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list

        self.tasklists = list(self.registry.tasklists)
        self.tasklists.sort()

        self.tasklist_menu = [f"{utils.hotkey(i + 1)} {t.title}"
                              for i, t in enumerate(self.tasklists)]

        self.sub_menu = [
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",
        ]

    @property
    def options(self):
        result = {str(i + 1): ReplaceCurrent(ViewTasklist, tasklist=t)
                  for i, t in enumerate(self.tasklists)}
        result['g'] = PreviousMenu()
        result['h'] = BackToMain()
        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.tasklist_menu)
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)
