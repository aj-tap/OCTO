from tkinter import Tk

from gui.pages import Menu, Result
from gui.container import Container

"""
Here we create our own Tk object called App --by
inheriting from Tk, to plug in our own configurations
such as the icon, the window title, and initialize
the frame classes from gui-menu to enable page switching.

Update:
We now accept a traffic-bot instance called my_bot
that we will pass to page classes so that widgets
that belong in those pages can access the traffic-bot
instance (for threshold and confidence)
"""


class App(Tk):

    def __init__(self, my_bot):
        super().__init__()

        self.my_bot = my_bot
        self.configure_window()
        self.frame_storage = {}

        container = Container()
        self.load_pages(container)

    def configure_window(self):
        self.resizable(False, False)
        self.wm_iconbitmap('../assets/traffic.ico')
        self.title('traffic-bot-counter')

    def load_pages(self, container):
        for i in (Menu, Result):
            frame = i(container, self, self.my_bot)
            self.frame_storage[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, page):
        frame = self.frame_storage[page]
        frame.tkraise()
