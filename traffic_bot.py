## Libraries 
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import glob
from sort import *

class TrafficBot:

    def __init__(self, yoloDir, inputFile):
        
        # Sort 
        self.tracker = Sort()
        self.memory = {}
        #self.counter = 0


        # input footage
        #self.inputFile = inputFile ### Dups remove it


        # paths to the YOLO weights, model configuration and coco class labels
        self.weightPath = os.path.sep.join([yoloDir, "yolov4.weights"])
        self.configPath = os.path.sep.join([yoloDir, "yolov4.cfg"])
        
        self.labelsPath = os.path.sep.join([yoloDir, "coco.names"])
        self.LABELS = open(self.labelsPath).read().strip().split("\n")

        # YOLO object detector trained on COCO dataset 
        print("[INFO] loading YOLO from disk...")
        net = cv2.dnn.readNetFromDarknet(self.configPath, self.weightPath)
        # If nvidia is available
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        # and determine only the *output* layer names that we need from YOLO
        ln = net.getLayerNames()
        ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
        print("[INFO] YOLO  was loaded from disk")


        # initialize the video stream, pointer to output video file, and frame dimensions
        print("[INFO] Loading the input video")
        self.vs = cv2.VideoCapture(inputFile)
        ### variables
        self.writer = None
        (self.W, self.H) = (None, None)
        self.frameIndex = 0
        print("[INFO] video input was sucessfully loaded")
        ###  line = [(179, 442), (1404, 436)]
        ### line = setLine()

        

    def setLine(self):
        """
        set the intersection line or area of interest.  
        """
        pass
  ####################################################################  
    def intersect(self, A,B,C,D):
        """
        Return true if line segments AB and CD intersect
        """
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

    def ccw(self, A,B,C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])


    def vidFrameChecker(self):
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

    def generateColor(self):
        """
       initialize a list of colors to represent each possible class label
        """
        np.random.seed(42)
        colors = np.random.randint(0, 255, size=(200, 3), dtype="uint8")
        return colors

    def runBot(self):
        while True:
            ### Read the next frame 
            (grabbed, frame) = self.vs.read() 
            if not grabbed:
                break

            ### If the frame dimensions are empty, grab them
            if W is None or H is None:
                (H,W) = frame.shape[:2]

            # construct a blob from the input frame and then perform a forward
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
            swapRB=True, crop=False)
            
            # pass of the YOLO object detector, giving us our bounding boxes # and associated probabilities
            net.setInput(blob)
            start = time.time()
            layerOutputs = net.forward(ln)
            end = time.time()
            boxes = []
            confidences = []
            classIDs = []

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
                        if confidence > args["confidence"]:
                            # scale the bounding box coordinates back relative to
                            # the size of the image, keeping in mind that YOLO
                            # actually returns the center (x, y)-coordinates of
                            # the bounding box followed by the boxes' width and
                            # height
                            box = detection[0:4] * np.array([W, H, W, H])
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
                idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"], args["threshold"])