from trafficBot import *

if __name__ == "__main__":
    # sample
    sample = TrafficBot("yolo-coco-V4", "input.mp4", "output")

    sample.vidFrameChecker()  ## will return vidframe void.
    sample.runBot()
