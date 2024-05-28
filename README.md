# Weather Teller

Weather Teller is a Python-based application that provides current weather details for a specified city using the WeatherAPI and reads the weather information aloud using the `win32com` library on Windows.

## Features

- Fetches current weather data for a given city.
- Provides temperature in Celsius.
- Reads the weather information aloud using text-to-speech.
- User can exit the application by typing "quit".

## Usage

1. Replace `'0b19c581cbdc49d9b77162323242805'` in `weatherteller.py` with your actual WeatherAPI key. You can get an API key by signing up on the [WeatherAPI website](https://www.weatherapi.com/).
2. Run the `weatherteller.py` script:
    ```sh
    python weatherteller.py
    ```
3. Enter the city name when prompted, or type "quit" to exit the application.
4. The weather information will be printed on the screen and read aloud.
