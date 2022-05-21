from tkinter import Tk, Frame

from gui.graph_buttons import GraphButtons
from gui.menu import Menu
from OctoBot import TrafficBot


class App(Tk):
    """
    A class to create the instance of the application itself. Inherits from the Tk object
    from the tkinter library in order to access some of its key methods and attributes.
    To create and configure our window.

    This entire class is built to interact with the bot instance and fully relies on its
    functions and attributes.

    ...
    Methods
    -------
    configure_window()
        Sets the icon and the title for the main window of the application.
    start_process()
        Calls run bot to start the machine learning application.
    """

    def __init__(self):
        super().__init__()
        self.configure_window()
        self.main_container = Frame(self)

        self.main_container.grid(row=0, column=0, padx=15, pady=15)
        self.menu = Menu(self, self.main_container)

    def start_process(self):

        self.withdraw()

        bot = TrafficBot(self.menu.input_path, self.menu.output_dir,
                         self.menu.intersection, self.menu.confidence,
                         self.menu.threshold)

        bot.run_bot()

        GraphButtons(self.menu).render_widgets(5)

        self.deiconify()

    def configure_window(self):
        self.resizable(False, False)
        self.wm_iconbitmap('assets/traffic.ico')
        self.title('OCTO-BOT')
