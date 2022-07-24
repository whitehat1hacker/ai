from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import json
import os
#import time
#import msvcrt as m
#from time import sleep
#from playsound import playsound
import msvcrt as m
import webbrowser
import pyjokes
#import wikipedia
import random





def wait():
    m.getch()


APRIL = pyttsx3.init('sapi5')
voice=APRIL.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_ZiraM'
rate = APRIL.getProperty('rate')
APRIL.setProperty('rate', 170)
voices = APRIL.getProperty('voices')
APRIL.setProperty('voice',assistant_voice_id)


def speak(audio):
    print('APRIL: ' + audio)
    APRIL.say(audio)
    APRIL.runAndWait()


def time():
    Time = datetime.datetime.now().strftime('%I:%M: %p')
    speak('It is')
    speak(Time)


def date():
    today = datetime.datetime.now().strftime(
        'the date today is %d %m %Y, please notice that the format is day, month, year')
    speak(today)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 3 and hour < 12:
        speak('Good morning sir. it is a great day today')
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)

    elif hour >= 12 and hour < 18:
        speak('Good afternoon sir')
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)

    elif hour >= 18 and hour < 22:
        speak('Good evening sir')
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)

    elif hour >= 22 and hour < 3:
        speak('It is late sir, let us take a nap')
        speak('it is')
        Time = datetime.datetime.now().strftime('%I %M: %p')
        speak(Time)
        speak('How can I help you now')
        print('')
        print('listening ...')
        print('')





model = Model(r"C:\Users\asmid\PycharmProjects\vosk\vosk-model-en-in-0.5\vosk-model-en-in-0.5")  # assets/vosk-model-en-us-0.22 ## assets/model-light-with-graph
os.system('cls')
welcome()
rec = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)



stream.start_stream()

a = 0





while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        print('sir: ' + result['text'])

        if "hello" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('Hello sir, how can I help you?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        elif "time" in result['text']:
            Time = datetime.datetime.now().strftime('%I %M: %p')
            speak('It is')
            speak(Time)
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "date" in result['text']:
            today = datetime.datetime.now().strftime('%h')
            speak(today)
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        elif "2" in result['text']:
            rand = random.choice("hi, hello, by")
            speak(rand)
            print('')
            print('listening ...')
            print('')

        elif "month" in result['text']:
            today = datetime.datetime.now().strftime('%m')
            speak(today)
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who are you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('Hi, I am your virtual assistant. How can I help you now, sir?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "April" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('yes sir')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')



        elif "who made you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who make you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who created you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who create you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "where are you from" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('i am from India')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "relaxing music" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is some music for you, hope you enjoy')
            os.startfile('chill songs.mp3')
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "arcade" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is some music for you, hope you enjoy')
            os.startfile('arcade.mp3')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "note" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak(f'This is notepad for sir to note')
            os.system('notepad')
            speak(f'What else would you like me do do, sir?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')




        elif "stop" in result or "exit" in result or "bye" in result['text']:
            speak("Assistant is off. Goodbye sir")
            quit()

        elif "joke" in result['text']:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
            speak(f'What else would you like me do do, sir?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        elif "google" in result['text']:
            try:
                webbrowser.open("https://www.google.com")
                speak("opening google")
                print("opening google")
            except:
                speak("Internet connection error")
                print("")
        else:
            os.system('cls')
            stream.stop_stream()
            print('sir: ' + result['text'])
            speak('sorry please repeat again')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')





