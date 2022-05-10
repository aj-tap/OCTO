"""
Similar to file_path, here we will render widgets
related to accepting a path but this time, it's for
the output directory.

The button will trigger ask_for_path which
utilizes filedialog to accept then save a string
of the selected directory and then trigger the
setter function in traffic_bot to set
the output_directory_path in there.

We will access the input_file_path in the bot
instance through the parent_container
(self.parent_container.bot).
"""

from tkinter import filedialog as fd
from tkinter.ttk import Label, Button

from gui.inputs.abstract.path import Path


class DirectoryPath(Path):
    def __init__(self, parent_container):
        super().__init__(parent_container)

    def render_widgets(self, r):
        Label(self.parent_container, text="Output directory: ") \
            .grid(sticky='w', row=r, column=1)

        self.entry.grid(sticky='w', ipadx=80, row=r, column=2, columnspan=3)

        Button(self.parent_container, text="Choose directory", command=lambda: self.ask_for_path()) \
            .grid(sticky='w', row=r, column=5)

    def ask_for_path(self):
        self.path = fd.askdirectory()
        self.entry.insert(0, self.path)

        self.parent_container.bot.set_output_dir(self.path)
