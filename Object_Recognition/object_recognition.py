# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:54:04 2021

@author: Ahmed EL-brawany
"""

import cv2 as cv
import numpy as np
import sys

sys.path.append('../')
from Object_Recognition.Object_Distance import Object_Distance as od
from camera.camera import *
from Output_Texts.Texts import *


class object_detection:
    # names of the objects available for detection.
    classes_names = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train',
                     'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter',
                     'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
                     'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase',
                     'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat',
                     'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle',
                     'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                     'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut',
                     'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable', 'toilet',
                     'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
                     'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
                     'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

    __instance = None  # Singleton instance

    def __init__(self):
        """
        constructor of the object_recognition class.
        """

        if object_detection.__instance != None:
            raise Exception("Singleton can not be instantiated more then once!")
        else:
            object_detection.__instance = self
            self.name = 'object'
            
            # list of tuples which contains objects detected and their distance from the camera
            self.objects_detected = []
            # list of objects center x coordinates in the image to specify the object in which direction (left, front, right).
            self.objects_center = []   

            self.confThreshold = 0.2  # confidence threshold
            self.nmsThreshold = 0.5  # non-maximum suppression threshold
            
            # path to the model configuration
            model_configuration = r"/home/pi/Desktop/Organized/Object_Recognition/yolov4-tiny.cfg"  
            # path to model weights
            model_weights = r"/home/pi/Desktop/Organized/Object_Recognition/yolov4-tiny.weights"  

            self.network = cv.dnn.readNetFromDarknet(model_configuration, model_weights)  # load model configuration and weights into a network

            self.network.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)  # Ask network to use specific computation backend where it supported
            self.network.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)  # Ask network to make computations on specific target device

    @staticmethod
    def get_instance():
        """
        this method is used to return a singleton instance of the factory class, and ensure that only one instance is created.
        :return: Singleton instance of the object_recognition class
        """
        if object_detection.__instance == None:
            object_detection()
        return object_detection.__instance

    def get_input(self, img):
        """
        This method is responsible for accepting the input image and prepare it for output processing
        :param img: image taken from camera.
        :return: None
        """
        # self.img = cv.imread("test_dir.png")
        self.img = img
        #print(self.img.shape)

        # convert the image into a Blob image
        blob_img = cv.dnn.blobFromImage(self.img, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)
        #print(blob_img.shape)

        # pass the image into the network input
        self.network.setInput(blob_img)

    def output(self):
        """
        this method is responsible for processing the image in the network and gives an info text about the objects
        detected in the image and their distances from the camera.
        :return: to be continued...
        """
        layers_names = self.network.getLayerNames()
        # print(layers_names)

        outputNames = [layers_names[i[0] - 1] for i in self.network.getUnconnectedOutLayers()]

        #print(outputNames)

        outputs = self.network.forward(outputNames)
        self.__find_objects(outputs)
        text = self.__get_text()
        self.objects_detected.clear()
        self.objects_center.clear()
        if not text:
            text += "no objects detected."
        text = "Object result: " + text
        #print(text)
        return text


    def __find_objects(self, outputs):
        """
        This method is responsible for adding bounding boxes to the objects in the image, applying
        non-maximal suppression, and provide object width in pixels for object distance calculation
        :param outputs: network output information
        :return: None
        """
        hT, wT, c = self.img.shape
        bbox = []
        classIds = []
        confs = []
        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > self.confThreshold:
                    w, h = int(det[2] * wT), int(det[3] * hT)
                    x, y = int(det[0] * wT), int(det[1] * hT)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

        #print(len(bbox))

        indices = cv.dnn.NMSBoxes(bbox, confs, self.confThreshold, self.nmsThreshold)

        for i in indices:
            i = i[0]
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            obdist = od(w, self.classes_names[classIds[i]])
            dist = obdist.calculate()

            self.objects_detected.append((self.classes_names[classIds[i]], dist))
            self.objects_center.append(x)

                

    def __get_text(self):
        """
        this method is used to generate text containing info about objects detected, their directions
        and distances from the camera
        :return: info text about objects detected, their directions and distances from the camera
        """
        texts_object = Texts()
        return texts_object.get_object_text(self.img.shape, self.objects_detected, self.objects_center)


