from __future__ import print_function
from __future__ import division
import mraa, datetime
from constants import constants as x
from tracking import myLoc, effectiveActuatorHeight1, effectiveActuatorHeight2
import pwm_funcs as pwm
from twisted.internet import task, reactor
import solarserver as s

class Run:
	"""The Run class connects client<-->server, sends tilt data, and moves the actuators."""
	def __init__(self, client_ip, client_port, maxActuatorHeight, speedUpFactor):

		self.client = s.WSClient(client_ip, client_port)
		self.client.debug = True
		self.minActuatorHeight = 0 
		self.maxActuatorHeight = maxActuatorHeight
		self.speedUpFactor = speedUpFactor
		if speedUpFactor < 1:
			self.speedUpFactor = 1
		tiltPercent = 0
		self.stop = False
		self.demoT = datetime.datetime(x.year, x.month, x.day, 0, 0, 0)
		#self.startDay = datetime.datetime(x.year, x.month, x.day, 0, 0, 0)

	def connectToServer(self):
		s.connectWS(self.client)

	def reactorLoop(self, tiltDemoDay = True):
		if not tiltDemoDay:	
			print("tiltDemoDay")			
			loop = task.LoopingCall(self.tiltInfinitely)
		else:
			print("tiltDemoDay")			
			loop = task.LoopingCall(self.tiltDemoDay)

		#INITIATE LOOP
		loop.start(1/self.speedUpFactor) #x.secToWait

		reactor.run()
		
	"""Actuator a, tilting the panel up and down to maintain a 45 degree angle with the sun, is called every second by the reactor timer."""
	def tiltDemoDay(self):

		daysPast = ( (int(self.demoT.strftime('%d'))) - x.day)
		monthsPast = ( (int(self.demoT.strftime('%m'))) - x.month)
		yearsPast = ( (int(self.demoT.strftime('%y'))) - x.year)


		print("startDay: ", x.day, "; ", int(self.demoT.strftime('%d')))

		print(daysPast, " days ,", monthsPast, "months ,", yearsPast, "years ", "has elapsed", "at a speedup of x", x.speed)

		self.demoT = self.demoT + datetime.timedelta(minutes = 1)

		#Initializing UTC time
		print(self.demoT.strftime('%H:%M:%S UTC'))

		#Printing Local Time
		prnt = self.demoT + datetime.timedelta(hours = x.offset)
		print((prnt.strftime('%H:%M:%S')), x.tz)

		print("\n", "|", "\n", "V", "\n")

		#Calculate heights; VERIFY self.demoT IS ITERATING
		height = myLoc.calcTiltHeight(x.distAO1, self.demoT)
		myLoc.printTiltHeight(x.distAO1, self.demoT)
		tiltPercent = effectiveActuatorHeight1 / self.maxActuatorHeight
		self.client.update(tiltPercent)
		# a = pwm.Actuator(3, tiltPercent, 700, True) #comment these two lines out to see realtime values on your machine (ubuntu isn't mraa compatible)
		# a.move(tiltPercent)



	"""Actuator a, tilting the panel up and down to maintain a 45 degree angle with the sun, is called every second by the reactor timer."""
	def tiltInfinitely(self):
		#Initializing UTC time
		d = datetime.datetime.utcnow()
		print(d.strftime('%H:%M:%S UTC'))

		#Printing Local Time
		d = d + datetime.timedelta(hours = x.offset)
		print((d.strftime('%H:%M:%S')), x.tz)

		print("\n", "|", "\n", "V", "\n")

		#Calculate heights
		height = myLoc.calcTiltHeight(x.distAO1, datetime.datetime.utcnow())
		myLoc.printTiltHeight(x.distAO1, datetime.datetime.utcnow())
		tiltPercent = effectiveActuatorHeight1 / self.maxActuatorHeight
		self.client.update(tiltPercent)

		##write to stats
		f = file("stats.py")
		f = open('stats.py', 'w')
		print("As of ", datetime.datetime.now().strftime('%H:%M:%S UTC'), file = f)
		f.write("Tilting actuator height: \r")
		f.write(str(effectiveActuatorHeight1))
		f.write("\nPanning actuator height: ")
		f.write( str(effectiveActuatorHeight2))
		f.close()

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

