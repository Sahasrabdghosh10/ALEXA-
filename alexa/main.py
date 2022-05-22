import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from GoogleNews import GoogleNews





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
googlenews = GoogleNews()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            talk('hello dear how can i help you ?')
            print( "listening .....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('playing ', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)



    elif 'tell about' in command:
        person = command.replace('tell about ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')


    elif 'are you single' in command:
        talk('I am in a relationship with wifi')


    elif 'joke' in command:
        talk(pyjokes.get_joke())


    elif 'weather' in command :
        city = command.replace('weather of ', '')



        talk('displaying the weather report of this city  ')
        url = 'https://wttr.in/{}'.format(city)
        res= requests.get(url)
        print(res.text)


    elif 'tech' in command:
        talk('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Tech')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5])
        talk(a)

    elif 'politics' in command:
        talk('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Politics')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5])
        talk(*a)

    elif 'sports' in command:
        talk('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Sports')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5])
        talk(*a[1:5])

    elif 'cricket' in command:
        talk('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('cricket')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5])
        talk(*a[1:5])

    elif 'football' in command:
        talk('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('football')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5])
        talk(*a[1:5])

    elif 'geopolitics' in command:
        talk('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('geopolitics')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5])
        talk(*a)


    else:
        talk('DONT SPEAK NONSENSE ')


while True:
    run_alexa()