from tkinter.ttk import Label, Button
from tkinter import Frame
from Graph import GraphCSV


class Result(Frame):
    """
    A class that inherits tkinter Frame properties where we
    will render our result related tkinter widgets into.
    """

    def __init__(self, main_container):
        """
        Parameters
        -------
        main_container : Frame
            This is where the Menu page will be rendered into.

        ...
        Note; self refers to the Result page itself, which is a frame, this means
        we can render widgets into self.
        """

        super().__init__(main_container)

        # app.bot.graph_csv.get_data_arr()

        Label(self, text="By: Aldwin Tapican and Marjolo Mabuti").pack()

        self.grid(row=0, column=0, sticky='nsew')
