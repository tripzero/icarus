# **Maximum power point tracking (MPPT)**
*Intel OSTC SmartHouse Solar Panel Demo*

Download Pysolar as a dependency. 
> $ sudo pip3 install pysolar

1. Input location coordinates into the config.json. Input the distance from the pivot point of the panel to the actuator--actuator1 is for tilting up/down and actuator2 is for panning.
*Note: hour_after_UTC is -7 for PST because Coordinated Universal Time is 7 hours ahead of Pacific Time. Be sure to verify timezone inputs.*

2. To see an overview of altitude/azimuth statistics of the input location as compared to that of Intel's Hillsboro, OR campus, run:

> $ python3 tracking.py

3. To view a simulation of actuator heights throughout the day, input relevant demoInfo within the config.json and run:

> $ python3 demo.py

4. To move the actuators to the optimal heights according to the current local time,specify "moveActuatorPerUnitOfSeconds" to specify how often the solar panels should move, as well as the distance from each actuator to the origin (pivot point) and then run:

> $ python3 actuator_pwm.py
