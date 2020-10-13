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
 
import shared_all

##### Do not change above this line ##########################################


import bus_service_1
import bus_service_2
import stepcounter
import treadmill
import row
import flip
import weight
import slide
import bench
import basket
import phone

shared_all.calibrate_gyro(180)


bus_service_1.base_to_stepcounter()
stepcounter.run()

bus_service_1.stepcounter_to_treadmill()
treadmill.align()
treadmill.run()

bus_service_1.treadmill_to_row()
row.align()
row.run()

bus_service_1.row_to_weight()
weight.align()
weight.run()

bus_service_1.weight_to_phone()
phone.align()
phone.run()

bus_service_1.phone_to_slide()
slide.align()
slide.run()
slide.take_slide_to_home()
