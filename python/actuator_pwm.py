# Pulse width modification is used to move the actuator variably. 
#Documentation:  http://iotdk.intel.com/docs/master/mraa/python/mraa.html#mraa.Pwm
import mraa, time
from tracking import effectiveActuatorHeight
import pwm_funcs as pwm

maxActuatorHeight = 2
myPercent = effectiveActuatorHeight / maxActuatorHeight
a = pwm.Actuator(3, maxActuatorHeight, myPercent, 700, True)
a.set(myPercent, 700)