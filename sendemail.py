import pyttsx3
import smtplib
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening ma'am........")
        r.pause_threshold = 1 
        r.energy_threshold = 300    #voice cancellation

        audio = r.listen(source,0,4)     #4 second wait krega and will move forward

    try:
        print("understanding........")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said : {query}\n")
    except Exception as e:
        print("please say that again")
        return "none"
    return query

def send_email(sender_email, sender_password, recipient_email, subject, content):
    from email.message import EmailMessage
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(content)

    with smtplib.SMTP("smtp.gmail.com", 587):
        server.starttls()
        server.login(sender_email, sender_password)
        server.sender_message(msg)
        
        print("Email sent successfully...")
        speak("Email sent successfully...")

recipient_mapping = {"eve " : "evevoiceassistant@gmail.com"}

sender_email = "xyz@gmail.com"
sender_password = "xyz"