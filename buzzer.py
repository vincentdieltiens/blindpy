import hid, time
import datetime as dt
from threading import Timer, Lock

LOCK = Lock()

class Buzzer:
	def __init__(self):
		self.devices = []
		self.buzz = []
		self.lights = []
		
		#print hid.enumerate(0x054c, 0x1000)
		for deviceIndex, d in enumerate(hid.enumerate(0x054c, 0x1000)):
			dev = hid.device(0x054c, 0x1000, d["path"])
			dev.set_nonblocking(True)
		
			for i in range(0, 10):
				dev.read(5)
			self.devices.append(dev)

			#self.lights.append([])
			#for x in range(0, 4):
			#lights = [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0]
			self.lights.append([0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0])
			#self.lights[deviceIndex] = lights
		
	def count(self):
		return len(self.devices)

	def turnOn(self, deviceIndex, buzzIndex, duration=None, after=None):
		lights = self.lights[deviceIndex]
		lights[buzzIndex + 2] = 0xFF
		
		self.devices[deviceIndex].write(lights)
		
		if duration:
			t = Timer(duration, self.turnOff, (deviceIndex, buzzIndex, after))
			t.start()
			#self.turnOff(deviceIndex, buzzIndex)

	def turnOff(self, deviceIndex, buzzIndex, after=None):
		lights = self.lights[deviceIndex]
		lights[buzzIndex + 2] = 0x0
		self.devices[deviceIndex].write(lights)

		if after:
			after()

	def waitClick(self, deviceIndex=None, buzzIndex=None):
		def isValid(data):
			return data is not None and len(data) > 2 and (data[2] > 0 or data[3] > 0 or data[4] > 240)

		def isActive(i):
			if deviceIndex is not None and buzzIndex is not None:
				info = getInfo(i)
				return info['buzz'] == buzzIndex
			return False

		def getInfo(i):
			return {'buzz': i//5, 'button': i % 5}

		answers = [
			#1
			[0, 0, 1, 0, 240],
			[0, 0, 16, 0, 240],
			[0, 0, 8, 0, 240],
			[0, 0, 4, 0, 240],
			[0, 0, 2, 0, 240],
			#2
			[0, 0, 32, 0, 240],
			[0, 0, 0, 2, 240],
			[0, 0, 0, 1, 240],
			[0, 0, 128, 0, 240],
			[0, 0, 64, 0, 240],
			#3
			[0, 0, 0, 4, 240],
			[0, 0, 0, 64, 240],
			[0, 0, 0, 32, 240],
			[0, 0, 0, 16, 240],
			[0, 0, 0, 8, 240],
			#
			[0, 0, 0, 128, 240],
			[0, 0, 0, 0, 248],
			[0, 0, 0, 0, 244],
			[0, 0, 0, 0, 242],
			[0, 0, 0, 0, 241]
		]

		while 1:
			for device in self.devices:
				data = device.read(5)
				
				if isValid(data):
					for i, d in enumerate(answers):
						if d == data and isActive(i):
							return getInfo(i)


	def blink(self, deviceIndex, buzzIndex):
		self.turnOn(deviceIndex, buzzIndex)
		time.sleep(0.2)
		self.turnOff(deviceIndex, buzzIndex)
		time.sleep(0.2)
		self.turnOn(deviceIndex, buzzIndex)
		time.sleep(0.2)
		self.turnOff(deviceIndex, buzzIndex)

	def getDevice(self, index):
		return self.devices[index]

	def close(self):
		for dev in self.devices:
			dev.close()