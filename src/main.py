import network
import config
import uwebsockets.client

def connect(ssid = config.NETWORK_SSID, password = config.NETWORK_PASSWORD):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())

def start():
    with uwebsockets.client.connect("ws://" + config.SERVER) as websocket:
        websocket.send("🥐")

connect()
start()