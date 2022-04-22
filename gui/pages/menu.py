"""
Here we will create our Menu page that will inherit
Frame which will act as a page.

self (this is Menu) = where the widgets will be rendered.

app = to access app-bot and change bot properties and methods
for threshold, confidence, paths, intersection line.

main_container = where the menu will be rendered.
A frame object needs a Tk object or another frame
to render into in this case we will render into
the main_container.

next_page = result page.
"""

from tkinter import Frame
from tkinter.ttk import Button

from gui.inputs.confidence_level import ConfidenceLevel
from gui.inputs.directory_path import DirectoryPath
from gui.inputs.file_path import FilePath
from gui.inputs.intersection_line import IntersectionLine
from gui.inputs.threshold_level import ThresholdLevel


class Menu(Frame):
    def __init__(self, app, main_container, next_page):
        super().__init__(main_container)

        self.bot = app.bot
        self.render_widgets()

        Button(self, text="Start",
               command=lambda: app.show_frame(next_page))\
            .grid(row=5, column=1, ipadx=15)

        self.grid(row=0, column=0, sticky='nsew')

    def render_widgets(self):
        FilePath(self).render_widgets(1)
        DirectoryPath(self).render_widgets(2)
        ConfidenceLevel(self).render_widgets(3)
        ThresholdLevel(self).render_widgets(3)
        IntersectionLine(self).render_widgets(4)
