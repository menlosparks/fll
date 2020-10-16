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
import flip
##### Do not change above this line ##########################################

def align(adjust_for_mission=0):
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE, speed_mm_s=25,
         min_intensity=robot_setup.WHITE_MIN_INTENSITY[color_sensor_center])

    shared_all.move_straight(distance_mm= 70, speed_mm_s= -70)
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.turn_arc(distance=180, angle=70, speed_mm_s =70)

def run():
    crane_motor.run_until_stalled(-300, Stop.COAST, 35)
    crane_motor.run_time(720, 700)

    #try 2nd flip
    # shared_all.move_crane_to_floor(crane_motor)
    # shared_all.turn_arc(distance=10, angle=10, speed_mm_s =55)
    # crane_motor.run_until_stalled(-300, Stop.COAST, 35)
    # crane_motor.run_time(720, 700)

