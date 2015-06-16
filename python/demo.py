#demo.py
#TODO: make demo_d utilize the config location
import tracker_funcs as t
import json, datetime

with open('config.json') as dataFile:
	config = json.load(dataFile)

#Intializing demo start time, actuator positioning relative to origin
dyear = config["locationInfo"]["year"]
dmonth = config["locationInfo"]["month"]
dday = config["locationInfo"]["day"]
dhour = config["locationInfo"]["hour"]
doffset = config["locationInfo"]["utc_time_diff"]
dminute = config["locationInfo"]["minute"]
dsecond = config["locationInfo"]["second"]
distAO1 = config["distInfo"]["distActuatorToOrigin"]
distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]

#intializing time
demo_d = datetime.datetime(dyear, dmonth, dday, dhour, dminute, dsecond, tzinfo = datetime.timezone.utc)
print("Input time (PST): ", demo_d)
demo_d += datetime.timedelta(hours = 7) #Converted inputted PST --> UTC standard 7 hours ahead
print("Output time(UTC): ", demo_d)

#Demo the day
lat = config["locationInfo"]["latitude"]
name = config["locationInfo"]["name"]
lon = config["locationInfo"]["longitude"]
demoLoc = t.Location(name, lat, lon, demo_d, distAO1, distAO2)
demoLoc.demoDay(37.3, -121.99, demo_d)
