#!/usr/bin/env python

from icarus.actuator_pwm import Run
from icarus.constants import Config
from os.path import expanduser
import json
import signal
import time
import site, os

from pkg_resources import resource_filename
print __name__
f = resource_filename("icarus", "config.json")

configFile = Config(f, "Hillsboro")

if not configFile:
	print("config file import failz0rs")
	quit()

go = Run(configFile.serverAddress, configFile.serverPort, configFile)
go.connectToServer()

#start reactor
signal.signal(signal.SIGINT, signal.SIG_DFL)
go.reactorLoop()
