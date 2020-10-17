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
 
import shared_all

##### Do not change above this line ##########################################

def run (): 
    shared_all.move_rack_to_floor ()
    shared_all.move_straight(distance_mm=50, speed_mm_s=120)
    
    while shared_all.did_motor_stall(motor =rack_motor , max_degrees =30 , speed = 80):
        shared_all.move_straight(distance_mm=6, speed_mm_s=-20)

    shared_all.move_crane_up (motor=rack_motor, degrees=25)
    shared_all.drive_raising_crane (duration_ms=900, robot_distance_mm=20, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=20)
    shared_all.move_crane_to_angle(motor=rack_motor, target_angle=75)
    shared_all.drive_raising_crane (duration_ms=900, robot_distance_mm=40, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=-20)


## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
shared_all.calibrate_gyro(-90)
# align()
run()


