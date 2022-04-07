import tkinter as tk
import tkinter.filedialog as fd


# NOTE: Extract functions and extract functions and extract functions
# TODO: DRY, KISS, shred functions then pack them in new classes, and
#       create separate folder for GUI related classes and functions

class GuiMenu(tk.Tk):

    def __init__(self):
        super().__init__()

        # configure window
        self.resizable(False, False)
        self.wm_iconbitmap('./assets/traffic.ico')
        self.title('traffic-bot-counter')

        # create a container w/ Frame (similar to html <div>)
        self.container = tk.Frame(self, highlightbackground='gray', highlightthickness=1)
        self.container.grid(sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)

        # initialize text entries
        self.input_entry = tk.Entry(self.container, bg="white")
        self.output_entry = tk.Entry(self.container, bg="white")

        # initialize value entries
        self.min_confidence = tk.IntVar()
        self.min_confidence.set(50)

        self.threshold_lvl = tk.IntVar()
        self.threshold_lvl.set(40)

        self.generate_ui()

    def generate_ui(self):
        # INPUT FILE
        tk.Label(self.container, text="Input file: ") \
            .grid(sticky='w', row=1, column=1)

        # input_entry will be generated in between
        self.input_entry.grid(sticky='w', ipadx=80, row=1, column=2, columnspan=3)

        tk.Button(self.container, text="Choose file: ", command=lambda: self.gui_input_dir()) \
            .grid(sticky='w', row=1, column=5)

        # OUTPUT DIRECTORY
        tk.Label(self.container, text="Output directory: ") \
            .grid(sticky='w', row=2, column=1)

        # output_entry will be generated in between
        self.output_entry.grid(sticky='w', ipadx=80, row=2, column=2, columnspan=3)

        tk.Button(self.container, text="Choose directory: ", command=lambda: self.gui_output_dir()) \
            .grid(sticky='w', row=2, column=5)

        # MIN CONFIDENCE LEVEL
        tk.Label(self.container, text="Min confidence %: ") \
            .grid(sticky='w', row=3, column=1)
        tk.OptionMenu(self.container, self.min_confidence, *range(50, 101, 10)) \
            .grid(sticky='w', row=3, column=2)
        print(self.min_confidence.get())

        # THRESHOLD LEVEL
        tk.Label(self.container, text="Threshold level %: ") \
            .grid(sticky='w', row=4, column=1)
        tk.OptionMenu(self.container, self.threshold_lvl, *range(40, 101, 10)) \
            .grid(sticky='w', row=4, column=2)
        print(self.threshold_lvl.get())

        # AREA OF INTEREST
        tk.Label(self.container, text="Area of Interest: ") \
            .grid(sticky='e', row=3, column=3)
        tk.Button(self.container, text="Select two points", command=lambda: print("TRIGGER OPEN CV FUNCTION")) \
            .grid(sticky='w', row=3, column=4)

        # SUBMIT BUTTON
        tk.Button(self.container, text="START", command=lambda: print("RUN BOT!" +
                                                                      "(also write user inputs to bot script)")) \
            .grid(sticky='nsew', row=5, column=1, columnspan=2, padx=5, ipadx=10)

    def gui_input_dir(self):
        app.input_filename = fd.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("mp4 Files", "*.mp4"), ("All Files", "*.*")))
        self.input_entry.insert(0, app.input_filename)
        print(app.input_filename)

    def gui_output_dir(self):
        app.output_dir = fd.askdirectory()
        self.output_entry.insert(0, app.output_dir)
        print(app.output_dir)


app = GuiMenu()
app.mainloop()
