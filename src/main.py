import time
import struct

from lib.lis3dh import LIS3DH_I2C
from machine import Pin, I2C
import config
import network
import socket


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
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    gyro = LIS3DH_I2C(i2c)

    address = socket.getaddrinfo(config.SERVER, config.PORT)[0][-1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(address)
    while True:
        x, y, z = gyro.acceleration
        print(time.localtime(), ":  ", x, y, z)
        data = struct.pack("3f", x, y, z)
        sock.send(data)
        time.sleep(0.1)


connect()
start()
