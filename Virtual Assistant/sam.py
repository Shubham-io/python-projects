import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            # print("the command is printed=", Query)

        except Exception as e:
            # print(e)
            print("waiting for response...")
            return "None"

        return Query


def speak(audio):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 140)

    engine.say(audio)
    engine.runAndWait()


def tellTime():

    time = str(datetime.datetime.now())
    # this "2020-06-05 17:50:14.582630"
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("Current time is" + hour + "Hours and" + min + "Minutes")


def Hello():
    speak("hello sir, how can I help you")


def specific_query():
    sq = takeCommand().lower()
    return sq


def Take_query():

    Hello()

    while (True):

        query = takeCommand().lower()

        if "open notepad" in query:
            speak("Opening notepad ")
            path = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(path)
            continue

        elif "close notepad" in query:
            speak("Closing notepad ")
            path = 'taskkill/im notepad.exe'
            os.system(path)

            continue

        elif "open google.com" in query:
            speak("Opening google")
            webbrowser.open("www.google.com")
            continue

        elif "tell the time" in query:
            tellTime()
            continue

        # this will exit and terminate the program
        elif "terminate yourself" in query:
            speak("terminated successfully")
            exit()

        elif "define blockchain" in query:
            result = wikipedia.summary('blockchain', sentences=1)
            print(result)
            speak(result)
            continue

        elif "thank you sam" in query:
            speak("it's my pleasure")
            continue

        elif "create a file" in query:
            speak("what do you want to name the file")
            fileName = specific_query()
            with open(fileName + ".txt", "w") as file:
                speak("file has created")
                speak("what do you want to write inside it")
                content = specific_query()
                file.write(str(content))
                speak("file has been written")
                continue

        elif "open the file" in query:
            speak("opening the file")
            os.startfile(fileName+".txt")
            continue

        elif "what is your name" in query:
            speak("I am sam. Your Virtual Assistant.")
            continue


# main function starts here
Take_query()



#  ✅ Available Voice Commands
# 📝 Notepad

# "open notepad"

# "close notepad"

# 🌐 Web

# "open google.com"

# ⏰ Time

# "tell the time"

# 📚 Knowledge

# "define blockchain"

# 📄 Files

# "create a file"
# (Sam will ask for the file name and content)

# "open the file"
# (Opens the last created file)

# 🗣️ Assistant Interaction

# "what is your name"

# "thank you sam"

# ❌ Exit

# "terminate yourself"