from tkinter import Frame
from tkinter.ttk import Label, Button


class Menu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Menu")

        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = Button(self, text="Start",
                         command=lambda: controller.show_frame(Result))

        button1.grid(row=1, column=1, padx=10, pady=10)


class Result(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Result")
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = Button(self, text="Back",
                         command=lambda: controller.show_frame(Menu))

        button1.grid(row=1, column=1, padx=10, pady=10)
