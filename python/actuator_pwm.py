# Pulse width modification is used to move the actuator variably. 
#Documentation:  http://iotdk.intel.com/docs/master/mraa/python/mraa.html#mraa.Pwm
import mraa, datetime
from time import sleep
import tracking as t
import pwm_funcs as pwm
from twisted.internet import task, reactor
import solarserver as s

minActuatorHeight, maxActuatorHeight = 0, 2
tiltPercent = 0

#instatiate client and tell it connect to local host.
solarServer = s.SolarServer()
client = s.WSClient("127.0.0.1", "6000")
print("READ actuator_pwm.py")
print(client)

"""Actuator a is for tilting the panel up and down--the angle towards to sun--to maintain a 45 degree angle. It should be called every second by the reactor timer."""
def moveA():
	print(datetime.datetime.now().strftime('%H:%M:%S PST'))
	print("|")
	print("V")
	t.myLoc.calcTiltingHeight(t.distAO1, datetime.datetime.now())
	tiltPercent = t.effectiveActuatorHeight1 / maxActuatorHeight
	client.update(tiltPercent)
	
	a = pwm.Actuator(3, tiltPercent, 700, True) #comment these two lines out if you want to see height change over time on your machine (ubuntu pc is not mraa compatible)
	a.move(tiltPercent)

loop = task.LoopingCall(moveA)
loop.start(1.0) #seconds; l.stop() can stop the looping
reactor.run()


"""Actuator b is for panning the panel horizonally according to the azimuth. It is currently NOT implemented in the SmartHouse."""
def moveB():
	print(datetime.datetime.now().strftime('%H:%M:%S PST'))
	print("|")
	print("V")
	t.myLoc.calcPanningHeight(t.distAO2, datetime.datetime.now())
	panPercent = t.effectiveActuatorHeight2 / maxActuatorHeight
	client.update(tiltPercent2)
	b = pwm.Actuator(3, panPercent, 700, True) #comment these two lines out if you want to see height change over time on your machine (ubuntu pc is not mraa compatible)
	b.move(panPercent)
