import os
import speech_recognition as sr

def takeCommand():

    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

while True:

    wake_up=takeCommand()

    if "wake up" in wake_up:
        os.startfile('C:/Users/DELL/PycharmProjects/VoiceAssistant/Jasper.py')
        break