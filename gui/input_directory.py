from tkinter import filedialog as fd
from tkinter.ttk import Entry, Label, Button

"""
Here we will create a class to render widgets
related to the input directory such as the label
and entry field.

The button will trigger accept_input_directory_path which 
utilizes filedialog to accept then save a string 
of the selected mp4 file to input_directory_filepath.
"""


class InputDirectory:
    def __init__(self, parent_container):
        self.container = parent_container
        self.input_directory_path = None
        self.input_entry = Entry(parent_container)

    def render_input_directory_widgets(self, r):
        Label(self.container, text="Output directory: ") \
            .grid(sticky='w', row=r, column=1)

        self.input_entry.grid(sticky='w', ipadx=80, row=r, column=2, columnspan=3)

        Button(self.container, text="Choose directory", command=lambda: self.accept_input_directory_path()) \
            .grid(sticky='w', row=r, column=5)

    def accept_input_directory_path(self):
        self.input_directory_path = fd.askdirectory()
        self.input_entry.insert(0, self.input_directory_path)
        print(self.input_directory_path)
