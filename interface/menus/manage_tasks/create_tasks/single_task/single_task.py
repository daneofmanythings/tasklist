from tasks import Task
from interface.menu import Menu
from interface.loader import Loader

__all__ = ["SingleTask"]


class SingleTask(Menu):
    HEADER = (
        '',
        'MAIN / MANAGE TASKS / CREATE TASK / SINGLE TASK (\'-c\' to cancel)'
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
        if isinstance(result, Task):
            registry.add_task(result)
        return 0
