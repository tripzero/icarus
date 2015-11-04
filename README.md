# **Icarus**
*Solar panel solar tracking controller*

##Description
Icarus is solar panel controller software that can be used with a hardware controller (such as the Intel Edison or any device with PWM) and a linear actuator to move a solar panel so that it tracks the sun.  It is estimated that a solar panel can get 40-55% better output throughout the day if it positions itself towards the sun at optimal angles.  At the moment, the controller supports one axis giving an estimated 15% efficiency.  There is code to do two axis, but this is untested.  Icarus uses pysolar for acurate computation of solar azimuth and altitude throughout the day.

##Installation
Download Pysolar 0.6 as a dependency. ``` $ sudo python setup.py install ```

Clone mraa and follow the install/build instructions; cmake-gui is useful during the build process to enable -DBUILDSWIGPYTHON, -BUILDSWIG. Next, confirm mraa.py and _mraa.so are in dist-packages.

```$ git clone https://github.com/intel-iot-devkit/mraa.git```


```$ mv /usr/local/lib/python2.7/site-packages/ /usr/local/lib/python2.7/dist-packages```

*(To confirm the mraa build process is complete, open a python shell. 'import mraa' should result in "mraa: FATAL error, failed to initialise platform")*

Input location coordinates into the config.json. Input the distance from the pivot point of the panel to the actuator--actuator1 is for tilting up/down and actuator2 is for panning.
*Note: hour_after_UTC is -7 for PST because Coordinated Universal Time is 7 hours ahead of Pacific Time. Verify timezone inputs carefully.*

##Usage
To see an overview of altitude/azimuth statistics of the input location as compared to that of Intel's Hillsboro, OR campus, run: ```$ python tracking.py```


To simulate actuator heights throughout the day, input relevant SimulationInfo in the config.json and run:
```$ python simulate_heights.py```


To demo the actuators infinitely, the "demoLocationInfo" must be accurate (don't worry about the timezone--it's based upon the datetime of the user's machine) in the config.json. Secondly, the config.json needs "distInfo" including "moveActuatorPerUnitOfSeconds" to specify how often the panels should move, as well as the two respective variables for the distance from actuator to origin (pivot point). Run: 
``` $ python run_actuators.py```


In order to run the nodejs-server, download ws, a node.js websocket library. ```npm install -g ws```
*source: https://github.com/websockets/ws*


*mraa documentation: http://iotdk.intel.com/docs/master/mraa/python/*

