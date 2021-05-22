import json, struct, threading
from sensor_information import SensorInformation
import time
import pandas as pd


class Main:
    def __init__(self):
        self.sensor = SensorInformation()

        # self.sensor.matrixRed()
        self.camera = cam()
        self.testingSequence()
        # self.sensor.matrixGreen()  # send radio message that valid data has been established
        self.mainSequence()

    def testingSequence(self):
        while not (flag):
            testInfo = self.sensor.sensorAggregate()
            flag = self.infoValidation(testInfo)

    def mainSequence(self):
        cameraThread = threading.Thread(target=self.camera.file_record())
        radioThread = threading.Thread(target=self.sendInformation())

        radioThread.start()
        cameraThread.start()

    def infoValidation(self, temp):

        return True

    def sendInformation(self):
        #templist = ["humidity","temperature", "pressure", "acceleration", "accelRaw", "orientation", "latitude", "longitude", "time", "altitude", "epv", "ept", "speed"]
        global df
        df = pd.DataFrame()
        while True:
            sensor_dict = self.sensor.sensorAggregate()
            
            struct = struct.pack(
                "ffff",
                sensor_dict["longitude"],
                sensor_dict["latitude"],
                sensor_dict["altitude"],
                sensor_dict["time"],
            )
            # will send only positional data for now
            df = df.append(sensor_dict, ignore_index = True)
            
        


def testprint():
    sensor = SensorInformation()
    try:
        while True:
            sensor_dict = sensor.sensorAggregate()
            print(json.dumps(sensor_dict))
            time.sleep(0.1)
    except (KeyboardInterrupt):
        sensor.killThread()

if __name__ == "__main__":
    try:
        testprint()
    except:
        df.to_csv('sensor_information') 
