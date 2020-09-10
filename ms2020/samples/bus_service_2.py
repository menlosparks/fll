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

def base_to_basket(adjust_for_mission=0):
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=80, 
            speed_mm_s=100, 
        target_angle= 0 + adjust_for_mission)

    shared_all.turn(-90)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=300, 
            speed_mm_s=180, 
        target_angle= -90 + adjust_for_mission)

    shared_all.move_to_color(color_sensor=color_sensor_right,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=100, 
            speed_mm_s=180, 
        target_angle= -90 + adjust_for_mission)

    shared_all.turn(-45)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=50, 
            speed_mm_s=180, 
        target_angle= -135 + adjust_for_mission)
