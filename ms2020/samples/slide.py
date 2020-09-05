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
 
##### Do not change above this line ##########################################



def slide():
    shared_all.move_crane_to_floor(rack_motor)
    # shared_all.move_crane_up( motor = rack_motor, degrees = 30)
    shared_all.move_straight(distance_mm=50, speed_mm_s=100)

    while shared_all.did_motor_stall(motor =rack_motor , max_degrees =80 , speed = 80):
        shared_all.log_string('Motor stalled')
        shared_all.move_straight(distance_mm=4, speed_mm_s=-20)

    # if shared_all.did_motor_stall(motor =rack_motor , max_degrees = 90, speed = 80):
    #     shared_all.log_string('Motor stalled')
    #     shared_all.move_straight(distance_mm=-8, speed_mm_s=100)
    #     # shared_all.move_crane_up( motor = rack_motor, degrees = 15)
    # else:
    #     shared_all.log_string('No stalled')


    # shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=0, robot_turn_angle=0, 
    #     motor=rack_motor, crane_angle=70)
    # shared_all.move_crane_up( motor = rack_motor, degrees = 15)

    # shared_all.move_crane_down( motor = rack_motor, degrees = 8)
    # shared_all.move_crane_up( motor = rack_motor, degrees = 15)
    # shared_all.move_crane_down( motor = rack_motor, degrees = 8)

    # shared_all.drive_raising_crane(duration_ms=1500, robot_distance_mm=0, robot_turn_angle=0, 
    #     motor=rack_motor, crane_angle=90)

    # shared_all.move_straight(distance_mm=40, speed_mm_s=100)
    
slide() 