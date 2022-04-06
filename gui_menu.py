import tkinter as tk


class GuiMenu(tk.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.wm_iconbitmap('./assets/traffic.ico')
        self.title('traffic-bot-counter')

        self.container = tk.Frame(self, highlightbackground='gray', highlightthickness=1)
        self.container.grid(sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)
        self.generate_ui()

    def gui_input_dir(self):
        app.input_filename = tk.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                           filetypes=(("mp4 Files", "*.mp4"), ("All Files", "*.*")))
        tk.Label(self.container, text=app.input_filename, bg="white", pady=2).grid(sticky='w', row=1, column=2)

    def gui_output_dir(self):
        app.output_filename = tk.filedialog.askdirectory()
        tk.Label(self.container, text=app.output_filename, bg="white", pady=2).grid(sticky='w', row=2, column=2)

    def generate_ui(self):
        tk.Label(self.container, text="Input file")\
            .grid(sticky='w', row=1, column=1)
        tk.Button(self.container, text="Choose file", command=lambda: self.gui_input_dir())\
            .grid(sticky='w', row=1, column=3)
        tk.Label(self.container, text="", bg="white", padx=80, pady=2).grid(sticky='w', row=1, column=2)

        tk.Label(self.container, text="Output directory")\
            .grid(sticky='w', row=2, column=1)
        tk.Button(self.container, text="Choose directory", command=lambda: self.gui_output_dir())\
            .grid(sticky='w', row=2, column=3)
        tk.Label(self.container, text="", bg="white", padx=80, pady=2).grid(sticky='w', row=2, column=2)

        # TO BE CONFIGURED
        tk.Label(self.container, text="Min confidence %")\
            .grid(sticky='w', row=3, column=1)
        tk.OptionMenu(self.container, *range(0, 101, 10))\
            .grid(sticky='w', row=3, column=2)

        tk.Label(self.container, text="Threshold level") \
            .grid(sticky='w', row=4, column=1)
        tk.OptionMenu(self.container, *range(0, 101, 10)) \
            .grid(sticky='w', row=4, column=2)


app = GuiMenu()
app.mainloop()
