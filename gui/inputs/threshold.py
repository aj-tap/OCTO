from tkinter.ttk import Label, OptionMenu
from tkinter import IntVar

"""
In this class we will accept a container
in the constructor to render this widget
and also the traffic-bot instance in order
to modify the threshold variable inside
of traffic-bot.
"""


class ThresholdLevel:
    def __init__(self, parent_container):
        self.container = parent_container
        self.threshold_lvl = IntVar()
        self.threshold_lvl.set(40)

    def render_threshold_level_widgets(self, r):
        Label(self.container, text="Threshold level % : ") \
            .grid(sticky='e', row=r, column=3)

        OptionMenu(self.container, self.threshold_lvl,
                   command=self.modify_threshold_level,
                   *range(40, 101, 10)) \
            .grid(sticky='w', row=r, column=4)

    def modify_threshold_level(self, threshold_lvl):
        self.container.bot.setThreshold(threshold_lvl*.01)
