from buzzer import Buzzer
import time

buzzer = Buzzer()

if buzzer.count():
	print "Step 1 : Confirm each buzzer"
	teams = ['A', 'B', 'C', 'D']
	for i, team in enumerate(teams):
		print 'Team ', team
		buzzer.turnOn(0, i)
		print buzzer.waitClick(0, i)
		buzzer.turnOff(0, i)
		
	

	#buzzer.close()
else:
	print "No buzzer found!"