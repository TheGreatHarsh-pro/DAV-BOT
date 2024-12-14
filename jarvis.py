    
import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
import NewsRead





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)
    try:
        print("loading...")
        query  = r.recognize_google(audio,language='en-in')
     
    except Exception as e:
        print("I cannot understand please repeat ")
        speak("I cannot understand please repeat")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "start functioning" in query:
            from GreetMe import greetMe
            greetMe()

            speak("dear guest please enter your name, using keybord")
            name=input("what is your name ?")
            speak("nice to meet you "+name+" ji")
            speak("I am AI functioned chatbot and I can help you with many of your important daily tasks like opening an app, telling time, doing searches, telling temperature, telling you a joke or random fact or just chat with me. Tell me with what can I help you"+name+" ji")

            while True:
                query = takeCommand().lower()
                if "sleep mode" in query:
                    speak("Ok boss, You can call me anytime"+name+" ji")
                    break                     
                elif "i am fine" in query:
                    speak("that's great ! With what can I help you with"+name+"ji")
                elif "What is your name" in query:
                    speak("My name is DAVbot")
                elif "good" in query:
                    speak("that's great ! With what can I help you with"+name+"ji")
                elif "What is your name" in query:
                    speak("My name is DAVbot")
                elif "nice" in query:
                    speak("that's great ! With what can I help you with"+name+"ji")
                elif "What is your name" in query:
                    speak("My name is DAVbot")


                elif "tell me a joke" in query:
                    speak("want to  know a construction joke ??")
                    speak("")
                    speak("I am still working on it")
                    speak("what else i can do for"+name+" ji")
                    
                
                elif "tell me another joke" in query:
                    speak("Why was the math book sad?")
                    speak("It had too many problems.")
                    
                elif "fun fact" in query:
                    speak("Here are some fun facts: A snail can sleep for three years")
                    speak("Bananas are naturally radioactive.")
                    speak("The average person laughs about 17 times a day.")
                    speak("With what else can I help you with ?")
                elif "how are you" in query:
                    speak("Perfect ! With what can I help you with ?")

                elif ("introduce yourself to sir") in query:
                    speak("Hello !My name is DAVbot, and I am a chatbot linked with artificial intelligence ready to help you with your daily tasks... Would you like to know about my functions ??")


                   
                
                elif "thank you" in query:
                    speak("you are welcome, "+name+" ji")
                
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "weather" in query:
                    search = "weather in ghaziabad"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "temperature right now" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "about D A V" in query:
                    speak('''The D.A.V. College Managing Committee, familiarly known as D A V C M C, is a non-governmental educational organisation in India and overseas with over 900 schools,[2] 75 colleges and a university. 
                        It is based on the ideals of Dayananda Saraswati and Arya Samaj.
                        The Dayanand Anglo-Vedic (D A V) education system also comprises colleges offering graduates and post-graduates degrees in areas of study all over India.''')
                
                
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,"+name+" ji")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")   
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                                
                elif "tired" in query:
                    speak("Playing your favourite songs, "+name+" ji")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=V1RPi2MYptM")

                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "what is my name" in query:
                    speak("your name is"+name+" ji")   
                
                elif "stop functioning" in query:
                    speak("shutting down,"+name+" ji")
                    exit() 