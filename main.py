import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

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


if __name__ == "__main__":
    while True:
        flag = 0
        get = sr.Recognizer()
        instruct = ""
        with sr.Microphone() as source:
            audio = get.listen(source)
        try:
            # print("Recognizing...")
            instruct = get.recognize_google(audio, language='en-in')
            # print(f"User said : {instruct}\n")
        except Exception as e:
            pass
        if 'hello jarvis' in instruct.lower() :
            wishMe()
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
                    break

                elif 'open whatsapp' in query:
                    speak("Opening Whatsapp Sir")
                    webbrowser.open("web.whatsapp.com")
                
                elif 'open meeting' in query:
                    speak("Opening Google Meet")
                    webbrowser.open("meet.google.com")

                elif 'shutdown' in query:
                    speak("Shutting Down Service")
                    exit(0)
        else:
            continue
        