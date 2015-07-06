import json
import datetime
from pprint import pprint
import tracker_funcs as t

#Initialize inputs
with open('config.json') as dataFile: # print("config.json: ") # pprint(config)
	config = json.load(dataFile)

distAO1 = config["distInfo"]["distActuatorToOrigin"]
distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]
secToWait = config["distInfo"]["moveActuatorPerUnitOfSeconds"]
name = config["demoLocationInfo"]["name"]
tz = config["demoLocationInfo"]["tz_name"]
lat = config["demoLocationInfo"]["latitude"]
lon = config["demoLocationInfo"]["longitude"]

d = datetime.datetime.now()
def printTime():
	print("Current local time is ", d, "and timezone is ", tz)
#JF1 example location
def calcExample():
	print()
	jf1 = t.Location("JF1", 45.541718, -122.960381, d, distAO1, distAO2)
	t.printLocationInfo(jf1)
	jf1.calcTiltingHeight(distAO1, jf1.time)
	jf1.calcPanningHeight(distAO2, jf1.time)
	print()

#Config file's location
myLoc = t.Location(name, lat, lon, d, distAO1, distAO2)
t.printLocationInfo(myLoc)
effectiveActuatorHeight1 = myLoc.calcTiltingHeight(distAO1, myLoc.time)
effectiveActuatorHeight2 = myLoc.calcPanningHeight(distAO2, myLoc.time)


printTime()
calcExample()
