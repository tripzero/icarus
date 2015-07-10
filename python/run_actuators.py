from actuator_pwm import Run
from solarserver import MyServer
import json 
from constants import constants as x
import signal

#instantiate websocketclient
go = Run("127.0.0.1", "8080", x.maxActuatorHeight, x.speed)
print("client obj:", go.client)

#instantiate server + factory/listening
#server = MyServer()

#connect wsclient <--> autobahn myserver
go.connectToServer()

#start reactor


signal.signal(signal.SIGINT, signal.SIG_DFL)

go.reactorLoop(x.speed)

# signal = signal.signal(signal.SIGINT, signal.SIG_DFL)
