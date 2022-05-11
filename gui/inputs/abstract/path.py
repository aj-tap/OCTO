from abc import ABC, abstractmethod
from tkinter.ttk import Entry


class Path(ABC):
    """
    This is an abstract class for file_path
    and directory_path to avoid repeating
    the same constructor.

    ...
    Methods
    -------
    render_widgets(r)
        Requires implementing classes to have a function
        that will render widgets.
    ask_for_path()
        Requires implementing classes to have a function
        that will input a path.
    """

    def __init__(self, parent_container):
        """
        Parameter
        -------
        parent_container : Frame
            Where we will render our widgets into. Also, so we can access
            the bot property.
        """

        self.parent_container = parent_container
        self.path = None
        self.entry = Entry(parent_container)

    @abstractmethod
    def render_widgets(self, r):
        pass

    @abstractmethod
    def ask_for_path(self):
        pass
