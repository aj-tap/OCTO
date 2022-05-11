from tkinter.ttk import Label, Button


class IntersectionLine:
    """
    A class to render widgets related to the
    input of the intersection line.

    ...
    Methods
    -------
    render_widgets(r)
        Renders the widgets related to the intersection
        line
    draw_intersection_line()
        Accesses the bot property from the parent_container
        in order to use the trigger function to summon the
        openCV window that will accept two points to draw
        a line.
    """

    def __init__(self, parent_container):
        """
        Parameter
        -------
        parent_container : Frame
            Where we will render our widgets into. Also, so we can access
            the bot property.
        """

        self.parent_container = parent_container

    def render_widgets(self, r):
        """
        Parameter
        -------
        r : int
            An integer to specify the row where we will render the widget.
        """

        Label(self.parent_container, text="Intersection Line: ") \
            .grid(sticky='w', row=r, column=1)

        Button(self.parent_container, text="Draw", command=self.draw_intersection_line) \
            .grid(sticky='w', row=r, column=2)

    def draw_intersection_line(self):
        self.parent_container.bot.line_finder.pop_window()
