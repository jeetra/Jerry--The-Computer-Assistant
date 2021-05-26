from selenium import webdriver # to control browser operations
# from  datetime import datetime
import pyjokes
import wikipedia
import pywhatkit
import time
import os
import smtplib # import pyttsx3  # pip import pyttsx3
import webbrowser
import speech_recognition as sr  # pip install speechRecognition
import datetime
import sys
from speak1 import speak

# import wolframalpha

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


# print(current_time)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!!")
   
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon sir!!")
   
    else:
        speak("Good evening sir!!")
        print("Good evening sir!!")
    speak("Jerry on your service ")
    speak("It's :")
    speak(current_time)

    speak(", how may I help you today?")


def takeCommand():
    # It takes mircophone input from the user and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"User said :{query}\n")

        except Exception as e:
            # print(e)

            print("Say that again please....")
            # speak("Say that again please....")
            return "NONE"
    return query


email_list = {
                    dictionary having name as key and email address as passowrd
            
}




def myWork():
    print("1. To communicate with others I can send email to person you like.")
    speak("1. To communicate with others I can send email to person you like.")
    print("2. to explore new content I can take you to Google chrome.")
    speak("2. to explore new content I can take you to Google chrome.")
    print("3. I can play any song on youtube for you.")
    speak("3. I can play any song on youtube for you.")
    print("4. I can search anything on wikipedia for you.")
    speak("4. I can search anything on wikipedia for you.")
    print("5. I can open any software in the system.")
    speak("5. I can open any software in the system.")
    print("6. I can open youtube on your command.")
    speak("6. I can open youtube on your command.")
    print("7. For new learning I can open geeksforgeeks site.")
    speak("7. For new learning I can open geeksforgeeks site.")
    print("8. To make you feel happy, I can play songs on youtube.")
    speak("8. To make you feel happy, I can play songs on youtube.")
    print("9. I can show you time to keep you on time everywhere.")
    speak("9. I can show you time to keep you on time everywhere.")
    print("10. I can put the system on sleep")
    speak("10. I can put the system on sleep")
    print("11. I can lock on your command")
    speak("11. I can lock on your command")
    print("12. I can take selfies")
    speak("12. I can take selfies")
    print("13. I can take screenshots")
    speak("13. I can take screenshots")
    print("14. I can show any location on map")
    speak("14. I can show any location on map")
    print("15. I can show you weather of any city you like")
    speak("15. I can show you weather of any city you like")
    print("16. I can download youtube videos for you")
    speak("16. I can download youtube videos for you")
    print("17. I can make pencil sketch for you of your photos")
    speak("17. I can make pencil sketch for you photos")
    print("18. I can download instagram's user profile you like")
    speak("18. I can download instagram's user profile you like")





def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email address, 'passowrd of email address')
    server.sendmail('your email address', to, content)
    server.close()


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    # start1()
    clear()
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'what can you do' in query:
            myWork()

        elif 'open youtube' in query:
            print("Opening youtube")
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening google chrome")
            speak("Opening google chrome")
            webbrowser.open("google.com")

        elif 'open geeks for geeks' in query:
            print("Opening geeksforgeeks site")
            speak("Opening geeksforgeeks site")
            webbrowser.open("geeksforgeeks.com")

        elif 'play' in query:
            speak("Just a moment, playing it")
            pywhatkit.playonyt(query)

        elif 'wikipedia' in query:
            speak("Just a moment, searching wikipedia")
            thing = query.replace('wikipedia', '')
            info = wikipedia.summary(thing, 2)
            print(info)
            speak("According to wikipedia, ")
            speak(info)

        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif 'the time' in query:
            strt=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strt)


        elif 'the weather' in query:
            os.system('python weather.py')

        elif 'lock my pc' in query:
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif 'put the laptop in sleep' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'minimise windows' in query:
            speak("Minimisng all windows")
            os.system('''powershell -command "(new-object -com shell.application).minimizeall()"''')

        elif 'open powerpoint' in query:
            speak("Opening microsoft powerpoint 2016")
            codePath = "address of powerpoint's exe file"
            os.startfile(codePath)

        elif "open excel" in query:
             speak("Opening microsoft Excel 2016")
             codePath = "address of excel's exe file"
             os.startfile(codePath)

        elif 'open word' in query:
            print("Opening microsoft word 2016")
            speak("Opening microsoft word 2016")
            wordPath = "address of word's exe file"
            os.startfile(wordPath)

        elif 'open sublime' in query:
            speak("Opening Sublime Text")
            limePath = "address of sublime's exe file"
            os.startfile(limePath)

        elif 'send email' in query:
            try:
                print("To whom should I send the mail")
                speak("To whom should I send the mail")
                name = takeCommand()
                to = email_list[name]
                print(to)
                speak("What should I say")
                print("What should I say")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend ,I am not able to send this email")

        elif 'take a photo' in query:
            os.system("python camera.py")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Jeet sir.")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)

        elif "who are you" in query:
            speak("I am a virtual assistant, created by Jeet")

        elif "write a note" in query:
            speak("What should I write, sir")
            note = takeCommand()
            file = open('Notes.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strt=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strt)
                file.write(" :- ")
                file.write(note)
                speak('Note written')
            else:
                file.write(note)
                speak('Note written')

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Notes.txt", "r")
            print(file.read())
            speak(file.read(6))

        
        elif 'send whatsapp message' in query:
            pywhatkit.sendwhatmsg('your mobile number with countrycode', 'mesaage to be sent', hour of message to be sent, minute of message to be sent)
            speak("Done")

        elif 'download youtube video' in query:
            try:
                speak("Enter the url of video??")
                os.system('python Download_Youtube_video.py')
                speak("Video Downloaded.")

            except Exception as e:
                print(e)
                speak("Not able to download due to some error !, see terminal")

        elif 'take a screenshot' in query:
            speak("Taking a screenshot in 8 seconds")
            os.system('python Screenshot.py')
            speak("Screenshot taken.")

        elif 'find location' in query:
                os.system('python map.py')

        elif 'download instagram profile' in query:
            speak("Enter the username of profile?")
            try:
                os.system('python insta.py')
                speak("Profile downloaded.")
            except Exception as e:
                print(e)
                speak("Not able to download due to some error!, see terminal")

        elif 'generate qr code' in query:
            os.system('python generate_QR_code.py')

        elif 'make a pencil sketch' in query:
            os.system('python image_to_pencil_sketch.py')

        elif 'show weather' in query:
            os.system('python weather.py')

        elif 'bye' in query:
            speak("bye sir!, have a good day")
            sys.exit()
