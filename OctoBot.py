# Libraries
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import glob
from sort import *
from WriterCsv import *
# from LineFinder import *
# from Graph import *


# import CoodFinder

class TrafficBot:

    def __init__(self, input_file=None, output=None, intersection=None, confidence_level=0.5,
                 threshold=0.3, yolo_directory="yolo-coco-V4"):
        # Writer object
        self.memory = {}
        self.writer_csv = WriterCsv()

        # input footage
        self.inputFile = input_file

        # Setup Colors directory
        self.COLORS = self.generate_color()

        # Confidence Level
        self.confidence_level = float(confidence_level)
        # Threshold level
        self.threshold = float(threshold)
        # Setup Output Directory
        self.output = output
        self.clear_output_directory()

        # Paths to the YOLO weights, model configuration and coco class labels
        self.weightPath = os.path.sep.join([yolo_directory, "yolov4.weights"])
        self.configPath = os.path.sep.join([yolo_directory, "yolov4.cfg"])

        self.labelsPath = os.path.sep.join([yolo_directory, "coco.names"])
        self.LABELS = open(self.labelsPath).read().strip().split("\n")

        # YOLO object detector trained on COCO dataset
        print("[INFO] loading YOLO from disk...")
        self.net = cv2.dnn.readNetFromDarknet(self.configPath, self.weightPath)
        # If nvidia is available
        # self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        # and determine only the *output* layer names that we need from YOLO
        self.ln = self.net.getLayerNames()
        self.ln = [self.ln[i - 1] for i in self.net.getUnconnectedOutLayers()]
        print("[INFO] YOLO  was loaded from disk")

        # initialize the video stream, pointer to output video file, and frame dimensions
        print("[INFO] Loading the input video")
        self.vs = cv2.VideoCapture(input_file)
        # Variables
        self.writer = None
        (self.W, self.H) = (None, None)
        self.frameIndex = 0
        print("[INFO] video input was successfully loaded")

        # self.line = [(210, 622), (1183, 582)]  # temp remove it
        self.line = intersection
        self.total = self.video_frame_checker()

        # Graph object
        #self.graph_csv = GraphCSV()

    def clear_output_directory(self):
        files = glob.glob(str(self.output) + "/*.png")
        for f in files:
            os.remove(f)

    def intersect(self, A, B, C, D):
        """
        Return true if line segments AB and CD intersect
        """
        return self.ccw(A, C, D) != self.ccw(B, C, D) and self.ccw(A, B, C) != self.ccw(A, B, D)

    def ccw(self, A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    def video_frame_checker(self):
        """
        1. try to determine the total number of frames in the video file
        2. an error occurred while trying to determine the total
        3. number of frames in the video file
        """
        try:
            prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() \
                else cv2.CAP_PROP_FRAME_COUNT
            total = int(self.vs.get(prop))
            print("[INFO] {} total frames in video".format(total))
        except:
            print("[INFO] could not determine # of frames in video")
            print("[INFO] no approx. completion time can be provided")
            total = -1
        return total

    def generate_color(self):
        """
       initialize a list of colors to represent each possible class label
        """
        np.random.seed(42)
        colors = np.random.randint(0, 255, size=(200, 3), dtype="uint8")
        return colors

    def run_bot(self):
        print("BOT RUNNING...")
        tracker = Sort()
        counter = 0
        while True:

            # read the next frame from the file
            (grabbed, frame) = self.vs.read()

            # if the frame was not grabbed, then we have reached the end of the stream
            if not grabbed:
                break

            # if the frame dimensions are empty, grab them
            if self.W is None or self.H is None:
                (self.H, self.W) = frame.shape[:2]

            # construct a blob from the input frame and then perform a forward
            # pass of the YOLO object detector, giving us our bounding boxes
            # and associated probabilities
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                         swapRB=True, crop=False)
            self.net.setInput(blob)
            start = time.time()
            layerOutputs = self.net.forward(self.ln)
            end = time.time()

            # initialize our lists of detected bounding boxes, confidences,
            # and class IDs, respectively
            boxes = []
            confidences = []
            classIDs = []

            # loop over each of the layer outputs
            for output in layerOutputs:
                # loop over each of the detections
                for detection in output:
                    # extract the class ID and confidence (i.e., probability)
                    # of the current object detection
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]

                    # filter out weak predictions by ensuring the detected
                    # probability is greater than the minimum probability
                    if confidence > self.confidence_level:
                        # scale the bounding box coordinates back relative to
                        # the size of the image, keeping in mind that YOLO
                        # actually returns the center (x, y)-coordinates of
                        # the bounding box followed by the boxes' width and
                        # height
                        box = detection[0:4] * np.array([self.W, self.H, self.W, self.H])
                        (centerX, centerY, width, height) = box.astype("int")

                        # use the center (x, y)-coordinates to derive the top
                        # and and left corner of the bounding box
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))

                        # update our list of bounding box coordinates,
                        # confidences, and class IDs
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)

            # apply non-maxima suppression to suppress weak, overlapping
            # bounding boxes
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_level, self.threshold)

            dets = []
            if len(idxs) > 0:
                # loop over the indexes we are keeping
                for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    dets.append([x, y, x + w, y + h, confidences[i]])

            np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
            dets = np.asarray(dets)
            tracks = tracker.update(dets)

            boxes = []
            indexIDs = []
            c = []
            previous = self.memory.copy()
            self.memory = {}

            for track in tracks:
                boxes.append([track[0], track[1], track[2], track[3]])
                indexIDs.append(int(track[4]))
                self.memory[indexIDs[-1]] = boxes[-1]

            if len(boxes) > 0:
                i = int(0)
                for box in boxes:
                    # extract the bounding box coordinates
                    (x, y) = (int(box[0]), int(box[1]))
                    (w, h) = (int(box[2]), int(box[3]))

                    # draw a bounding box rectangle and label on the image
                    # color = [int(c) for c in COLORS[classIDs[i]]]
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

                    color = [int(c) for c in self.COLORS[indexIDs[i] % len(self.COLORS)]]
                    cv2.rectangle(frame, (x, y), (w, h), color, 2)

                    if indexIDs[i] in previous:
                        previous_box = previous[indexIDs[i]]
                        (x2, y2) = (int(previous_box[0]), int(previous_box[1]))
                        (w2, h2) = (int(previous_box[2]), int(previous_box[3]))
                        p0 = (int(x + (w - x) / 2), int(y + (h - y) / 2))
                        p1 = (int(x2 + (w2 - x2) / 2), int(y2 + (h2 - y2) / 2))
                        cv2.line(frame, p0, p1, color, 3)

                        if self.intersect(p0, p1, self.line[0], self.line[1]):
                            counter += 1
                            print("[INFO] Frame {} object id {}:{} passed the line coord = {}".format(self.frameIndex,
                                                                                                      indexIDs[i],
                                                                                                      self.LABELS[
                                                                                                          classIDs[i]],
                                                                                                      previous_box))
                            print("\n")

                            temp = []
                            # ['FRAME','INDEX','TYPE','CFLVL']
                            temp = {'FRAME': self.frameIndex, 'INDEX': indexIDs[i], 'TYPE': self.LABELS[classIDs[i]],
                                    'CFLVL': confidences[i]}
                            self.writer_csv.append_data(temp)

                    # text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                    # text = "{}".format(indexIDs[i])
                    text = "{}={}: {:.4f}".format(indexIDs[i], self.LABELS[classIDs[i]], confidences[i])
                    # print("object id registered{}={}: {:.4f} \n".format(indexIDs[i], LABELS[classIDs[i]], confidences[i]))
                    cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    i += 1

            # draw line
            cv2.line(frame, self.line[0], self.line[1], (0, 255, 255), 5)

            # draw counter
            cv2.putText(frame, str(counter), (100, 200), cv2.FONT_HERSHEY_DUPLEX, 5.0, (0, 255, 255), 10)
            # counter += 1

            # saves image file
            cv2.imwrite("output/frame-{}.png".format(self.frameIndex), frame)

            # check if the video writer is None
            if self.writer is None:
                # initialize our video writer
                fourcc = cv2.VideoWriter_fourcc(*"MJPG")

                self.writer = cv2.VideoWriter(self.output, fourcc, 30,
                                              (frame.shape[1], frame.shape[0]), True)

            # some information on processing single frame
            # if self.total > 0:
            #	elap = (end - start)
            #	print("[INFO] single frame took {:.4f} seconds".format(elap))
            #	print("[INFO] estimated total time to finish: {:.4f}".format(
            #		elap * self.total))

            # write the output frame to disk
            self.writer.write(frame)

            # increase frame index
            self.frameIndex += 1

            if self.frameIndex >= 4000:
                print("[INFO] cleaning up...")
                self.writer.release()
                self.vs.release()
                exit()

        # release the file pointers

        print("[INFO] cleaning up...")
        writer.release()
        vs.release()
