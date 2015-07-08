from __future__ import print_function
import mraa, datetime
from constants import constants as x
from tracking import myLoc, effectiveActuatorHeight1, effectiveActuatorHeight2
import pwm_funcs as pwm
from twisted.internet import task, reactor
import solarserver as s

class Run:
	"""The Run class connects client<-->server, sends tilt data, and moves the actuators."""
	def __init__(self, client_ip, client_port, maxActuatorHeight):

		self.client = s.WSClient(client_ip, client_port)
		self.client.debug = True
		self.minActuatorHeight = 0 
		self.maxActuatorHeight = maxActuatorHeight
		tiltPercent = 0

	def connectToServer(self):
		s.connectWS(self.client)

	def reactorLoop(self):
		loop = task.LoopingCall(self.moveA)
		loop.start(x.secToWait)
		reactor.run()

	"""Actuator a, tilting the panel up and down to maintain a 45 degree angle with the sun, is called every second by the reactor timer."""
	def moveA(self):
		d = datetime.datetime.utcnow()
		print(d.strftime('%H:%M:%S UTC'))
		d = d + datetime.timedelta(hours = x.offset)
		print((d.strftime('%H:%M:%S')), x.tz)
		print("\n", "|", "\n", "V", "\n")
		height = myLoc.calcTiltHeight(x.distAO1, datetime.datetime.utcnow())
		myLoc.printTiltHeight(x.distAO1, datetime.datetime.utcnow())
		tiltPercent = effectiveActuatorHeight1 / self.maxActuatorHeight
		self.client.update(tiltPercent)
		# a = pwm.Actuator(3, tiltPercent, 700, True) #comment these two lines out to see realtime values on your machine (ubuntu isn't mraa compatible)
		# a.move(tiltPercent)
	
	"""Actuator b is for panning the panel horizonally according to the azimuth. Currently NOT implemented in the DollHouse."""
	def moveB():
		print(datetime.datetime.utcnow().strftime('%H:%M:%S PST'))
		print(" |", "\n", "V")
		myLoc.calcPanHeight(x.distAO2, datetime.datetime.utcnow())
		myLoc.printPanHeight(x.distAO2, datetime.datetime.utcnow())
		panPercent = effectiveActuatorHeight2 / maxActuatorHeight
		client.update(tiltPercent2)
		# b = pwm.Actuator(3, panPercent, 700, True) #comment these two lines out if you want to see height change over time on your machine (ubuntu pc is not mraa compatible)
		# b.move(panPercent)

