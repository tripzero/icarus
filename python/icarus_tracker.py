#!/usr/bin/env python

from icarus.actuator_pwm import Run
from icarus.constants import Config
from os.path import expanduser
import json
import signal
import time
import site, os
import argparse
from pkg_resources import resource_filename

parser = argparse.ArgumentParser()
parser.add_argument('--configFile', dest="configFile", default="config.json", nargs=1, help="config file to use")
parser.add_argument('--location', dest="location", default="Hillsboro", nargs=1, help="location to use as defined in the config file")

args = parser.parse_args()

f = None

try:
	if args.configFile:
		with open(args.configFile, 'r') as tempFile:
			f = args.configFile
except:
	print("Warning: couldn't find user config: {0}.  Using default.".format(args.configFile))
	f = None
	pass

if not f:
	f = resource_filename("icarus", "config.json")
	print ("using config resource: " + str(f))

print ("using location: ", args.location[0])

configFile = Config(f, args.location[0])

if not configFile:
	print("config file import failz0rs")
	quit()

go = Run(configFile.serverAddress, configFile.serverPort, configFile)
go.connectToServer()

#start reactor
signal.signal(signal.SIGINT, signal.SIG_DFL)
go.reactorLoop()
