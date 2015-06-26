from threading import Thread
import sys
from twisted.internet import gireactor #default reactor uses a min size of 5, max size of 10.
try: 
	gireactor.install()
except:
	print("Gireactor already installed")

from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS, WebSocketClientProtocol, WebSocketClientFactory, connectWS

from twisted.internet import reactor
from twisted.python import log

from pwm_funcs import Actuator
import struct #TODO: why?
import json

#class for testing
class SolarServer():
	
	def __init__(self):
		#super().__init__(self, pin, percent, period, isPWM)
		log.startLogging(sys.stdout)

		#Running the server
		factory = WebSocketServerFactory("ws://localhost:6000")
		factory.protocol = MyServerProtocol
		
		listenWS(factory) #Listen for incoming WebSocket connections from clients.

		def run(self):
			reactor.run()


class WSClient(WebSocketClientFactory):

	server, connected = None, None

	def __init__(self, address, port):
		WebSocketClientFactory.__init__(self, "ws://{0}:{1}".format(address, port), debug=True, origin='null')

		self.protocol = WSClientProtocol
		connectWS(self)

	def register(self, server):
		self.server = server
		if self.connected:
			self.connected()

	def send(self, msg):
		msg = bytes(msg) #tiltdata
		if self.server:
			print("sending:", msg)
			self.server.sendMessage(msg, True)

	def update(self, tiltInfo): #TODO
		if not self.server:
			return
			j = {"tiltPercentage" : tiltInfo}
			self.send(json.dumps(j)) #json dump ; float error

	def unregister(self):
		self.server = None


class WSClientProtocol(WebSocketClientProtocol):
	debug, debugCodePaths = False, False

	def onConnect(self, response):
		print("Server connected: {0}".format(response.peer))

	def onOpen(self):
		print("WebSocket connection open.")
		self.factory.register(self)

	def onMessage(self, payload, isBinary):
		if isBinary:
			print("Binary message received: {0} bytes".format(len(payload)))
		else: #payload is text; convert UTF8 --> Python
			print("Text message received: {0}".format(payload.decode('utf8')))

	def onClose(self, wasClean, code, reason):
		print("WebSocket connection closed: {0}".format(reason))
		self.factory.unregister()

class MyServerProtocol(WebSocketServerProtocol):
	lightServer = None
	debug, debugCodePaths = True, True

	def onOpen(self):
		print("Ready to connect")

	def onConnect(self, request): 
		print("Client connecting: {}".format(request.peer))

	def onMessage(self, payload, isBinary): #TODO: how to write this func
		#self.sendMessage(payload, isBinary) #echo back a message
		
		print("got a message: ", len(payload))
		if not isBinary:
			return

		# payload = np.frombuffer(payload, np.uint8)

		# cmd = payload[0]  #TODO: what is cmd

		# print("cmd=", cmd)

		# if cmd == 0x01:
		# 	self.setLights(payload)
		# elif cmd == 0x02:
		# 	self.setNumLights(payload)
		# elif cmd == 0x03:
		# 	self.clear()


	#TODO: setHeight function? copying logic from actuator ?

	def clear(self):
		print('clearing')
		MyServerProtocol.lightServer.clear()

	def connectionLost(self, reason):
		WebSocketServerProtocol.connectionLost(self, reason)
