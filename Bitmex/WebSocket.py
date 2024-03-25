import websocket
import json

def on_message(ws, message):
    print("Received message:")
    print(json.loads(message))

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    sub_request = json.dumps({
        "op": "subscribe",
        "args": ["instrument:XBTUSD"]
    })
    ws.send(sub_request)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://www.bitmex.com/realtime",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
