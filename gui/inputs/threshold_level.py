from tkinter.ttk import Label, OptionMenu

from gui.inputs.abstract.level import Level


class ThresholdLevel(Level):
    """
    This class is for widgets and functionalities
    that are related to the input of the threshold level.

    ...
    Methods
    --------
    render_widgets(r)
        Renders the widgets related to the input of threshold level
        such as the OptionMenu.
    set_new_level(new_lvl)
        Accesses the bot property from parent_container to use the
        setter method defined in the backend for the threshold level.
    """

    def __init__(self, parent_container):
        """
        Parameter
        -------
        parent_container : Frame
            Where we will render our widgets into. Also, so we can access
            the bot property.
        """

        super().__init__(parent_container)

    def render_widgets(self, r):
        """
        Parameter
        -------
        r : int
            An integer to specify the row where we will render the widget.
        """

        Label(self.parent_container, text="Threshold level % : ") \
            .grid(sticky='e', row=r, column=3)

        OptionMenu(self.parent_container, self.level,
                   command=self.set_new_level,
                   *range(40, 101, 10)) \
            .grid(sticky='w', row=r, column=4)

    def set_new_level(self, new_lvl):
        """
        Parameter
        -------
        new_lvl : int
            An integer to specify the desired threshold level.
        """

        self.parent_container.threshold = new_lvl * .01