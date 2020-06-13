import pyttsx3  # pip install pyttsx3-- May require pypiwin32--support in python 3.7
import datetime
import speech_recognition as sr  # pip install SpeechRecognition--- Require PyAudio
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishMe():
    speak("Welcome back sir!")
    time()
    date()

    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    elif 18 <= hour < 24:
        speak("Good Evening sir")
    else:
        speak("Good Night sir")

    speak("jarvis at your service. Please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', '123')
    server.sendmail('abc@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("E:/PyCharm/Jarvis/ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)


def jokes():
    joke = pyjokes.get_joke()
    speak(joke)


if __name__ == "__main__":
    #wishMe()

    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                # sendEmail(to, content)
                speak(content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the mail")
        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Users/God/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        # elif 'logout' in query:
        #     os.system("shutdown -l")
        # elif 'shutdown' in query:
        #     os.system("shutdown /s /t 1")
        # elif 'restart' in query:
        #     os.system("shutdown /r /t 1")
        # elif 'play songs' in query:
        #     song_dir = "E:/Songs"
        #     songs = os.listdir(song_dir)
        #     os.startfile(os.path.join(song_dir, songs[0]))
        elif 'remember that' in query:
            speak("What should I remember")
            data = takeCommand()
            speak("you said me to remember " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that " + remember.read())
            remember.close()
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()  

        elif 'offline' in query:
            quit()
