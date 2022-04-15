from tkinter import Frame
from tkinter.ttk import Label, Button

"""
Here we'll create our own Frame objects that 
will act as the pages to be rendered in app. 

A Frame object needs a Tk object or another 
frame to render into (parent_container) here 
we will render into the container provided in app.
    
We will also accept app itself (controller) to 
access the show_frame method that will enable
us to switch pages.
"""


class Menu(Frame):
    def __init__(self, parent_container, controller):

        super().__init__(parent_container)

        label = Label(self, text="Menu")
        label.grid(row=0, column=1, padx=10, pady=10)
        button1 = Button(self, text="Start",
                         command=lambda: controller.show_frame(Result))
        button1.grid(row=1, column=1, padx=10, pady=10)


class Result(Frame):

    def __init__(self, parent_container, controller):

        super().__init__(parent_container)

        label = Label(self, text="Result")
        label.grid(row=0, column=1, padx=10, pady=10)
        button1 = Button(self, text="Back",
                         command=lambda: controller.show_frame(Menu))
        button1.grid(row=1, column=1, padx=10, pady=10)
