from interface import Main

__all__ = ['App']


class App:
    def __init__(self, registry):
        self.registry = registry
        self.menu_trace = [Main]

    def run_current(self):
        print(self.menu_trace)
        result = self.menu_trace[-1].run(self.registry)
        if result == 1:
            pass
        elif result == 0:
            self.menu_trace.pop()
        elif result == -1:
            self.menu_trace = [Main]
        else:
            self.menu_trace.append(result)
