from interface import utils
from interface.returns import PreviousFrame, NextFrame
from interface.frames.view_all_tasklists import ViewAllTasklists


__all__ = ['FindTasklist']


class FindTasklist:
    TITLE = "FIND TASKLIST"

    @classmethod
    def run(self, registry, header_list, **optionals):
        M = FindTasklist(registry, header_list)
        return M.run_instance()

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.menu = [
            f"{utils.hotkey('1')} View All",
            # f"{utils.hotkey('2')} Search Titles",
        ]

        self.sub_menu = [
            f"{utils.hotkey('g')}o back",
        ]

        self.options = {
            '1': NextFrame(ViewAllTasklists),
            # '2': NextMenu(SearchTasklistTitles),
            'g': PreviousFrame(),
        }

    def display_string(self):
        result = "\n"
        result += utils.header_string(utils.paint_header(self.header_list))
        result += "\n"
        result += utils.menu_string(self.menu)
        result += "\n"
        result += utils.sub_menu_string(self.sub_menu)
        return result

    def run_instance(self):
        utils.clear_terminal()
        print(self.display_string())
        return utils.get_menu_input(self.options)
