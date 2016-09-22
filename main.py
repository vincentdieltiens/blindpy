from buzzer import Buzzer
from sony_buzzer import SonyBuzzer

class DeviceMock():
	def __init__(self):
		pass
	
	def write(self, data):
		pass

	def read(self, len):
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
		controller_index, button_index = raw_input('Indexes : ').split(',')
		index = (int(controller_index) * 5) + int(button_index)
		print controller_index, button_index, signals[index]
		
		return signals[index]

class SonyBuzzMock():
	@staticmethod
	def get_devices():
		return [DeviceMock()]
##
##
##
try:
	devices = SonyBuzzer.get_devices()
	#devices = SonyBuzzMock.get_devices()
	buzzer = Buzzer(devices)
	
	teams = ['A', 'B', 'C', 'D']
	index = None
	for i, team in enumerate(teams):
		controller = buzzer.get_controller(0, i)
		print 'Team ', team
		controller.light_on(i)
		r = buzzer.read(0, i, 0, timeout=4) # accepts read for controller i and button 0
		controller.light_off(i)
		
		if r is not None:
			index = i
			print "Player OK"
		else:
			break

	teams = teams[0:index+1]

	for i, team in enumerate(teams):
		controller = buzzer.get_controller(0, i)
		controller.light_blink(4, 0.2)

except IOError:
	print "No buffer found"