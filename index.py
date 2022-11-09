import requests
from pprint import pprint


API_Key = 'b3bca54ed048aa38a5cb0cd1f64368c7'

city = input("Enter a City Name: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"$q=+city"

weather_data = requests.get(base_url).json()

pprint(weather_data)
