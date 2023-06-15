from interface.menu import MenuReturn, Menu
from interface.menu import MenuReturnState as state
from config.theme import CURRENT_ACTIVE, MENU_HIGHLIGHT, GREYED_OUT, ERROR
from config.globals import MENU_PADDING, HEADER_PADDING, PROMPT
from interface import utils


# @work_in_progress
class CurrentTasklist(Menu):

    HEADER = (
        utils.color_text('CURRENT TASKLIST', *CURRENT_ACTIVE),
    )

    MENU = ()

    OPTIONS = {}

    @classmethod
    def display_string(self):
        return utils.table_to_string(self.HEADER, HEADER_PADDING)

    @classmethod
    def task_status(self, tasklist, registry):
        result = list()
        for task in tasklist.tasks:
            if task in registry._tasks:
                if tasklist.tasks[task]:
                    result.append(utils.color_text(
                        "(COMPLETE) ", *MENU_HIGHLIGHT))
                else:
                    result.append(utils.color_text(
                        "(in progress) ", *GREYED_OUT))
            else:
                result.append(utils.color_text("(NOT FOUND) ", *ERROR))

        return result

    @classmethod
    def run(self, registry):
        TL = registry._current_tasklist
        task_table = TL.listify()[1:]
        selection_nums = [f"{i + 1}) " for i in range(len(task_table))]

        while True:
            task_printable = [sn + ts + tt for sn, ts,
                              tt in zip(selection_nums, self.task_status(TL, registry), task_table)]
            utils.clear_terminal()
            print(self.display_string())
            print(utils.table_to_string(task_printable, MENU_PADDING))
            print(' ' * MENU_PADDING +
                  "Toggle completion (#) | Process tasklist (p) | Process as complete (c)")

            chosen_action = input(PROMPT)

            if chosen_action in [str(i + 1) for i in range(len(task_table))]:
                TL.toggle_status(task_table[int(chosen_action) - 1])
                continue
            elif chosen_action == 'p':
                pass
            elif chosen_action == 'c':
                pass
            else:
                return MenuReturn(state.PREVIOUS_MENU, None)
