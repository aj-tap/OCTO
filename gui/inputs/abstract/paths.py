"""
This is an abstract class for file_path
and directory_path to avoid repeating
the constructor.
"""

from abc import ABC, abstractmethod
from tkinter.ttk import Entry


class Path(ABC):
    def __init__(self, parent_container):
        self.parent_container = parent_container
        self.path = None
        self.entry = Entry(parent_container)

    @abstractmethod
    def render_widgets(self, r):
        pass

    @abstractmethod
    def ask_for_path(self):
        pass
