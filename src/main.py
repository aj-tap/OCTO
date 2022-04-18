from src.traffic_bot import TrafficBot
from gui.app import App


if __name__ == "__main__":

    # sample
    sample = TrafficBot("..\yolo-coco-V4", "..\input.mp4", "..\output")

    # sample
    app = App(sample)
    app.mainloop()

    # sample.vidFrameChecker()  ## will return vidframe void.
    # sample.runBot()
