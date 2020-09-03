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



def runtrial():
    shared_all.move_straight(distance_mm=70, speed_mm_s=50)
    shared_all.move_straight(distance_mm=70, speed_mm_s=-50)

    shared_all.move_to_color(
        color_sensor = color_sensor_center,
        stop_on_color = Color.RED,
        speed_mm_s = 100)

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=200, 
        speed_mm_s=100, 
        target_angle=45)


    shared_all.turn_arc(distance=50,angle=60, speed_mm_s=100) # turn in an arc

    shared_all.turn_to_angle( gyro=gyro, target_angle=90) # turn to face suoth

    shared_all.drive_raising_crane(duration_ms = 800, 
        robot_distance_mm = 70, 
        robot_turn_angle = 30, 
        motor = crane_motor, 
        crane_angle = 60)

    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=0, robot_turn_angle=0, 
        motor=rack_motor, crane_angle=70)

runtrial()

