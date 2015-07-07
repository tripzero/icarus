from __future__ import print_function
import tracker_funcs as t
import json, datetime, copy
import Pysolar.constants as c
from constants import constants as x

demoTime = datetime.datetime(x.sYear, x.sMonth, x.sDay, 4, 18, 34) #tzinfo = datetime.timezone.utc)
print ("Input time (", x.sZone, ")", demoTime.strftime('%H:%M:%S'))
demoTime += datetime.timedelta(hours = -x.sOffset) #Converted inputted (PST) --> UTC standard (+7 hrs)
print ("Input time (UTC): ", demoTime.strftime('%H:%M:%S'))

#Simulate the day
print ("Demoing: ", x.sName)
demoLoc = t.Location(x.sName, x.sLat, x.sLon, demoTime, x.distAO1, x.distAO2)

#Sunrise calculation
sunset_endtime = demoLoc.calcSunsetTime(x.sLat, x.sLon)
print("sunset_time: ", sunset_endtime)
print ("Sunrise (UTC) time is: ", demoLoc.calcSunriseTime(x.sLat, x.sLon, demoTime))

demoLoc.simulateDemoDay(x.sLat, x.sLon, x.sOffset, x.sZone, sunset_endtime)
