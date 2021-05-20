import time, os
from sense_hat import SenseHat
from gps import *


class SensorInformation:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_imu_config(False, True, True)
        self.green = [0, 255, 0]
        self.red = [255, 0, 0]
        self.gpsp = GpsPoller()
        self.gpsp.start()

    def sensorAggregate(self):
        time = gpsd.utc, " + ", gpsd.fix.time
        sensorDict = {
            "humidity": self.sense.get_humidity(),
            "temperature": self.sense.get_temperature(),
            "pressure": self.sense.get_pressure(),
            "acceleration": self.sense.get_accelerometer(),
            "accelRaw": self.sense.get_accelerometer_raw(),
            "Orientation": self.sense.get_orientation_degrees(),
            "latitude": gpsd.fix.latitude,
            "longitude": gpsd.fix.longitude,
            "time": time,
            "altitude": gpsd.fix.altitude,
            "epv": gpsd.fix.epv,
            "ept": gpsd.fix.ept,
            "speed": gpsd.fix.speed,
        }

        return sensorDict

    @classmethod
    def matrixRed(self):
        mat = [red] * 64
        self.sense.set_pixels(mat)

    @classmethod
    def matrixGreen(self):
        mat = [green] * 64
        self.sense.set_pixels(mat)

    def matrixOff(self):
        self.sense.clear()


class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        gps = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = True

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()
