from tkinter.ttk import Label, OptionMenu
from tkinter import IntVar

"""
This class is similar to ThresholdLevel 
it will accept a container in the constructor 
to render this widget and also the traffic-bot 
instance in order to modify the threshold 
variable inside of traffic-bot.
"""


class ConfidenceLevel:
    def __init__(self, parent_container):
        self.container = parent_container
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
        self.container.bot.setConfidence(confidence_lvl * .01)
