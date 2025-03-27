import requests

def get_weather(city):
    """
    Fetches weather details for the provided city using OpenWeatherMap API.

    Parameters:
    - city: str, name of the city for which the weather needs to be fetched.

    Returns:
    - None: Prints the weather details to the console.
    """
    # API Key for OpenWeatherMap (You need to get your own API Key)
    api_key = "your_api_key_here"

    # Base URL of OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Construct final URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    try:
        # Send GET request to the OpenWeatherMap API
        response = requests.get(complete_url)

        # If the request was successful, process the data
        if response.status_code == 200:
            data = response.json()

            # Parse the data
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]

            # Extracting details
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            description = weather["description"]
            wind_speed = wind["speed"]

            # Displaying the weather information
            print(f"Weather in {city.capitalize()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description.capitalize()}")
            print(f"Wind Speed: {wind_speed} m/s")

        else:
            # If the API response status is not successful
            print(f"City {city} not found. Please check the city name.")

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors (network issues, invalid API key, etc.)
        print(f"Error: Unable to fetch data. {e}")

def main():
    print("Welcome to the Weather Program!\n")
    
    # Get user input for city name
    city = input("Enter the name of the city: ")
    
    # Get weather details for the entered city
    get_weather(city)

if __name__ == "__main__":
    main()
