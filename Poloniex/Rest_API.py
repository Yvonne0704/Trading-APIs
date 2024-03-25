import requests

def get_poloniex_btc_price():
    url = "https://poloniex.com/public?command=returnTicker"
    response = requests.get(url)
    data = response.json()
    print("BTC price in USDT on Poloniex:", data['USDT_BTC']['last'])

get_poloniex_btc_price()