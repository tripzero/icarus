#!/usr/bin/env python

import ina219
import mppt
import time

output = ina219.Ina219()

mppt = mppt.Mppt(14, output, None, 16)

mppt.begin()

while True:
	mppt.poll()
	print("current volts: ", mppt.volts)
	print("current amps: ", mppt.current)
	print("pwm Value:", mppt.pwmValue)
	time.sleep(1)



