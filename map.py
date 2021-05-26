import webbrowser
from speak1 import speak

speak("Enter the location you want to search: ")
location =input("Enter the location you want to search: ")
#speak("User asked to Locate")
#speak(location)
speak("Opening Google Maps with your location")
webbrowser.open("https://www.google.nl/maps/place/" + location + "")