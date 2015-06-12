import tracker_funcs as t
import json, datetime
from pprint import pprint

#Initialize inputs
with open('config.json') as dataFile:
	config = json.load(dataFile)
print("config.json: ")
pprint(config)

#Configure time
curr_time = datetime.datetime.now()
print("Local time: ", curr_time)

#Example: JF1
print()
jf1 = t.Location("JF1", 45.541718, -122.960381)
t.printLocationInfo(jf1)
t.calcTiltingHeight(jf1, 2.8)
t.calcPanningHeight(jf1, 2.8)
print()

#From config.json
print("Current location via config.json:")
myLoc = t.Location( config["locationInfo"]["name"], config["locationInfo"]["latitude"], config["locationInfo"]["longitude"])
distTiltToOrigin = config["distInfo"]["distActuatorToOrigin"]
t.printLocationInfo(myLoc)
inches = t.calcTiltingHeight(myLoc, distTiltToOrigin)
effectiveActuatorHeight1 = inches

#calculating second actuator (panning)
distPanToOrigin = config["distInfo"]["distPanningActuatorToOrigin"]
effectiveActuatorHeight2 = t.calcPanningHeight(myLoc, distPanToOrigin)
