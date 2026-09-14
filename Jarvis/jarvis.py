# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx
import webbrowser
import speech_recognition as sr
import pyttsx3
import musicLibrary
import os

# pip install openai
# from openai import OpenAI
# from openai import OpenAI
# client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# pip install google generativeai

apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": "chrome.exe",
    "paint": "mspaint.exe",
    "vscode": "code",
}
import datetime
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
 
def process_command(c):
    c = c.lower().strip()

    if c.startswith("open "):
        target = c.removeprefix("open ").strip()

        if target in apps:
            speak(f"Opening {target}")
            os.startfile(apps[target])
        else:
            speak(f"searching for {target}")
            webbrowser.open(f"https://www.google.com/search?q={target}")

        '''
        c = c.lower().strip()
        if c.startswith("open "):
            site = c.removeprefix("open ").strip()
            speak(f"Searching for {site}")
            webbrowser.open(f"https://www.google.com/search?q={site}")   
        '''
    
    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:])
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("I don't have that song")

    elif "the time" in c.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strfTime}")

 
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            word = input("You: ")

            if "jarvis" in word.lower():
                speak("Yes, How can I help you")

                # Stay active until user says "sleep" or "exit"
                while True:
                    command = input("You: ")
                    if command.lower() in ["sleep", "exit", "stop"]:
                        speak("Going to sleep")
                        break

    
                    process_command(command)

        except Exception as e:
            print("Error; {0}".format(e))
            
