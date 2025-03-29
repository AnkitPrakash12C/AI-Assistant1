import pyttsx3
import datetime
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


voice = int(input("Press 1 for male voice.\nPress 2 for female voice"))
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

def takeCommandCMD():
    query = input("How can I help you?\n")
    return query

if __name__ == "__main__":
    wishme()
    getvoices(2)
    while True:
        query = takeCommandCMD().lower()

        if 'time' in query:
            time()
            continue

        if 'date' in query:
            date()
            continue

        if 'greetings' in query:
            greetings()
            continue

        if 'bye' in query:
            speech("Goodbye")
            break
