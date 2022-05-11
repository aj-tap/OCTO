from tkinter.ttk import Label, Button
from tkinter import Frame, Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class Result(Frame):
    """
    A class that inherits tkinter Frame properties where we
    will render our result related tkinter widgets into.
    """

    def __init__(self, app, main_container, previous_page):
        """
        Parameters
        -------
        app : App
            The App class itself, in order for us to access
            the properties of the bot which is also a property of App
            which we will then need to set the necessary data for
            the threshold, confidence paths, and intersection line.
        main_container : Frame
            This is where the Menu page will be rendered into.
        previous_page : Any
            This is to raise the previous page---Menu.

        ...
        Note; self refers to the Result page itself, which is a frame, this means
        we can render widgets into self.
        """

        super().__init__(main_container)

        app.bot.graph_csv.get_data_arr()

        Button(self, text="Bar Graph", command=lambda: plot_bar()).pack()
        Button(self, text="Scatter Plot", command=lambda: plot_scatter()).pack()

        Label(self, text="By: Aldwin Tapican and Marjolo Mabuti").pack()

        self.grid(row=0, column=0, sticky='nsew')

        def plot_bar():
            app.bot.graph_csv.plot_data_bar()

        def plot_scatter():
            app.bot.graph_csv.plot_data_scatter()
