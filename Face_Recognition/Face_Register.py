import numpy as np
import face_recognition as frc


class register:
    
    def __init__(self, people):
        self.people = people  #np.load('people/people.npy', allow_pickle=False)
    
    def train(self, numpyImage):
        """Train method used to recognize and add encodings of new faces
                
        :param numpyImage: the numpy array equivalent of an RGB camera snapshot
        :type numpyImage: ndarray
        :returns: None
        """
        faces = frc.face_locations(numpyImage)
        try:
            encodings = frc.face_encodings(numpyImage, faces)[0]
        except:
            return 0 
            
        encodings = np.array(encodings).reshape(1, 128)
        print(encodings.shape)
        #print(self.people.shape)
        print(self.people)
        
        if np.size(self.people) == 0: 
            print("emptyyyyyy")
            self.people = encodings
        else:
            print("not emptyyyyyy")
            self.people = np.vstack((self.people, encodings)) # When resetting people.npy file, comment out this file
        
        np.save('/home/pi/Desktop/Organized/Face_Recognition/people/people.npy', self.people, allow_pickle=False)
        return 1


