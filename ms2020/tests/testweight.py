#!/usr/bin/env pybricks-micropython

import sys
import os
# from pybricks import ev3brick as brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                InfraredSensor, UltrasonicSensor, GyroSensor)
# from pybricks.parameters import Port, Stop, Direction, Button, Color
# from pybricks.tools import wait, StopWatch
# from pybricks.robotics import DriveBase
# from pybricks.ev3devices import Motor
 
sys.path.append('../shared')
sys.path.append('../samples')
# import robot_setup
 
# from robot_setup import left_motor
# from robot_setup import right_motor
# from robot_setup import robot
# from robot_setup import rack_motor
# from robot_setup import crane_motor
# from robot_setup import gyro
# from robot_setup import touch_sensor
# from robot_setup import color_sensor_back
# from robot_setup import color_sensor_right
# from robot_setup import color_sensor_center
# from robot_setup import touch_sensor
# from robot_setup import ultrasound
 
# from robot_setup import SOUND_VOLUME
# from robot_setup import WHEEL_DIAMETER_MM
# from robot_setup import AXLE_TRACK_MM
# from robot_setup import SENSOR_TO_AXLE
# from robot_setup import WHEEL_CIRCUM_MM
# from robot_setup import DEGREES_PER_MM
 
import shared_all

##### Do not change above this line ##########################################

import bus_service_1
import weight
INITIAL_ANGLE=-90

shared_all.calibrate_gyro(INITIAL_ANGLE)

weight.align(adjust_for_mission=0)
weight.run(adjust_for_mission=0)
bus_service_1.weight_to_phone(adjust_for_mission=0)


# import testphone
# phone.align(adjust_for_mission=0)
# phone.run()