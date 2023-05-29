from interface import Main


class App:
    def __init__(self, registry):
        self.registry = registry
        self.current_menu = Main

    def run_current(self):
        self.current_menu = self.current_menu.run(self.registry)
