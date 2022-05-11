from tkinter import Tk, Frame
from gui.pages.menu import Menu
from gui.pages.result import Result


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
    load_pages(main_container)
        Renders the frames unto the main_container in the form of a stack.
    show_frame(page)
        Raises the specified frame (or page) from the stack.
    """

    def __init__(self, bot):
        """
        Parameters
        -------
        bot : bot
            The object counter / traffic bot instance. For the frames (or pages)
             to access the getters/setters of the bot (used for threshold, confidence,
             path, intersection line).
        """

        super().__init__()
        self.configure_window()

        self.frame_storage = {}
        self.bot = bot
        self.main_container = Frame(self)

        self.main_container.grid(row=0, column=0, padx=15, pady=15)
        self.load_pages(self.main_container)

        self.mainloop()

    def configure_window(self):
        self.resizable(False, False)
        self.wm_iconbitmap('assets/traffic.ico')
        self.title('OCTO bot')

    def load_pages(self, main_container):
        """
        Parameters
        -------
        main_container: Frame
            This is the container where the Menu and Result frames (or pages) will be rendered into.
        """

        self.frame_storage[Menu] = Menu(self, main_container, Result)
        self.frame_storage[Result] = Result(self, main_container, Menu)
        self.show_frame(Menu)

    def start_btn(self):
        self.bot.run_bot()

    def show_frame(self, page):
        """
        Parameters
        -------
        page: Any
            The specified page is the frame to be raised or shown.
        """

        frame = self.frame_storage[page]
        frame.tkraise()



