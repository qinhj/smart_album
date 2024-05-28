# ///////////////////////////////////////////////////////////////
#
# BY: hongjie.qin@spacemit.com
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
from abc import ABC
from enum import Enum, auto

def _not_implemented(*args, **kwargs):
    raise NotImplementedError("Sorry, not implement yet.")


class TaskState(Enum):
    ERROR = auto()
    PREPARE = auto()
    RUNNING = auto()
    FINISHED = auto()


class ICallback(ABC):

    def __init__(self):
        pass

    def __call__(self, cmd: str, state: TaskState, *args, **kwargs):
        return _not_implemented(*args, **kwargs)


class DefaultCallback(ICallback):

    def __init__(self):
        pass

    def __call__(self, cmd: str, state: TaskState, *args, **kwargs):
        print(f"{cmd} {state}")