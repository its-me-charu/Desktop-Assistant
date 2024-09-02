import pyttsx3
#import speech_recognition 
import datetime



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe(query):
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour >12 and hour<=18:
        speak("Good Afternoon!")
 
    else:
        speak("Good Evening!")

    speak("I am Eva mam. Please tell me how may I help you ?")

