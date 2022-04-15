from src.gui_menu import GuiMenu
from src.traffic_bot import TrafficBot

# Driver code
if __name__ == "__main__":
    # sample
    app = GuiMenu()
    app.mainloop()

    # sample
    sample = TrafficBot("..\yolo-coco-V4", "..\input.mp4", "..\output")

    sample.vidFrameChecker()  ## will return vidframe void.
    sample.runBot()
