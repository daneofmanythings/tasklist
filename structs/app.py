from interface.menu import MenuReturnState as state


class App:
    def __init__(self, registry, starting_menu):
        self.registry = registry
        self.menu_stack = [starting_menu]
        self.optionals = dict()

    def header_list(self):
        return [menu.TITLE for menu in self.menu_stack]

    def run_current(self):

        current_menu = self.menu_stack[-1]

        # storing the optional args to be used with the next menu
        menu_return, self.optionals = current_menu.run(
            self.registry, self.header_list(), **self.optionals
        )

        match menu_return.return_state:
            case state.NextMenu:
                self.menu_stack.append(menu_return.returned_menu)
            case state.ReplaceCurrent:
                self.menu_stack.pop()
                self.menu_stack.append(menu_return.returned_menu)
            case state.PreviousMenu:
                self.menu_stack.pop()
            case state.StayCurrent:
                pass
            case state.BackToMain:
                self.menu_stack = [self.menu_stack[0]]
