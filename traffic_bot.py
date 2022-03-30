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
        self.configPath = os.path.sep.join([yoloDir, "yolov4.weights"])
        
        self.labelsPath = os.path.sep.join([yoloDir, "coco.names"])
        self.LABELS = open(labelsPath).read().strip().split("\n")

        # YOLO object detector trained on COCO dataset 
        net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
        # If nvidia is available
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        # and determine only the *output* layer names that we need from YOLO
        ln = net.getLayerNames()
        ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]


        # initialize the video stream, pointer to output video file, and frame dimensions
        self.vs = cv2.VideoCapture(inputFile)
        self.writer = None
        (self.W, self.H) = (None, None)
        self.frameIndex = 0

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
        pass
  ####################################################################

