from camera import cam
from bmpsensor import bmp
import pandas


class Activation:
    def __init__(self, cam, bmp):
        self.camera = cam
        self.bmp = bmp

    def start(self):
        # while(gpsstilltransmitting)
        self.bmp.transmit_data()
        self.camera.file_record

        # after while

        self.bmp.stop()
        self.camera.stop()