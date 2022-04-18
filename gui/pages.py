from tkinter import Frame
from tkinter.ttk import Label, Button

from gui.confidence_level import ConfidenceLevel
from gui.input_directory import InputDirectory
from gui.input_file import InputFile
from gui.threshold_level import ThresholdLevel

"""
Here we'll create our own Frame objects that 
will act as pages to be rendered in app. 

A Frame object needs a Tk object or another 
frame to render into (parent_container) here 
we will render into the container provided in app.
    
We will also accept app itself (controller) to 
access the show_frame method that will enable
us to switch pages.
"""


class Menu(Frame):
    def __init__(self, parent_container, controller, my_bot):
        super().__init__(parent_container)

        self.render_curated_widgets(my_bot)

        Button(self, text="Start",
               command=lambda: controller.show_frame(Result))\
            .grid(row=5, column=1, ipadx=15)

    def render_curated_widgets(self, my_bot):
        InputFile(self, my_bot).render_input_file_widgets(1)
        InputDirectory(self, my_bot).render_input_directory_widgets(2)
        ConfidenceLevel(self, my_bot).render_confidence_level_widgets(3)
        ThresholdLevel(self, my_bot).render_threshold_level_widgets(3)


class Result(Frame):
    def __init__(self, parent_container, controller, my_bot=None):
        super().__init__(parent_container)

        Label(self, text="By: Aldwin Tapican and Marjolo Mabuti").grid(row=1, column=1, columnspan=2)

        Button(self, text="Back",
               command=lambda: controller.show_frame(Menu))\
            .grid(row=2, column=1, padx=10, pady=10)
