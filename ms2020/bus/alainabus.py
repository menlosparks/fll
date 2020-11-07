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
 
import shared_all

##### Do not change above this line ##########################################
#alainabus1-3 part of missions 

def bballtobase ()
    shared_all.turn(angle= -60, speed_mm_s = 100):
    shared_all.move_straight (distance_mm=90, speed_mm_s=-100)

def basetostep ()
    shared_all.move_straight_target_direction(gyro=gyro, distance_mm=885, speed_mm_s=130, target_angle=0):






    ## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
shared_all.calibrate_gyro(-90)
# align()
bballtobase ()
basetostep () 

