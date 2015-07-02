import tracker_funcs as t
import json, datetime, copy
import pysolar.constants as c
#from pysolar.simulate import simulate_span

with open('config.json') as dataFile:
	config = json.load(dataFile)

#Intializing simulation demo start time, actuator positioning relative to origin
dyear = config["SimulationInfo"]["year"]
dmonth = config["SimulationInfo"]["month"]
dday = config["SimulationInfo"]["day"]
dhour = config["SimulationInfo"]["hour"]
dminute = config["SimulationInfo"]["minute"]
dsecond = config["SimulationInfo"]["second"]
dname = config["SimulationInfo"]["name"]
doffset = config["SimulationInfo"]["hours_after_UTC"]
dlat = config["SimulationInfo"]["lat"]
dlon = config["SimulationInfo"]["lon"]

#doffset = config["demoLocationInfo"]["hours_after_UTC"]
distAO1 = config["distInfo"]["distActuatorToOrigin"]
distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]

#Intializing time
demo_d = datetime.datetime(dyear, dmonth, dday, dhour, dminute, dsecond, tzinfo = datetime.timezone.utc)
print("Input time: ", demo_d.strftime('%H:%M:%S'))
demo_d += datetime.timedelta(hours = -doffset) #Converted inputted (PST) --> UTC standard (+7 hrs)
print("Utilized time(UTC): ", demo_d.strftime('%H:%M:%S'))

#Simulate the day
print("Demoing: ", dname, "...")
demoLoc = t.Location(dname, dlat, dlon, demo_d, distAO1, distAO2)
demoLoc.simulateDemoDay(dlat, dlon, doffset, "PST")
