from tasks import Task
from interface.menu import Menu
from interface.loader import Loader
from interface.editor import Editor

__all__ = ["SingleTask"]


class SingleTask(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE TASKS / CREATE TASK / SINGLE TASK'
    )
    MENU = (
        '',
    )
    OPTIONS = {
    }

    @classmethod
    def run(self, registry):
        t = Task()
        L = Loader(self.show(), t)
        result = L.run()
        if result is None:
            return 0
        while True:
            will_edit = input('Save (s) | Edit (e) | Cancel (-c) > ')
            if will_edit == 's':
                registry.add_task(result)
                #####################
                # SAVE REGISTRY TOO #
                #####################
                return 0
            elif will_edit == 'e':
                e = Editor(self.show(), result)
                result = e.run()
            else:
                return 0
