
import pyttsx3
tts= pyttsx3.init()
voices=tts.getProperty('voices')
tts.setProperty('voice',voices[0].id)
print("welcome to RoboSpeaker 1.1.0")
text2="welcome to RoboSpeaker 1.1.0, i am an artificial voice, and say whatever you type!"
tts.say(text2)
tts.runAndWait()
text=input("enter your text here: ")
tts.say(text)
tts.runAndWait()

    