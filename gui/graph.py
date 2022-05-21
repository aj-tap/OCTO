from tkinter.ttk import Button

from Graph import GraphCSV


class GraphButtons:
    def __init__(self, parent_container):
        self.parent_container = parent_container
        self.graph = GraphCSV()
        self.graph.get_data_arr()

    def render_widgets(self, r):
        Button(self.parent_container, text="Bar Graph", command=lambda: self.graph.plot_data_bar())\
            .grid(row=r, column=4, sticky='nsew')
        Button(self.parent_container, text="Scatter Plot", command=lambda: self.graph.plot_data_scatter())\
            .grid(row=r, column=5, sticky='nsew')
