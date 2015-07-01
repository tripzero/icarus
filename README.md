# **Maximum power point tracking (MPPT)**
*Intel OSTC DollHouse Solar Panel Demo*

The goal of this project is to intergrate Pysolar API with python code w/ mraa-bindings to move actuators thereby allowing for maximum solar panel efficency according to the sun's position.

<iframe src="https://3dwarehouse.sketchup.com/embed.html?mid=ue44d2411-e37e-4c25-9bee-8ae0a81f8ab5&width=400&height=300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" width="400" height="300" allowfullscreen></iframe>

![logo](https://3dwarehouse.sketchup.com/warehouse/getpubliccontent?contentId=60b12dc9-d177-47dd-9213-45144566ce93 "Doll House")

[DollHouse replica](https://3dwarehouse.sketchup.com/model.html?id=ue44d2411-e37e-4c25-9bee-8ae0a81f8ab5 "Notice the angled roof's is suboptimal during midday, temporarily resulting in negative actuator heights!")

Download Pysolar as a dependency. 
> $ sudo pip3 install pysolar

Input location coordinates into the config.json. Input the distance from the pivot point of the panel to the actuator--actuator1 is for tilting up/down and actuator2 is for panning.
*Note: hour_after_UTC is -7 for PST because Coordinated Universal Time is 7 hours ahead of Pacific Time. Be sure to verify timezone inputs.*


To see an overview of altitude/azimuth statistics of the input location as compared to that of Intel's Hillsboro, OR campus, run:
> $ python3 tracking.py


To simulate actuator heights throughout the day, input relevant demoSimulationInfo in the config.json and run:
> $ python3 demo.py


To move the actuators to the optimal heights according to the current local time,specify "moveActuatorPerUnitOfSeconds" to specify how often the solar panels should move, as well as the distance from each actuator to the origin (pivot point) and  run:
> $ python3 actuator_pwm.py

*mraa documentation: http://iotdk.intel.com/docs/master/mraa/python/*
