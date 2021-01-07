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

def alignold():
    shared_all.move_crane_to_top(crane_motor)
    shared_all.move_straight(distance_mm=550, speed_mm_s=160)

def runold2 ():
    shared_all.move_straight(distance_mm=550, speed_mm_s=160)
    shared_all.move_crane_to_floor(motor=rack_motor)
    shared_all.drive_raising_crane(duration_ms=50, robot_distance_mm=-37, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=80)
    shared_all.move_straight (distance_mm=550, speed_mm_s=-160)
    

#(NEW RUN, DO NOT USE FUNCTION 'runold') ####


def align():
    shared_all.calibrate_gyro(-45)


    shared_all.move_straight_target_direction(gyro=gyro,
        distance_mm=480, speed_mm_s=170, target_angle=-45)

    shared_all.move_to_color(color_sensor=color_sensor_center, 
        stop_on_color=Color.GREEN, max_distance_mm=40)

    shared_all.move_straight(distance_mm=30, speed_mm_s=40)

def run():
    shared_all.move_crane_down(rack_motor, 70)
    shared_all.move_hook_to_floor()
    shared_all.move_straight(distance_mm=20, speed_mm_s=-50)

    shared_all.drive_raising_crane (duration_ms=800, robot_distance_mm=-20, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=20)
    shared_all.drive_raising_crane (duration_ms=1900, robot_distance_mm=-70, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=30)
    shared_all.move_straight(distance_mm=40, speed_mm_s=-130)
    shared_all.move_crane_up(rack_motor, 30)

    #backup
    shared_all.move_straight(distance_mm=600, speed_mm_s=-200)
    # shared_all.move_rack_to_top()


    ## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
# shared_all.calibrate_gyro(-90)
# align()
# runold()


