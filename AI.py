import os
import time
import speech_recognition as sr


import pyttsx3
import datetime

# voice Engine Settings
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate' , 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # Input and returns String
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query

path = "D:\Anuraj\Education\open cv\Automation.py"
os.startfile(path)

while True:
    s = takeCommand()
    s = s.lower()
    if 'stop and shutdown friday' in s or 'shutdown friday' in s or 'off friday' in s or 'goodbye friday' in s or 'good night friday' in s or 'tata ' \
                                                                                                                                    'friday' \
            in s:

        hour = int(datetime.datetime.now().hour)
        if 4 <= hour < 20:
            speak('Have a Good day Sir')
        else:
            speak('Good Night Sir')
        os.system("TASKKILL /F /IM py.exe")
        exit()

    # if 'reboot friday' in s.lower():
    #     speak("Rebooting...")
    #     os.system("TASKKILL /F /IM py.exe")
    #     variable = 1

