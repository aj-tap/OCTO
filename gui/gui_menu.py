import tkinter as tk
import tkinter.filedialog as fd


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
