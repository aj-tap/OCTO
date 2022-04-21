from tkinter.ttk import Label, OptionMenu

from gui.inputs.abstract.levels import Levels

"""
This class is similar to ThresholdLevel 
it will accept a container in the constructor 
to render the widgets.


"""


class ConfidenceLevel(Levels):
    def __init__(self, parent_container):
        super().__init__(parent_container)

    def render_widgets(self, r):
        Label(self.container, text="Min confidence % : ") \
            .grid(sticky='w', row=r, column=1)

        OptionMenu(self.container, self.level,
                   command=self.set_new_level,
                   *range(50, 101, 10))\
            .grid(sticky='w', row=r, column=2)

    def set_new_level(self, new_lvl):
        self.container.bot.setConfidence(new_lvl * .01)
