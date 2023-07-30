from interface import utils
from interface.returns import PreviousMenu, NextMenu, BackToMain, ReplaceCurrent
from interface.frames.view_task import ViewTask


__all__ = ['SearchTaskTitles']


class SearchTaskTitles:

    TITLE = "VIEW SEARCH RESULTS"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = SearchTaskTitles(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list, search_term):
        self.registry = registry
        self.header_list = header_list
        self.search_term = search_term

        self.tasks = list(self.registry.tasks)
        self.tasks.sort()

        self.task_menu = [f"{utils.hotkey(i + 1)} {t.title}"
                          for i, t in enumerate(self.tasks)
                          if self.search_term in t.title]

        self.sub_menu = [
            f"{utils.hotkey('g')}o back",
            f"{utils.hotkey('h')}ome",
        ]

    @property
    def options(self):
        result = {str(i + 1): ReplaceCurrent(ViewTask, task=t)
                  for i, t in enumerate(self.tasks)}
        result['g'] = PreviousMenu()
        result['h'] = BackToMain()
        return result

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.task_menu)
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):

        while True:
            utils.clear_terminal()
            print(self.display_string())
            return utils.get_menu_input(self.options)
    pass
