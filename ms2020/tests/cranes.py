#!/usr/bin/env pybricks-micropython

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
sys.path.append('../samples')
import robot_setup
 
from robot_setup import left_motor
from robot_setup import right_motor
from robot_setup import robot
from robot_setup import rack_motor
from robot_setup import crane_motor
from robot_setup import gyro
from robot_setup import touch_sensor
from robot_setup import color_sensor_back
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
from robot_setup import WHITE_MIN_INTENSITY
from robot_setup import BLACK_MAX_INTENSITY
 
import shared_all

##### Do not change above this line ##########################################



shared_all.move_crane_to_floor(crane_motor)
shared_all.move_crane_up(crane_motor, 90)
shared_all.move_crane_to_top(crane_motor)

shared_all.move_rack_to_top()

shared_all.move_rack_to_floor()
shared_all.move_crane_up(rack_motor, 90)
shared_all.move_crane_down(rack_motor, 90)
shared_all.move_rack_to_top()
shared_all.log_string('crane motor ' +str(crane_motor))
shared_all.log_string('rack motor ' +str(rack_motor))
shared_all.log_string('left motor ' +str(left_motor))
shared_all.log_string('right motor ' +str(right_motor))


