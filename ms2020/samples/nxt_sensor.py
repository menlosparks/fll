#!/usr/bin/env pybricks-micropython
# import ev3dev.ev3 as ev3
# import sys
# import os
# import pybricks.nxtdevices as nxt
# # from pybricks.nxtdevices import UltrasonicSensor
# import pybricks.ev3devices as ev3dev
# from pybricks.tools import wait, StopWatch
# from pybricks import ev3brick as brick
# from pybricks.ev3devices import UltrasonicSensor,TouchSensor
# from pybricks.parameters import Port, Stop, Direction, Button, Color
# sys.path.append('../shared')
 
# import robot_setup

# # us = ev3.UltrasonicSensor()
# # us = nxt.UltrasonicSensor(Port.S2)






import sys
import os
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
 
sys.path.append('../shared')
import robot_setup
 
from robot_setup import left_motor
from robot_setup import right_motor
from robot_setup import robot
from robot_setup import rack_motor
from robot_setup import crane_motor
from robot_setup import gyro
from robot_setup import touch_sensor
from robot_setup import color_sensor_left
from robot_setup import color_sensor_right
from robot_setup import color_sensor_center
from robot_setup import touch_sensor
from robot_setup import ultrasound
 
from robot_setup import SOUND_VOLUME
from robot_setup import WHEEL_DIAMETER_MM
from robot_setup import AXLE_TRACK_MM
from robot_setup import SENSOR_TO_AXLE
from robot_setup import WHEEL_CIRCUM_MM
from robot_setup import DEGREES_PER_MM
 
##### Do not change above this line ##########################################







color_sensor_center = None##ColorSensor(Port.S4)
touch_sensor= None## TouchSensor(Port.S2)
message='Staring ultrasomic'
brick.sound.beep(1100, 80, 7)
print(message)
brick.display.text(message)

def test_sensor():
    # while touch_sensor.pressed() == False :
    while ultrasound.distance() > 10:
        message='Distance ' + str(ultrasound.distance())
        print(message)
        brick.display.text(message)
        wait(1000)

# us = ev3dev.UltrasonicSensor(Port.S1)
test_sensor()
