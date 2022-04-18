from tkinter import Tk, Frame

from gui.pages.menu import Menu
from gui.pages.result import Result

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
        self.configure_window()
        self.frame_storage = {}

        self.container = Frame(self)
        self.container.grid(row=0, column=0, padx=15, pady=15)

        self.load_pages(self.container, my_bot)

    def configure_window(self):
        self.resizable(False, False)
        self.wm_iconbitmap('../assets/traffic.ico')
        self.title('traffic-bot-counter')

    def load_pages(self, container, my_bot):
        self.frame_storage[Menu] = Menu(container, self, Result, my_bot)
        self.frame_storage[Result] = Result(container, self, Menu)

        self.frame_storage[Menu].grid(row=0, column=0, sticky="nsew")
        self.frame_storage[Result].grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, page):
        frame = self.frame_storage[page]
        frame.tkraise()
