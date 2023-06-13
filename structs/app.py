from interface.menu import MenuReturn
from interface.menu import MenuReturnState as state


class App:
    def __init__(self, registry, starting_menu):
        self.registry = registry
        self.menu_stack = [starting_menu]

    def run_current(self):
        print(self.menu_stack)

        current_menu = self.menu_stack[-1]
        result: MenuReturn = current_menu.run(self.registry)

        match result.return_state:
            case state.NEXT_MENU:
                self.menu_stack.append(result.returned_menu)
            case state.PREVIOUS_MENU:
                self.menu_stack.pop()
            case state.STAY_CURRENT:
                pass
            case state.REPLACE_CURRENT:
                self.menu_stack.pop()
                self.menu_stack.append(result.returned_menu)
            case state.BACK_TO_MAIN:
                self.menu_stack = [self.menu_stack[0]]
