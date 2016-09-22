import hid

class SonyBuzzer():
	@staticmethod
	def get_devices():
		devices = []
		for device_index, d in enumerate(hid.enumerate(0x054c, 0x1000)):
			dev = hid.device(0x054c, 0x1000, d["path"])
			dev.set_nonblocking(True)
			
			for i in range(0, 10):
				dev.read(5)
			
			devices.append(dev)

		return devices