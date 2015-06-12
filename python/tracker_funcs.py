#!/usr/bin/env python
# import pysolar #docs.pysolar.org/en/latest/
import datetime, json
from pysolar.solar import * #TODO: potentially inefficent?
from pprint import pprint
from math import tan, cos, radians

curr_time = datetime.datetime.now()

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
		if a < 0:
			raise ValueError("Cannot calculate. Sun is below the horizon.")
		return a

	def azimuth(self, lat, lon):
		a = get_azimuth(lat, lon, curr_time)
		return a


"""Print all relevant location data"""
def printLocationInfo(loc):
	print("location object name: ", loc.name)
	print_coords(loc)
	print_alt(loc)
	print_azimuth(loc)

def print_coords(loc):
	print("Coordinates of " + str(loc.name) + ": (", loc.lat, ",", loc.lon, ")")
def print_alt(loc):
	print(str(loc.name) + " alt: ", loc.alt(loc.lat, loc.lon))
def print_azimuth(loc):
	print(str(loc.name) + " azimuth: ", loc.azimuth(loc.lat, loc.lon))

# a = Actuator height #Note-first, panning actuator calculations
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

"""Calculate the most effective height of the first tilting actuator based upon the assumption solar panels are most efficent angled 45 degrees to the sun. Dist(a, o) is represented by base. Math: tan(S1) = a / distActuatorToOrigin & S1 = 90 - altitude ==> a = tan(90-altitude) * distActuatorToOrigin"""
def calcTiltingHeight(loc, actuatorOriginDist):
	val = 90 - loc.alt(loc.lat, loc.lon)
	left = tan(radians(val))
	right = actuatorOriginDist
	a = left * right
	print("Calculated, effective actuator height: ", a, " inches")
	return a

#######################################################################################################################
#New stuff 

"""Return the value calculated via the law of consines, the # of inches the second actuator must be move in order to pan the solar panel according to the azimuth."""
def calcPanningHeight(loc, distPanningToOrigin):
	azimuth = loc.azimuth(loc.lat, loc.lon)
	azimuth = -azimuth
	# if azimuth < 0:
	# 	azimuth = 360 + azimuth
	val = 2*distPanningToOrigin*distPanningToOrigin - (2*distPanningToOrigin*distPanningToOrigin*cos((radians(azimuth))))
	x = math.sqrt(val)
	print("value to sqrt: ", val)
	print("Effective panning height(x): ", x)
	print("azimuth: ", azimuth, " ", radians(azimuth))
	return x

