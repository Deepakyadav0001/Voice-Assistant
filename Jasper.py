import os
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
from selenium_web import *
from news import *
from pickupline import *
from weather import *
import google

engine = pyttsx3.init('sapi5')
engine.getProperty('rate')
rate=engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Unable to capture voice say again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        r = sr.Recognizer()

        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wake up' in query:
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak("Good Morning!")

                elif hour >= 12 and hour < 18:
                    speak("Good Afternoon!")

                else:
                    speak("Good Evening!")

                speak(" online and ready Sir ")

        elif 'search' and 'wikipedia' in query:
            info=query.replace("wikipedia","")
            info=query.replace("search","")
            info=info.replace("on","")
            info=info.replace("Jasper","")
            Info=str(info)
            speak(f"searching {Info} on wikipedia")
            assist = wiki()
            assist.search(Info)


        elif 'search' in query:
            text=query.replace("search","")
            text=text.replace("Jasper","")
            text=text.replace("on","")
            text=text.replace("google","")
            Text=str(text)
            speak(f"searching {Text} on google")
            find = google()
            find.search(Text)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing {} on youtube' + song)
            pywhatkit.playonyt(song)

        elif 'pick' and 'up' and 'line' in query:
            print("here, Some pickup line for you")
            speak("here, Some pickup line for you")
            print(pickuplines)
            speak(pickuplines)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%p")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            strDate= datetime.datetime.now().strftime("%d:%B:%Y")
            speak(f"Sir, the date is{strDate}")

        elif 'whatsapp' and 'message' in query:
            name = query.replace("whatsapp message", "")
            name=name.replace("send","")
            name=name.replace("to","")
            Name = str(name)
            speak(f"what's the message for{name}")
            message = takeCommand()
            msg=message
            from whatsapp import whatsappmsg
            whatsappmsg(Name,msg)

        elif "whatsapp" and "call" in query:
            from whatsapp import whatsappcall
            name=query.replace("whatsapp call","")
            name=name.replace("make","")
            name=name.replace("Jasper","")
            name=name.replace("to","")
            Name=str(name)
            speak(f"making whatsapp call to {Name}")
            whatsappcall(Name)

        elif "whatsapp" and "video" and "call" in query:
            from whatsapp import whatsappvideocall
            name=query.replace("whatsapp video call","")
            name=name.replace("make","")
            name=name.replace("Jasper","")
            name=name.replace("a","")
            name=name.replace("to","")
            Name=str(name)
            speak(f"making whatsapp video call to {Name}")
            whatsappvideocall(Name)

        elif "whatsapp" and "chat" in query:
            from whatsapp import whatsappchat
            name=query.replace("whatsapp chat","")
            name=name.replace("Jasper","")
            name=name.replace("open","")
            name=name.replace("of","")
            Name=str(name)
            speak(f"opening whatsapp chat of {Name}")
            whatsappchat(Name)

        elif 'bitcoin' in query:
            from bitcoinword import num
            speak("getting bitcoin price...")
            speak("Currently bitcoin price is" + num)
            print("Currently solana price is" + num)

        elif 'ethereum' in query:
            from etherenumword import num
            speak("getting ethereum price...")
            speak("Currently ethereum price is" + num)
            print("Currently solana price is" + num)

        elif 'binance' and 'coin' in query:
            from binanceword import num
            speak("getting binance coin price...")
            speak("Currently binance coin price is" + num)
            print("Currently solana price is" + num)

        elif 'xrp' in query:
            from xrpword import num

            speak("getting ripple price...")
            speak("Currently ripple price is" + num)
            print("Currently ripple price is" + num)

        elif 'cardano' in query:
            from cardanoword import num

            speak("getting cardano price...")
            speak("Currently cardano price is" + num)
            print("Currently cardano price is" + num)

        elif 'solana' in query:
            from solanaword import num

            speak("getting solana price...")
            speak("Currently solana price is" + num)
            print("Currently solana price is" + num)

        elif 'news' in query:
            print("Sure Sir, Here some latest news")
            speak("Sure Sir, Here some latest news")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        elif 'temperature' in query:
            speak("Today temperature in new delhi is" + str(temp()) + "degree celsius")
            speak("And Today's weather is" + str(des()))

        elif 'postman' in query:
            speak("opening postman")
            os.startfile("C:/Users/DELL/AppData/Local/Postman/Postman.exe")

        elif 'pycharm' in query:
            speak("opening pycharm")
            os.startfile("C:/Program Files/JetBrains/PyCharm Community Edition 2022.2/bin/pycharm64.exe")

        elif 'mysql workbench' in query:
            speak("opening mysql workbench")
            os.startfile("C:/Program Files/MySQL/MySQL Workbench 8.0 CE/MySQLWorkbench.exe")

        elif 'visual studio' in query:
            speak("opening visual studio")
            os.startfile("C:/Users/DELL/AppData/Local/Programs/Microsoft VS Code/Code.exe")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'is' and 'your' and 'name' in query:
            speak("My name is Jasper and I am a voice assistant")

        elif 'your' and 'crush' in query:
            speak("Don't want to say, but if you want to know , I like Siri, She is intelligent and adorable")

        elif 'sleep' in query:
            speak("Okay Sir, going to sleep")
            speak("have a good night")
            break

        elif 'favourite' and 'food' in query:
            speak("I really like electricity")

        elif 'brother' in query:
            speak("my brother name is jarvis, he is a top notch voice assistant, and  I really want to be like him "
                  "one day")



