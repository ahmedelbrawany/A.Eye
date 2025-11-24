import cv2
import pytesseract
import numpy as np
from scipy.ndimage import interpolation as inter

class OCR:
    
    __instance = None
    
    def __init__(self):
        if OCR.__instance !=None:
            raise Exception("Singleton can not be instantiated more than once!")
        else:
            OCR.__instance = self
            self.name = "OCR"
            
    @staticmethod
    def get_instance():
        if OCR.__instance == None:
            OCR.__instance = OCR()
        return OCR.__instance

        
    def resize(self, img):
        """Method to grayscale the input image and resize it over 300 DPI

        :param img: image taken as input
        :type img: ndarray
        :returns: img: grayscaled and resized image
        """
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
        return img
        
    def binarize(self, img):
        """Method to binarize gray image using thresholding
        
        :param img: image from the previous pipeline phase
        :type img: ndarray
        :returns: img: binarized image using CLAHE histogram and thresholding
        """
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 3)
        #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        return img
    
    def __find_score(self, arr, angle):
        """Method to find rotation score used by the skewing method
            
        :param arr: image from previous pipeline stage in array format
        :type arr: ndarray
        :param angle: slope angle of the image
        :type angle: ndarray
        :returns:
            - hist
            - score
        """
        data = inter.rotate(arr, angle, reshape=False, order=0)
        hist = np.sum(data, axis=1)
        score = np.sum((hist[1:] - hist[:-1]) ** 2)
        return hist, score

    def skew(self, img):
        """Method to skew sloped images
        
        :param img: image taken as input from previous pipeline stage
        :type img: ndarray
        :returns: data: image after being skewed
        """
        delta = 1
        limit = 5
        angles = np.arange(-limit, limit+delta, delta)
        scores = []
        for angle in angles:
            hist, score = self.__find_score(img, angle)
            scores.append(score)
        best_score = max(scores)
        best_angle = angles[scores.index(best_score)]
        # correct skew
        data = inter.rotate(img, best_angle, reshape=False, order=0)
        return data
        
    def removeNoise(self, img):
        """Method to remove noise by blurring filters

        :param img: image taken as input from pipeline
        :type img: ndarray
        :returns: img: image after being blurred and denoised
        """
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.filter2D(img, -1, kernel)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        img = cv2.medianBlur(img, 1)
        return img
    
    def remove_borders(self, image):
        """Method to remove unnecessary borders from image

        :param image: image taken as input from pipeline
        :type img: ndarray
        :returns: crop: image after being borders-croped
        """
        contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = lambda x:cv2.contourArea(x))
        cnt = contours[-1]
        x,y,w,h = cv2.boundingRect(cnt)
        crop = image[y:y+h, x:x+w]
        return (crop)
    

    def get_input(self, img):
        """Method to call from object to get input to the class

        :param img: image taken as input
        :type img: ndarray
        :returns: None
        """
        self.img = img
    
    def output(self):
        """Pipeline used to recognize and extract text from image

        :returns: text: text recognized by tesseract
        """
        custom_config = r'--oem {} --psm {}'.format(1, 3)
        text = pytesseract.image_to_string(self.img, lang='eng', config=custom_config)
        if text.strip() == '':
            text = 'no text has been detected'
        text = "Read result: " + text
        return text
    


