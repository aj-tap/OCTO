from tkinter import Frame

"""
Here we create our own Frame object called
Container in order for to set our own 
configurations and write more modular code.

The superclass constructor can accept the
parameters of the superclass (Frame) so we 
can pass in highlight-background and thickness.
"""


class Container(Frame):
    def __init__(self):
        super().__init__(highlightbackground='gray', highlightthickness=1)

        self.pack(side="top", fill="both", expand=True, pady=5, padx=5)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
