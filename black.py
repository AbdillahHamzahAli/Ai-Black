import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print('initializing Black')

MASTER = 'Hamzah'

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

# speak

def speak(text):
    engine.say(text)
    engine.runAndWait()

# function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >=12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")

# microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again please")
        query = None

    return query

# main start here
speak("Hello my name is Black,i can help you")
wishMe()
query = takeCommand()

