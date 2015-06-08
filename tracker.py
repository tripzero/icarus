#!/usr/bin/env python
# import pysolar #docs.pysolar.org/en/latest/
import datetime, json
from pysolar.solar import *
from pprint import pprint
from math import tan, radians

#Set-Up Inputs
with open('config.json') as dataFile:
	config = json.load(dataFile)
print("config.json: ")
pprint(config)
print("\n")

curr_time = datetime.datetime.now()
print("Local time: ", curr_time)

def print_coords(loc):
	print("Coordinates of " + str(loc.name) + ": (", loc.lat, ",", loc.lon, ")")
def print_alt(loc):
	print(str(loc.name) + " alt: ", loc.alt(loc.lat, loc.lon))
def print_azimuth(loc):
	print(str(loc.name) + " azimuth: ", loc.azimuth(loc.lat, loc.lon))

"""A location has time-specific altitude, azimuth values (degrees) as per Pysolar"""
class Location:
	"""Returns a new Location object"""
	def __init__(self, name, lat, lon):
		self.name = name
		self.lat = lat
		self.lon = lon

	def coords(self):
		return (self.lat, self.lon)

	def alt(self, lat, lon):
		a = get_altitude(lat, lon, curr_time)
		return a

	def azimuth(self, lat, lon):
		a = get_azimuth(lat, lon, curr_time)
		return a

# a = Actuator height
# o = origin
# H = distance from actuator to the pivot socket = distActuatorToPivot
#         /|  |
#        / |  |
#       /  |  |
#      /   |  | 
#    H/    |  a
#    /     |  | 
#   /      |  |
#  /       |  |
# /S1______|  |
#O<-pivot bolt
# ---------<-distActuatorToOrigin

"""Calculate the most effective height of the actuator based upon the assumption solar panels are most efficent angled 45 degrees to the sun. Dist(a, o) is represented by base. Math: tan(S1) = a / distActuatorToOrigin & S1 = 90 - altitude ==> a = tan(90-altitude) * distActuatorToOrigin"""
def calcActuatorHeight(loc, actuatorOriginDist):
	val = 90 - loc.alt(loc.lat, loc.lon)
	print("val: ", val)

	left = tan(radians(val))
	print("left: ", left)
	right = actuatorOriginDist
	a = left * right
	print("Calculated height of actuator, a, is: ", a, " inches")
	return a


"""Print all relevant location Data"""
def printLocationInfo(loc):
	print("location object name: ", loc.name)
	#print(loc.coords())
	print_coords(loc)
	print_alt(loc)
	print_azimuth(loc)


#Example: JF1
jf1 = Location("JF1", 45.541718, -122.960381)
print("Example")
printLocationInfo(jf1)
calcActuatorHeight(jf1, 2.8)
print()

#From config.json
print("Current location via config.json:")
myLoc = Location("inputLocation" , config["locationInfo"]["latitude"], config["locationInfo"]["longitude"])
distActuatorToOrigin = config["distInfo"]["distActuatorToOrigin"]
printLocationInfo(myLoc)
calcActuatorHeight(myLoc, distActuatorToOrigin)


#Additional functions that would be cool:
#write a function that gives # of hours of sunlight based upon coords/month/day


