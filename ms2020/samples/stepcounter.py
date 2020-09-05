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

def step():

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=230, 
        speed_mm_s=25, 
        target_angle=0)

    shared_all.move_straight(distance_mm=70, speed_mm_s=-100)
    shared_all.turn( angle=-45)
    shared_all.turn_arc(distance=100,angle=45, speed_mm_s=100) # turn in an arc

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=200, 
        speed_mm_s=150, 
        target_angle=0)

shared_all.calibrate_gyro()
step()