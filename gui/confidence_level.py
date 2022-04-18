from tkinter.ttk import Label, OptionMenu
from tkinter import IntVar


class ConfidenceLevel:
    def __init__(self, parent_container, bot):
        self.container = parent_container
        self.bot = bot
        self.min_confidence = IntVar()
        self.min_confidence.set(50)

    def render_confidence_level_widgets(self, r):
        Label(self.container, text="Min confidence % : ") \
            .grid(sticky='w', row=r, column=1)

        OptionMenu(self.container, self.min_confidence,
                   command=self.modify_confidence_level,
                   *range(50, 101, 10))\
            .grid(sticky='w', row=r, column=2)

    def modify_confidence_level(self, confidence_lvl):
        self.bot.setConfidence(confidence_lvl * .01)
