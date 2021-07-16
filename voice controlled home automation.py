from tkinter import *
from PIL import ImageTk,Image
import pyttsx3 ##used for speak engine
import speech_recognition as sr # used for voice to text conversion
import threading
import datetime
from boltiot import Bolt
class led_control:
    
    def onled(self,x):
        api_key = "YOUR API KEY"
        device_id  = "YOUR DEVICE ID"
        mybolt = Bolt(api_key, device_id)
        response = mybolt.digitalWrite(x,'HIGH')
        print (response)
    def offled(self,x):
        api_key = "YOUR API KEY"
        device_id  = "YOUR DEVICE ID"
        mybolt = Bolt(api_key, device_id)
        response = mybolt.digitalWrite(x,'LOW')
        print (response)
    
        
a=led_control()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
    # print(voices[1].id)
engine.setProperty('voice', voices[0].id)
    
class ActivateJarvis:
    def __init__(self):

        self.__speak("Intializing..")
        print("Intializing ..")
        self.__speak("Welcome back sir ")
    

    def __speak(self,audio):
        engine.say(audio)
        engine.runAndWait()
    def wishme(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.__speak("Good Morning!")

        elif hour>=12 and hour<18:
            self.__speak("Good Afternoon!")   

        else:
            self.__speak("Good Evening!")  

        self.__speak("I am Jarvis Sir. Please tell me how may I help you")
        #request=self.__takecommand()
        self.__run()
        
    
    def __takecommand(self):
        self.r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            self.r.pause_threshold=0.5
            self.audio=self.r.listen(source)
        try:
            print("Recognizing...")
            self.query=self.r.recognize_google(self.audio,language='en-in')
            print("{}".format(self.query))
        except Exception as e:
            print("Please say again..")
            return "None"
        return self.query
    def __run(self):
        
        
        while True:
            self.requestQuery=self.__takecommand().lower()
            
            if "green" in self.requestQuery and "on" in self.requestQuery:
                a.onled(1)
            elif "green" in self.requestQuery and "off" in self.requestQuery:
                a.offled(1)
            elif "blue" in self.requestQuery and "on" in self.requestQuery:
                a.onled(2)
            elif "blue" in self.requestQuery and "off" in self.requestQuery:
                a.offled(2)
            elif "read" in self.requestQuery and "on" in self.requestQuery:
                a.onled(3)
            elif "read" in self.requestQuery and "off" in self.requestQuery:
                a.offled(3)
            elif "exit" in self.requestQuery:
                exit()
                
        
        




root =Tk()
root.geometry("600x630")
root.title("JARVIS")
root.configure(bg="black")
root.iconbitmap('Jarvis31.ico')
file = 'Jarvis3.gif'
info=Image.open(file)
#print(info)
frames=info.n_frames
#print(frames)
im=[PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
count=0
def animation(count):
    b.destroy()
    im2=im[count]
    gif.configure(image=im2)
    count+=1
    if count==frames:
        count=0
    root.after(50,lambda:animation(count))        


if __name__=="__main__":
    

    gif=Label(image="")
    gif.pack()
    b=Button(root,text="start",command=lambda:animation(count))
    b.pack()
    AJ=ActivateJarvis()
    j=Button(root,text="",fg="white",bg="black",padx=500,command=threading.Thread(target=lambda:AJ.wishme()).start())
    j.pack()
    
