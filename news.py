import requests

api_address="https://newsapi.org/v2/top-headlines?country=us&apikey=3ae4c068c75d4c2da4125a8ee9881325"
json_data=requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append(" Number "+str(i+1)+"," +json_data["articles"][i]["title"]+".")

    return ar

