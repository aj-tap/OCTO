from tkinter import Frame, NORMAL, DISABLED
from tkinter.ttk import Button

from gui.graph import GraphButtons
from gui.inputs.confidence_level import ConfidenceLevel
from gui.inputs.directory_path import DirectoryPath
from gui.inputs.file_path import FilePath
from gui.inputs.intersection_line import IntersectionLine
from gui.inputs.threshold_level import ThresholdLevel


class Menu(Frame):
    """
    A class that inherits tkinter Frame properties where we
    will render our menu related tkinter widgets into.

    ...
    Methods
    -------
    render_widgets()
        Renders the rest of the necessary widgets needed for the
        application.
    check()
        Checks if required parameters are fulfilled.
    """

    def __init__(self, app, main_container):
        """
        Parameters
        -------
        main_container : Frame
            This is where the Menu page will be rendered into.
        """

        super().__init__(main_container)

        self.input_path = None
        self.output_dir = None
        self.confidence = .5
        self.threshold = .4
        self.intersection = None

        self.intersection_line = IntersectionLine(self)

        self.render_widgets()

        self.start_btn = Button(self, text="Start",
                                command=lambda: app.start_process())
        self.start_btn.grid(row=5, column=1, ipadx=15)

        self.start_btn.configure(state=DISABLED)

        self.grid(row=0, column=0, sticky='nsew')


    def render_widgets(self):
        """
        Parameters
        --------
        self :
            refers to Menu itself, in which the widgets will be
            rendered into.
        """

        FilePath(self).render_widgets(1)
        DirectoryPath(self).render_widgets(2)
        ConfidenceLevel(self).render_widgets(3)
        ThresholdLevel(self).render_widgets(3)
        self.intersection_line.render_widgets(4)
        GraphButtons(self).render_widgets(5)

    def check(self):
        if self.input_path:
            self.intersection_line.draw.configure(state=NORMAL)
        if self.input_path and self.output_dir \
                and self.confidence and self.threshold\
                and self.intersection:
            self.start_btn.configure(state=NORMAL)
        else:
            self.start_btn.configure(state=DISABLED)
