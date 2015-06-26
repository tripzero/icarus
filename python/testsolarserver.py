import solarserver
import actuator_pwm as a


test = solarserver.SolarServer(3, a.tiltPercent, 700, True)
test.move(tiltPercent)
test.run() #TODO: difference between ^

# import lightserver
# from lights import OpenCvDriver, LightArray

# leds = lightserver.LightArrayServer(10, OpenCvDriver((20,20,20,20)))

# leds.run()