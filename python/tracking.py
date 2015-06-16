import tracker_funcs as t
import json, datetime
from pprint import pprint
from pysolar.time import get_delta_t, tt_offset, get_leap_seconds


#Initialize inputs
with open('config.json') as dataFile: # print("config.json: ") # pprint(config)
	config = json.load(dataFile)


distAO1 = config["distInfo"]["distActuatorToOrigin"]
distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]
name = config["locationInfo"]["name"]
lat = config["locationInfo"]["latitude"]
lon = config["locationInfo"]["longitude"]

#TODO: allow for current time input?
#Configure Pacific time
d = datetime.datetime.now()
print("Current local time is ", d)



# curr_time = datetime.datetime(2015, 6, 15, 23, 00, 00, tzinfo = datetime.timezone.utc)
# original_time = curr_time
print("Local time: ", d)

#Example: JF1
print()
jf1 = t.Location("JF1", 45.541718, -122.960381, d, distAO1, distAO2)
t.printLocationInfo(jf1)
jf1.calcTiltingHeight(distAO1)
jf1.calcPanningHeight(distAO2)
print()

#From config.json
print("Current location via config.json:")
myLoc = t.Location(name, lat, lon, d, distAO1, distAO2)
t.printLocationInfo(myLoc)
inches = myLoc.calcTiltingHeight(distAO1)
effectiveActuatorHeight1 = inches

#calculating second actuator (panning)
effectiveActuatorHeight2 = myLoc.calcPanningHeight(distAO2)
