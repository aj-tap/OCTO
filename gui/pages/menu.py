from tkinter import Frame
from tkinter.ttk import Button

from gui.inputs.confidence import ConfidenceLevel
from gui.inputs.directory_path import DirectoryPath
from gui.inputs.file_path import FilePath
from gui.inputs.intersection_line import IntersectionLine
from gui.inputs.threshold import ThresholdLevel

"""
Here we will create our Menu page which is 
a child of Frame.

A Frame object needs a Tk object or another 
frame to render into (parent_container) here 
we will render into the container provided in app.
    
We will also accept app itself (controller) to 
access the show_frame method that will enable
us to switch pages.
"""


class Menu(Frame):
    def __init__(self, parent_container, controller, result, my_bot):
        super().__init__(parent_container)

        self.bot = my_bot
        self.render_widgets()

        Button(self, text="Start",
               command=lambda: controller.show_frame(result))\
            .grid(row=5, column=1, ipadx=15)

    def render_widgets(self):
        FilePath(self).render_input_file_widgets(1)
        DirectoryPath(self).render_input_directory_widgets(2)
        ConfidenceLevel(self).render_confidence_level_widgets(3)
        ThresholdLevel(self).render_threshold_level_widgets(3)
        IntersectionLine(self).render_intersection_line_widgets(4)

