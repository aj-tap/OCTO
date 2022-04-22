"""
In this class we will simply render a Label
and a Button for triggering an opencv function
to accept two points and to draw a line from
the traffic_bot instance in the parent_container.
"""

from tkinter.ttk import Label, Button


class IntersectionLine:
    def __init__(self, parent_container):
        self.parent_container = parent_container

    def render_widgets(self, r):
        Label(self.parent_container, text="Intersection Line: ") \
            .grid(sticky='w', row=r, column=1)

        Button(self.parent_container, text="Draw", command=self.draw_intersection_line) \
            .grid(sticky='w', row=r, column=2)

    def draw_intersection_line(self):
        self.parent_container.bot.temporaryTriggerForIntersectionLine()