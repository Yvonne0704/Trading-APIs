import requests

url = "https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBTUSD&depth=5"
response = requests.get(url)

if response.ok:
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")