from __future__ import print_function
import tracker_funcs as t
import json, datetime, copy
from constants import constants as x

#Local time
demoStartTime = datetime.datetime(x.sYear, x.sMonth, x.sDay, 4, 18, 34) #tzinfo = datetime.timezone.utc)
print ("Pre-process time (", x.sZone, ")", demoStartTime.strftime('%H:%M:%S'))

#UTC time
utcPreTime = demoStartTime + datetime.timedelta(hours = -x.sOffset) #Converted inputted (PST) --> UTC standard (+7 hrs)
print ("Pre-process time (UTC): ", utcPreTime.strftime('%H:%M:%S'))

#Initialize simulation
print ("Demoing: ", x.sName)
demoLoc = t.Location(x.sName, x.sLat, x.sLon, demoStartTime, x.distAO1, x.distAO2)

#sunRISE calculation
pre = demoStartTime
sunriseTime = demoLoc.calcSunriseTime(x.sLat, x.sLon, pre)
print ("Sunrise (UTC) time: ", sunriseTime)

#Sunset calculation
post = demoStartTime
sunsetTime = demoLoc.calcSunsetTime(x.sLat, x.sLon, post) + datetime.timedelta(hours = 19.5) #the latest sunset is ~11:42 PM
print("Sunset (UTC) time: ", sunsetTime)


demoLoc.simulateDemoDay(x.sLat, x.sLon, x.sOffset, x.sZone, sunsetTime)