# transceiver code
import adafruit_rfm9x
import board
import busio
import digitalio
import sys

sys.path.append("/Desktop/code/Telemetry/Pi/")
from sensor_information import SensorInformation

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DIgitalInOut(board.RFM9X_RST)

LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
rfm9x.tx_power = 18
while True:
    sensor_info = SensorInformation.sensor_byte
    rfm9x.send(sensor_info)
