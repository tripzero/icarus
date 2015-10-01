import json

class Config:

	"""The Config class is a template for intializing/importing constants."""
	def __init__(self, file_str, location):
		
		with open(file_str) as dataFile: # print("config.json: ") # pprint(config)
			config = json.load(dataFile)
	
		self.serverAddress = config["server"]["address"]
		self.serverPort = config["server"]["port"]
		self.simulationMode = config["simulationMode"]
		self.file_str = file_str
		self.distAO1 = config["distInfo"]["distActuatorToOrigin"]
		self.distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]
		self.secToWait = config["distInfo"]["moveActuatorPerUnitOfSeconds"]
		self.maxActuatorHeight = config["distInfo"]["maxActuatorHeight"]
		
		self.name = config[location]["name"]
		self.lat = config[location]["latitude"]
		self.lon = config[location]["longitude"]
		self.rate = config[location]["speedUpRate"]

		self.offset = config[location]["hours_after_UTC"]
		self.tz = config[location]["tz_name"]
		self.speed = config[location]["speedUpRate"]
		self.year = config[location]["year"]
		self.month = config[location]["month"]
		self.day = config[location]["day"]