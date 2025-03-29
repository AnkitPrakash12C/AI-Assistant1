import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import pywhatkit
import requests
from Demos.mmapfile_demo import page_size
from newsapi import NewsApiClient
from scripts.regsetup import description
from wikipedia import languages
import clipboard
import os
import psutil
import time as t

engine  = pyttsx3.init()

def speech(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice== 1:
        engine.setProperty('voice', voices[0].id)
        speech("Hello")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speech("Hello")

    speech("how are you?")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speech("The current time is " + Time)

def date():
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now().strftime("%B")
    date = int(datetime.datetime.now().day)
    speech("Today's date is " + str(date) + " " + month + " " + str(year))

def greetings():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speech("Good morning, how can I help you?")
    elif hour >= 12 and hour < 18:
        speech("Good afternoon, how can I help you?")
    elif hour >= 18 and hour < 22:
        speech("Good evening, how can I help you?")
    else:
        speech("Good night, how can I help you?")

def wishme():
    speech("Welcome back, what can i help you with?")

def searchGoogle():
    speech("What should I search on Google?")
    search = takeCommandMic()
    speech("Searching on Google...")
    wb.open('https://www.google.com/search?q=' + search)

def news():
    newsapi = NewsApiClient(api_key='7dd122eb25aa46e6807e4908f5aa6af1')
    speech("On which topic do you want to hear the news?")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q= topic,language='en', page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y[description]}')
        speech((f'{x}{y[description]}'))

    speech("That's it for now")

def text2speech():
    text = clipboard.paste()
    print(text)
    speech(text)

def screenshot():
    name_img = t.time()
    name_img = f'D:\Sem6\AI-Assistant1\screenshots\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def getBattery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    if percent >= 75:
        speech("Battery is good"+ str(percent) + " percent")
    elif percent >= 40 and percent < 75:
        speech("Battery is moderate"+ str(percent) + " percent")
    elif percent >= 15 and percent < 40:
        speech("Battery is low"+ str(percent) + " percent")
    else:
        speech("Battery is critical"+ str(percent) + " percent")



# voice = int(input("Press 1 for male voice.\nPress 2 for female voice"))
# getvoices(voice)

# while True:
#     audio = input("Enter the text you want to convert to speech (or 'bye' to quit): \n")
#
#     if audio.lower() == 'greetings':
#         greetings()
#         continue
#
#     if audio.lower() == 'date':
#         date()
#         continue
#     if audio.lower() == 'time':
#         time()
#         continue
#     if audio.lower() == 'bye':
#         speech("Goodbye")
#         break
#     speech(audio)

#http://api.openweathermap.org/data/2.5/weather?q={City Name)&units=imperial&appid=(c770033c605911f05f2e0f60bfaaacb1)

def takeCommandCMD():
    query = input("How can I help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speech("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommandMic().lower()

        if 'time' in query:
            time()
            continue

        if 'date' in query:
            date()
            continue

        if 'greeting' in query:
            greetings()
            continue

        if 'wikipedia' in query:
            speech("searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speech(result)

        elif 'google' in query:
            searchGoogle()
            continue

        elif 'video' in query:
            speech("Which youtube video do you want to play?")
            topic = takeCommandMic()
            speech("Playing on youtube...")
            pywhatkit.playonyt(topic)

        elif 'weather' in query:
            city = 'jamshedpur'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=c770033c605911f05f2e0f60bfaaacb1'
            res = requests.get(url)
            data = res.json()

            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            desp = data['weather'][0]['description']
            wind = data['wind']['speed']
            humidity = data['main']['humidity']

            print(weather)
            print(temp)
            print(desp)
            print(wind)
            print(humidity)

            speech(f'Weather in {city} is')
            speech('Temperature : {} degree Celsius'.format(temp))
            speech('Weather is {}'.format(desp))
            speech('Humidity is {}'.format(humidity))
            speech('Wind speed is {}'.format(wind))
            continue

        elif 'news' in query:
            speech("Fetching news...")
            news()
            continue

        elif 'read' in query:
            text2speech()
            continue

        elif 'open' in query:
            path = 'E:\Mine\Ben 10\Ben 10 Alien Force\Ben 10 Alien Force S02E01 Dual Audio 720p HD WEB-DL - DeadToonsIndia.mkv'
            os.startfile(path)

        elif 'screenshot' in query:
            screenshot()

        elif 'battery' in query:
            getBattery()

        elif 'play songs' in query:
            songs_dir = 'C:\\Users\\Ankit Prakash\\Desktop\\Heart\\HeartM'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            continue

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        if 'bye' in query:
            speech("Goodbye")
            break


