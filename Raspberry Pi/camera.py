from picamera import PiCamera

class cam:
	def__init__(self):
		self.camera = PiCamera()
		self.camera.resolution = (1280,720)
		self.camera.framerate = 60
		#self.camera.start_preview()


	@staticmethod
	def file_record(self):
		self.camera.start_recording('flight_video.h264')
		self.camera.wait_recording(600)
		self.stop()
	
	@staticmethod
	def stop(self):
		self.camera.stop_recording()