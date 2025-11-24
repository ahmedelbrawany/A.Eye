import sys
sys.path.append('../')
sys.path.append(r'/home/pi/.local/lib/python3.7/site-packages/')
from voice_recognition.voice_recognition import *
from Factory.Factory import *
from voice_recognition.voice_recognition import *
from text_to_speech.text_to_speech import text_to_speech as tts
from camera.camera import *
import cv2 as cv
import os
from time import time
    
def get_name(vr):
    try:
        speak("what is the person name?", "register_error")
    except:
        print("mimic error")

    name = vr.name()
    try:
        speak(f"the name you entered {name} for conformation say yes to try again say no", "test_name")
    except:
        print("mimic error")

    conform = vr.conform()
    if conform == 'yes':
        return name
    else:
        return get_name(vr)
    
def speak(text, status):
    speech = tts.get_instance()
    speech.conf_param(text, status)
    speech.mimic_output()



def main():
    factory = Factory.get_instance()
    vr = voice_recognition()
    cam = camera()
    try:
        speak("I am ready", "ready_to_go")
    except:
        print("mimic error")
    while True:
        vr.start()
        try:
            speak("Welcome to A.EYE", "welcome")
        except:
            print("mimic error")
        while True:
            
            """
            get object from voice recognition
            """
            try:
                speak("Choose a mode.", "welcome")
            except:
                print("mimic error")
                    

            mode = vr.mode()
            mode = mode.lower()
            t1 = time()
            print(f"mode : {mode}")
            if "try again" in mode:
                try:
                    speak(f"I do not know what{mode.split(':')[1]} means", "mode_error")
                    continue
                except:
                    print("mimic error")
            if "sleep now" in mode:
                try:
                    speak("bye for now", "sleep")
                    break
                except:
                    print("mimic error")
            if "shutdown" in mode:
                try:
                    speak("bye bye", "shutdown")
                    os.system("sudo shutdown -h now")
                except:
                    print("mimic error")

            
            obj = factory.get_objects(mode)


            #get image from camera
            im = cam.snapshot()

            
            if 'register' in mode:
                obj.get_input(im)
                t = obj.output()
                success = None
                if 'no face' in t:
                    success = obj.register.train(cv.cvtColor(im, cv.COLOR_BGR2RGB))
                else:
                    try:
                        speak(f"this is {t.split(':')[1]}. registration failed", "register_error")
                        continue
                    except:
                        print("mimic error")
                if not success:
                    try:
                        speak("there is no face detected in the picture registration failed", "register_error")
                        continue
                    except:
                        print("mimic error")
                else:
                    name = get_name(vr)
                    line = f'{len(obj.names)+1}, {name} \n'
                    obj.names.append(line)
                    with open('/home/pi/Desktop/Organized/Face_Recognition/people/people.txt', 'a') as file:
                        file.write(line)

            
            obj.get_input(im)
            t = obj.output()
            print(f'response time : {time()-t1} sec')
            try:
                speak(t, obj.name)
            except:
                print('mimic error')


            

if __name__=="__main__":
    main()



