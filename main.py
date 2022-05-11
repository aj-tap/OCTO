from OctoBot import *
from gui.app import App

if __name__ == "__main__":

    bot = TrafficBot("yolo-coco-V4", "sample.mp4", "output")

    #TEMPORARY; to be moved to app

    app = App(bot)
    # sample.run_bot()


"""
TO UPDATE:
use two threads

traffic bot is only instantiated after pressing the start button

pressing start will switch to the result page

print frames in gui

logic in main
"""