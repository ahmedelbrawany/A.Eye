# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:04:03 2021

@author: Ahmed EL-brawany
"""

from gtts import gTTS
import os, subprocess



class text_to_speech:
    
    __instance = None
    
    def __init__(self):
        if text_to_speech.__instance != None:
            raise Exception("Singleton can not be instantiated more than once!")
        else:
            text_to_speech.__instance = self

            

        
    @staticmethod
    def get_instance():
        if text_to_speech.__instance == None:
            text_to_speech.__instance = text_to_speech()
        return text_to_speech.__instance
    
    def conf_param(self, text, name, language = 'en'):
        self.text = text
        self.language = language
        self.output_filename = f'../output_mp3/output_{name}.mp3'
    
    def mimic_output(self):
        os.system(fr'cd /home/pi/mimic && ./mimic -t "{self.text}" -voice slt_hts -o /home/pi/Desktop/Organized/output_mp3/{self.output_filename}')
        self.__play_mp3()
        
    def gtts_output(self):
        self.__generate_mp3()
        self.__play_mp3()
        
        
    def __generate_mp3(self):
        print("gen")
        self.output = gTTS(text= self.text, lang= self.language, slow=False)
        self.output.save(self.output_filename)
        print("finish")


    def __play_mp3(self):
        print("playing")
        os.system(f'mpv {self.output_filename}')








