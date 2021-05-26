import pyttsx3
engine = pyttsx3.init('sapi5')  # microsoft Speech api
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 210)
engine.setProperty('volume', 1.0)

def speak(audio: object) -> object:
   """

   :rtype: object
   """
   engine.say(audio)
   engine.runAndWait()

if __name__=='__main__':
    speak()