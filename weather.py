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

# Print header
print("🌤️  Weather Checker")
print("=" * 40)

# Loop to allow checking multiple cities
keep_going = True

while keep_going:
    # Ask user which city they want
    city = input("\nWhich city do you want to check? (e.g., Durham,NC,US): ")

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
        print(f"\nError fetching weather data: {response.status_code}")
        print(response.text)

    # Ask if user wants to check another city
    print()
    another = input("Check another city? (yes/no): ").lower()

    if another != 'yes':
        keep_going = False
        print("\nThanks for using Weather Checker! Stay safe out there! 🌤️")
        print("=" * 40)
