from random import sample
from datetime import datetime
import interface.utils as utils
from interface.utils import color_text
from config.theme import MENU_HIGHLIGHT
from config.globals import HEADER_PADDING, MENU_PADDING, SAVE_PATH, PROMPT
from structs.tasklist import Tasklist
from interface.menu import Menu, MenuReturn
from interface.menu import MenuReturnState as state
from structs.registry import save_registry


class GenerateTasklist(Menu):

    HEADER = (
        'MAIN / MANAGE TASKLISTS / ' +
        color_text('GENERATE TASKLIST', *MENU_HIGHLIGHT),
    )
    MENU = ()
    OPTIONS = {}

    @classmethod
    def display_string(self):
        return utils.table_to_string(self.HEADER, HEADER_PADDING)

    @classmethod
    def run(self, registry):
        utils.clear_terminal()
        print(self.display_string())
        time_alloted = 60  # TODO: pull this out to a config/selection
        tasklist_title = str(datetime.utcnow())
        TL = Tasklist(tasklist_title)
        for task in sample(registry._tasks, k=len(registry._tasks)):
            if time_alloted >= 0:
                TL.add_task(task.title)
                time_alloted -= int(task.length)
                continue
            break
        print(utils.table_to_string(TL.listify(), MENU_PADDING))
        print('Save and set current (s) | Generate again (g) | Cancel (any)')

        result = input(PROMPT)
        while True:
            if result == 's':
                registry.add_tasklist(TL)
                registry.set_current_tasklist(TL)
                save_registry(registry, SAVE_PATH)
                return MenuReturn(state.PREVIOUS_MENU, None)
            elif result == 'g':
                return MenuReturn(state.STAY_CURRENT, None)
            else:
                return MenuReturn(state.PREVIOUS_MENU, None)
