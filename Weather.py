import requests
import sys
import os
from dotenv import load_dotenv 

load_dotenv()

if len(sys.argv)<2:
    print("Usage: python weather.py <city>")
    sys.exit()

city = sys.argv[1]

API_KEY= os.getenv("API_KEY")

if not city:
    print("City cannot be empty")
    sys.exit()

if not API_KEY:
    print("API key not found. Check your .env file")
    sys.exit()

url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url,timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Error:",e)
    sys.exit()


temp = data["main"]["temp"]
weather = data["weather"][0]["description"]
humidity=data["main"]["humidity"]
wind = data["wind"]["speed"]

print(f"\nWeather in {city.capitalize()}:")
print("-"*40)
print(f"🌡️  Temperature : {temp}°C")
print(f"☁️  Condition   : {weather}")
print(f"💧  Humidity    : {humidity}%")
print(f"🌬️  Wind Speed  : {wind} m/s")

if data.get("cod") !=200:
    print("City not found. Please recheck your input")
    sys.exit()