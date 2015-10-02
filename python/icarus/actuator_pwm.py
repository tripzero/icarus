#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
import datetime, sys
import solarserver as s
from constants import Config
import tracker_funcs
from twisted.internet import task, reactor
import pytz

class Run:
	"""The Run class connects client<-->server, sends tilt data, and moves the actuators."""
	def __init__(self, client_ip, client_port, config):

		self.client = s.WSClient(client_ip, client_port)
		self.client.debug = True
		self.config = config
		self.minActuatorHeight = 0 
		self.maxActuatorHeight = config.maxActuatorHeight
		self.speedUpFactor = config.speed
		if self.speedUpFactor < 1:
			self.speedUpFactor = 1
		tiltPercent = 0
		self.stop = False
		self.tz = pytz.timezone(self.config.tz)

		if config.simulationMode:
			self.demoT = datetime.datetime(config.year, config.month, config.day, 0, 0, 0, tzinfo=pytz.utc)
			print("Localized: Demo time: ", self.demoT)
		
		#recently added
		self.myLoc = tracker_funcs.Location(config.name, config.lat, config.lon,
			datetime.datetime.utcnow(), config.distAO1, config.distAO2)
		self.effectiveActuatorHeight1 = self.myLoc.calcTiltHeight(config.distAO1, self.myLoc.time)
		self.effectiveActuatorHeight2 = self.myLoc.calcPanHeight(config.distAO2, self.myLoc.time)

	def connectToServer(self):
		s.connectWS(self.client)

	def reactorLoop(self):
		if not self.config.simulationMode:	
			print("tilt Infinitely")			
			loop = task.LoopingCall(self.tiltRealTime)
		else:
			print("tilt DemoDay")			
			loop = task.LoopingCall(self.tiltDemoDay)

		#Initiate loop, cap the speed
		if self.speedUpFactor > 25:
			self.speedUpFactor = 25
		loop.start(1/self.speedUpFactor)

		reactor.run()
		
	"""Actuator a, tilting the panel up and down to maintain a 45 degree angle with the sun, is called every second by the reactor timer."""
	def tiltDemoDay(self):
		daysPast = ( (int(self.demoT.strftime('%d'))) - self.config.day)
		monthsPast = ( (int(self.demoT.strftime('%m'))) - self.config.month)
		yearsPast = ( (int(self.demoT.strftime('%Y'))) - self.config.year)

		print("startDay: ", self.config.month, "/", self.config.day, "/", self.config.year, "  ",  (self.demoT.strftime('Current Demo Day: %m/%d/%y')) )
		print(daysPast, " days ,", monthsPast, "months ,", yearsPast, "years ", "has elapsed", "at a speedup of x", self.speedUpFactor)

		#Add a minute
		self.demoT = self.demoT + datetime.timedelta(minutes = 1)

		#Initializing UTC time
		print(self.demoT)
		print()

		#Printing Local Time, Preparing time to send over Websocket
		time_to_update = str(self.demoT.astimezone(self.tz).strftime('%H:%M:%S ')) + str(self.config.tz) 
		print("\r\n", "|", "\n", "|", "\n", "V", "\n\r")

		height = self.myLoc.calcTiltHeight(self.config.distAO1, self.demoT)
		
		tiltPercent = height / self.maxActuatorHeight
		if tiltPercent < 0:
			tiltPercent = 0 #altitude < 0 then ignore
		if tiltPercent > 1: 
			tiltPercent = 1

		tiltPercent = 100 - (tiltPercent * 100)

		print("tiltPercent: ", tiltPercent)
		print("time: ", time_to_update)
		self.client.update(tiltPercent, time_to_update) #send tiltPercent to client


	"""Tilt actuator a up/down in REAL-TIME (speedup factor = 1) to maintain a 45 degree angle with the sun, every second."""
	def tiltRealTime(self):

		#Elapsed time prints
		daysPast = ( (int(self.demoT.strftime('%d'))) - self.config.day)
		monthsPast = ( (int(self.demoT.strftime('%m'))) - self.config.month)
		yearsPast = ( (int(self.demoT.strftime('%Y'))) - self.config.year)
		print(daysPast, " days ,", monthsPast, "months ,", yearsPast, "years", "has elapsed", "at a speedup of x", self.speedUpFactor)

		#Initializing UTC time
		d = datetime.datetime.utcnow()
		print(d.strftime('Date: %m/%d/%y'))
		print(d.strftime('%H:%M:%S UTC'))

		#Printing Local Time; prepping time to send to websocket via update func
		d = d + datetime.timedelta(hours = self.config.offset)
		time_to_update = str(d.strftime('%m/%d/%y | %H:%M:%S ')) + str(self.config.tz) 
		print((d.strftime('%H:%M:%S')), config.tz)
		print("\n", "|", "\n", "|", "\n", "V", "\n")

		#Calculate heights
		height = myLoc.calcTiltHeight(self.config.distAO1, datetime.datetime.utcnow())
		myLoc.printTiltHeight(self.config.distAO1, datetime.datetime.utcnow())
		tiltPercent = height / self.maxActuatorHeight
		print("tiltPercent: ", tiltPercent*100)
		self.client.update(tiltPercent*100, time_to_update)
	
	"""Actuator b is for panning the panel horizonally according to the azimuth. Currently NOT in the DollHouse."""
	def moveB():
		print(datetime.datetime.utcnow().strftime('%H:%M:%S PST'))
		print(" |", "\n", "V")
		myLoc.calcPanHeight(config.distAO2, datetime.datetime.utcnow())
		myLoc.printPanHeight(config.distAO2, datetime.datetime.utcnow())
		panPercent = effectiveActuatorHeight2 / maxActuatorHeight
		client.update(tiltPercent2*100, "TO-DO")


