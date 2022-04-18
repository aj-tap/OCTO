from tkinter.ttk import Label, OptionMenu
from tkinter import IntVar


class ThresholdLevel:
    def __init__(self, parent_container, bot):
        self.container = parent_container
        self.threshold_lvl = IntVar()
        self.threshold_lvl.set(40)
        self.bot = bot

    def render_threshold_level_widgets(self, r):
        Label(self.container, text="Threshold level % : ") \
            .grid(sticky='e', row=r, column=3)

        OptionMenu(self.container, self.threshold_lvl,
                   command=self.modify_threshold_level,
                   *range(40, 101, 10)) \
            .grid(sticky='w', row=r, column=4)

        # command parameter in OptionMenu to trigger changes

    def modify_threshold_level(self, threshold_lvl):
        self.bot.setThreshold(threshold_lvl*.01)
