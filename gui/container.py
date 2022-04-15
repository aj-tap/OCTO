from tkinter import Frame


class Container(Frame):
    def __init__(self):
        super().__init__()

        self.pack(side="top", fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
