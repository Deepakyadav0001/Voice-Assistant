import requests

api_address="http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=38942e0cfa08f0fe2a0c696b3e47a823"
json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description=json_data["weather"][0]["description"]
    return description

