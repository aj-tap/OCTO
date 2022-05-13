from threading import Thread
from gui.app import App

if __name__ == "__main__":
    # bot = TrafficBot("yolo-coco-V4", "sample.mp4", "output")

    # TEMPORARY; to be moved to app
    app = App()
    app.mainloop()
    # Thread(target=app2.mainloop()).start()

    # sample.run_bot()

"""
TO UPDATE:
* fix output directory bug, frames don't show up in the output dir
* fix window not responding bug on runbot (tried threading, didnt work),
try async await?
"""
