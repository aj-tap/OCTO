from tkinter import Tk

from src.traffic_bot import TrafficBot as bot

from gui.pages import Menu, Result
from gui.container import Container


class App(Tk):
    """
    Here we create our own Tk object called App --by
    inheriting from Tk to plug in our own configurations
    such as the icon, the window title, and initialize
    the frame classes from gui-menu to enable page switching.
    """

    def __init__(self, my_bot):

        # superclass constructor
        super().__init__()

        self.my_bot = my_bot

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
            frame = i(container, self, self.my_bot)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # display Menu by default instead of Result page
        self.show_frame(Menu)

    def show_frame(self, page):
        # bring the chosen page upfront
        frame = self.frames[page]
        frame.tkraise()

