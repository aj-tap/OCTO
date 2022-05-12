from OctoBot import *

from threading import Thread
from tkinter import NORMAL

from gui.app import App
from gui.pages.menu import Menu

if __name__ == "__main__":
    # bot = TrafficBot("yolo-coco-V4", "sample.mp4", "output")

    # TEMPORARY; to be moved to app
    app = App()
    app.mainloop()

    # Thread(target=app2.mainloop()).start()

    # sample.run_bot()

"""
TO UPDATE:
* use two threads (OPTIONAL)
* traffic bot is only instantiated after pressing the start button
* start button can only be pressed if all entries are filled
* pressing start will switch to the result page
* print frames in gui
* logic in main

FLOW:
* disable start button
* input everything in the gui
* check if required fields are filled
* if true, enable start button
* on-start button click hide tkinter window
* display result page 
* create octobot instance
* after run bot, un-hide tkinter window
"""
