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

configFile = Config(f)

if not configFile:
	print("config file import failz0rs")
	quit()

# except IOError:	
	# try:
	# 	configFile = Config(str(lst[0]))

	# except IOError:
	# 	try:
	# 		configFile = Config(str(home) + "/.config/icarus/config.json")
		
	# 	except IOError:
	# 			configFile = Config("/etc/icarus/config.json")

#instantiate websocketclient
go = Run("127.0.0.1", "8080", configFile)
print("client obj:", go.client)

#connect wsclient <--> autobahn myserver
go.connectToServer()

#start reactor
signal.signal(signal.SIGINT, signal.SIG_DFL)
go.reactorLoop(configFile.speed)
