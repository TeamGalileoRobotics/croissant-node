import time

import adafruit_lis3dh
import board
import busio
import config
import digitalio
import network
import uwebsockets.client


def connect(ssid=config.NETWORK_SSID, password=config.NETWORK_PASSWORD):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())


def start():
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    cs = digitalio.DigitalInOut(board.D5)  # Set to appropriate CS pin!
    int1 = digitalio.DigitalInOut(board.D6)  # Set to correct pin for interrupt!
    lis3dh = adafruit_lis3dh.LIS3DH_SPI(spi, cs, int1=int1)

    with uwebsockets.client.connect("ws://" + config.SERVER) as websocket:
        while True:
            x, y, z = lis3dh.acceleration
            websocket.send((x, y, z))
            time.sleep(0.1)


connect()
start()
