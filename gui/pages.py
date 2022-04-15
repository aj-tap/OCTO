from tkinter import Frame, filedialog as fd
from tkinter.ttk import Entry, Label, Button

from gui.confidence_level import ConfidenceLevel
from gui.input_directory import InputDirectory
from gui.input_file import InputFile

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

        InputFile(self).render_input_file_widgets(1)
        InputDirectory(self).render_input_directory_widgets(2)
        ConfidenceLevel(self).render_confidence_level_widgets(3)

        start = Button(self, text="Start",
                       command=lambda: controller.show_frame(Result))

        start.grid(row=4, column=1)


class Result(Frame):
    def __init__(self, parent_container, controller):
        super().__init__(parent_container)

        label = Label(self, text="Result")
        label.grid(row=0, column=1, padx=10, pady=10)
        button1 = Button(self, text="Back",
                         command=lambda: controller.show_frame(Menu))
        button1.grid(row=1, column=1, padx=10, pady=10)
