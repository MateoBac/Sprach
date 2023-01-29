import speech_recognition as sr
import win32com.client as wincl
import random
import datetime


#Antwortslisten
Test = ['Alles in ordnung', 'Alles Klar','Dass War Ein test']
WEISS   = ( 255, 255, 255)


# obtain audio from the microphone
r = sr.Recognizer()

def say(sag):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(sag)



global Text
Text = ''
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:

        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='de-DE')


        except Exception as e:

            return "None"
        return statement



say('Bereit')

while True:
    Text = takeCommand().lower()
    

    if Text.startswith('python'):
        print(Text)
        Text = Text.replace("python", "")
        if 'test' in Text:
            say(random.choice(Test))

        elif 'exit' in Text:
            exit()


        elif 'uhrzeit' in Text or ' uhr' in Text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f'Wir Haben {strTime}')


        elif 'langsam' in Text:
            say('dass ich Langsam Bin Ist Googels Schuld da Dies Mich Schelcht Verarbeitet')







