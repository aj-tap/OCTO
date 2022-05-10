import cv2


class LineFinder:
    def __init__(self, input_file):
        self.input_file = input_file
        self.get_img()
        self.img = cv2.imread('frame-1.png', 1)
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.counter = 0

    def get_img(self):
        video = cv2.VideoCapture(self.input_file)
        grabbed, frame = video.read()
        cv2.imwrite("frame-1.png", frame)

    def read_img(self):
        cv2.imshow('image', self.img)

    def get_line(self):
        return [(self.x1, self.y1), (self.x2, self.y2)]

    def click_frame(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            if (self.counter % 2) == 0:
                print("set for 1st coordinates: ", x, ' ', y)
                self.x1 = x
                self.y1 = y
            else:
                print("set for 2nd coordinates: ", x, ' ', y)
                self.x2 = x
                self.y2 = y
            self.counter = self.counter + 1
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(self.img, str(x) + ',' +
                        str(y), (x, y), font,
                        1, (255, 0, 0), 2)
            self.read_img()

    def pop_window(self):
        self.read_img()
        cv2.setMouseCallback('image', self.click_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Testing
# test = LineFinder("input.mp4")
# test.pop_window()
