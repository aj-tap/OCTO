from tkinter import filedialog as fd
from tkinter.ttk import Entry, Label, Button

"""
Here we will create a class to render widgets
related to the input file such as the label
and entry field.

The button will trigger accept_input_path which 
utilizes filedialog to accept then save a string 
of the selected mp4 file to input_filepath.

Update:
We now pass a traffic-bot instance to the constructor
in order to access the setter method in traffic-bot
to modify the inputPath variable inside tb.
"""


class InputFilePath:
    def __init__(self, parent_container, my_bot):
        self.container = parent_container
        self.input_file_path = None
        self.input_entry = Entry(parent_container)
        self.bot = my_bot

    def render_input_file_widgets(self, r):
        Label(self.container, text="Input file: ") \
            .grid(sticky='w', row=r, column=1)

        self.input_entry.grid(sticky='w', ipadx=80, row=r, column=2, columnspan=3)

        Button(self.container, text="Choose file", command=lambda: self.accept_input_path()) \
            .grid(sticky='w', row=r, column=5)

    def accept_input_path(self):
        self.input_file_path = fd.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("mp4 Files", "*.mp4"), ("All Files", "*.*")))
        self.input_entry.insert(0, self.input_file_path)

        self.bot.setInputFile(self.input_file_path)
