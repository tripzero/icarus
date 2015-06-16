# Pulse width modification is used to move the actuator variably. 
#Documentation:  http://iotdk.intel.com/docs/master/mraa/python/mraa.html#mraa.Pwm
import mraa, time
from tracking import effectiveActuatorHeight1, effectiveActuatorHeight2
import pwm_funcs as pwm

#Actuator a is for tilting the panel up and down--the angle towards to sun--to maintain a 45 degree angle
maxActuatorHeight = 2
myPercent = effectiveActuatorHeight1 / maxActuatorHeight
a = pwm.Actuator(3, maxActuatorHeight, myPercent, 700, True)
a.set(myPercent)


#Actuator b is for panning the panel horizonally--according to the azimuth
maxActuatorHeight = 2 #TODO: Confirm maxActuatorHeight is equivalent for both actuators and both will use mraa pwm
myPercent = effectiveActuatorHeight2 / maxActuatorHeight
b = pwm.Actuator(3, maxActuatorHeight, myPercent, 700, True)
b.set(myPercent)
