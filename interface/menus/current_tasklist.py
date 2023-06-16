from interface import utils
from interface.utils import hotkey
from interface.menu import MenuReturn, Menu
from interface.menu import MenuReturnState as state
from config.theme import CURRENT_ACTIVE, MENU_HIGHLIGHT, GREYED_OUT, ERROR
from config.globals import MENU_PADDING, HEADER_PADDING, PROMPT, SAVE_PATH
from structs.registry import save_registry


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
        task_table = registry._current_tasklist.listify()[1:]
        selection_nums = [
            f"{hotkey(str(i + 1))} " for i in range(len(task_table))]

        while True:
            task_printable = [sn + ts + tt for sn, ts,
                              tt in zip(selection_nums, self.task_status(registry._current_tasklist, registry), task_table)]
            utils.clear_terminal()
            print(self.display_string())
            print(utils.table_to_string(task_printable, MENU_PADDING))
            print(' ' * MENU_PADDING +
                  f"toggle status {hotkey('#')} | {hotkey('p')}rocess | process {hotkey('a')}ll | {hotkey('s')}ave")

            chosen_action = input(PROMPT)

            if chosen_action in [str(i + 1) for i in range(len(task_table))]:
                registry._current_tasklist.toggle_status(
                    task_table[int(chosen_action) - 1])
                continue
            elif chosen_action == 'p':
                for task in registry._current_tasklist.tasks:
                    if registry._current_tasklist.tasks[task]:
                        registry.task_complete(task)
                registry.remove_current_tasklist()
                break
            elif chosen_action == 'a':
                for task in registry._current_tasklist.tasks:
                    registry.task_complete(task)
                registry.remove_current_tasklist()
                break
            elif chosen_action == 's':
                break
            else:
                continue

        save_registry(registry, SAVE_PATH)
        return MenuReturn(state.PREVIOUS_MENU, None)
