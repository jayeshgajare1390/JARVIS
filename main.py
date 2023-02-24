import os
import smtplib
import time as x
import psutil
from Recordings import Record_Option
from Phonenumber import Phonenumber_location_tracker
import PyPDF2
import pywikihow
from bs4 import BeautifulSoup
import qrcode
import wolframalpha
from pytube import YouTube
import instaloader
import pyautogui
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import datetime
import random
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime,QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

password="jayesh"

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

OPENWEATHER_APP_ID = ("73124639adb72a6c6998dc5be00cc611")


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.taskexecution()

    # convert voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            #audio = r.listen(source, timeout=5, phrase_time_limit=8)
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said:{self.query}")

        except Exception as e:
            #speak("say that again...")
            return "none"
        # query = query.lower()
        return self.query

    def run(self):
        # speak("please say wakeup to continue")
        while True:
            self.query=self.takecommand()
            if "wake up" in self.query or "makeup" in self.query or "breakup" in self.query or "break up" in self.query:
                self.taskexecution()


    # task execution
    def taskexecution(self):
        wish()
        while True:
            self.query = self.takecommand().lower()
            # logical building for tasks
            if "notepad" in self.query:
                speak("opening notepad")
                os.name("notepad")
                # npath = "C:\\Windows\\system32\\notepad.exe"
                # os.startfile(npath)


            elif "command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "what is" in self.query or "who is" in self.query:
                question = self.takecommand()
                answer = computational_intelligence(question)
                speak(answer)

            elif "calculate something" in self.query:
                question = self.takecommand()
                answer = computational_intelligence(question)
                speak(answer)

            elif 'remember that' in self.query:
                speak("what should i remember sir")
                rememberMessage = self.takecommand()
                speak("you said me to remember" + rememberMessage)
                remember = open('data.txt', 'w')
                remember.write(rememberMessage)
                remember.close()

            elif 'remember anything' in self.query or "reminder" in self.query:
                remember = open('data.txt', 'r')
                speak("you said me to remember that" + remember.read())

            elif ('silence' in self.query) or ('silent' in self.query) or ('keep quiet' in self.query) or ('wait for' in self.query):
                silenceTime(self.query)

            elif "play music" in self.query:
                music_dir = "F:\\New Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif ("today" in self.query):
                day = Cal_day()
                speak("Today is " + day)

            elif 'video' in self.query or "video" in self.query:
                speak("ok playing videos")
                video_dir = 'F:\\Video'
                v = random.choice(video_dir)
                os.startfile(os.path.join(video_dir, v))

            elif "qr code" in self.query:
                qrCodeGenerator()

            elif 'send email' in self.query:
                verifyMail()

            elif ("college time table" in self.query) or ("schedule" in self.query):
                shedule()

            elif ('where i am' in self.query) or ('where we are' in self.query):
                locaiton()

            elif ('system condition' in self.query) or ('condition of the system' in self.query):
                speak("checking the system condition")
                condition()

            elif ("read" in self.query) or ("pdf" in self.query) or ("book" in self.query):
                pdf_reader()

            elif "whats up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                          'i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)
                ans_take_from_user_how_are_you = self.takecommand()
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'ok' in ans_take_from_user_how_are_you:
                    speak('okey..')
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                    speak('oh sorry..')
            elif 'make you' in self.query or 'created you' in self.query or 'develop you' in self.query:
                ans_m = " For your information Jayesh Created me ! I give Lot of Thanks to Him "
                speak(ans_m)
            elif "who are you" in self.query or "about you" in self.query or "your details" in self.query:
                about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
                speak(about)
            elif "hello" in self.query or "hello Jarvis" in self.query:
                hel = "Hello Jayesh JC ! How May i Help you.."
                speak(hel)
            elif "your name" in self.query or "sweat name" in self.query:
                na_me = "Thanks for Asking my name my self ! Jarvis"
                speak(na_me)
            elif "how you feel" in self.query:
                speak("feeling Very sweet after meeting with you")

            elif "tell me news" in self.query or "news" in self.query:
                speak("please wait sir,i am fetching the latest news")
                news()

            elif "internet speed" in self.query:
                import speedtest
                st = speedtest.Speedtest()
                d1 = st.download()
                up = st.upload()
                speak(f"sie we have {d1} bit per second downloading speed and {up} bit per second uploading speed")

                # try:
                #     os.system('cmd /k "speedtest"')
                # except:
                #     speak("there is no internet connction")


            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is{ip}")

            elif "GOOGLE" in self.query or "SEARCH" in self.query or "WEB BROWSER" in self.query or "CHROME" in self.query or "BROWSER" in self.query:
                speak("Opening")
                speak("GOOGLE CHROME")
                os.system("chrome")

            elif "mobile camera" in self.query:
                import urllib.request
                import cv2
                import numpy as np
                import time
                try:
                    speak(f"Boss openinging mobile camera")
                    URL = "http://192.168.43.109:8080/shot.jpg"
                    while True:
                        img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                        img = cv2.imdecode(img_arr, -1)
                        cv2.imshow('IPWebcam', img)
                        q = cv2.waitKey(1)
                        if q == ord("q"):
                            speak(f"Boss closing mobile camera")
                            break

                    cv2.destroyAllWindows()

                except Exception as e:
                    speak("Boss there is some technical error while opening mobile camera")

            elif "wikipedia" in self.query:
                speak("what do you want to search")
                s=self.takecommand()
                speak("searching wikipedia...")
                results = wikipedia.summary(s, sentences=2)
                speak("according to wikipedia")
                speak(results)

            if ('play a song' in self.query) or ('youtube' in self.query) or ("download a song" in self.query) or (
                    "download song" in self.query):
                # commands for opening youtube, playing a song in youtube, and download a song in youtube
                yt(self.query)

            elif "activate how to do mod" in self.query:
                speak("How to do mode is activated")
                while True:
                    speak(" please tell me what you want to know")
                    how = self.takecommand()
                    try:
                        if "exit" in self.query or "close" in self.query:
                            speak("ok sir,how to do mode is closed")
                            break
                        else:
                            max_results = 1
                            how_to = pywikihow.search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak(f"sorry sir,i am not able to find this{how}")


            elif "temperature" in self.query:
                speak("which city you want know temperature:")
                search = input()
                url = f"https://www.google.com/search?q={'temperature' + search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current temperature of {search} is {temp}")


            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open google" in self.query:
                speak("sir,what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "no thanks" in self.query:
                speak("thanks for using me sir,have a good day")
                sys.exit()
            # To close any application
            elif "close notepad" in self.query:
                speak("ok sir,closing notepad")
                os.system("taskkill /f /im notepad.exe")
            # To set alarm

            elif 'weather' in self.query:
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = get_weather_report(city)
                speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = 'F:\\New Music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "tell me joke" in self.query or "joke" in self.query:
                speak(f"Hope you like this one sir")
                joke = get_random_joke()
                speak(joke)
                speak("For your convenience, I am printing it on the screen sir.")
                print(joke)
                # joke = pyjokes.get_joke()
                # speak(joke)

            elif "shutdown the laptop" in self.query:
                os.system("shutdown /s /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.d11,SetSuspendState 0,1,1")

            elif "restart the laptop" in self.query:
                os.system("shutdown /r /t 5")

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                x.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait sir,i am fetching the latest news")
                news()

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir,let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"sir i am not sure,but i think we are in {city} city of {country} country")

                except Exception as e:
                    speak("sorry sir,due to network issue i am not able to find where we are.")
                    pass

            elif "ask" in self.query or "can i ask" in self.query:
                speak("what you want to know boss")
                question = self.takecommand()
                answer = computational_intelligence(question)
                speak(answer)

            elif ('send a message' in self.query):
                whatsapp(self.query)

            elif ("create a new contact" in self.query):
                AddContact()
                # Command for searching for a contact
            elif ("number in contacts" in self.query):
                NameIntheContDataBase(self.query)
                # Command for displaying all contacts
            elif ("display all the contacts" in self.query):
                Display()

            elif ("recording" in self.query) or ("screen recording" in self.query) or (
                    "voice recording" in self.query):
                try:
                    speak("Boss press q key to stop recordings")
                    option = self.query
                    Record_Option(option=option)
                    speak("Boss recording is being saved")
                except:
                    speak("Boss an unexpected error occured couldn't start screen recording")

            elif ("track" in self.query) or ("track a mobile number" in self.query) or ("phone number" in self.query):
                speak("Boss please enter the mobile number with country code")
                try:
                    location, servise_prover, lat, lng = Phonenumber_location_tracker()
                    speak(
                        f"Boss the mobile number is from {location} and the service provider for the mobile number is {servise_prover}")
                    speak(f"latitude of that mobile nuber is {lat} and longitude of that mobile number is {lng}")
                    print(location, servise_prover)
                    print(f"Latitude : {lat} and Longitude : {lng}")
                    speak("Boss location of the mobile number is saved in Maps")
                except:
                    speak("Boss an unexpected error occured couldn't track the mobile number")

            elif "instagram profile" in self.query:
                speak("sir please enter the your username")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user{name}")
                x.sleep(5)
                speak("sir would you like to download profile picture of this user")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak(
                        "i am done sir,profile picture is downloaded in our main folder .now i am ready for next command")
                else:
                    pass

            elif "power left" in self.query or "battery" in self.query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percentage
                speak(f"sir our system have {percentage} percentage battery")

            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir,tell me the name for this screenshot")
                name = self.takecommand().lower()
                speak("hold the screen sir for few seconds,i am taking screenshot")
                x.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir,the screenshot is saved in our main folder.now i am ready for next task")

            elif "thank you" in self.query:
                speak("it's my pleasure")

            elif "do some calculation" in self.query or "can you calculate" in self.query or "calculation" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What calculation you want to do")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                speak("your result is...")
                speak(eval_binary_expr(*(my_string.split())))

            elif "hide all files" in self.query or "hide this folder " in self.query or "visible this folder" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("sir.all the files are in this folder are now hidden")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak(
                        "sir,all files in this folder are now visible to everyone . i wish you are taking this decision on your peace")

                elif "leave it" in condition:
                    speak("ok sir")

                speak("sir,do you have any other work")

            elif ('your age' in self.query) or ('are you single' in self.query) or ('are you there' in self.query) or (
                    'tell me something' in self.query) or ('thank you' in self.query) or ('in your free time' in self.query) or (
                    'i love you' in self.query) or ('can you hear me' in self.query) or "do you ever get tired" in self.query:
                Fun(self.query)

            elif ("you can sleep" in self.command) or ("sleep now" in self.command):
                self.talk("Okay boss, I am going to sleep you can call me anytime.")
                break

            elif ("wake up" in self.command) or ("get up" in self.command):
                self.talk("boss, I am not sleeping, I am in online, what can I do for u")

            elif ("goodbye" in self.command) or ("get lost" in self.command):
                self.talk("Thanks for using me boss, have a good day")
                sys.exit()

            elif "shutdown" in self.query:
                speak("Do you really want to shut down your pc Say Yes or else No")
                print("Say Yes or else No")
                ans_from_user = self.takecommand()
                if 'yes' in ans_from_user:
                    speak("due to security reason,please tell password to shutdown system")
                    z = self.takecommand()
                    if (z == password):
                        speak('Shutting Down...')
                        speak("bye sir")
                        os.system('shutdown -s')
                    elif 'no' in ans_from_user:
                        speak('shutdown abort')

            elif "restart" in self.query:
                speak("Do you really want to restart your pc Say Yes or else No")
                print("Say Yes or else No")
                ans_from_user = self.takecommand()
                if 'yes' in ans_from_user:
                    speak("due to security reason,please tell password to shutdown system")
                    z = self.takecommand()
                    if (z == password):
                        speak('Restarting...')
                        os.system('shutdown /r /t 5')
                    elif 'no' in ans_from_user:
                        speak('restart abort')

            elif "sleep the system" in self.query:
                speak("pc is going to sleep mode..")
                speak("bye sir")
                os.system("rundll32.exe powrprof.d11,SetSuspendState 0,1,1")

            else:
                temp = self.query.replace(' ', '+')
                g_url = "https://www.google.com/search?q="
                res_g = "sorry! i cant understand but if you want to search on internet say Yes or else No"
                speak(res_g)
                print("Say Yes or No")
                ans_from_user = self.takecommand()
                if 'yes' in ans_from_user:
                    speak('Opening Google...')
                    webbrowser.open(g_url + temp)
                elif 'no' in ans_from_user:
                    speak('Google Search Aborted')

def pdf_reader():
    speak("Boss enter the name of the book which you want to read")
    n = input("Enter the book name: ")
    n = n.strip()+".pdf"
    book_n = open(n,'rb')
    pdfReader = PyPDF2.PdfFileReader(book_n)
    pages = pdfReader.numPages
    speak(f"Boss there are total of {pages} in this book")
    speak("plsase enter the page number Which I nedd to read")
    num = int(input("Enter the page number: "))
    page = pdfReader.getPage(num)
    text = page.extractText()
    speak(text)

def whatsapp(self,query):
    try:
        query = query.replace('send a message to','')
        query = query.strip()
        name, numberID, F = SearchCont(query)
        if F:
            print(numberID)
            speak(f'Boss, what message do you want to send to {name}')
            message = self.takecommand()
            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            print(hour, min)
            if "group" in query:
                kit.sendwhatmsg_to_group(numberID, message, int(hour), int(min) + 1)
            else:
                kit.sendwhatmsg(numberID, message, int(hour), int(min) + 1)
                speak("Boss message have been sent")
        if F == False:
            speak(f'Boss, the name not found in our data base, shall I add the contact')
            AddOrNot = self.takecommand()
            print(AddOrNot)
            if ("yes" in AddOrNot) or ("add" in AddOrNot) or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                AddContact()
            elif ("no" in AddOrNot):
                speak('Ok Boss')
    except:
        print("Error occured, please try again")

    # Add contacts
def AddContact():
    speak(f'Boss, Enter the contact details')
    name = input("Enter the name :").lower()
    number = input("Enter the number :")
    NumberFormat = f'"{name}":"+91{number}"'
    ContFile = open("Contacts.txt", "a")
    ContFile.write(f"{NumberFormat}\n")
    ContFile.close()
    speak(f'Boss, Contact Saved Successfully')

    # Search Contact
def SearchCont(name):
    with open("Contacts.txt", "r") as ContactsFile:
        for line in ContactsFile:
            if name in line:
                print("Name Match Found")
                s = line.split("\"")
                return s[1], s[3], True
    return 0, 0, False

    # Display all contacts
def Display():
    ContactsFile = open("Contacts.txt", "r")
    count = 0
    for line in ContactsFile:
        count += 1
        ContactsFile.close()
        ContactsFile = open("Contacts.txt", "r")
        speak(f"Boss displaying the {count} contacts stored in our data base")
        for line in ContactsFile:
            s = line.split("\"")
            print("Name: " + s[1])
            print("Number: " + s[3])
        ContactsFile.close()

    # search contact
def NameIntheContDataBase(self,query):
    line = query
    line = line.split("number in contacts")[0]
    if ("tell me" in line):
        name = line.split("tell me")[1]
        name = name.strip()
    else:
        name = line.strip()
        name, number, bo = SearchCont(name)
        if bo:
            print(f"Contact Match Found in our data base with {name} and the mboile number is {number}")
            speak(f"Boss Contact Match Found in our data base with {name} and the mboile number is {number}")
        else:
            speak("Boss the name not found in our data base, shall I add the contact")
            AddOrNot = self.takecommand()
            print(AddOrNot)
            if ("yes add it" in AddOrNot) or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                AddContact()
                speak(f'Boss, Contact Saved Successfully')
            elif ("no" in AddOrNot) or ("don't add" in AddOrNot):
                speak('Ok Boss')
# covid
def Covid(self,s):
    try:
        from covid_india import states
        details = states.getdata()
        if "check in" in s:
            s = s.replace("check in","").strip()
            print(s)
        elif "check" in s:
            s = s.replace("check","").strip()
            print(s)
        elif "tech" in s:
            s = s.replace("tech","").strip()
            s = states[s]
            ss = details[s]
            Total = ss["Total"]
            Active = ss["Active"]
            Cured = ss["Cured"]
            Death = ss["Death"]
            print(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            speak(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            x.sleep(5)
            speak("Boss do you want any information of other states")
            I = self.takecommand()
            print(I)
            if ("check" in I):
                Covid(I)
            elif("no" in I):
                speak("Okay boss stay home stay safe")
            else:
                speak("Okay boss stay home stay safe")
    except:
        speak("Boss some error occured, please try again")
        speak("Boss do you want any information of other states")
        I = self.takecommand()
        if("yes" in I):
            speak("boss, Which state covid status do u want to check")
            Sta = self.takecommand()
            Covid(Sta)
        elif("no" in I):
            speak("Okay boss stay home stay safe")
        else:
            speak("Okay boss stay home stay safe")


def condition():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage + " percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    speak(f"Boss our system have {percentage} percentage Battery")
    if percentage >= 75:
        speak(f"Boss we could have enough charging to continue our work")
    elif percentage >= 40 and percentage <= 75:
        speak(f"Boss we should connect out system to charging point to charge our battery")
    elif percentage >= 15 and percentage <= 30:
        speak(f"Boss we don't have enough power to work, please connect to charging")
    else:
        speak(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")

# Time caliculating algorithm
def silenceTime(query):
    print(query)
    x = 0
    # caliculating the given time to seconds from the speech commnd string
    if ('10' in query) or ('ten' in query):
        x = 600
    elif '1' in query or ('one' in query):
        x = 60
    elif '2' in query or ('two' in query):
        x = 120
    elif '3' in query or ('three' in query):
        x = 180
    elif '4' in query or ('four' in query):
        x = 240
    elif '5' in query or ('five' in query):
        x = 300
    elif '6' in query or ('six' in query):
        x = 360
    elif '7' in query or ('seven' in query):
        x = 420
    elif '8' in query or ('eight' in query):
        x = 480
    elif '9' in query or ('nine' in query):
        x = 540
    silence(x)

    # Silence
def silence(k):
    t = k
    s = "Ok boss I will be silent for " + str(t / 60) + " minutes"
    speak(s)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        x.sleep(1)
        t -= 1
    speak("Boss " + str(k / 60) + " minutes over")

# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    t = x.strftime("%I:%M %p")
    day = Cal_day()
    print(t)
    if (hour >= 0) and (hour <= 12) and ('AM' in t):
        speak(f'Good morning boss, its {day} and the time is {t}')
    elif (hour >= 12) and (hour <= 16) and ('PM' in t):
        speak(f"good afternoon boss, its {day} and the time is {t}")
    else:
        speak(f"good evening boss, its {day} and the time is {t}")

def shedule():
    day = Cal_day().lower()
    speak("Boss today's shedule is")
    Week = {
            "monday": "Boss from 9:00 to 9:50 you have Cultural class, from 10:00 to 11:50 you have mechanics class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00",
            "tuesday": "Boss from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have biology lab from 2:00",
            "wednesday": "Boss today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
            "thrusday": "Boss today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have sensors class, from 1:00 to 2:00 you have brake, and today you have english lab from 2:00",
            "friday": "Boss today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00",
            "saturday": "Boss today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
            "sunday": "Boss today is holiday but we can't say anything when they will bomb with any assisgnments"}
    if day in Week.keys():
        speak(Week[day])
def verifyMail(self):
    try:
        speak("what should I say?")
        content = self.takecommand()
        speak("To whom do u want to send the email?")
        to = input("Enter Email Addrese you want to send Mail:")
        SendEmail(to, content)
        speak("Email has been sent to " + str(to))
    except Exception as e:
        print(e)
        speak("Sorry sir I am not not able to send this email")

# Email Sender
def SendEmail(to, content):
    print(content)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jayeshgajare1390@gmail.com', '8856074209Jay')
    server.sendmail("jayeshgajare1390@gmail.com", to, content)
    server.close()

def yt(self,query):
    print(query)
    if 'play' in query:
        speak("Boss can you please say the name of the song")
        song = self.takecommand()
        if "play" in song:
            song = song.replace("play", "")
        speak('playing ' + song)
        print(f'playing {song}')
        pywhatkit.playonyt(song)
        print('playing')
    elif "download" in query:
        speak("Boss please enter the youtube video link which you want to download")
        link = input("Enter the YOUTUBE video link: ")
        yt = YouTube(link)
        speak(f"Downloading{yt.title}")
        yt.streams.get_highest_resolution().download()
        speak(f"Boss downloaded {yt.title} from the link you given into the main folder")
    elif 'youtube' in query:
        speak('opening your youtube')
        webbrowser.open('https://www.youtube.com/')
    else:
        No_result_found()

def qrCodeGenerator():
    speak(f"Boss enter the text/link that you want to keep in the qr code")
    input_Text_link = input("Enter the Text/Link : ")
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
                       )
    QRfile_name = (str(datetime.datetime.now())).replace(" ", "-")
    QRfile_name = QRfile_name.replace(":", "-")
    QRfile_name = QRfile_name.replace(".", "-")
    QRfile_name = QRfile_name + "-QR.png"
    qr.add_data(input_Text_link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"QRCodes\{QRfile_name}")
    speak(f"Boss the qr code has been generated")

def Cal_day():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        return day_of_the_week
#Fun commands to interact with jarvis
def Fun(query):
    print(query)
    if 'your name' in query:
        speak("My name is jarvis")
    elif 'my name' in query:
        speak("your name is Sujith")
    elif 'university name' in query:
        speak("you are studing in Amrita Vishwa Vidyapeetam, with batcheloe in Computer Science and Artificail Intelligence")
    elif 'what can you do' in query:
        speak("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
    elif 'your age' in query:
        speak("I am very young that u")
    elif 'date' in query:
        speak('Sorry not intreseted, I am having headache, we will catch up some other time')
    elif 'are you single' in query:
        speak('No, I am in a relationship with wifi')
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    elif 'are you there' in query:
        speak('Yes boss I am here')
    elif 'tell me something' in query:
        speak('boss, I don\'t have much to say, you only tell me someting i will give you the company')
    elif 'thank you' in query:
        speak('boss, I am here to help you..., your welcome')
    elif 'in your free time' in query:
        speak('boss, I will be listening to all your words')
    elif 'i love you' in query:
        speak('I love you too boss')
    elif 'can you hear me' in query:
        speak('Yes Boss, I can hear you')
    elif 'do you ever get tired' in query:
        speak('It would be impossible to tire of our conversation')
    else :
        No_result_found()

#no result found
def No_result_found(self):
    speak('Boss I couldn\'t understand, could you please say it again.')

def locaiton():
    speak("Wait boss, let me check")
    try:
        IP_Address = get('https://api.ipify.org').text
        print(IP_Address)
        url = 'https://get.geojs.io/v1/ip/geo/' + IP_Address + '.json'
        print(url)
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        tZ = geo_data['timezone']
        longitude = geo_data['longitude']
        latidute = geo_data['latitude']
        org = geo_data['organization_name']
        print(city + " " + state + " " + country + " " + tZ + " " + longitude + " " + latidute + " " + org)
        speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
        speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
    except Exception as e:
        speak("Sorry boss, due to network issue i am not able to find where we are.")
        pass

def news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
                'News daily newsletter', 'Mobile app', 'Get in touch']

    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() not in unwanted:
            # print(x.text.strip())
            speak(x.text.strip())


def computational_intelligence(question):
    try:
        client = wolframalpha.Client('LJUK64-8LUYE47EE2')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None





startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("../../Pictures/JARVIS/LIVE i.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/JARVIS/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())