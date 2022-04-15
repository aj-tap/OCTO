from tkinter.ttk import Label, OptionMenu
from tkinter import IntVar


class ThresholdLevel:
    def __init__(self, parent_container):
        self.container = parent_container
        self.threshold_lvl = IntVar()
        self.threshold_lvl.set(40)

    def render_threshold_level_widgets(self, r):
        Label(self.container, text="Threshold level % : ") \
            .grid(sticky='e', row=r, column=3)

        OptionMenu(self.container, self.threshold_lvl, *range(40, 101, 10)) \
            .grid(sticky='w', row=r, column=4)

        print(self.threshold_lvl.get())
