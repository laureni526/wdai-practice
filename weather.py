#!/usr/bin/env python3
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# OpenWeatherMap API endpoint
url = "http://api.openweathermap.org/data/2.5/weather"

# Ask user which city they want
print("🌤️  Weather Checker")
print("=" * 40)
city = input("Which city do you want to check? (e.g., Durham,NC,US): ")

# Parameters for the requested city
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'imperial'  # Use Fahrenheit
}

# Make the API request
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Extract weather information
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    conditions = data['weather'][0]['description']
    humidity = data['main']['humidity']

    # Display the weather
    print(f"\n🌤️  Current Weather in {city}")
    print(f"=" * 40)
    print(f"Temperature: {temp}°F")
    print(f"Feels like: {feels_like}°F")
    print(f"Conditions: {conditions.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"=" * 40)
else:
    print(f"Error fetching weather data: {response.status_code}")
    print(response.text)
