"""
This page is similar to Menu class, but here we
will render the results and summon the graph.

self = where the widgets will be rendered.

app = to access app-bot and change bot properties and methods
for threshold, confidence, paths, intersection line.

main_container = where the menu will be rendered.
A frame object needs a Tk object or another frame
to render into in this case we will render into
the main_container.

next_page = result page.
"""

from tkinter.ttk import Label, Button
from tkinter import Frame, Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class Result(Frame):
    def __init__(self, app, main_container, previous_page):
        super().__init__(main_container)

        Button(self, text="Plot", command=lambda: plot()).pack()

        Button(self, text="Back",
               command=lambda: app.show_frame(previous_page)).pack()

        Label(self, text="By: Aldwin Tapican and Marjolo Mabuti").pack()

        self.grid(row=0, column=0, sticky='nsew')

        # TEMPORARY
        def plot():
            window = Tk()
            window.title('Result')
            window.wm_iconbitmap('../assets/traffic.ico')
            window.geometry("500x500")
            # the figure that will contain the plot
            fig = Figure(figsize=(5, 5),
                         dpi=100)
            # list of squares
            y = [i ** 2 for i in range(101)]
            # adding the subplot
            plot1 = fig.add_subplot(111)
            # plotting the graph
            plot1.plot(y)
            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig,
                                       master=window)
            canvas.draw()
            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()
            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas,
                                           window)
            toolbar.update()
            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()
