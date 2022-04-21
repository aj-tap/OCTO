from tkinter import Frame
from tkinter.ttk import Button

from gui.inputs.confidence_level import ConfidenceLevel
from gui.inputs.directory_path import DirectoryPath
from gui.inputs.file_path import FilePath
from gui.inputs.intersection_line import IntersectionLine
from gui.inputs.threshold_level import ThresholdLevel

"""
Here we will create our Menu page. 

We inherit from Frame because Menu is basically
just another Frame.

A Frame object needs a Tk object or another 
frame to render into in this case we will render
into the parent_container.
    
We will also accept app itself (controller) to 
access the show_frame and allow us to switch pages.

In addition we will accept the result page for us to be able
to call it, and we will also accept my_bot which is an 
instance of traffic_bot for us to access it's attributes
and methods.
"""


class Menu(Frame):
    def __init__(self, parent_container, controller, result):
        super().__init__(parent_container)

        self.bot = controller.bot

        self.render_widgets()

        Button(self, text="Start",
               command=lambda: controller.show_frame(result))\
            .grid(row=5, column=1, ipadx=15)

    def render_widgets(self):
        FilePath(self).render_widgets(1)
        DirectoryPath(self).render_widgets(2)
        ConfidenceLevel(self).render_widgets(3)
        ThresholdLevel(self).render_widgets(3)
        IntersectionLine(self).render_widgets(4)

