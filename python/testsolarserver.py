import solarserver
import actuator_pwm as a

if __name__ == '__main__':
    import sys
    from twisted.python import log
    # log.startLogging(sys.stdout)

def whenImConnected():
	testclient.send(bytes("printing some data"), True)

testsuite = a.Run("127.0.0.1", "666", 2)
#TODO: create a test class in this file which has a server
testsuite.reactorLoop()

testserver = solarserver.MyServer() #ERROR
testclient = solarserver.WSClient("localhost", "80")
testclient.connected = True
whenImConnected()
testclient.debug = False
testserver.debug = False

#self.server.sendMessage(msg, True)

print("Printing testclient obj: ", testclient)
print("Printing testserver obj: ", testserver)

