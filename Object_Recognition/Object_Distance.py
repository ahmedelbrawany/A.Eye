import math       

class Object_Distance:
    # focal length of Raspberry pi camera
    F = 453

    # average width of all objects in concern
    ObjectWidth = {'person':45,'bicycle':180,'car':175,'motorbike':271,
    'bus':250,'train':320,'truck':260,'bottle': 9,'traffic light':35,
    'fire hydrant':18,'stop sign':76,'boat':563,'book':14,'aeroplane':6440,
    'apple':8,'parking meter':240,'bench':45,'bird':25,'cat':47.5,
    'dog':64.5,'horse':190,'sheep':117,'cow':245,'elephant':500 ,
    'bear':305,'zebra':200,'giraffe':240,'backpack':23,'umbrella':110,
    'handbag':18,'tie':9.5,'suitcase':42,'frisbee':22.5,'skis':160,
    'snowboard':24.5,'sports ball':19,'kite':80,'baseball bat':86.4,
    'baseball glove':3.75,'skateboard':20,'surfboard':50,'fork':20,
    'tennis racket':27,'wine glass':10.8,'cup':11,'knife':33,'sofa':227,
    'spoon':16,'bowl':25,'banana':13,'sandwich':12,'orange':8,'pizza':33,
    'broccoli':46,'carrot':20,'hot dog':15,'donut':9,'cake':27.5,
    'chair':50,'pottedplant':18.5,'bed':76,'diningtable':206,'toilet':51,
    'tvmonitor':132,'laptop':39,'mouse':10,'remote':4,'keyboard':40,
    'cell phone':7,'microwave':50,'oven':60,'toaster':40,'sink':82.5,
    'refrigerator':85,'clock':40,'vase':20,'scissors':22,'teddy bear':25,
    'hair drier':23,'toothbrush':13}
    

    def __init__(self, P , obj):
        """
        constructor of Object_Distance class
        :param P: width of object in pixels.
        :param obj: name of object detected in image.
        """
        self.P = P
        self.obj = obj
        # getting average width of the object
        self.W = self.ObjectWidth[obj] 


 
    # a method for finding distance 
    def calculate(self):
        """
        this method is used to calculate the distance of the object from the camera.
        :return: distance between the object detected and the camera.
        """

        self.D = (self.W  * self.F) / (self.P)

        if self.D >=100:
            return str(math.ceil(self.D/100))
        else:
            return str(round(self.D/100,2))

        


        
