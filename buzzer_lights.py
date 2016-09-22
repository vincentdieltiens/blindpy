class BuzzerLights():
	"""
		Represents the 4 ligts (red button) for a given device
	"""
	def __init__(self, device):
		self.device = device
		self.lights = [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0]
	
	def on(self, controller_index):
		self.lights[controller_index + 2] = 0xFF # light parameters begin at index 2
		self.device.write(self.lights)
	
	def off(self, controller_index):
		self.lights[controller_index + 2] = 0x0
		self.device.write(self.lights)
	
	def blink(self, controller_index, times=3, sleep_duration=0.2):
		for x in range(0, times):
			self.on(controller_index)
			time.sleep(sleep_duration)
			self.off(controller_index)
			time.sleep_duration(sleep_duration)

