# Pulse width modification is used to move the actuator variably. 
#Documentation:  http://iotdk.intel.com/docs/master/mraa/python/mraa.html#mraa.Pwm
import mraa, time

class Actuator:
	#isPWM is true iff Pwm module is utilized	
	def __init__(self, pin, maxHeight, percent, period, isPWM):
		self.pin = pin
		self.maxHeight = maxHeight
		self.percent = percent
		self.period = period
		self.isPWM = isPWM
		if isPWM:
			self.module = mraa.Pwm(pin)

	def set(self, percent):
		if self.isPWM:
			self.module.enable(True)
			self.module.period_us(700)

			val = 0
			while val <= percent:
				print(val)
				self.module.write(val)
				time.sleep(0.09)
				val = val + 0.01
