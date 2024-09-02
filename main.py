import pyttsx3
import speech_recognition 
import requests
import pyautogui
from bs4 import BeautifulSoup       #FOR WEBSCRAPPING(API)
import datetime
import os
import keyboard
import speedtest
import pyjokes


for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from intro import play_gif
play_gif



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



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetMe import greetMe
            greetMe(query)

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Sure boss , just say wake up whenever you need my help")
                    break


                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done boss")
                    speak(f"Your new password is{new_pw}")

            

                elif "hello" in query:
                    speak("hello ma'am , how are you ?")

                elif "i am fine" in query:
                    speak("good to hear that")

                elif "are you a robot" in query:
                    speak("Yes I am a robot, but I'm a good one. Let me prove it. How can I help you?")

                elif "how can you help me" in query:
                    speak("I can help you with many things such as Answering your questions and help you in your daily tasks easily ")

                elif "how are you" in query:
                    speak("great boss")


                elif "thank" in query:
                    speak("my pleasure boss")

                elif 'tell me a joke' in query:
                   joke = pyjokes.get_joke()
                   speak(joke)

                elif "open" in query:
                    from application import openappweb
                    openappweb(query)
                elif "close" in query:
                    from application import closeappweb
                    closeappweb(query)

                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                

                elif "calculate" in query:
                    from calculator import WolfRamAlpha
                    from calculator import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                elif "whatsapp" in query:
                    from WhatsApp import sendMessage
                    sendMessage()

                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "pause" in query:
                     pyautogui.press("k")
                     speak("video paused")
                elif "play" in query:
                     pyautogui.press("k")
                     speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temprature in delhi is "
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search = "Weather check in delhi is "
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "news" in query:
                    from newsRead import latestnews
                    latestnews()

                elif "translate" in query:
                    from translator import translategl
                    query = query.replace("eve","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

                elif "let's have a game" in query:
                    from game import game_play
                    game_play()

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")




                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"ma'am, the time is {strTime}")

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break


                elif "finally sleep" in query:
                        speak("Going to sleep,ma'am")
                        exit()


''' import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
from requests import get
import sys
import time
import os
import cv2
import pywhatkit
import pyjokes
import pyautogui





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Eva mam. Please tell me how may I help you")

def takeCommand():
    it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS','YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ADDRESS ', to, content)
    server.close()

#for latest news
def news():
    main_url = ""

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"Today's {day[i]} news is : ",head[i])
        speak(f"Today's {day[i]} news is : {head[i]}")

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query

        if 'hii' in query:
            speak("Hello Boss. How may I help you?")

        elif 'how are you' in query:
            speak("I am fine boss. You say how are you doing?")

        elif 'i am good' in query:
            speak("Good to hear boss. Have you taken up your meal")

        elif 'yes i already had my meal' in query:
            speak("That's great. Please tell me what should i do next")

        elif 'i am not feeling well today what to do' in query:
            speak("Please go to the doctor boss and make sure you follow the diet to ensure good health")

        elif 'open word' in query:
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(wordPath)

        elif 'open excel' in query:
            excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(excelPath)

        elif 'open powerpoint' in query:
            pointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(pointPath)

        elif 'open outlook' in query:
            outlookPath = "C:\\Users\\charu\\AppData\\Local\\Packages\\Microsoft.OutlookForWindows_8wekyb3d8bbwe"
            os.startfile(outlookPath)

        elif 'open office' in query:
            offciePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office Tools"
            os.startfile(officePath)

        elif 'open paint' in query:
            paintPath = "C:\\Users\\charu\\AppData\\Local\\Packages\Microsoft.Paint_8wekyb3d8bbwe"
            os.startfile(paintPath)

        elif 'open solitaire gameS' in query:
            solitairepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Games\\Solitaire with Themes.lnk"
            os.startfile(solitairepath)

        elif 'open amazon' in query:
            amapath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Amazon.com.lnk"
            os.startfile(amapath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("mam, what should i search on youtube")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open google' in query:
            speak("mam, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'send whatsapp message' in query:
            kit.sendwhatmsg("+917836989080", "this is testing msg",4,133)
            time.sleep(120)
            speak("Message has been sent")


        elif 'play music' in query:
            music_dir = "C:\\Users\\charu\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            speak("Your IP Address is {ip}")
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\charu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'song on youtube' in query:
            kit.playonyt("see you again")

        elif 'email to charu' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "EMAIL TO THE OTHER PERSON"
                sendEmail(to,content)
                speak("Email has been sent to charu")

            except Exception as e:
                print(e)
                speak("Sorry Ma'am, I am not able to send this mail to charu")
                      
        elif 'you can sleep' in query:
            speak("Thankyou for using me Ma'am , Have a Nice Day")
            sys.exit()
        
        elif 'close word' in query:
            speak("Okay Ma'am , closing word")
            os.system("taskill /f /im word.exe")

        #to set an alarm
        elif "set alarm" in query:
            mn = int(datetime.datetime.now().hour)
            if mn==22:
                music_dir = "C:\\Users\\charu\\Music"
                songs = os.listdir(music_dir)
                os.startfile(os.oath.join(music_dir,songs[0]))
        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dil,SetSuspendState 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'tell me the news' in query:
            speak("Fetching the latest news ma'am. It may take a while..loading please wait... ")
            news()
        
        elif "write an email" in query:
                    print("To whom do you want to send email?")
                    speak("To whom do you want to send email?")

                    recipient_name = takeCommand().lower()
                    from sendemail import recipient_mapping
                    recipient_email = recipient_mapping.get(recipient_name)

                    if recipient_email:
                        print("what is the subject of the email")
                        speak("what is the subject of the email")

                        subject = takeCommand().lower()
                        from sendemail import send_email
                        from sendemail import sender_email
                        from sendemail import sender_password

                        print("What is the message of the email?")
                        speak("What is the message of the email?")
                        content = takeCommand().lower()

                        send_email(sender_email, sender_password, recipient_email, subject, content)

                    else:
                        print("Sorry! I am not able to find your address details.")
                        speak("Sorry! I am not able to find your address details.")



        
    '''