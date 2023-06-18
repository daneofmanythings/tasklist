from random import shuffle
from datetime import datetime
import interface.utils as utils
from interface.utils import color_text, hotkey
from config.theme import MENU_HIGHLIGHT
from config.globals import HEADER_PADDING, MENU_PADDING, SAVE_PATH, PROMPT
from structs.tasklist import Tasklist
from structs.task import is_due
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
        due_tasks = list(filter(is_due, registry._tasks.values()))
        shuffle(due_tasks)
        for task in due_tasks:
            if time_alloted >= 0:
                TL.add_task(task.title)
                time_alloted -= int(task.length)
                continue
            break
        print(utils.table_to_string(TL.listify(), MENU_PADDING))
        print(' ' * MENU_PADDING +
              f"{hotkey('s')}ave | {hotkey('r')}edo | {hotkey('-c')}ancel")

        while True:
            result = input(PROMPT)
            if result == 's':
                registry.add_tasklist(TL)
                registry.set_current_tasklist(TL)
                save_registry(registry, SAVE_PATH)
                return MenuReturn(state.PREVIOUS_MENU, None)
            elif result == 'r':
                return MenuReturn(state.STAY_CURRENT, None)
            elif result == '-c':
                return MenuReturn(state.PREVIOUS_MENU, None)
            else:
                continue
