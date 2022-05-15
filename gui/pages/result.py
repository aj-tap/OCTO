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
        graph = GraphCSV()
        graph.get_data_arr()

        Button(self, text="Bar Graph", command=lambda: graph.plot_data_bar()).pack()
        Button(self, text="Scatter Plot", command=lambda: graph.plot_data_scatter()).pack()

        Label(self, text="By: Aldwin Tapican and Marjolo Mabuti").pack()

        self.grid(row=0, column=0, sticky='nsew')
