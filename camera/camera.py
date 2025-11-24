import cv2 as cv
import numpy as np
import os
from picamera.array import PiRGBArray
from picamera import PiCamera


class camera:

    def __init__(self):
        self.frames = []

        self.stream_flag = 1

    def snapshot(self):
        self.frames.clear()
        self.vid = cv.VideoCapture(0)
        self.vid.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        self.vid.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
        self.vid.set(cv.CAP_PROP_FPS, 20)


        while (True):

            # Capture the video frame
            # by frame
            ret, frame = self.vid.read()

            if ret:
                self.frames.append(frame)

            if len(self.frames)==10:
                break

        # After the loop release the cap object
        self.vid.release()
        blur_values = []
        for frame in self.frames:
            blur_values.append(self.blur_calculations(frame))
            
        
        
        return self.frames[blur_values.index(max(blur_values))]
    
    def blur_calculations(self, img):
        lap_var = cv.Laplacian(img, cv.CV_64F).var()
        return lap_var
    
    def snapshot2(self):
        self.frames.clear()
        self.cam  = PiCamera()
        self.cam.resolution = (640,480)
        self.cam.framerate = 30
        self.rawCapture = PiRGBArray(self.cam, size=(640,480))
        for frame in self.cam.capture_continuous(self.rawCapture, format="bgr", use_video_port= True):
            self.frames.append(frame.array)
            if len(self.frames)>=10:
                break
            self.rawCapture.truncate(0)
        
        blur_values = []
        for frame in self.frames:
            blur_values.append(self.blur_calculations(frame))
            
        return self.frames[blur_values.index(max(blur_values))]
    
    def snapshot3(self):
        os.system('raspistill -w 640 -h 480 -o /home/pi/Desktop/Organized/camera/snapshot.jpg')
        


