from tkinter.ttk import Label, OptionMenu
from tkinter import IntVar


class ConfidenceLevel:
    def __init__(self, parent_container):
        self.container = parent_container
        self.min_confidence = IntVar()
        self.min_confidence.set(50)

    def render_confidence_level_widgets(self, r):
        Label(self.container, text="Min confidence % : ") \
            .grid(sticky='w', row=r, column=1)

        OptionMenu(self.container, self.min_confidence, *range(50, 101, 10))\
            .grid(sticky='w', row=r, column=2)

        print(self.min_confidence.get())
