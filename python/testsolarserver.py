import solarserver
import actuator_pwm as a

if __name__ == '__main__':
    import sys
    from twisted.python import log
    # log.startLogging(sys.stdout)

def whenImConnected():
	testclient.send("printing some data")

testsuite = a.Run("127.0.0.1", "666")
#TODO: create a test class in this file which has a server

testserver = solarserver.MyServer() #ERROR
testclient = solarserver.WSClient("localhost", "80")
testclient.connected = whenImConnected
testclient.debug = False
testserver.debug = False
# test = solarserver.SolarServer(3, a.tiltPercent, 700, True)
# test.move(tiltPercent)



print("Printing testclient obj: ", testclient)
print("Printing testserver obj: ", testserver)

testserver.run() #TODO: why no prints
#TODO: call testclient.run





# import lightserver
# from lights import OpenCvDriver, LightArray

# leds = lightserver.LightArrayServer(10, OpenCvDriver((20,20,20,20)))

# leds.run()