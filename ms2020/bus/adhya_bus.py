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
import shared_all
 
from robot_setup import left_motor
from robot_setup import right_motor
from robot_setup import robot
from robot_setup import rack_motor
from robot_setup import crane_motor
from robot_setup import gyro
from robot_setup import touch_sensor
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

def tread_to_weight():
    shared_all.move_straight(distance_mm=50, speed_mm_s=200)
   shared_all.turn(angle=90, speed_deg_s=200)
   shared_all.move_reverse(max_distance=65, speed_mm_s=75)
   shared_all.move_straight(distance_mm=450, speed_mm_s=175)


def weight_to_cell():  
    shared_all.move_reverse( max_distance=25 , speed_mm_s= 100)
    shared_all.turn(angle=-90, speed_deg_s=100)
    shared_all.move_reverse(max_distance=55, speed_mm_s=100)


def cell_to_black():
    shared_all.turn(angle=-110, speed_deg_s=150)
    shared_all.move_straight(distance_mm=120, speed_mm_s=100)


def row_to_weight():
    shared_all.turn(angle=-90, speed_deg_s=100)
    shared_all.move_straight(distance_mm=40, speed_mm_s=100)
    shared_all.turn(angle=90, speed_deg_s=100)
    shared_all.move_straight(distance_mm=50, speed_mm_s=100)
    shaared_all.turn(angle=-90, speed_deg_s=100)



# Calibrate the gyro point in the direction at the start
# shared_all.calibrate_gyro(0)
# weight_to_cell()
# cell_to_black
# tread_to_weight

