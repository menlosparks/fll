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


def align_to_row_local(adjust_for_mission=0):
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=350, 
            speed_mm_s=110, 
            target_angle= -90+ adjust_for_mission)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=100, 
            speed_mm_s=-100, 
            target_angle= 0+ adjust_for_mission)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLUE, alternative_color=Color.BLUE)
    shared_all.move_straight( distance_mm=20, speed_mm_s=-50)


def align_to_row_special(adjust_for_mission=0):
        shared_all.move_straight(distance_mm=180, speed_mm_s=120)
        shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)
        shared_all.move_to_color(color_sensor=color_sensor_center,
                stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
        shared_all.move_straight(distance_mm=14, speed_mm_s=120)

def dorow(adjust_for_mission=0):
        shared_all.turn_to_direction( gyro=gyro, target_angle=-37+ adjust_for_mission)
        # shared_all.move_straight(distance_mm=10, speed_mm_s=120)
        shared_all.move_crane_to_floor(rack_motor)
        row.shake()
        shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=-80, robot_turn_angle=-20, 
                motor=rack_motor, crane_angle=-5)
        shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=35, robot_turn_angle=-45, 
                motor=rack_motor, crane_angle=-5)
        shared_all.turn(8)        
        shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=-10, robot_turn_angle=0, 
                motor=rack_motor, crane_angle=90)


INITIAL_ANGLE=-90

shared_all.calibrate_gyro(INITIAL_ANGLE)

adjust_for_mission=0 - INITIAL_ANGLE
# shared_all.push_back_reset_gyro(distance_mm = 80, reset_gyro = True, new_gyro_angle =0 )
# adjust_for_mission=-90

# bus_service_1.treadmill_to_row()
# bus_service_1.align_to_row(adjust_for_mission)
# align_to_row_local()
# row.row()
# bus_service_1.push_tires()


align_to_row_special()
dorow()
