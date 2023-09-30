from interface.returns import FrameReturnState as state
from collections import namedtuple


FrameData = namedtuple('FrameData', 'frame optionals')


class App:
    def __init__(self, registry, starting_menu):
        self.registry = registry
        self.frame_stack = [FrameData(starting_menu, {})]

    def header_list(self):
        return [frame_data.frame.TITLE for frame_data in self.frame_stack]

    def run_current(self):
        frame_data = self.frame_stack[-1]
        current_frame = frame_data.frame
        frame_optionals = frame_data.optionals

        # storing the optional args to be used with the next frame
        frame_return, next_optionals = current_frame.run(
            self.registry, self.header_list(), **frame_optionals
        )

        # pulling out any executable from the previous frame
        if 'execute' in next_optionals:
            next_optionals['execute']()
            del next_optionals['execute']

        match frame_return.return_state:
            case state.NextFrame:
                self.frame_stack.append(
                    FrameData(frame_return.returned_frame, next_optionals))
            case state.ReplaceCurrent:
                self.frame_stack.pop()
                self.frame_stack.append(
                    FrameData(frame_return.returned_frame, next_optionals))
            case state.PreviousFrame:
                self.frame_stack.pop()
            case state.StayCurrent:
                pass
            case state.BackToMain:
                self.frame_stack = [self.frame_stack[0]]

    def run(self):
        try:
            while True:
                self.run_current()
        except KeyboardInterrupt:
            pass
