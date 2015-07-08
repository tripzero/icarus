import json
import datetime
from pprint import pprint
import tracker_funcs as t
from constants import constants as x

d = datetime.datetime.utcnow()
def printTime():
	print "Local timezone (", x.tz, "):", (d + datetime.timedelta(hours = x.offset)).strftime('%H:%M:%S'), "/ ", d.strftime('%H:%M:%S UTC')

#JF1 example location
def calcExample():
	print
	jf1 = t.Location("JF1", 45.541718, -122.960381, d, x.distAO1, x.distAO2)
	t.printLocationInfo(jf1)
	jf1.calcTiltHeight(x.distAO1, jf1.time)
	jf1.calcPanHeight(x.distAO1, jf1.time)
	jf1.printTiltHeight(x.distAO1, jf1.time)
	jf1.printPanHeight(x.distAO2, jf1.time)
	print

myLoc = t.Location(x.name, x.lat, x.lon, d, x.distAO1, x.distAO2)
effectiveActuatorHeight1 = myLoc.calcTiltHeight(x.distAO1, myLoc.time)
effectiveActuatorHeight2 = myLoc.calcPanHeight(x.distAO2, myLoc.time)

def printDemoHeights():
	t.printLocationInfo(myLoc)
	myLoc.printTiltHeight(x.distAO1, myLoc.time)
	myLoc.printPanHeight(x.distAO2, myLoc.time)
