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

def shift_phone(adjust_for_mission = 0):
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 100, 
        speed_mm_s= 110, 
        target_angle= -90+ adjust_for_mission)
    shared_all.move_crane_to_floor(rack_motor)
    shared_all.drive_raising_crane(duration_ms=1100, robot_distance_mm=-80, robot_turn_angle=-25, 
        motor=rack_motor, crane_angle=-15)



INITIAL_ANGLE=180

shared_all.calibrate_gyro(INITIAL_ANGLE)
ust_for_mission=0 - INITIAL_ANGLE

# bus_service_1.align_to_weight(adjust_for_mission=0)
# weight.raise_weight(adjust_for_mission=0)
# # adjust_for_mission=180

# weight.raise_weight()


bus_service_1.weight_to_phone(adjust_for_mission=0)
bus_service_1.align_to_phone(adjust_for_mission=0)
shift_phone(adjust_for_mission=0)
# flip.shift_phone(adjust_for_mission=0)
# flip.flip_small()
