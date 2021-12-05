from sys import version_info
import speech_recognition as sr
import pyaudio
import os
import time
import pyttsx3
from gtts import gTTS
from time import ctime
import random
import datetime
import webbrowser
import wikipedia
import playsound

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Goodmorning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good evening sir")


r=sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        print('Say something')
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("sorry, i didn't get that")
        except sr.RequestError:
            speak("sorry,my speech service is down")
        return voice_data
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()        

'''
def speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1, 10000000)
    audio_file='audio-' + str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
            
'''
def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('my name is iki')
    elif 'time' in voice_data:
        print(ctime())
        speak(ctime())
    elif 'search' in voice_data:
        search=record_audio('what do you want to search for')
        url='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what i found for' +search)
    elif 'location' in voice_data:
        location=record_audio('what is the location')
        url='https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of' +location)
  
    elif 'wikipedia' in voice_data:
        speak("Searching wikipedia...")
        query=voice_data.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in voice_data:
        webbrowser.openm("youtube.com")
    elif 'open google' in voice_data:
        webbrowser.openm("google.com")    
    elif 'open stackoverflow' in voice_data:
        webbrowser.openm("stackoverflow.com")    
    elif 'play music' in voice_data:
        music_dr='D:'
        songs=os.listdir(music_dr)
        print(songs)
    elif 'exit' or 'thank you' or 'bye' or 'talk to to you later' in voice_data:
        speak('It was nice talking to you my friend see you soon')
        exit()    
    



time.sleep(1)
hour=int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    speak("Goodmorning sir")
elif hour>=12 and hour<18:
    speak("Good Afternoon sir")
else:
    speak("Good evening sir")
speak("How can i help you")
while 1 : 
    voice_data=record_audio()
    print(voice_data)            
    respond(voice_data)
