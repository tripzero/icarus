# **Maximum power point tracking (MPPT)**
*Intel OSTC SmartHouse Solar Panel Demo*

Please download Pysolar as a dependency via $ sudo pip3 install pysolar

1. Input location coordinates into the config.json. Feel free to change the input demo start time. Input the distance from the pivot point of the panel to the actuator--actuator1 is for tilting up/down and actuator2 is for panning.

To see an overview of altitude/azimuth statistics of the input location as compared to that of the Intel Hillsboro campus, run:

> $ python3 tracking.py


To view a simulation of actuator heights throughout the day, run:

> $ python3 demo.py


To move the actuators to the optimal heights according to the current local time, make sure to specify "moveActuatorPerUnitOfSeconds" to specify how often the solar panels should move, and then run:

> $ python3 actuator_pwm.py
