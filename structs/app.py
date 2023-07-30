from interface.returns import MenuReturnState as state
from collections import namedtuple


FrameData = namedtuple('FrameData', 'menu optionals')


class App:
    def __init__(self, registry, starting_menu):
        self.registry = registry
        self.frame_stack = [FrameData(starting_menu, {})]

    def header_list(self):
        return [frame_data.menu.TITLE for frame_data in self.frame_stack]

    def run_current(self):
        frame_data = self.frame_stack[-1]
        current_menu = frame_data.menu
        frame_optionals = frame_data.optionals

        # storing the optional args to be used with the next frame
        menu_return, next_optionals = current_menu.run(
            self.registry, self.header_list(), **frame_optionals
        )

        if 'execute' in next_optionals:
            next_optionals['execute']()
            del next_optionals['execute']

        match menu_return.return_state:
            case state.NextMenu:
                self.frame_stack.append(
                    FrameData(menu_return.returned_menu, next_optionals))
            case state.ReplaceCurrent:
                self.frame_stack.pop()
                self.frame_stack.append(
                    FrameData(menu_return.returned_menu, next_optionals))
            case state.PreviousMenu:
                self.frame_stack.pop()
            case state.StayCurrent:
                pass
            case state.BackToMain:
                self.frame_stack = [self.frame_stack[0]]
