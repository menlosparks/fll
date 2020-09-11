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

def flip_small():
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.move_straight(distance_mm=60, speed_mm_s=90)
    shared_all.drive_raising_crane(duration_ms=300, robot_distance_mm=20, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=110)
    shared_all.move_crane_to_top(crane_motor)

def flip_bigt():
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.move_straight(distance_mm=70, speed_mm_s=50)
    left_motor.run_angle( 120,  10, Stop.BRAKE, True)
    right_motor.run_angle(120,  10, Stop.BRAKE, True)

    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=50, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=100)
    shared_all.drive_raising_crane(duration_ms=200, robot_distance_mm=30, robot_turn_angle=0, 
        motor=crane_motor, crane_angle=30)

def  pull_phone_back(adjust_for_mission = 0):

    ### change lane to the left
    shared_all.turn_arc(distance=30, angle = 60, speed_mm_s=-70)
    shared_all.turn_arc(distance=30, angle = -60, speed_mm_s=-70)

    shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + adjust_for_mission) 
    shared_all.move_straight(distance_mm=90, speed_mm_s=110)
    shared_all.move_crane_to_floor(rack_motor) 
    shared_all.drive_raising_crane(duration_ms=1100, robot_distance_mm=-130, robot_turn_angle=0, 
        motor=rack_motor, crane_angle=-15)
    shared_all.move_crane_up(rack_motor, 210) 

def shift_phone(adjust_for_mission = 0):
    shared_all.move_crane_to_floor(rack_motor)

    shared_all.turn_arc(distance=50,angle = 18, speed_mm_s=30)
    shared_all.move_crane_up(rack_motor, 70)

    pull_phone_back(adjust_for_mission )

    ### change lane to the left
    shared_all.turn_arc(distance=80, angle = 80, speed_mm_s=-100)
    shared_all.turn_arc(distance=80, angle = -80, speed_mm_s=-100)

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 10, 
        speed_mm_s= 100, 
        target_angle= -90 + adjust_for_mission)


def do_flips_bigtire(adjust_for_mission=0):
    flip_bigt()

# flip_small()
# wait(6000)
# flip_small()
# wait(6000) 

# flip_bigt()
