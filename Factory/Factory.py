import sys

sys.path.append("../")
from Object_Recognition.object_recognition import *
from text_recognition.OCR import *
from Face_Recognition.FaceRecognition import *
from Money_Recognition.MR import *


class Factory:
    __instance = None  # singleton instance

    def __init__(self):
        """
        constructor of the Factory class
        """
        if Factory.__instance != None:
            raise Exception("Singleton can not be instantiated more than once!")
        else:
            Factory.__instance = self
            self.objects = None

    @staticmethod
    def get_instance():
        """
        this method is used to return a singleton instance of the factory class, and ensure that only one instance is created.
        :return: Singleton instance of the Factory class
        """
        if Factory.__instance == None:
            Factory()
        return Factory.__instance

    def get_objects(self, inp):
        """
        This method is the essence of the factory class where it returns an instances of other classes (classes in concern) based on its input.
        :param input: data provided to the factory for it to decide which instance to create.
        :return: returns a list of objects required based on the input provided
        """

        if "object" in inp:
            self.objects=object_detection.get_instance()

        elif "read" in inp:
            self.objects=OCR.get_instance()
            
        elif "people" in inp or "register" in inp:
            self.objects=FaceRecognition.get_instance()
            
        elif "money" in inp:
            self.objects= money_recognition.get_instance()
            
    
        return self.objects


