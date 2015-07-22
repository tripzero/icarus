import json

class Config:

	"""The Config class is a template for intializing/importing constants."""
	def __init__(self, file_str):
		
		with open(file_str) as dataFile:
			config = json.load(dataFile)
	
		self.file_str = file_str
		self.distAO1 = config["distInfo"]["distActuatorToOrigin"]
		self.distAO2 = config["distInfo"]["distPanningActuatorToOrigin"]
		self.secToWait = config["distInfo"]["moveActuatorPerUnitOfSeconds"]
		self.maxActuatorHeight = config["distInfo"]["maxActuatorHeight"]
		
		self.name = config["demoLocationInfo"]["name"]
		self.lat = config["demoLocationInfo"]["latitude"]
		self.lon = config["demoLocationInfo"]["longitude"]
		self.rate = config["demoLocationInfo"]["speedUpRate"]

		self.offset = config["demoLocationInfo"]["hours_after_UTC"]
		self.tz = config["demoLocationInfo"]["tz_name"]
		self.speed = config["demoLocationInfo"]["speedUpRate"]
		self.year = config["demoLocationInfo"]["year"]
		self.month = config["demoLocationInfo"]["month"]
		self.day = config["demoLocationInfo"]["day"]

		#used in simulate_heights.py
		self.sYear = config["SimulationInfo"]["year"]
		self.sMonth = config["SimulationInfo"]["month"]
		self.sDay = config["SimulationInfo"]["day"]
		# dhour = config["SimulationInfo"]["hour"]
		# dminute = config["SimulationInfo"]["minute"]
		# dsecond = config["SimulationInfo"]["second"]
		self.sName = config["SimulationInfo"]["name"]
		self.sOffset = config["SimulationInfo"]["hours_after_UTC"]
		self.sLat = config["SimulationInfo"]["lat"]
		self.sLon = config["SimulationInfo"]["lon"]
		self.sZone = config["SimulationInfo"]["tz_name"]

# constants = Config('../config_module/config.json')
# constants = Config('../config.json')