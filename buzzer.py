from datetime import datetime

from controller import ControllerSignal, BuzzerController
from buzzer_lights import BuzzerLights

class Buzzer():
	def __init__(self, devices):
		self.devices = devices
		self.controllers = []
		self.lights = []
		
		for device_index, dev in enumerate(devices):
			buzz_lights = BuzzerLights(dev)
			self.lights.append(buzz_lights)
			
			self.controllers.append([])
			for i in range(0, 4):
				controller = BuzzerController(dev, i, buzz_lights)
				self.controllers[device_index].append(controller)
			
	def get_lights(self, device_index):
		return self.lights[device_index]
	
	def get_devices(self):
		return self.devices

	def get_controllers(self, device_index):
		return self.controllers[device_index]
	
	def get_controller(self, device_index, controller_index):
		return self.controllers[device_index][controller_index]

	def read(self, device_index=None, controller_index=None, 
		     button_index=None, timeout=None):
		start_time = datetime.now()
		while 1:
			stop_time = datetime.now()
			delta = stop_time - start_time

			if timeout is not None and delta.seconds > timeout:
				return None

			for device in self.devices:
				data = ControllerSignal(device_index, device.read(5))
				if data.is_valid() and data.matches(device_index, controller_index, button_index):
					return data