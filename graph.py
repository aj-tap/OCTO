import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter


class GraphCSV:

    def __init__(self, filename="result.csv"):
        self.filename = filename
        self.frame = []
        self.index = []
        self.confidence_lvl = []
        self.type_of_object = []

    def get_data_arr(self):
        with open(self.filename, 'r', ) as csvfile:
            file = csv.DictReader(csvfile)
            for col in file:
                self.frame.append(int(col['FRAME']))
                self.index.append(int(col['INDEX']))
                self.confidence_lvl.append(float(col['CFLVL']))
                self.type_of_object.append(col['TYPE'])

    def print_data(self):
        for i in range(len(self.frame)):
            print("Frame: ", self.frame[i], "object: ", self.type_of_object[i], "ID: ", self.index[i])

    def plot_data_scatter(self):
        x1 = np.asarray(self.frame)
        y1 = np.asarray(self.confidence_lvl)
        plt.scatter(x1, y1)
        plt.title('Objects Detected')
        plt.xlabel('Frames')
        plt.ylabel('Confidence Level')
        plt.show()
        print(x1)
        print(y1)

    def plot_data_bar(self):
        obj_types = Counter(self.type_of_object)
        x = np.array(list(obj_types.keys()))
        y = np.array(list(obj_types.values()))
        plt.title('Number of Objects Detected')
        plt.xlabel('Object Type')
        plt.ylabel('Detected')
        plt.bar(x, y)
        plt.show()
## for debuging 
#test = GraphCSV()
#test.get_data_arr()
#test.print_data()
#test.plot_data_bar()
#test.plot_data_scatter()
