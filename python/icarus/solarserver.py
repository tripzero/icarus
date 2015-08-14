from threading import Thread
import sys

from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS, WebSocketClientProtocol, WebSocketClientFactory, connectWS
from twisted.internet import reactor
from twisted.python import log
import struct
import json

class MyServer():
	
	def __init__(self):
		log.startLogging(sys.stdout)

		#Running the server
		factory = WebSocketServerFactory("ws://localhost:8080")
		factory.protocol = MyServerProtocol
		
		listenWS(factory) #Listen for incoming WebSocket connections from clients.
		log.startLogging(sys.stdout)

	def run(self):
		reactor.run()

	def unregister(self):
		self.server = None

class WSClient(WebSocketClientFactory):

	serverConnection, connected = None, None

	def __init__(self, address, port):
		WebSocketClientFactory.__init__(self, "ws://{0}:{1}".format(address, port), debug=False, origin='null')

		self.protocol = WSClientProtocol

	def register(self, serverConnection):
		self.serverConnection = serverConnection
		if self.connected:
			self.connected()

	def send(self, msg): #msg = tilt data
		msg = bytes(msg)
		if self.serverConnection:
			print("sending:", msg)
			self.serverConnection.sendMessage(msg, True)

	def update(self, tiltInfo, datetime): 
		if not self.serverConnection:
			return
		j = {"tiltPercentage" : tiltInfo}
		k = {"datetime" : datetime}
		self.send(json.dumps(j))
		self.send(json.dumps(k))

	def unregister(self):
		self.serverConnection = None

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
	debug, debugCodePaths = True, True

	def onOpen(self):
		print("Ready to connect")

	def onConnect(self, request): 
		print("Client connecting: {}".format(request.peer))

	def onMessage(self, payload, isBinary):
		print "got a message: ", len(payload)
		if not isBinary:
			return

	def clear(self):
		print('clearing')
		MyServerProtocol.lightServer.clear()

	def connectionLost(self, reason):
		WebSocketServerProtocol.connectionLost(self, reason)
