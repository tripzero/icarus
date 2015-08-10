#!/usr/bin/env python

from icarus.actuator_pwm import Run
from icarus.solarserver import MyServer
from icarus.constants import Config
from os.path import expanduser
import json
import signal
import time

#import config.json
try:
	configFile = Config("config.json")

except IOError:
	try:
		home = expanduser("~")
		configFile = Config(str(home) + "/.config/icarus/config.json")
	
	except IOError:
			configFile = Config("/etc/icarus/config.json")

#instantiate websocketclient
go = Run("127.0.0.1", "8080", configFile)
print("client obj:", go.client)

#instantiate testserver + factory/listening
#server = MyServer()

#connect wsclient <--> autobahn myserver
go.connectToServer()

#start reactor
signal.signal(signal.SIGINT, signal.SIG_DFL)
go.reactorLoop(configFile.speed)
