import tracker_funcs as t
import json, datetime, copy
import pysolar.constants as c
from pysolar.simulate import simulate_span

with open('config.json') as dataFile:
	config = json.load(dataFile)

#Intializing demo start time, actuator positioning relative to origin
dyear = config["startTimeInfo"]["year"]
dmonth = config["startTimeInfo"]["month"]
dday = config["startTimeInfo"]["day"]
dhour = config["startTimeInfo"]["hour"]
dminute = config["startTimeInfo"]["minute"]
dsecond = config["startTimeInfo"]["second"]
doffset = config["locationInfo"]["hours_after_UTC"]
distAO1 = config["distInfo"]["distActuatorToOrigin"]
distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]

#Intializing time
demo_d = datetime.datetime(dyear, dmonth, dday, dhour, dminute, dsecond, tzinfo = datetime.timezone.utc)
print("Input time: ", demo_d.strftime('%H:%M:%S'))
demo_d += datetime.timedelta(hours = -doffset) #Converted inputted (PST) --> UTC standard (+7 hrs)
print("Utilized time(UTC): ", demo_d.strftime('%H:%M:%S'))

#Demo the day
lat = config["locationInfo"]["latitude"]
name = config["locationInfo"]["name"]
lon = config["locationInfo"]["longitude"]
demoLoc = t.Location(name, lat, lon, demo_d, distAO1, distAO2)
demoLoc.simulateDemoDay(37.3, -121.99, -7, "PST")
