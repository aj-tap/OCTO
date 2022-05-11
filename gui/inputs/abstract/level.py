
from abc import ABC, abstractmethod
from tkinter import IntVar


class Level(ABC):
    """
    This is an abstract class for threshold
    and confidence to avoid repeating
    the same constructor.

    ...
    Methods
    -------
    render_widgets(r)
        Requires implementing classes to have a function
        that will render widgets.
    set_new_level(new_lvl)
        Requires implementing classes to have a function
        that will set the user's desired level.
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
        self.level = IntVar()
        self.level.set(50)

    @abstractmethod
    def render_widgets(self, r):
        pass

    @abstractmethod
    def set_new_level(self, new_lvl):
        pass
