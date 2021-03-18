from picamera import PiCamera
from bmpsensor import bmp
from threading import Thread
import board
import busio
import adafruit_bmp3xx



class Activation:
    def __init__(self, cam, bmp):
        self.camera = cam
        self.bmp = bmp

    def start(self):
        # while(gpsstilltransmitting)
        self.thread1 = Thread(target=self.bmp.transmit_data())
        self.thread2 = Thread(target=self.camera.file_record())
        #self.thread3 = Thread(target=self.)

        # after while




class bmp:
    def __init__(self):
        # I2C setup
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.bmp = adafruit_bmp3xx.BMP3XX_I2C(self.i2c)
        self.bmp.pressure_oversampling = 8
        self.bmp.temperature_oversampling = 2
        self.p0 = 0

    @classmethod
    def transmit_data(self):
        self.transmit = True
        while transmit:
            """print(
                "Pressure: {:6.4f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature)
            )"""
            return bmp.pressure, bmp.temperature, self.hypersometric(bmp.pressure, bmp.temperature)
            time.sleep(1)

    @staticmethod
    def stop(self):
        self.transmit = False

    @staticmethod
    def hypersometric(self, P, T):
        return (((self.p0 / P) ** (1 / 5.257)) - 1) * (T + 273.15) / 0.0065

class cam:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.framerate = 60
        self.camera.start_preview()


    @staticmethod
    def file_record(self):
        self.camera.start_recording('flight_video.h264')
        self.camera.wait_recording(600)


    @staticmethod
    def stop(self):


    @staticmethod
    def stop(self):
        self.camera.stop_recording()

if __name__ == "__main__":
    camera = cam()
    bmpsensor = bmp()
    activator1 = Activation(camera, bmpsensor)