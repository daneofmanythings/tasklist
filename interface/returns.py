from enum import Enum, auto
from collections import namedtuple


class FrameReturnState(Enum):
    NextFrame = auto()
    ReplaceCurrent = auto()
    PreviousFrame = auto()
    StayCurrent = auto()
    BackToMain = auto()


# Mimicing rust enums
FrameReturn = namedtuple('FrameReturn', 'return_state returned_frame')


# The return 'types' for menus.
# TODO: optionals put into the 'rust enum'?
def NextFrame(menu, **optionals):
    return FrameReturn(FrameReturnState.NextFrame, menu), optionals


def ReplaceCurrent(menu, **optionals):
    return FrameReturn(FrameReturnState.ReplaceCurrent, menu), optionals


def PreviousFrame(**optionals):
    return FrameReturn(FrameReturnState.PreviousFrame, None), optionals


def StayCurrent(**optionals):
    return FrameReturn(FrameReturnState.StayCurrent, None), optionals


def BackToMain(**optionals):
    return FrameReturn(FrameReturnState.BackToMain, None), optionals
