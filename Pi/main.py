import json, struct, threading
from sensor_information import SensorInformation
import time
import csv
from datetime import datetime
import pprint


class Main:
    def __init__(self):
        self.sensor = SensorInformation()

        # self.sensor.matrixRed()
        # self.camera = cam()
        # self.testingSequence()
        # self.sensor.matrixGreen()  # send radio message that valid data has been established
        self.mainSequence()

    def testingSequence(self):
        while not (flag):
            testInfo = self.sensor.sensorAggregate()
            flag = self.infoValidation(testInfo)

    def mainSequence(self):
        cameraThread = threading.Thread(target=self.camera.file_record())

        # send information class
        radioThread = threading.Thread(target=self.saveInformation())

        radioThread.start()
        # cameraThread.start()

    def infoValidation(self, temp):

        return True

    def saveInformation(self):
        # templist = ["humidity","temperature", "pressure", "acceleration", "accelRaw", "orientation", "latitude", "longitude", "time", "altitude", "epv", "ept", "speed"]
        now = datatime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(dt_string + "_sensor_information.csv", "a", newline="") as f:
            while True:
                sensor_dict = self.sensor.sensorAggregate()
                sensor_values = list(sensor_dict.values())
                # will send only positional data for now
                struct = struct.pack(d
                    "ffff",
                    sensor_dict["longitude"],
                    sensor_dict["latitude"],
                    sensor_dict["altitude"],
                    sensor_dict["time"],
                )

                wr = csv.writer(f, dialect="excel")
                wr.writerow(sensor_values)


def testprint():
    sensor = SensorInformation()
    try:
        while True:
            sensor_dict = sensor.sensorAggregate()
            pprint.pprint(sensor_dict)
            time.sleep(0.1)
    except (KeyboardInterrupt):
        sensor.killThread()


if __name__ == "__main__":
    try:
        testprint()
    except:
        pass
