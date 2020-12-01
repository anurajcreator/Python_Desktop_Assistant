# imported libraries
import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import time
import random

# list for random sorry's
list = ['i did not get that, please repeat', ' say that again please sir', 'pardon me sir']

# voice Engine Settings
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Greetings Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    elif 18 <= hour <= 21:
        speak('Good Evening')
    else:
        speak('Good Night')

    speak("how may i help you")


# Input Function for starting (hiding the processes)
def takeCommandf():
    # Input and returns String
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        #print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        # print("said that again please")
        return "None"
    return query


# Input function for rest of the period.
def takeCommand():
    # Input and returns String
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except ValueError as e:
        exit()
    except Exception as e:
        print(e)
        speak(random.choice(list))
        return "None"
    return query


# main-f dude.
if __name__ == "__main__":
    while True:
        query = takeCommandf().lower()
        if 'hello vision' in query or 'hi vision' in query:
            speak("Hello Mr.Anuraj")
            wishMe()
            while True:
                query = takeCommand().lower()

                if 'wikipedia' in query:
                    speak('Searching...')
                    query = query.replace("wkipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia....")
                    speak(results)
                    print(results)

                elif 'open youtube' in query:
                    wb.open_new("https://www.youtube.com")

                elif 'open google' in query:
                    wb.open_new("https://www.google.com")

                elif 'search youtube for' in query:
                    query = query.replace("search youtube for", "")
                    url = 'https://www.youtube.com/results?search_query='
                    wb.open_new(url + query)

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak("The time is " + strTime)

                elif 'open docs' in query:
                    path = "C:\\Users\\anura\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Docs.lnk"
                    os.startfile(path)

                elif 'open gmail' in query:
                    path = "C:\\Users\\anura\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Gmail.lnk"
                    os.startfile(path)

                elif 'open whatsapp' in query:
                    wb.open_new('https://web.whatsapp.com/')


                elif 'open ng rock' in query:
                    path = "C:\\Users\\anura\\Downloads\\Compressed\\ngrok-stable-windows-amd64\\ngrok.exe"
                    os.startfile(path)

                elif 'open minecraft server' in query or 'open mcss' in query:
                    path = "C:\\Users\\anura\\Downloads\\Compressed\\mcss_win-x86-64_v11.4.1\\mcss.exe"
                    os.startfile(path)

                elif 'open tee launcher' in query or 'open minecraft' in query:
                    path = 'C:\\Users\\anura\\AppData\\Roaming\\.minecraft\\TLauncher.exe'
                    os.startfile(path)

                elif 'what are you doing ' in query :
                    speak("Waiting for your response sir")

                elif ('stop'  or 'sign out' or 'nothing else') in query:
                    break

                elif 'open pycharm' in query:
                    path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
                    os.startfile(path)



        elif 'off' in query or 'shutdown' in query:
            exit()
