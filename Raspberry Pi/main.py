from sensor_information import SensorInformation
import threading


class Main():
    def __init__(self):
        self.sensor = SensorInformation()
        self.sensor.matrixRed()
        self.camera = cam()
        self.testingSequence()
        self.sensor.matrixGreen() #send radio message that valid data has been established
    
    def testingSequence(self):
        while not(flag):
            testInfo = self.sensor.sensorAggregate()
            flag = self.infoValidation(testInfo)


    def mainSequence(self):
        cameraThread = threading.Thread(target = self.camera.file_record())
        radioThread = threading.Thread(target = self.sendInformation())



    def infoValidation(self, temp):
        pass

    def sendInformation(self):



    



if __name__ == "__main__":
    main = Main()
    