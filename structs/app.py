from interface.menu import MenuReturnState as state
from collections import namedtuple


MenuData = namedtuple('MenuData', 'menu optionals')


class App:
    def __init__(self, registry, starting_menu):
        self.registry = registry
        self.menu_stack = [MenuData(starting_menu, {})]

    def header_list(self):
        return [menu_data.menu.TITLE for menu_data in self.menu_stack]

    def run_current(self):
        menu_data = self.menu_stack[-1]
        current_menu = menu_data.menu
        menu_optionals = menu_data.optionals

        # storing the optional args to be used with the next menu
        menu_return, optionals = current_menu.run(
            self.registry, self.header_list(), **menu_optionals
        )

        match menu_return.return_state:
            case state.NextMenu:
                self.menu_stack.append(
                    MenuData(menu_return.returned_menu, optionals))
            case state.ReplaceCurrent:
                self.menu_stack.pop()
                self.menu_stack.append(
                    MenuData(menu_return.returned_menu, optionals))
            case state.PreviousMenu:
                self.menu_stack.pop()
            case state.StayCurrent:
                pass
            case state.BackToMain:
                self.menu_stack = [self.menu_stack[0]]
