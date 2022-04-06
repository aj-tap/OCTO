from tkinter import filedialog
import tkinter as tk


def gui_input_dir():
    app.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("mp4 Files", "*.mp4"), ("All Files", "*.*")))


class GuiMenu(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.wm_iconbitmap('./assets/traffic.ico')
        self.title('traffic-bot-counter')

        container = tk.Frame(self)
        container.pack(fill="both", padx=150, pady=5)

        label = tk.Label(self, text="This is the start page")
        label.pack()

        btn = tk.Button(self, text="button test", command=lambda: gui_input_dir())
        btn.pack()


app = GuiMenu()
app.mainloop()
