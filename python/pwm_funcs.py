# Pulse width modification is used to move the actuator variably. 
#Documentation:  http://iotdk.intel.com/docs/master/mraa/python/mraa.html#mraa.Pwm
import mraa, time

"""An instance of this class can be moved a certain percentage"""
class Actuator:
	#isPWM is true iff Pwm module is utilized	
	def __init__(self, pin, percent, period, isPWM):
		self.pin = pin
		self.isPWM = isPWM
		if isPWM:
			x = mraa.Pwm(pin)
		self.percent = percent
		self.period = period

	def move(self, percent):
		if self.isPWM:
			if percent < 0:
				return
			x.enable(True)
			x.period_us(700)
			x.write(percent)
			
			#Demo movement code:
			# val = 0
			# while val <= percent:
			# 	print(val)
			# 	x.write(val)
			# 	time.sleep(0.09)
			# 	val = val + 0.01
