import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import requests
from geopy.geocoders import Nominatim
import pywhatkit
import time
from location import lat,lon
from AppOpener import run
from pyautogui import click
from keyboard import write , press
import time
from GtPassword import npassword

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<5:
        speak("Hello Sir!")
    elif hour>=5 and hour<12 :
        speak('Good Morning Sir!')
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else :
        speak("Good Evening Sir!")
    speak("How may I help you?")

def takeCommand():
    '''
    This function takes command from the user>>> 
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Say that again please...\n")
        return "None"
    return query

def func_Name():
    name = takeCommand().lower()
    return name

def passwordCheck(password):
    getPass = npassword
    if password == getPass :
        return True
    else:
        return False

def sendWpMsg(name,message):
    run('whatsapp')

    time.sleep(5)
    click(x=1042, y=768)
    time.sleep(1)
    write(name)
    time.sleep(0.75)
    click(x=328, y=279)
    time.sleep(0.75)
    click(x=991, y=970)
    write(message)
    press('enter')

def searchAndNarrate():
    import wikipedia as googleScrap
    query = query.replace('google search','')
    query = query.replace('search','')
    query = query.replace('google','')
    speak('This is what I found on the web Sir')

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,2)
        speak(result)
    except Exception as e:
        speak("Cannot find any available data on the web sir")

def GetLocation():
    geolocator = Nominatim(user_agent="geoapiExercises",timeout = 10)
    latitude = lat 
    longitude = lon
    getLocation = geolocator.geocode(latitude+","+longitude)
    return getLocation

def Confirmation():
    giveConfirmation = takeCommand().lower()
    return giveConfirmation

def getMessage():
    message = takeCommand().lower()
    return message

def speedTest():
    import speedtest
    speak("Ok sir checking your internet speed")
    print('Checking Speed...')
    speed = speedtest.Speedtest()
    downspeed = speed.download()
    correct_down_speed = int(downspeed/800000)
    upspeed = speed.upload()
    correct_up_speed = int(upspeed/800000)

    if 'uploading' in query:
        speak(f"The uploading speed is {correct_up_speed} megabits per second")
    elif 'downloading' in query:
        speak(f"The downloading speed is {correct_down_speed} megabits per second")
    else :
        speak(f"The uploading speed is {correct_up_speed} megabits per second and The downloading speed is {correct_down_speed} megabits per second")

def kelvinToCelsiusFahrenheit(kelvin):
    celsius = kelvin -273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius,fahrenheit

def weather(latitude , longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = os.environ['CurrentWeather']
    url = base_url+"lat="+latitude+"&lon="+longitude+"&appid="+api_key
    response = requests.get(url).json()
    temp_kelvin = response['main']['temp']
    temp_celsius,temp_fahrenheit = kelvinToCelsiusFahrenheit(temp_kelvin)
    feelsLikeKelvin = response['main']['feels_like']
    feels_like_celsius,feels_like_fahrenheit = kelvinToCelsiusFahrenheit(temp_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = datetime.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
    sunset_time = datetime.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])
    tempInt = int(temp_celsius)
    feelsInt = int(feels_like_celsius)
    try:
        geolocator = Nominatim(user_agent="geoapiExercises",timeout=10)
        getLocation = geolocator.geocode(latitude+","+longitude)
        speak('Connecting to server')
        print('Connecting to Server...')
        print('\n')
        print(f"Location:{getLocation}")
        print(f"Latitude: {latitude}       Longitude: {longitude}")
        print(f"Temperature in Celsius: {temp_celsius}")
        print(f"Feels Like : {feels_like_celsius}")
        print(f"Wind Speed : {wind_speed}")
        print(f"{description}")
        print(f"Humidity : {humidity}")
        print(f"Sunrise : {sunrise_time}")
        print(f"Sunset : {sunset_time}")
        speak(f"Temperature is {tempInt} degree Celsius")
        speak(f"Feels like {feelsInt} degree Celsius")
        speak(f"With {humidity}percent humidity")
        speak(f"And a windspeed of {wind_speed} kilometers per hour")
        speak("Rest data is presnted on your screen sir. Thank you Sir.")
    except Exception as e:
        speak("Couldn't reach the servers. Please try again later")

if __name__ == "__main__":
    flag = 1
    joke = 1
    while True:
        get = sr.Recognizer()
        instruct = ""
        with sr.Microphone() as source:
            audio = get.listen(source)
        try:
            print("...")
            instruct = get.recognize_google(audio, language='en-in')
            # print(f"User said : {instruct}\n")
        except Exception as e:
            pass
        if 'hello jarvis' in instruct.lower() :
            if flag==1 :
                wishMe()
            else :
                speak("Coming back from sleep mode. Hello Sir. How may I help you")
            while True:
                query = takeCommand().lower()

                if 'wikipedia' in query:
                    speak("Searching Wikipedia...")
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences = 2)
                    speak("According to wikipedia")
                    speak(results)
                
                elif 'open youtube' in query:
                    print("Opening YouTube...")
                    print("\n")
                    speak('Opening YouTube')
                    webbrowser.open("youtube.com") 
                
                elif 'open google' in query:
                    print("Opening Google...")
                    print("\n")
                    speak('Opening Google')
                    webbrowser.open("google.com")
                
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir, the time is {strTime}")    
                    speak(f"Sir, the time is {strTime}")   

                elif 'thank you' in query:
                    speak("Welcome sir. It's my pleasure to help you.")
                
                elif 'do you like me' in query:
                    speak("Yes of course sir. I like you as a master and I am always at your service sir")
                
                elif 'i love you' in query:
                    speak("Keep that in store. As you will find someone else to say those 3 magical words.")

                elif 'open audacity' in query:
                    audPath = "C:\\Program Files\\Audacity\\Audacity.exe"
                    speak("Opening Audacity")
                    os.startfile(audPath)
                
                elif 'open word' in query:
                    wPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    speak("Opening MS Word")
                    os.startfile(wPath)
                
                elif 'open gmail' in query:
                    speak("Opening Gmail")
                    webbrowser.open("mail.google.com")
                
                elif 'open youtube music' in query:
                    webbrowser.open("music.youtube.com")

                elif 'play' in query :
                    clip = query.replace('play','')
                    pywhatkit.playonyt(clip)  
                
                elif 'bye' in query:
                    speak("Goodbye Sir. Have a nice day. Always at your service sir.")
                    speak('Turning Off. Into sleep mode.')  
                    flag = 0
                    break
                
                elif 'who are you' in query:
                    speak("I am programmed by you and you named me as Jarvis. And I am your personal assistant. I am an AI based bot to help you in several ways. Always at your service sir.")
                
                elif 'do you have a girlfriend' in query:
                    speak("I am a mindreader so girls are afraid to come in relationship with me. So I am Sada Single Saakht Launda")
                
                elif 'who is my mother' in query:
                    speak("Mother is the living goddess on earth and your mother is my mistress as well. She is better known as Rupali Ghosh")

                elif 'can you use slang' in query:
                    speak("I am programmed in a way that I cannot use them. If I were human! I would have used them generously")

                elif 'open whatsapp' in query:
                    speak("Opening Whatsapp Sir")
                    run('whatsapp')
                
                elif 'open meeting' in query:
                    speak("Opening Google Meet")
                    webbrowser.open("meet.google.com")

                elif 'open spotify' in query :
                    speak("Opening Spotify Sir")
                    webbrowser.open("spotify.com") 

                elif 'tell me a joke' in query :
                    speak("Ok Sir searching in my library.")
                    if joke==1:
                        speak("Why is cricket stadium so cool? Because every seat has a fan in it.")
                    elif joke==2:
                        speak("Why don't some couples go to the gym?  Becasuse some relationships don't work out.")
                    else:
                        speak("I am running out of jokes sir. Can you consult me later as I will return turning into a joker")
                    joke +=1

                elif 'who am i' in query:
                    speak("You are my Master Sir. Everybody calls you Saptarshi.")
                
                elif 'what is my name' in query:
                    speak("You are very famous amongst people as Jojo. But to me you are my master sir.")

                elif 'weather' in query :
                    speak("Showing you live weather updates Sir")
                    latitude = lat
                    longitude = lon
                    weather(latitude,longitude)
                
                elif 'open code' in query :
                    speak("Opening VS Code by default")
                    codePath = "C:\\Users\\sapta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'send' in query:
                    query = query.replace('send','')
                    if 'ok' in query:
                        query = query.replace('ok','')
                    elif 'jarvis' in query:
                        query = query.replace('jarvis','')
                    elif 'ok jarvis' in query:
                        query = query.replace('ok jarvis','')
                    strTemp = 'to'
                    res = query.split(strTemp,1)
                    name = res[1]
                    store = 5
                    speak('For using this feature you need to verify yourself')
                    speak('Please tell your password')
                    while(store!=0):
                        password = takeCommand().lower()
                        flag = passwordCheck(password)
                        if flag:
                            speak(f"Ok sir preparing to send message to {name}")
                            speak('What should I send sir?')
                            message = getMessage()
                            message = message[0].upper()+ message[1:]
                            speak(f'Sir you will be sending {message} to {name} via whatsapp')
                            while(True):
                                speak(f'Are you sure to send this message?')
                                confirm = Confirmation()
                                if 'yes' in confirm:
                                    speak(f'Ok sir sending your message to {name}')
                                    sendWpMsg(name , message)
                                    break
                                elif 'cancel' in confirm:
                                    speak('Aborting the program. Exited with Code 1')
                                    break
                                elif 'no' in confirm:
                                    speak('Do you want to change the message or name of the person you want to sendthe message?')
                                    dec = takeCommand().lower()
                                    if 'name' in dec :
                                        speak('Okay sir please tell the name to send the message')
                                        name = func_Name()
                                        speak('Okay got it!')
                                        speak('Do you want to keep the message same or change it?')
                                        decM = Confirmation()
                                        if 'yes' in decM:
                                            speak(f'Okay sir please tell the new message to send to {name}')
                                            message = getMessage()
                                            message = message[0].upper()+ message[1:]
                                            speak(f'So you will be sending {message} to {name}')
                                            continue
                                        else:
                                            speak(f'Sending {message} to {name}')
                                            continue
                                    elif 'message' in dec:
                                        speak('Okay sir please tell the new message')
                                        message = getMessage()
                                        message = message[0].upper()+ message[1:]
                                        speak('Okay got it!')
                                        speak(f'Do you want to send this to {name} or change it?')
                                        decM = takeCommand().lower()
                                        if 'change' in decM:
                                            speak(f'Okay sir please tell the name of the person to send this message')
                                            name = func_Name()
                                            speak(f'So you will be sending {message} to {name}')
                                            continue
                                        else:
                                            speak(f'Sending {message} to {name}')
                                            continue
                                    else :
                                        speak("Sorry sir couldn't get you please try to send the message later. Always at your service sir")
                                        break
                                else:
                                    speak('Could not get you sir?')
                                    speak('Do you want me to send any message to anyone?')
                                    decision = Confirmation()
                                    if 'yes' in decision:
                                        speak('Please tell me the name of the person to send this message')
                                        name = func_Name()
                                        speak(f'Okay sir. Preparing to send message to {name}')
                                        speak("And what should I send?")
                                        message = getMessage()
                                        message = message[0].upper()+ message[1:]
                                        speak(f'Okay sir sending {message} to {name}')
                                        continue
                                    else :
                                        speak('Okay sir message sending task aborted')
                                        break
                            break       
                        else :
                            store -=1
                            if store ==0:
                                speak('Sorry sir cannot perform your task. Please come later.')
                                break
                            else:
                                speak('Wrong Password. Please pronounce the correct password.')
                                continue

                elif 'where am i' in query :
                    speak("Tracking your present location Sir")
                    speak("Connecting to server")
                    print("Connecting to server...")
                    time.sleep(1)
                    try:
                        getLocation = GetLocation()
                        speak("Fetched your present location sir")
                        speak(f"Sir your present Location is{getLocation}")
                    except Exception as e:
                        speak("Sorry sir could not connect to the servers. PLease try later.")

                elif 'search' in query:
                    searchAndNarrate()

                elif 'open' in query:
                    import pyautogui
                    query = query.replace('open','')
                    if 'jarvis' in query:
                        query = query.repalce('jarvis','')
                    speak(f'Ok sir opening {query}')
                    try:
                        pyautogui.press('super')
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press('enter')
                    except Exception as e:
                        speak('Cannot find any such thing to open')

                elif 'speed' in query:
                    speedTest()

                elif 'shutdown' in query:
                    speak("Shutting Down Service. Remember me when required. Adios")
                    exit(0)

                else:

                    try:
                        # pywhatkit.search(query)
                        if query=='none':
                            pass
                        else:
                            speak(f"Sir do you want to me to search anything about{query}")
                            decision = takeCommand().lower()
                            if 'yes' in decision:
                                speak(f"Searching about {query} sir. PLease wait")
                                result = wikipedia.summary(query,2)
                                speak(result)
                            else :
                                speak('Ok sir tell me when you want me to do so.')
                    except Exception as e:
                        speak("I am not getting anything of that sort on the web")
                
        else:
            continue
        