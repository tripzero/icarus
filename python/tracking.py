import tracker_funcs as t
import json, datetime
from pprint import pprint

#Initialize inputs
with open('config.json') as dataFile:
	config = json.load(dataFile)
print("config.json: ")
pprint(config)

distAO1 = config["distInfo"]["distActuatorToOrigin"]
distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]
name = config["locationInfo"]["name"]
lat = config["locationInfo"]["latitude"]
lon = config["locationInfo"]["longitude"]

#Configure time
curr_time = datetime.datetime(2015, 6, 15, 23, 00, 00, tzinfo = datetime.timezone.utc)
original_time = curr_time
print("Local time: ", curr_time)

#Example: JF1
print()
jf1 = t.Location("JF1", 45.541718, -122.960381, curr_time, distAO1, distAO2)
t.printLocationInfo(jf1)
jf1.calcTiltingHeight(distAO1)
jf1.calcPanningHeight(distAO2)
print()

#From config.json
print("Current location via config.json:")
myLoc = t.Location(name, lat, lon, curr_time, distAO1, distAO2)
t.printLocationInfo(myLoc)
inches = myLoc.calcTiltingHeight(distAO1)
effectiveActuatorHeight1 = inches

#Demo Seattle to figure out range of Actuator values
myLoc.demoDay(37.3, -121.99, curr_time)

#calculating second actuator (panning)
effectiveActuatorHeight2 = myLoc.calcPanningHeight(distAO2)
