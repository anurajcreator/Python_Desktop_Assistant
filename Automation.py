# Search not working properly many modification needed started on 09/03/2020


# imported libraries
from __future__ import print_function
import spur
import paramiko

import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import requests



#Chrome_Audio
def get_audio(s):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == s:
            return volume.GetMasterVolume()

def set_audio(s, f):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == s:
            volume.SetMasterVolume(f, None)


#whatsapp variables
# wsp_dic = {1: 'Shreya', 2: 'Atrayan', 3: 'Argha Nath', 4: 'Saikat Mondal', 5: 'Saikat Das', 6: 'Papa', 7: 'Aruna'}
w_token = 0

# chrom profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=D:\\Anuraj\\selenium profile\\Profile 1")

paramiko.SSHClient().set_missing_host_key_policy(paramiko.AutoAddPolicy())
shell = spur.SshShell(hostname='0.tcp.ngrok.io', port=16434, username='pi', password='raspberry')

# driver_path = "C:\\Users\\anura\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe"
count = 0
# if count == 0:
# driver = webdriver.Chrome()


# list for random sorry's
list = ['i did not get that, please repeat', ' say that again please sir', 'pardon me sir']
slist = ['search google', 'how to', 'what is', 'search in google', 'search']

# voice Engine Settings
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 175)


# driver = webdriver.Chrome()
# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Greetings Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        speak('Goodmorning Sir!')
    elif 12 <= hour < 18:
        speak('Goodafternoon Sir!')
    elif 18 <= hour <= 20:
        speak('Goodevening Sir!')

    speak("how may i help you?")
    # speak("mai apki kayse madat karsakta hu")


# Input Function for starting (hiding the processes)
def takeCommandf():
    # Input and returns String
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 0.6
        r.energy_threshold= 340
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"/User said: {query}\n")
    except Exception as e:
        # print(e)
        # print("said that again please")
        return "None"
    return query

# Input function for rest of the period.
def takeCommand():
    # Input and returns String
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5 )
        r.pause_threshold = 0.6
        r.energy_threshold=340
        print("Listening....")
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        return "None"
    return query


# main-f dude.
if __name__ == "__main__":
    while True:
        query = takeCommandf().lower()
        s = query
        if 'shutdown friday' in s or 'off 'in s or'goodbye friday'in s or'good night friday'in s or'tata friday' in s:
            hour = int(datetime.datetime.now().hour)
            if 4 <= hour < 20:
                speak('Have a Good day Sir')
            else:
                speak('Good Night Sir')
            exit()

        # elif 'reboot friday' in query:
        #     exit()

        elif 'hello friday' in query or 'hi friday' in query or 'friday' in query:
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




                # elif 'set vloume' in query:
                #     query = query.replace('set volume ', "")
                #     os.


                #Time and Date
                elif "what's the time" in query or 'tell me the time' in query or 'what is the time' in query:
                    mint = int(datetime.datetime.now().minute)
                    hour = int(datetime.datetime.now().hour)
                    sec = int(datetime.datetime.now().second)
                    if hour < 13 :
                        speak("The time is " + str(hour) + str(mint) + ' AM ')
                    else:
                        speak("The time is " + str(hour-12) + str(mint) + ' PM ')

                elif "what's the date" in query or 'tell me the date' in query or 'what is the date' in query:
                    dt = str(datetime.datetime.today())

                    speak("The date is " + dt[:10] )

                elif "what's the weather" in query or 'tell me the weather' in query or 'what is the weather' in query or 'how weather' in query or 'how the weather' in query:
                    res = requests.get('https://ipinfo.io/')
                    data = res.json()
                    city = data['city']
                    print(city)
                    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                    url = api_address + city
                    json_data = requests.get(url).json()
                    print(json_data)
                    temp = int((json_data['main']['temp']) - 270)
                    des =  (json_data['weather'][0]['main'])
                    speak(" Now at " + city + "  it is now   " + des + "   and the temperature is " + str(temp) + "degree celcius")

                elif 'open docs' in query:
                    path = "C:\\Users\\anura\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome " \
                           "Apps\\Docs.lnk "
                    os.startfile(path)

                elif 'open gmail' in query:
                    path = "C:\\Users\\anura\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome " \
                           "Apps\\Gmail.lnk "
                    os.startfile(path)

                # WHATSAPPP!!!!!
                elif 'open whatsapp' in query:
                    wb.open_new('https://web.whatsapp.com/')

                elif 'whatsapp' in query or 'send a message to' in query:
                    try:
                        query = query.replace("whatsapp ", "")
                    except:
                        pass
                    try:
                        query = query.replace("send a message to ", "")
                    except:
                        pass
                    try:
                        query = query.replace("whatsapp", "")
                    except:
                        pass

                    if len(query) == 0:
                        speak('Sir to whom?')
                        query = takeCommand().lower()
                    if count == 0:
                        driver = webdriver.Chrome(options=chrome_options)
                        count = 1
                    if 'WhatsApp' not in driver.title:
                        driver.get('https://web.whatsapp.com')
                        speak("sir please scan the Qr code, if already done just say ok to proceed")

                        while True:
                            check = takeCommand()
                            if 'proceed' in check or 'done' in check or 'ok' in check:
                                token = 1
                                break
                            elif 'quit' in check or 'exit' in check:
                                speak("exiting Whatsapp")
                                driver.quit()
                                token = 0
                                break
                    else:
                        token = 1

                    string = " 'This message is sent by my virtual assistant'**"

                    if token == 1:
                        speak("sir message please")
                        msg = takeCommand()
                        print("message = " + msg)
                        print("Name = " + query.title())

                        try:
                            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(query.title()))
                            user.click()
                            w_token = 1
                        except:
                            pass
                        if w_token == 0:
                            speak('User not found, type the User name, or type exit '
                                  'for canceling the message')
                            check = input()
                            if check != 'exit':
                                try:
                                    query = check
                                    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(query))
                                    user.click()
                                except:
                                    speak('Again User not found, please try again')

                            else:
                                speak("Message Canceled")
                                break
                        # except Exception as e:
                        #     search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                        #     search.send_keys(query.title())

                        msg_box = driver.find_element_by_xpath(
                            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]")

                        msg_box.send_keys('*' + msg + string)

                        button = driver.find_element_by_class_name('_3M-N-')
                        button.click()
                        speak('message send')


                #Normal Files
                elif 'open ng rock' in query:
                    path = "C:\\Users\\anura\\Downloads\\Compressed\\ngrok-stable-windows-amd64\\ngrok.exe"
                    os.startfile(path)

                elif 'open minecraft server' in query or 'open mcss' in query:
                    path = "C:\\Users\\anura\\Downloads\\Compressed\\mcss_win-x86-64_v11.4.1\\mcss.exe"
                    os.startfile(path)

                elif 'open tee launcher' in query or 'open minecraft' in query:
                    path = 'C:\\Users\\anura\\AppData\\Roaming\\.minecraft\\TLauncher.exe'
                    os.startfile(path)

                elif 'what are you doing' in query:
                    speak("Waiting for your response sir")

                elif 'exit browser' in query or 'quit browser' in query:
                    driver.quit()
                    count = 0

                elif 'open pycharm' in query:
                    path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
                    os.startfile(path)

                elif 'open discord' in query:
                    path = "C:\\Users\\anura\\AppData\\Local\\Discord\\app-0.0.306\\Discord.exe"
                    os.startfile(path)

                elif 'stop friday' in query or 'sign out friday' in query or 'nothing else friday' in query or 'timeout friday' in query:
                    break

                elif query == 'none':
                    continue


                #Google Search
                elif 'search' in query or 'how to' in query or 'what' in query:
                    for i in slist:
                        if i in query:

                            try:
                                query = query.replace("search google for", "")

                            except:
                                pass

                            try:
                                query = query.replace("search google", "")

                            except:
                                pass

                            try:
                                query = query.replace("search in google", "")

                            except:
                                pass

                            try:
                                query = query.replace("search", "")

                            except:
                                pass

                            try:
                                query = query.replace(" for ", "")
                            except:
                                pass
                            try:
                                if count == 0:
                                    driver = webdriver.Chrome(options=chrome_options)

                                    count = 1
                                driver.maximize_window()
                                driver.get('https://www.google.com')

                                driver.find_element_by_name('q').send_keys(query + Keys.ENTER)
                                y = takeCommand()
                                if 'first link' in y:
                                    search = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
                                    search[0].click()
                                elif 'tell me about' in y or 'wikipedia' in y:
                                    results = wikipedia.summary(query, sentences=3)
                                    speak(results)

                                # search = driver.find_element_by_xpath('//input[@value = "Google Search"]')
                                # search.click()
                            except:
                                pass



                # YOUTUBE!!!!!!!!!
                elif 'search youtube for' in query:
                    query = query.replace("search youtube for", "")
                    url = 'https://www.youtube.com/results?search_query='
                    wb.open_new(url + query)

                elif 'play' in query:
                    if get_audio('chrome.exe') > 0.5:
                        speak('Application volume is high!; Recognising voice is not going to work properly after this; , Either adjust the volume or exit manualy....')
                        check = takeCommand().lower()
                        if ('adjust' or 'lower') in check:
                            set_audio('chrome.exe', 0.5)
                            speak('Audio adjusted!')
                    query = query.replace("play", "")
                    if len(query) == 0:

                        try:
                            search = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
                            search.click()

                        except:
                            pass

                    else:
                        if count == 0:
                            driver = webdriver.Chrome(options=chrome_options)
                            count = 1
                    # browser.maximize_window()
                        try:

                            wait = WebDriverWait(driver, 3)
                            presence = EC.presence_of_element_located
                            visible = EC.visibility_of_element_located

                        # Navigate to url with video being appended to search_query
                            driver.get("https://www.youtube.com/results?search_query=" + query)

                        # play the video
                            wait.until(visible((By.ID, "video-title")))
                            driver.find_element_by_id("video-title").click()
                        except:
                            pass

                elif 'pause' in query:
                    try:
                        search = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
                        search.click()
                    except:
                        pass

                elif 'skip ad' in query or 'keep ad' in query or 'keypad' in query:

                    search = driver.find_element_by_xpath('//*[@id="skip-button:8"]/span/button/span')
                    search.click()
                    # except:
                    #     pass

                # YOUTUBE ENDED





                # else:
                #     print(query)
                #     speak(random.choice(list))



        # elif 'reboot mark' in query:
        #     speak("Rebooting...")
        #     # exit()
