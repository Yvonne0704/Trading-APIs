import requests

url = "https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=5"
response = requests.get(url)

if response.ok:
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
