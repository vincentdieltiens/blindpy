import hid, time

lights = []
def deviceInit():
	devices = []
	for d in hid.enumerate(0x054c, 0x1000):
		dev = hid.device(0x054c, 0x1000, d["path"])
		dev.set_nonblocking(True)
		for i in range(0, 10):
			dev.read(5)
		devices.append(dev)

		for x in range(0, 4):
			lights.append(0x0)
	return devices

class Buzzer:
	def __init__(self, device):
		self.device = device
		self.buzz = []

		for index in range(0, 4):
			print "add buzz"
			self.buzz.append(Buzz(self.device, index))

	def getDevice(self):
		return self.device

	def getBuzz(self, index):
		return self.buzz[index]

	def close(self):
		self.device.close()

class Buzz:
	def __init__(self, device, index):
		self.device = device
		self.index = index
		None

	def turnOn(self, duration=None):
		msg = [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0]
		msg[self.index + 2] = 0xFF
		self.device.write(msg)
		if duration:
			time.sleep(duration)
			self.turnOff()

	def turnOff(self):
		self.device.write([0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0]);

##
## 1. List the buzzers with a letter
##	

devices = deviceInit()
buzzers = []
for index, dev in enumerate(devices):
	buzzer = Buzzer(dev)
	buzzers.append(buzzer)

	buzzer.getBuzz(0).turnOn(1)
	buzzer.getBuzz(2).turnOn(3)

for buzzer in buzzers:
	buzzer.close()