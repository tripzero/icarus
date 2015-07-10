import json
import actuator_pwm as a
import solarserver
from constants import constants as x

if __name__ == '__main__':
    import sys
    from twisted.python import log
    # log.startLogging(sys.stdout)

def whenImConnected():
	testclient.send(json.dumps("printing some data").encode('utf8'))


testserver = solarserver.MyServer() 
#testclient = solarserver.WSClient("localhost", "8080")
#testclient.connected = True
#whenImConnected()
#testclient.debug = False
testserver.debug = False

#self.server.sendMessage(msg, True)

#print("Printing testclient obj: ", testclient)
print("Printing testserver obj: ", testserver)

testsuite = a.Run("127.0.0.1", "8080", 2, 1)
testsuite.connectToServer()

#make sure that the reactorLoop is after everything
testsuite.reactorLoop(x.speed)
