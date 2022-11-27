import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser


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
    speak("I am Jarvis.Your personal Assistant.Please tell me how may I help you?")

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
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
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