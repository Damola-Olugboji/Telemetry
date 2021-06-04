import time, os
from sense_hat import SenseHat
from gps import *
import threading
from datetime import datetime


class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = True

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()


global gpsp
gpsp = GpsPoller()


class SensorInformation:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_imu_config(False, True, True)
        self.green = [0, 255, 0]
        self.red = [255, 0, 0]
        gpsp.start()

    def sensorAggregate(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        sensorDict = {
            "time": time,
            "humidity": self.sense.get_humidity(),
            "temperature": self.sense.get_temperature(),
            "pressure": self.sense.get_pressure(),
            "acceleration": self.sense.get_accelerometer(),
            "accelRaw": self.sense.get_accelerometer_raw(),
            "Orientation": self.sense.get_orientation_degrees(),
            "latitude": gpsd.fix.latitude,
            "longitude": gpsd.fix.longitude,
            "altitude": gpsd.fix.altitude,
            "epv": gpsd.fix.epv,
            "ept": gpsd.fix.ept,
            "speed": gpsd.fix.speed,
        }

        return sensorDict

    def matrixRed(self):
        mat = [red] * 64
        self.sense.set_pixels(mat)

    def matrixGreen(self):
        mat = [green] * 64
        self.sense.set_pixels(mat)

    def matrixOff(self):
        self.sense.clear()

    def killThread(self):
        gpsp.running = False
        gpsp.join()
        print("Thread Killed")
