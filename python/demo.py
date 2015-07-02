import tracker_funcs as t
import json, datetime, copy
import pysolar.constants as c
#from pysolar.simulate import simulate_span

with open('config.json') as dataFile:
	config = json.load(dataFile)

#Intializing demo start time, actuator positioning relative to origin
dyear = config["demoSimulationInfo"]["year"]
dmonth = config["demoSimulationInfo"]["month"]
dday = config["demoSimulationInfo"]["day"]
dhour = config["demoSimulationInfo"]["hour"]
dminute = config["demoSimulationInfo"]["minute"]
dsecond = config["demoSimulationInfo"]["second"]
dname = config["demoSimulationInfo"]["name"]
doffset = config["demoSimulationInfo"]["hours_after_UTC"]
dlat = config["demoSimulationInfo"]["lat"]
dlon = config["demoSimulationInfo"]["lon"]

#doffset = config["locationInfo"]["hours_after_UTC"]
distAO1 = config["distInfo"]["distActuatorToOrigin"]
distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]

#Intializing time
demo_d = datetime.datetime(dyear, dmonth, dday, dhour, dminute, dsecond, tzinfo = datetime.timezone.utc)
print("Input time: ", demo_d.strftime('%H:%M:%S'))
demo_d += datetime.timedelta(hours = -doffset) #Converted inputted (PST) --> UTC standard (+7 hrs)
print("Utilized time(UTC): ", demo_d.strftime('%H:%M:%S'))

#Demo the day
print("Demoing: ", dname, "...")
demoLoc = t.Location(dname, dlat, dlon, demo_d, distAO1, distAO2)
demoLoc.simulateDemoDay(dlat, dlon, doffset, "PST")
