class ControllerSignal():
	signals = [
		# controller 1
		[0, 0, 1, 0, 240],
		[0, 0, 16, 0, 240],
		[0, 0, 8, 0, 240],
		[0, 0, 4, 0, 240],
		[0, 0, 2, 0, 240],
		# controller 2
		[0, 0, 32, 0, 240],
		[0, 0, 0, 2, 240],
		[0, 0, 0, 1, 240],
		[0, 0, 128, 0, 240],
		[0, 0, 64, 0, 240],
		# controller 3
		[0, 0, 0, 4, 240],
		[0, 0, 0, 64, 240],
		[0, 0, 0, 32, 240],
		[0, 0, 0, 16, 240],
		[0, 0, 0, 8, 240],
		# controller 4
		[0, 0, 0, 128, 240],
		[0, 0, 0, 0, 248],
		[0, 0, 0, 0, 244],
		[0, 0, 0, 0, 242],
		[0, 0, 0, 0, 241]
	]
	
	def __init__(self, device_index, data):
		self.data = data
		self.device_index = device_index
		
		
		self.valid = False
		for i, signal in enumerate(ControllerSignal.signals):
			if signal == data:
				self.controller_index = i // 5
				self.button_index = i % 5
				self.valid = True
	
	#def is_valid(self):
	#	return self.data is not None 
	#		and len(self.data) > 2
	#		and (data[2] > 0 or data[3] > 0 or data[4]> 240)
	def is_valid(self):
		return self.valid
	
	def matches(self, device_index=None, controller_index=None, button_index=None):
		if device_index is not None and device_index != self.device_index:
			return False
		elif controller_index is not None and controller_index != self.controller_index:
			return False
		elif button_index is not None and button_index != self.button_index:
			return False
		return True
	
	def get_controller_index():
		return self.controller_index
	
	def get_button_index():
		return self.button_index

class BuzzerController():
	"""
		Represents 1 of the 4 buzzer controllers with 5 buttons
	"""
	def __init__(self, device, controller_index, buzzer_lights):
		self.device = device
		self.controller_index = controller_index
		self.buzzer_lights = buzzer_lights
	
	def light_on(self, buzz_index):
		self.buzzer_lights.on(buzz_index)
	
	def light_off(self, buzz_index):
		self.buzzer_lights.off(buzz_index)
	
	def light_blink(self, times=3, sleep_duration=0.2):
		self.buzzer_lights.blink(self.controller_index, times, sleep_duration)
	
	def get_buzzer_lights(self):
		return self.buzzer_lights