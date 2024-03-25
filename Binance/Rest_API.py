import requests

def get_binance_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    print("BTCUSDT price on Binance:", data['price'])

get_binance_btc_price()