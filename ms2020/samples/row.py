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
def align(adjust_for_mission=0):
        shared_all.move_straight(distance_mm=180, speed_mm_s=150)
        shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)
        shared_all.move_to_color(color_sensor=color_sensor_center,
                stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
        shared_all.move_straight(distance_mm=20, speed_mm_s=120)

def shake():
    shared_all.move_straight(distance_mm=10, speed_mm_s=20)

    left_motor.run_angle( 120,  30, Stop.BRAKE, True)
    shared_all.move_crane_to_floor(rack_motor)

    shared_all.move_straight(distance_mm=10, speed_mm_s=-20)
    right_motor.run_angle( 120,  30, Stop.BRAKE, True)
    shared_all.move_crane_to_floor(rack_motor)

    shared_all.move_straight(distance_mm=10, speed_mm_s=-20)
    shared_all.move_crane_to_floor(rack_motor)


def run(adjust_for_mission=0):
    shared_all.turn_to_direction( gyro=gyro, target_angle=-37+ adjust_for_mission)
    shared_all.move_crane_to_floor(rack_motor)
    shake()
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=-80, robot_turn_angle=-20, 
            motor=rack_motor, crane_angle=-5)
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=25, robot_turn_angle=-50, 
            motor=rack_motor, crane_angle=-5)
    shared_all.turn(8)        
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=-10, robot_turn_angle=0, 
            motor=rack_motor, crane_angle=110)


