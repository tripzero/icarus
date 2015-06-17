# Pulse width modification is used to move the actuator variably. 
#Documentation:  http://iotdk.intel.com/docs/master/mraa/python/mraa.html#mraa.Pwm
import mraa, datetime
from time import sleep
import tracking as t
import pwm_funcs as pwm

minActuatorHeight = 0
maxActuatorHeight = 2

"""Actuator a is for tilting the panel up and down--the angle towards to sun--to maintain a 45 degree angle"""
while True:
	sleep(t.secToWait)
	print(datetime.datetime.now().strftime('%H:%M:%S PST'))
	print("|")
	print("V")
	t.myLoc.calcTiltingHeight(t.distAO1, datetime.datetime.now())
	tiltPercent = t.effectiveActuatorHeight1 / maxActuatorHeight
	
	a = pwm.Actuator(3, tiltPercent, 700, True) #comment these two lines out if you want to see height change over time
	a.move(tiltPercent)


"""Actuator b is for panning the panel horizonally according to the azimuth. It is currently not implemented in the SmartHouse."""
##rewrite in akin format ^^^ if eventually reinstated
# maxActuatorHeight = 2
# panningPercent = t.effectiveActuatorHeight2 / maxActuatorHeight
# b = pwm.Actuator(3, panningPercent, 700, True)
# b.move(panningPercent)
