from tkinter import Tk

from gui.pages import Menu, Result
from gui.container import Container

from src.traffic_bot import TrafficBot as tb


class App(Tk):
    """
    Here we create our own Tk object called App --by
    inheriting from Tk to plug in our own configurations
    such as the icon, the window title, and initialize
    the frame classes from gui-menu to enable page switching.
    """

    def __init__(self):  # , tb):
        # self.bot = tb

        # superclass constructor
        super().__init__()
        # window configurations
        self.resizable(False, False)
        self.wm_iconbitmap('../assets/traffic.ico')
        self.title('traffic-bot-counter')

        # create a container from custom container class
        container = Container()

        # this is where we will store our pages
        self.frames = {}

        # to load page frames from gui-menu
        self.load_pages(container)

    def load_pages(self, container):
        for i in (Menu, Result):
            # We simply render Menu and Result using grid
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # display Menu by default instead of Result page
        self.show_frame(Menu)

    def show_frame(self, page):
        # bring the chosen page upfront
        frame = self.frames[page]
        frame.tkraise()
        self.bot.setThreshold()

