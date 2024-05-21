import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=e8b295bd1f02443f82671855242105&q={city}"

r = requests.get(url)
# print(r.text)
weatherdic = json.loads(r.text)
w = weatherdic["current"]["temp_c"]
feelslike = weatherdic["current"]["feelslike_c"]
updated = weatherdic["current"]["last_updated"]

engine.say(f"The currnet weather in {city} is {w} degrees celcius and feels like {feelslike} degree celcius. This weather report was last updated on {updated}. Thank you!")
engine.runAndWait()