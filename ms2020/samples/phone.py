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
import flip
##### Do not change above this line ##########################################

def align(adjust_for_mission=0):
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)

    shared_all.move_straight(distance_mm= 60, speed_mm_s= 110)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission) 


def shift(adjust_for_mission = 0):
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission) 
    shared_all.move_crane_to_floor(rack_motor)
    shared_all.move_crane_up(rack_motor, 40)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 77, 
        speed_mm_s= 110, 
        target_angle= -90+ adjust_for_mission)

    #Pull phone back
    shared_all.move_crane_to_floor(rack_motor)

    shared_all.drive_raising_crane(duration_ms=2500, robot_distance_mm=-170, robot_turn_angle=-20, 
        motor=rack_motor, crane_angle=-10)
    shared_all.move_crane_to_top(rack_motor)

    #Shift left to use crane motor
    shared_all.turn_arc(distance=80,angle=70, speed_mm_s=-100)
    shared_all.turn(-70)

def run():
    shift(adjust_for_mission=0)
    flip.flip_small()