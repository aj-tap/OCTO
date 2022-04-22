"""
Here we will create an App class that inherits from
Tk which is the main window of a tkinter application
to create and configure our window.

bot = App will accept a bot instance for its pages to
access the functions of the bot (for threshold, confidence,
path, intersection line).

frame_storage = will store the page objects and utilize
show_frame to bring a page up.

main_container = is a Frame instance that will act as a
container which we will use to render our pages (Menu and Result).
"""

from tkinter import Tk, Frame
from gui.pages.menu import Menu
from gui.pages.result import Result


class App(Tk):
    def __init__(self, bot):
        super().__init__()
        self.configure_window()

        self.frame_storage = {}
        self.bot = bot
        self.main_container = Frame(self)

        self.main_container.grid(row=0, column=0, padx=15, pady=15)
        self.load_pages(self.main_container)

    def configure_window(self):
        self.resizable(False, False)
        self.wm_iconbitmap('../assets/traffic.ico')
        self.title('traffic-bot-counter')

    def load_pages(self, main_container):
        self.frame_storage[Menu] = Menu(self, main_container, Result)
        self.frame_storage[Result] = Result(self, main_container, Menu)
        self.show_frame(Menu)

    def show_frame(self, page):
        frame = self.frame_storage[page]
        frame.tkraise()
