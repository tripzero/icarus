# Pulse width modification is used to move the actuator variably. 
#Documentation:  http://iotdk.intel.com/docs/master/mraa/python/mraa.html#mraa.Pwm
import mraa, time


class Actuator:
	#isPWM is true iff Pwm module is utilized	
	def __init__(self, pin, maxHeight, percent, period, isPWM):
		self.pin = pin
		self.isPWM = isPWM
		if isPWM:
			x = mraa.Pwm(pin)
		self.maxHeight = maxHeight
		self.percent = percent
		self.period = period

	def set(self, percent):
		if self.isPWM:
			x.enable(True)
			x.period_us(700)

			val = 0
			while val <= percent:
				print(val)
				x.write(val)
				time.sleep(0.09)
				val = val + 0.01
