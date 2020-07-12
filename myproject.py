import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr


engine = pyttsx3.init('sapi5') #sapi5 is microsoft speech recognition API.
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
#print(voices[0].id)

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour>12 and hour<18:
        speak('good afternoon')
    else:
        speak("good evening")
    speak('Hi amulya ,I am ladooo. Please tell me how I may help you')
def my_command():
    f = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        f.pause_threshold = 1
        f.adjust_for_ambient_noise(source, duration = 1)
        audio = f.listen(source)
    try:
        command = f.recognize_google(audio)
        print('You said '+command+'\n')
    except sr.UnknownValueError:
        print('Your last command could not be heard')
        command = my_command()
    return command


'''def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        command=r.recognize_google()
        print('recognizing..')
        query=r.recognize_google(audio, Language='en-in')
        print(f"user said that: {query}\n")
    except Exception as e:
        #print(e)

        print('say it again please..')
        return 'None'
    return query
'''
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = my_command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


    
