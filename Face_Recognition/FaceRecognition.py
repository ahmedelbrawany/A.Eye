
import numpy as np
import face_recognition as frc
import cv2 as cv
import sys
sys.path.append('../')
from Face_Recognition.Face_Register import *

class FaceRecognition:

    __instance = None
    
    def __init__(self):
        if FaceRecognition.__instance != None:
            raise Exception("Singleton can not be instantiated more than once!")
        else:
            try:
                self.people = np.load('/home/pi/Desktop/Organized/Face_Recognition/people/people.npy', allow_pickle=False)
            except:
                print("error 1")
                self.people = np.array([])
                
            self.names = []
            with open('/home/pi/Desktop/Organized/Face_Recognition/people/people.txt', 'r+') as file:
                x = file.readlines()
                for line in x:
                    self.names.append(line)
                
            self.name = "people"
            self.register = register(self.people)
            FaceRecognition.__instance = self

    @staticmethod
    def get_instance():
        if FaceRecognition.__instance == None:
            FaceRecognition.__instance = FaceRecognition()
        return FaceRecognition.__instance
            
    def get_input(self, image):
        """Method to get image as input

        :param image: numpy image used as input to the model
        :type image: ndarray
        :returns: None
        """
        self.numpyImage = image
        self.numpyImage = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        self.people = np.load('/home/pi/Desktop/Organized/Face_Recognition/people/people.npy', allow_pickle=False)
        self.register.people = self.people

    def output(self):
        """Test method used to recognize known personnals
        
        :returns: text: text describing the result of the recognition model
        """
        faces = frc.face_locations(self.numpyImage)
        encodings = frc.face_encodings(self.numpyImage, faces)
        
        matches = None
        text = ''
        for codec, face in zip(encodings, faces):
            matches = frc.compare_faces(self.people, codec, tolerance = 0.55) #threshold
            print(matches)

            for i in range(len(matches)):
                if matches[i]:
                    text += self.names[i]
        if text == '':
            text = 'no face has been recognized'
                
        text = "people result: " + text
        print(text)
        return text