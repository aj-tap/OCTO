from tkinter import Frame, filedialog as fd
from tkinter.ttk import Entry, Label, Button

from gui.confidence_level import ConfidenceLevel
from gui.input_directory import InputDirectory
from gui.input_file import InputFile
from gui.threshold_level import ThresholdLevel

"""
Here we'll create our own Frame objects that 
will act as the pages to be rendered in app. 

A Frame object needs a Tk object or another 
frame to render into (parent_container) here 
we will render into the container provided in app.
    
We will also accept app itself (controller) to 
access the show_frame method that will enable
us to switch pages.
"""


class Menu(Frame):
    def __init__(self, parent_container, controller):
        super().__init__(parent_container)

        self.input_fil = InputFile(self)
        self.input_fil.render_input_file_widgets(1)

        self.input_dir = InputDirectory(self)
        self.input_dir.render_input_directory_widgets(2)

        self.conf_lvl = ConfidenceLevel(self)
        self.conf_lvl.render_confidence_level_widgets(3)

        self.thr_lvl = ThresholdLevel(self)
        self.thr_lvl.render_threshold_level_widgets(3)

        self.start = Button(self, text="Start",
                            command=lambda: controller.show_frame(Result))

        # self.start["state"] = "disabled"

        self.start.grid(row=5, column=1, ipadx=15)


class Result(Frame):
    def __init__(self, parent_container, controller):
        super().__init__(parent_container)

        label = Label(self, text="Result")
        label.grid(row=0, column=1, padx=10, pady=10)
        button1 = Button(self, text="Back",
                         command=lambda: controller.show_frame(Menu))
        button1.grid(row=1, column=1, padx=10, pady=10)
