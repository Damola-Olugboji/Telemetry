# transceiver code
import adafruit_rfm9x
import board
import busio
import digitalio
import sys, os


spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)

LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
rfm9x.tx_power = 18
while True:
    tempfile = open("sensor.bin", "rb+")
    if os.stat("sensor.bin").st_size == 0:
        pass
    else:
        byte = tempfile.read(1)
        rfm9x.send(byte)
        tempfile.truncate(0)
