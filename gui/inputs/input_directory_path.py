from tkinter import filedialog as fd
from tkinter.ttk import Entry, Label, Button

"""
Here we will create a class to render widgets
related to the input directory such as the label
and entry field.

The button will trigger accept_input_directory_path which 
utilizes filedialog to accept then save a string 
of the selected mp4 file to input_directory_filepath.

Update:
Similar to InputFile we will now pass a traffic-bot
instance to the constructor for us to call the 
setter method in tb to modify the output directory path
variable.
"""


class InputDirectoryPath:
    def __init__(self, parent_container, my_bot):
        self.container = parent_container
        self.input_directory_path = None
        self.input_entry = Entry(parent_container)
        self.bot = my_bot

    def render_input_directory_widgets(self, r):
        Label(self.container, text="Output directory: ") \
            .grid(sticky='w', row=r, column=1)

        self.input_entry.grid(sticky='w', ipadx=80, row=r, column=2, columnspan=3)

        Button(self.container, text="Choose directory", command=lambda: self.accept_input_directory_path()) \
            .grid(sticky='w', row=r, column=5)

    def accept_input_directory_path(self):
        self.input_directory_path = fd.askdirectory()
        self.input_entry.insert(0, self.input_directory_path)

        self.bot.setOutput(self.input_directory_path)
