
from vosk import Model, KaldiRecognizer
import pyaudio
# obtain audio from the microphone

class voice_recognition():
    def __init__(self):
        model = Model(r"/home/pi/Desktop/Organized/voice_recognition/vosk-model-small-en-us-0.15")
        self.recognizer = KaldiRecognizer(model, 16000)
        self.cap = pyaudio.PyAudio()
        self.stream = self.cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)


    def name(self):
        self.stream.start_stream()
        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            text =""
            name = ""
            if self.recognizer.AcceptWaveform(data):
                text = self.recognizer.Result()
                text = eval(text)
                name = text['text']         

            if name:
                print(name)
                self.stream.stop_stream()
                #self.stream.close()
                return name
    def conform(self):
        self.stream.start_stream()
        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            text =""
            conform = ""
            if self.recognizer.AcceptWaveform(data):
                text = self.recognizer.Result()
                text = eval(text)
                conform = text['text']
                conform.lower()
            if "yes" in conform:
                conform='yes'
            elif "no" in conform:
                conform = 'no'
            else:
                conform = ''
                
            if conform:
                self.stream.stop_stream()
                #self.stream.close()
                return conform
            
    def start(self):
        self.stream.start_stream()
        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            text =""

            if self.recognizer.AcceptWaveform(data):
                text = self.recognizer.Result()
                text = eval(text)
                text = text['text'].lower()         

            if text=="wake up":
                self.stream.stop_stream()
                #self.stream.close()
                return
            print(text)
            
               
        
    def mode(self):
        self.stream.start_stream()
        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            text =""
            modes_detected = ""
            if self.recognizer.AcceptWaveform(data):
                text = self.recognizer.Result()
                text = eval(text)
                text = text['text'].lower()
                print(text)
                if "object" in text:
                    modes_detected += "object"

                elif "people" in text:
                    modes_detected += "people"

                elif "read" in text:
                    modes_detected += "read"
                    
                elif "register" in text:
                    modes_detected += "register"
                    
                elif "money" in text:
                    modes_detected += "money"
                    
                elif "sleep now" in text:
                    modes_detected += "sleep now"
                    
                elif "shutdown" in text.replace(" ", ""):
                    modes_detected += "shutdown"
                    
                else:
                    if not text == "":
                        modes_detected += "Try again:" + text


            if modes_detected:
                print(modes_detected)
                self.stream.stop_stream()
                return modes_detected
            
        



