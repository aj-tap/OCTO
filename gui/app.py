from tkinter import Tk, Frame

from gui.menu import Menu, Result
from gui.container import Container


class App(Tk):

    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.wm_iconbitmap('../assets/traffic.ico')
        self.title('traffic-bot-counter')

        # creating a container
        container = Container()

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Menu, Result):
            frame = F(container, self)

            # initializing frame of that object from
            # menu, result respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

