"""
This is an abstract class for threshold
and confidence to avoid repeating
the same constructor.
"""

from abc import ABC, abstractmethod
from tkinter import IntVar


class Levels(ABC):
    def __init__(self, parent_container):
        self.parent_container = parent_container
        self.level = IntVar()
        self.level.set(50)

    @abstractmethod
    def render_widgets(self, r):
        pass

    @abstractmethod
    def set_new_level(self, new_lvl):
        pass
