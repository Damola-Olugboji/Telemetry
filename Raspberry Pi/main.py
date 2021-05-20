import json, struct, threading
from sensor_information import SensorInformation


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
            with open("sensor_information.txt", "w") as f:
                f.write(json.dumps(sensor_dict))


def testprint(self):
    self.sensor = SensorInformation()
    while True:
        sensor_dict = self.sensor.sensorAggregate()
        print(json.dumps(sensor_dict))
        time.sleep(0.1)


if __name__ == "__main__":
    testprint()
