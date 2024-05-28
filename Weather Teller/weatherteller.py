import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    location = input("Input City Name For Weather Details or Write quit to exit \n")
    if location == "quit":
        speaker.Speak("Thanks For using Weather Teller")
        break
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key=0b19c581cbdc49d9b77162323242805&q={location}"
        r = requests.get(url)
        dict_weather = json.loads(r.text)
        celsius = dict_weather["current"]["temp_c"]
        print(f"Current Weather of {location} is {celsius} Degree Celsius ")
        speaker.Speak(f"Current Weather of {location} is {celsius} Degree Celsius ")
    except:
        print("Location Spelling Error")
        speaker.Speak("Location Spelling Error")