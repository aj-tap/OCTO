from OctoBot import *

if __name__ == "__main__":
    # sample
    sample = TrafficBot("yolo-coco-V4", "input.mp4", "output")

    sample.video_frame_checker()  ## will return vidframe void.
    #sample.line_finder.pop_window()
    sample.run_bot()

