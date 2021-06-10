import json, struct, threading
from sensor_information import SensorInformation
import time
import csv
from datetime import datetime
import pprint
import sys
import os.path


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
        #cameraThread = threading.Thread(target=self.camera.file_record())

        # send information class
        saveThread = threading.Thread(target=self.saveInformation)
        radioThread = threading.Thread(target=self.sendInformation)
        saveThread.start()
        radioThread.start()
        # cameraThread.start()

    def infoValidation(self, temp):

        return True

    def saveInformation(self):
        print("starting saveInformation")
        # templist = ["humidity","temperature", "pressure", "acceleration", "accelRaw", "orientation", "latitude", "longitude", "time", "altitude", "epv", "ept", "speed"]
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        while True:
            filename = open("sensor_information.txt", "a+")

            sensor_dict = self.sensor.sensorAggregate()
            sensor_values = list(sensor_dict.values())
            # will send only positional data for now
            filename.write(str(sensor_values) + "\n")
            

    def sendInformation(self):
        print("starting saveInformation")
        save_path = "/media/pi/CITCUITPY"
        filename = "sensor"
        while True:
            file1.write(self.sensor.sensor_byte())
            time.sleep(1)


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
        main = Main()
    except KeyboardInterrupt:
        import sys
        sys.exit()
