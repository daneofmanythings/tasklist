from interface import utils


class ViewTask:
    TITLE = "VIEW TASK"

    @classmethod
    def run(self, registry, header_list):
        pass

    def __init__(self, registry, header_list):
        self.registry = registry
        self.header_list = header_list
        self.sub_menu = {
            f"{utils.hotkey('s')}ave": 1,
            f"{utils.hotkey('e')}dit": 1,
            f"{utils.hotkey('-c')}ancel": 1,

        }

    def run_instance(self):
        while True:
            utils.clear_terminal()
            print(self.display_string(task))
            print(utils.submenu_string(self.sub_menu.keys()))

            response = input(PROMPT)
            if response == 's':
                self.registry.add_task(task)
                save_registry(self.registry, SAVE_PATH)
                return PreviousMenu()
            elif response == 'e':
                E = Editor(self.display_string(), task)
                task = E.run()
            elif response == '-c':
                return PreviousMenu()
            else:
                continue
