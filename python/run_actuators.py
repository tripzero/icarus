from actuator_pwm import Run
from solarserver import MyServer
import json 
from constants import constants as x
import signal

#instantiate websocketclient
go = Run("127.0.0.1", "8080", x.maxActuatorHeight, x.speed)
print("client obj:", go.client)

#instantiate server, thereby the factory/listening
server = MyServer()

#connect wsclient <--> server
go.connectToServer()

#start reactor
if x.realtime:
	go.reactorLoop(False)
else:
	go.reactorLoop()

#print("signal obj", signal)
signal = signal.signal(signal.SIGINT, signal.SIG_DFL)

#server.unregister() #VERIFY: this isn't working as is