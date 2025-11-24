# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 14:54:04 2021

@author: Ahmed EL-brawany
"""

import cv2 as cv
import numpy as np
import sys

sys.path.append('../')



class money_recognition:
    # names of the objects available for detection.
    classes_names = ['0.25', '0.5', '1', '5', '10', '20', '50','100', '200']

    __instance = None  # Singleton instance

    def __init__(self):
        """
        constructor of the object_recognition class.
        """

        if money_recognition.__instance != None:
            raise Exception("Singleton can not be instantiated more then once!")
        else:
            money_recognition.__instance = self
            self.name = 'money'

            self.confThreshold = 0.2  # confidence threshold
            self.nmsThreshold = 0.5  # non-maximum suppression threshold

            model_configuration = r"/home/pi/Desktop/Organized/Money_Recognition/yolov4-tiny-obj.cfg"  # path to the model configuration

            model_weights = r"/home/pi/Desktop/Organized/Money_Recognition/yolov4-tiny-obj_last.weights"  # path to model weights

            self.network = cv.dnn.readNetFromDarknet(model_configuration, model_weights)  # load model configuration and weights into a network

            self.network.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)  # Ask network to use specific computation backend where it supported
            self.network.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)  # Ask network to make computations on specific target device

    @staticmethod
    def get_instance():
        """
        this method is used to return a singleton instance of the factory class, and ensure that only one instance is created.
        :return: Singleton instance of the object_recognition class
        """
        if money_recognition.__instance == None:
            money_recognition()
        return money_recognition.__instance

    def get_input(self, img):
        """
        This method is responsible for accepting the input image and prepare it for output processing
        :param img: image taken from camera.
        :return: None
        """
        # self.img = cv.imread("test_dir.png")
        self.img = img
        print(self.img.shape)

        # convert the image into a Blob image
        blob_img = cv.dnn.blobFromImage(self.img, 1 / 255, (416, 416), [0, 0, 0], 1, crop=False)
        print(blob_img.shape)

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

        print(outputNames)

        outputs = self.network.forward(outputNames)
        text = self.__get_text(self.__find_money(outputs))
        if not text:
            text += "no money detected."
        text = "Money result: " + text
        print(text)
        return text

    def __find_money(self, outputs):
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
                    x  = int(x - w/2)
                    y= int(y-h/2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

        print(len(bbox))

        indices = cv.dnn.NMSBoxes(bbox, confs, self.confThreshold, self.nmsThreshold)
        money_detected = []
        for i in indices:
            i = i[0]

            money_detected.append(self.classes_names[classIds[i]])
            
        return money_detected
    
    def __get_text(self, money_list):
        text = ''
        for money in money_list:
            text += f'{money} EGP, '
            
        if money_list:
            text = 'I have recognized ' + text

        return text


