import board
import busio
import adafruit_bmp3xx


class bmp:
    transmit = False
    p0 = 0
    def __init__(self):

        #I2C setup
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
        self.bmp.pressure_oversampling = 8
        self.bmp.temperature_oversampling = 2
        

    @classmethod
    def transmit_data(self)
        transmit = True
        while transmit:
            """print(
                "Pressure: {:6.4f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature)
            )"""
            return bmp.pressure, bmp.temperature, self.hypersometric(bmp.pressure, bmp.temperature)
            time.sleep(1)
            
    @staticmethod
    def stop(self):
        transmit = False

    @staticmethod
    def hypersometric(self, P, T):
        return (((p0/P)^(1/5.257)) - 1) * (T+273.15)/ 0.0065



# SPI setup
"""from digitalio import DigitalInOut, Direction

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = DigitalInOut(board.D5)
bmp = adafruit_bmp3xx.BMP3XX_SPI(spi, cs)"""