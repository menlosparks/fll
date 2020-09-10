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


def raise_weight(adjust_for_mission=0):
    shared_all.move_crane_to_top(rack_motor)
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.move_crane_up( motor = crane_motor, degrees = 45)
    shared_all.move_straight(distance_mm=115, speed_mm_s=50)
    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=0, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=120)
    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=-70, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=-40)
    shared_all.move_crane_to_top(crane_motor)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + adjust_for_mission) 


# raise_weight()
