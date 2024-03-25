import requests

url = "https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=5"
response = requests.get(url)

if response.ok:
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")