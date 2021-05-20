from gps import *
import time, os


class SensorInformation:
    def __init__(self, sense):
        self.sense = sense
        self.sense.clear()
        self.sense.set_imu_config(False, True, True)
        self.green = [0, 255, 0]
        self.red = [255, 0, 0]

    @classmethod
    def sensorAggregate(self):

        gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)
        report = gpsd.next()
        if report["class"] == "TPV":
            lat = getattr(report, "lat", 0.0)
            lon = getattr(report, "lon", 0.0)
            time = getattr(report, "time", "")
            alt = getattr(report, "alt", "nan")
            epv = getattr(report, "epv", "nan")
            ept = getattr(report, "ept", "nan")
            speed = getattr(report, "speed", "nan")

        humidity = self.sense.get_humidity()
        temp = self.sense.get_temperature()
        pressure = self.sense.get_pressure()
        accel = self.sense.get_accelerometer()
        accel_raw = self.sense.get_accelerometer_raw()
        orientation = self.sense.get_orientation_degrees()

        sensorDict = {
            "humidity": humidity,
            "temperature": temp,
            "pressure": pressure,
            "acceleration": accel,
            "accelRaw": accel_raw,
            "Orientation": orientation,
            "latitude": lat,
            "longitude": lon,
            "time": time,
            "altitude": alt,
            "epv": epv,
            "ept": ept,
            "speed": speed,
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
