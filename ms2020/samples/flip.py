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
 
##### Do not change above this line ##########################################

def flip_small():
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.move_straight(distance_mm=60, speed_mm_s=90)
    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=30, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=110)
    shared_all.move_crane_to_top(crane_motor)

def flip_phone():
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.move_straight(distance_mm=60, speed_mm_s=90)
    shared_all.drive_raising_crane(duration_ms=350, robot_distance_mm=20, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=120)
    shared_all.move_crane_to_top(crane_motor)

def flip_bigt():
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.move_straight(distance_mm=20, speed_mm_s=50)
    left_motor.run_angle( 120,  10, Stop.BRAKE, True)
    right_motor.run_angle(120,  10, Stop.BRAKE, True)

    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=50, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=100)
    shared_all.drive_raising_crane(duration_ms=200, robot_distance_mm=30, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=30)


def do_flips_bigtire(adjust_for_mission=0):
    flip_bigt()

def bigt_align():
    shared_all.start_moving_crane_to_angle(crane_motor, 20)
    shared_all.turn(-180)
# flip_small()
# wait(6000)
# flip_small()
# wait(6000) 

# flip_bigt()
