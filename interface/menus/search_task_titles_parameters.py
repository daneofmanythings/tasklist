from interface import utils
from interface.menus.search_task_titles import SearchTaskTitles
from interface.menu import ReplaceCurrent
from config.globals import PROMPT


class SearchTaskTitlesParameters:
    TITLE = "SEARCH TASKS > PARAMETERS"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = SearchTaskTitlesParameters(registry, header_list, **optionals)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list

        self.menu = [
            "Enter a term to search for:",
        ]

    def display_string(self):
        result = "\n"
        result += utils.header_string(self.header_list)
        result += "\n"
        result += utils.menu_string(self.menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return ReplaceCurrent(SearchTaskTitles, search_term=input(PROMPT))
