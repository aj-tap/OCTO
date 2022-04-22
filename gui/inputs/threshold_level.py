"""
This class is for widgets and functionalities
that are related to the threshold level we will
accept a container in the constructor to render
this widget into.

We will access the threshold_lvl in traffic_bot
by accessing its instance from the parent_container
(self.container.bot)
"""

from tkinter.ttk import Label, OptionMenu

from gui.inputs.abstract.level import Levels


class ThresholdLevel(Levels):
    def __init__(self, parent_container):
        super().__init__(parent_container)

    def render_widgets(self, r):
        Label(self.parent_container, text="Threshold level % : ") \
            .grid(sticky='e', row=r, column=3)

        OptionMenu(self.parent_container, self.level,
                   command=self.set_new_level,
                   *range(40, 101, 10)) \
            .grid(sticky='w', row=r, column=4)

    def set_new_level(self, new_lvl):
        self.parent_container.bot.setThreshold(new_lvl * .01)
