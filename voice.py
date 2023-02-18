import speech_recognition as sr
import pyttsx3
import pywhatkit

def talk(command):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say("Playing "+ command)
    engine.runAndWait()

