from tkinter import Frame


class Container(Frame):
    def __init__(self):
        # this is the constructor for Frame, so we can add Frame parameters
        super().__init__(highlightbackground='gray', highlightthickness=1)
        self.pack(side="top", fill="both", expand=True, pady=5, padx=5)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
