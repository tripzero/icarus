from __future__ import print_function
import tracker_funcs as t
import json, datetime, copy
import Pysolar.constants as c
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
demoTime = datetime.datetime(dyear, dmonth, dday, dhour, dminute, dsecond) #tzinfo = datetime.timezone.utc)
print ("Input time: ", demoTime.strftime('%H:%M:%S'))
demoTime += datetime.timedelta(hours = -doffset) #Converted inputted (PST) --> UTC standard (+7 hrs)
print ("Input time (UTC): ", demoTime.strftime('%H:%M:%S'))


#Simulate the day
print ("Demoing: ", dname)
demoLoc = t.Location(dname, dlat, dlon, demoTime, distAO1, distAO2)

#Sunrise calculation
print ("Sunrise (UTC) time is: ", demoLoc.calcSunriseTime(dlat, dlon, demoTime))

demoLoc.simulateDemoDay(dlat, dlon, doffset, "PST")
