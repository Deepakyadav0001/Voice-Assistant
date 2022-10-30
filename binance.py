from requests import Request,Session
import json


url="https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
parameters={
    'slug':'bnb',
    'convert':'USD'
}
headers={
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'04405b53-46c9-4abc-93e1-e94d8360a3c9'
}


session=Session()
session.headers.update(headers)

response=session.get(url, params=parameters)
binance=json.loads(response.text)['data']['1839']['quote']['USD']['price']
