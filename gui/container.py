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
        super().__init__()  # (highlightbackground='gray', highlightthickness=0)

        self.pack(pady=15, padx=15)
