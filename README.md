# **Icarus**
*Solar panel solar tracking controller*

##Description
Icarus is solar panel controller software that can be used with a hardware
controller (such as the Intel Edison or any device with PWM) and a linear
actuator to move a solar panel so that it tracks the sun. It does this by
relying on geolocation and timezone information using the Pysolar library,
which will allow it to "know" when the sun rises and when it sets. It is
estimated that a solar panel can get 40-55% better output throughout theday if
it positions itself towards the sun atoptimal angles. At the moment, the
controller supports one axis giving an estimated 15% efficiency increase. 

##Installation

### Python dependencies
Icarus is written in Python and depends on libraries listed below.
Python dependencies can be installed using `pip install <python_module>`
(you need a live network connection).
* [Autobahn](http://autobahn.ws/python/): version 0.10.9
* [Icarus](https://github.com/tripzero/icarus)
* [Pysolar](http://pysolar.org/): version 0.6
* [Pytz](http://pytz.sourceforge.net/): version 2015.7
* [setuptools](https://pypi.python.org/pypi/setuptools): version 18.2
* [Six](https://pypi.python.org/pypi/six): version 1.10.0
* [Twisted](https://twistedmatrix.com/): version 15.4.0
* [txaio](https://pypi.python.org/pypi/txaio): version 2.0.4
* [zope.interface](https://pypi.python.org/pypi/zope.interface): version 4.1.3


To install Icarus tracker please run the command:
 ``` $ sudo python python/setup.py install ```
 
### Native library dependencies
* [MRAA](http://iotdk.intel.com/docs/master/mraa/) version 0.10.1

To install MRAA please follow the install/build instructions available here:
http://iotdk.intel.com/docs/master/mraa/building.html

```$ git clone https://github.com/intel-iot-devkit/mraa.git```
```$ mv /usr/local/lib/python2.7/site-packages/ /usr/local/lib/python2.7/dist-packages```

*(To confirm the mraa build process is complete, open a python shell. 'import
mraa' should result in "mraa: FATAL error, failed to initialise platform")*

##Configure Icarus tracker location settings
While Icarus comes with a preconfigured set of locations, you may want to input
your own location and timezone information. This is done using a
```config.json``` file, which is located at Icarus is configured using a config.json file. 
Input location coordinates into the config.json. Input the distance from the
pivot point of the panel to the actuator--actuator1 is for tilting up/down and
actuator2 is for panning.
*Note: hour_after_UTC is -7 for PST because Coordinated Universal Time is 7
hours ahead of Pacific Time. Verify timezone inputs carefully.*

##Usage
To see an overview of altitude/azimuth statistics of the input location as
compared to that of Intel's Hillsboro, OR campus, run: ```$ python tracking.py```


To simulate actuator heights throughout the day, input relevant SimulationInfo in the config.json and run:
```$ python simulate_heights.py```

To demo the actuators infinitely, the "demoLocationInfo" must be accurate
(don't worry about the timezone--it's based upon the datetime of the user's
machine) in the config.json. Secondly, the config.json needs "distInfo"
including "moveActuatorPerUnitOfSeconds" to specify how often the panels should
move, as well as the two respective variables for the distance from actuator to
origin (pivot point). Run: 
``` $ python run_actuators.py```


In order to run the nodejs-server, download ws, a node.js websocket library. ```npm install -g ws```
*source: https://github.com/websockets/ws*
