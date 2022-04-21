from tkinter import filedialog as fd
from tkinter.ttk import Label, Button

from gui.inputs.abstract.paths import Path

"""
Here we will create a class to render widgets
related to the input file such as the label
and entry field.

The button will trigger ask_for_path which 
utilizes filedialog to accept then save a string 
of the selected mp4 file to self.path and then
trigger a setter function in traffic_bot to 
set the input_file_path.

UPDATE: 
We will access the input_file_path in traffic_bot 
instance through the parent_container.
"""


class FilePath(Path):
    def __init__(self, parent_container):
        super().__init__(parent_container)

    def render_widgets(self, r):
        Label(self.container, text="Input file: ") \
            .grid(sticky='w', row=r, column=1)

        self.entry.grid(sticky='w', ipadx=80, row=r, column=2, columnspan=3)

        Button(self.container, text="Choose file", command=lambda: self.ask_for_path()) \
            .grid(sticky='w', row=r, column=5)

    def ask_for_path(self):
        self.path = fd.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("mp4 Files", "*.mp4"), ("All Files", "*.*")))
        self.entry.insert(0, self.path)

        self.container.bot.setInputFile(self.path)
