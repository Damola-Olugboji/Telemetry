# receiver code
import adafruit_rfm9x
import board
import busio
import digitalio

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DIgitalInOut(board.RFM9X_RST)

LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
# rfm9x.tx_power = 18


while True:
    packet = rfm9x.receive()
    if packet is None:
        LED.value = False
    else:
        LED.value = True
        packet_text = str(packet, "ascii")
        print("{0}".format(packet_text))


def sensor_data():
    while True:
        packet = rfm9x.receive()
        if packet is None:
            LED.value = False
        else:
            LED.value = True
            packet_text = str(packet, "ascii")
            return packet_text
