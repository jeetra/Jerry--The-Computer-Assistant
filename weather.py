from speak1 import speak

# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name
speak("Enter the city name")
CITY = input("Enter the city: ")
# API key
API_KEY = "38e505bccd2a6996d704ff5612f2970c"
#For Temperture in Celsius
units="metric"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY+"&units="+units
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"{CITY:-^30}")
   #speak(f"{CITY:-^30}")
   print(f"Temperature : {temperature}")
   speak(f"Today, the Temperature is, : {temperature}")
   print(f"Humidity : {humidity}")
   speak(f"The Humidity is, : {humidity}")
   print(f"Pressure : {pressure}")
   speak(f"The Pressure is, : {pressure}")
   print(f"Weather Report is: {report[0]['description']}")
   speak(f"And the, Weather Report is, : {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")
   speak("Error in the HTTP request")