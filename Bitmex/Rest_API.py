import requests

def get_bitmex_btc_price():
    url = "https://www.bitmex.com/api/v1/instrument?symbol=XBTUSD&columns=lastPrice"
    response = requests.get(url)
    data = response.json()
    if data:
        print("XBTUSD price on BitMEX:", data[0]['lastPrice'])

get_bitmex_btc_price()