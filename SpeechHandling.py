API_ENDPOINT = 'https://api.wit.ai/speech'
wit_access_token = 'your-access-token'
from AudioProcessor import *
from FacebookAutomater import *
import requests
import json
import pyttsx3
import gi
import os
def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 10):
    
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    
    # converting response content to JSON format
    data = json.loads(resp.content)
    
    # get text from data
    print(data)
    texts = data['text']
    os.remove(AUDIO_FILENAME) 

    
    # return the text
    return texts
def speakEmailAndPassword():
    text =  RecognizeSpeech('speech.wav')
    words = text.split()
    number=""
    i = 0
    for word in words:
        if(i==10):
            break
        if(word=="one"):
            number+=str(1)
        elif(word=="zero"):
            number+=str(0)
        elif(word=="two"):
            number+=str(2)
        elif(word=="three"):
            number+=str(3)
        elif(word=="four"):
            number+=str(4)
        elif(word=="five"):
            number+=str(5)
        elif(word=="six"):
            number+=str(6)
        elif(word=="seven"):
            number+=str(7)
        elif(word=="eight"):
            number+=str(8)
        elif(word=="nine"):
            number+=str(9)
        i+=1
    password = words[-1]
    print(password)
    print(number)
    if(fb.do_login(number,password)):
        speak("You have successfully logged in!")
        return 1
    else:
        print("error")
        return 0
def speak(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')

    # Set volume 0-1
    engine.setProperty('voice', voices[10].id)

    engine.setProperty('volume', 0.7)
    engine.say(message)
    engine.runAndWait()