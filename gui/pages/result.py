from tkinter.ttk import Label, Button
from tkinter import Frame

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

        Label(self, text="By: Aldwin Tapican and Marjolo Mabuti").grid(row=1, column=1, columnspan=2)

        Button(self, text="Back",
               command=lambda: controller.show_frame(menu)) \
            .grid(row=2, column=1, padx=10, pady=10)
