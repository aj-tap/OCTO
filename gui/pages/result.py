from tkinter.ttk import Label, Button
from tkinter import Frame, Tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

"""
This is where we will render the results.

A Frame object needs a Tk object or another 
frame to render into (parent_container) here 
we will render into the container provided in app.

We will also accept app itself (controller) to 
access the show_frame method that will enable
us to switch pages.
"""


class Result(Frame):
    def __init__(self, parent_container, controller, menu):
        super().__init__(parent_container)

        Button(self, text="Plot", command=lambda: plot()).pack()

        Button(self, text="Back",
               command=lambda: controller.show_frame(menu)).pack()

        Label(self, text="By: Aldwin Tapican and Marjolo Mabuti").pack()

        def plot():
            # the main Tkinter window
            window = Tk()

            # setting the title
            window.title('Result')

            # dimensions of the main window
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

