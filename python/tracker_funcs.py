#!/usr/bin/env python
# import pysolar #docs.pysolar.org/en/latest/
import datetime, json
from pysolar.solar import * #TODO: potentially inefficent?
from pprint import pprint
from pysolar.time import get_delta_t, tt_offset, get_leap_seconds
from math import tan, cos, radians

t = datetime.datetime(2015, 6, 15, 23, 00, 00, tzinfo = datetime.timezone.utc)

original = datetime.datetime.now()
"""A location has time-specific altitude, azimuth values (degrees) as per Pysolar. Using origin to actuator distances, the various effective actuator heights can be calculated."""
class Location:
	"""Returns a new Location object"""
	def __init__(self, name, lat, lon, time, o_a_dist1, o_a_dist2):
		self.name = name
		self.lat = lat
		self.lon = lon
		self.time = time
		self.o_a_dist1 = o_a_dist1
		self.o_a_dist2 = o_a_dist2
		original = time

	def incrementTime(self, time):
		self.time += datetime.timedelta(minutes= get_delta_t(self.time) + tt_offset - get_leap_seconds(self.time))
		# print("get_delta_t(self.time): ", get_delta_t(self.time))
		# print( ", tt_offset: ", tt_offset)
		# print( " get_leap_seconds(self.time): ", get_leap_seconds(self.time))
		

		##time.tt_offset - time.get_leap_seconds(self.d))
		#t += datetime.timedelta(hours= time.get_delta_t(self.time) + timeOffset)
		#self.time = self.time.now()

	def resetTime(self, time):
		time = original

	def coords(self):
		return (self.lat, self.lon)

	def alt(self, lat, lon, time):
		a = get_altitude(lat, lon, time)
		# if a < 0:
		# 	raise ValueError("Cannot calculate. Sun is below the horizon.")
		return a

	def azimuth(self, lat, lon, time):
		a = get_azimuth(lat, lon, time)
		return a

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
	def calcTiltingHeight(self, o_a_dist1):
		val = 90 - self.alt(self.lat, self.lon, self.time)
		left = tan(radians(val))
		right = o_a_dist1
		x = left * right
		print("Calculated, effective actuator height: ", x, " inches")
		return x

	"""Return the value calculated via the law of consines, the # of inches the second actuator must be move in order to pan the solar panel according to the azimuth."""
	def calcPanningHeight(self, o_a_dist2):
		azimuth = self.azimuth(self.lat, self.lon, self.time)
		# if azimuth < 0:
		# 	azimuth = 360 + azimuth
		val = 2*o_a_dist2*o_a_dist2 - (2*o_a_dist2*o_a_dist2*cos((radians(azimuth))))
		x = math.sqrt(val)
		print("value to sqrt: ", val)
		print("Effective panning height(x): ", x)
		print("azimuth: ", azimuth, " ", radians(azimuth))
		return x	

	def demoDay(self, lat, lon, dateTimeObj):
		print()
		try:
			# print("Demo of ", self.name, " ", dateTimeObj)
			# date = datetime.datetime(2015,5,15,6,55,0)
			# print("lat, lon: ", lat, " ", lon)
			# for h in range(0, 12):
			# 	date += datetime.timedelta(hours=+1)
			print("Demo of ", self.name, " ", dateTimeObj)
			print("lat, lon: ", lat, " ", lon, "\n")

			for h in range(0, 12):
				self.incrementTime(t)
				print(self.time)
				print_alt(self)
				print_actuator1(self)
				print()

			self.resetTime(original)
		except ValueError:
			self.resetTime(original)
			pass

"""Print all relevant location data"""
def printLocationInfo(loc):
	print("location object name: ", loc.name)
	print_coords(loc)
	print_alt(loc)
	print_azimuth(loc)

def print_coords(loc):
	print("Coordinates of " + str(loc.name) + ": (", loc.lat, ",", loc.lon, ")")
def print_alt(loc):
	print(str(loc.name) + " alt: ", loc.alt(loc.lat, loc.lon, loc.time))
def print_azimuth(loc):
	print(str(loc.name) + " azimuth: ", loc.azimuth(loc.lat, loc.lon, loc.time))
def print_actuator1(loc):
	print(str(loc.name) + " actuator height: ", loc.calcTiltingHeight(loc.o_a_dist1))


# """Calculate the most effective height of the first tilting actuator based upon the assumption solar panels are most efficent angled 45 degrees to the sun. Dist(a, o) is represented by base. Math: tan(S1) = a / distActuatorToOrigin & S1 = 90 - altitude ==> a = tan(90-altitude) * distActuatorToOrigin"""
# def calcTiltingHeight(loc, o_a_dist1):
# 	val = 90 - loc.alt(loc.lat, loc.lon)
# 	left = tan(radians(val))
# 	right = o_a_dist1
# 	a = left * right
# 	print("Calculated, effective actuator height: ", a, " inches")
# 	return a

#######################################################################################################################
#New stuff 

# """Return the value calculated via the law of consines, the # of inches the second actuator must be move in order to pan the solar panel according to the azimuth."""
# def calcPanningHeight(loc, o_a_dist2):
# 	azimuth = loc.azimuth(loc.lat, loc.lon)
# 	# if azimuth < 0:
# 	# 	azimuth = 360 + azimuth
# 	val = 2*o_a_dist2*o_a_dist2 - (2*o_a_dist2*o_a_dist2*cos((radians(azimuth))))
# 	x = math.sqrt(val)
# 	print("value to sqrt: ", val)
# 	print("Effective panning height(x): ", x)
# 	print("azimuth: ", azimuth, " ", radians(azimuth))
# 	return x