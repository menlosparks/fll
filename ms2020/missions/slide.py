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

#(OLD RUN, USE FUNCTION 'run')#########
def runold (): 
    shared_all.move_rack_to_floor ()
    shared_all.move_straight(distance_mm=60, speed_mm_s=120)
    
    while shared_all.did_motor_stall(motor =rack_motor , max_degrees =50 , speed = 320):
        # log_string('stalled - step back')
        shared_all.move_reverse(max_distance=6, speed_mm_s=20)

    shared_all.move_crane_to_angle(motor=rack_motor, target_angle=90)
    shared_all.drive_raising_crane (duration_ms=900, robot_distance_mm=80, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=-20)
    shared_all.move_crane_to_angle(motor=rack_motor, target_angle=120)
    shared_all.move_reverse(max_distance=20, speed_mm_s=100)

#(NEW RUN, DO NOT USE FUNCTION 'runold') ####

def run ():
    shared_all.move_straight(distance_mm=470, speed_mm_s=120)
    shared_all.move_crane_to_floor(motor=rack_motor)
    shared_all.drive_raising_crane(duration_ms=50, robot_distance_mm=-37, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=80)
    shared_all.move_straight (distance_mm=470, speed_mm_s=-120)
    


    ## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
# shared_all.calibrate_gyro(-90)
# align()
# runold()


