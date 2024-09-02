import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3935d08d06af4f9ea74f65ba6cbfeec2",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3935d08d06af4f9ea74f65ba6cbfeec2",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3935d08d06af4f9ea74f65ba6cbfeec2",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3935d08d06af4f9ea74f65ba6cbfeec2",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3935d08d06af4f9ea74f65ba6cbfeec2",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3935d08d06af4f9ea74f65ba6cbfeec2"
    }

    content = None
    url = None
   
    speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    print("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    field = input("Type the field of news that you want: ").lower()

    url = api_dict.get(field)
    if url is None:
        print("Invalid field. Please choose from the available options.")
        return

    print("URL was found:", url)

    news = requests.get(url).json()

    if "articles" not in news:
        print("No articles found in the response.")
        return

    articles = news["articles"]
    speak("Here is the first news.")
    
    for article in articles:
        title = article.get("title")
        if title:
            print(title)
            speak(title)
            news_url = article.get("url")
            if news_url:
                print(f"For more info visit: {news_url}")

            input("[Press 1 to continue] and [Press 2 to stop]: ")
            if input == 2:
                break
        
    speak("That's all")

latestnews()
