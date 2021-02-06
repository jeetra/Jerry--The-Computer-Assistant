import pyjokes
import wikipedia
import pywhatkit
from time import ctime
import os
import smtplib 
import pyttsx3 #pip importpyttsx3
import webbrowser
import speech_recognition as sr #pip install speechRecognition
import datetime
import sys


engine = pyttsx3.init('sapi5') #microsoft Speech api
voices=engine.getProperty ('voices') 
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)




def wishMe():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning sir!!")
		print("Good Morning sir!!")
	elif hour>=12 and hour<17:
		speak("good Afternoon sir!!")
		print("good Afternoon sir!!")
	else:
		speak("Good evening sir!!")
		print("Good evening sir!!")
	speak("Jerry on your service , how may I help you today?")
	print("Jerry on your service , how may I help you today?")



def speak(audio):	
	engine.say(audio)
	engine.runAndWait()

def takeCommand():
	#It takes mircophone input from the user and returns the string output
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 1
		audio=r.listen(source)

		try:
			print("Recognizing....")
			query=r.recognize_google(audio,language='en-in')
			print(f"User said :{query}\n")
		
		
		except Exception as e:
			#print(e)

			print("Say that again please....")
			#speak("Say that again please....")
			return"NONE"
	return query

email_list={
			'Jeet':'jeetraiwal@gmail.com',
			'Dad':'niranjankumarraiwal@gmail.com',
			'Mom':'manjulataraiwal@gmail.com',
			'Saurabh':'sourabh.raiwal@gmail.com',
			'Ved Sir':'vedkumargupta@ipsacademy.org',
			'Aishwarya':'aishwaryaaric12@gmail.com',
			'Vanshika':'somanivanshika30002@gmail.com',
			'Isha':'mehtaisha3006@gmail.com',
			'Priyanka':'bhardwaj.priyanka.99@gmail.com',
			'Manvendra':'manvendra.nema1@gmail.com'

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
	print("8. To make you feel happy, I can play songs.")
	speak("8. To make you feel happy, I can play songs.")
	print("9. I can show you time to keep you on time everywhere.")
	speak("9. I can show you time to keep you on time everywhere.")
	print("10. I can put the system on sleep")
	speak("10. I can put the system on sleep")
	print("11. I can lock on your command")
	speak("11. I can lock on your command")

def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('jolly.raiwal@gmail.com','Football@07')
	server.sendmail('jolly.raiwal@gmail.com',to,content)
	server.close()

if __name__=="__main__":
	wishMe()
	while True:
		query=takeCommand().lower()
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


		elif 'open geeksforgeeks' in query:
			print("Opening geeksforgeeks site")
			speak("Opening geeksforgeeks site")
			webbrowser.open("geeksforgeeks.com")


		elif 'play' in query:
			speak("Just a moment, playing music")
			pywhatkit.playonyt(query)
			#music_dir="C:\\music"
			#songs=os.listdir(music_dir)
			#print(songs)
			#os.startfile(os.path.join(music_dir,songs[0]))

		elif 'wikipedia' in query:
			speak("Just a moment, searching wikipedia")
			thing=query.replace('wikipedia','')
			info=wikipedia.summary(thing,3)
			print(info)
			speak(info)


		elif 'joke' in query:
			speak(pyjokes.get_joke())



		elif 'the time' in query:
			print(ctime())
			speak(ctime())


		elif 'lock my pc' in query:
			os.system("rundll32.exe user32.dll,LockWorkStation")
		
		elif 'put the laptop in sleep' in query:
			os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

		elif 'minimise windows' in query:
			speak("Minimisng all windows")
			os.system('''powershell -command "(new-object -com shell.application).minimizeall()"''')


	   

		elif 'open code' in query:
			speak("Opening Visual Studio Code")
			codePath="C:\\Users\\Jeet Raiwal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			print("O")
			os.startfile(codePath)


		elif 'open word' in query:
			print("Opening microsoft word 2016")
			speak("Opening microsoft word 2016")
			wordPath="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
			os.startfile(wordPath)

		elif 'open sublime' in query:
			speak("Opening Sublime Text")
			limePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(limePath)

		elif 'open notepad++' in query:
			speak("Opening notepad++")
			notePath="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
			os.startfile(notePath)


		elif 'send email' in query:
			try:
				print("To whom should I send the mail")
				speak("To whom should I send the mail")
				name=takeCommand()
				to=email_list[name]
				print(to)
				speak("What should I say")
				print("What should I say")
				content=takeCommand()
				sendEmail(to,content)
				speak("Email has been sent")
			except Exception as e:
				print(e)
				speak("Sorry my friend ,I am not able to send this email")


		elif 'send whatsup message' in query:
			pywhatkit.sendwhatmsg('9993417064', 'Happy birthday',17,46)

		else:
			if 'bye' in query:
				speak("bye sir!, have a good day")
				sys.exit()









