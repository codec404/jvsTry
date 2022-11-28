import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak('Good Morning Sir!')
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else :
        speak("Good Evening Sir!")
    speak("I am Jarvis. Your personal Assistant. Please tell me how may I help you?")

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
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def kelvinToCelsiusFahrenheit(kelvin):
    celsius = kelvin -273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius,fahrenheit

def weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = os.environ['CurrentWeather']
    city = "Memari"
    url = base_url+"appid="+api_key+"&q="+city

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
    print(f"City: {city}")
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
    speak("Rest data is presnted on your screen sir. Thank you Sir.")

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
                
                elif 'play music' in query:
                    webbrowser.open("music.youtube.com")            
                
                elif 'bye' in query:
                    speak("Goodbye Sir. Have a nice day. Always at your service sir.")
                    speak('Turning Off. Into sleep mode.')  
                    flag = 0
                    break

                elif 'open whatsapp' in query:
                    speak("Opening Whatsapp Sir")
                    webbrowser.open("web.whatsapp.com")
                
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
                    weather()
                    
                elif 'shutdown' in query:
                    speak("Shutting Down Service. Remember me when required. Adios")
                    exit(0)
        else:
            continue
        