from actuator_pwm import Run
from solarserver import MyServer
import json 

with open('config.json') as dataFile: 
	config = json.load(dataFile)
maxActuatorHeight = config["distInfo"]["maxActuatorHeight"]

#instantiate websocketclient
go = Run("127.0.0.1", "8080", maxActuatorHeight)
print("client obj:", go.client)

#instantiate server, thereby the factory/listening
server = MyServer()

#connect wsclient <--> server
go.connectToServer()



#start reactor
go.reactorLoop()



