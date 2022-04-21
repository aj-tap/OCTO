from tkinter.ttk import Label, Button


class IntersectionLine:
    def __init__(self, parent_container):
        self.container = parent_container

    def render_intersection_line_widgets(self, r):
        Label(self.container, text="Intersection Line: ") \
            .grid(sticky='w', row=r, column=1)

        Button(self.container, text="Draw", command=self.draw_intersection_line) \
            .grid(sticky='w', row=r, column=2)

    def draw_intersection_line(self):
        self.container.bot.temporaryTriggerForIntersectionLine()
