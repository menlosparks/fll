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

def base_to_stepcounter():
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=570, 
        speed_mm_s=100, 
        target_angle=0)

def stepcounter_to_treadmill():

    shared_all.turn( angle=-45)
    shared_all.turn_arc(distance=310,angle=45, speed_mm_s=150) # turn in an arc

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=170, 
            speed_mm_s=150, 
            target_angle=0)

    # go to pink and move back 3 cm
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)

    shared_all.move_straight(distance_mm=20, speed_mm_s=70)

def align_for_treadmill():
    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=90)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)

    shared_all.move_straight(distance_mm=-20, speed_mm_s=-90)

    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=182)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=120, 
            speed_mm_s=-100, 
            target_angle=182)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180)

def treadmill_to_row():
    shared_all.turn_arc(distance=80,angle=45, speed_mm_s=100) # turn in an arc
    shared_all.turn_arc(distance=80,angle=-45, speed_mm_s=100) # turn in an arc

    shared_all.move_to_color_reverse(color_sensor=color_sensor_right,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight(distance_mm=130, speed_mm_s=150)

    shared_all.turn(-90)
    shared_all.turn_to_direction( gyro=gyro,
    ####  Change yo 90
       target_angle=     90)

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=170, 
            speed_mm_s=-100, 
            ####  Change yo 90
            target_angle=     90)

    shared_all.turn(-90)
    # shared_all.turn_to_direction( gyro=gyro,
    # ####  Change yo 0(final) (or 180)
    #    target_angle=     180)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=60, 
            speed_mm_s=-100, 
        ####  Change yo 0(final) (or 180)
        target_angle= 0)

def row_to_weight():
    shared_all.move_straight(distance_mm=50, speed_mm_s=100)
    shared_all.turn(-55)
    shared_all.turn_arc(distance=200,angle=-55, speed_mm_s=100)

    # shared_all.move_straight(distance_mm=140, speed_mm_s=90)
    # shared_all.turn(180)
    # shared_all.turn_to_direction( gyro=gyro, target_angle=160) 
    # shared_all.move_straight(distance_mm=60, speed_mm_s=90)


import stepcounter
import treadmill
import row
import flip
shared_all.calibrate_gyro()


base_to_stepcounter()
stepcounter.step()
stepcounter_to_treadmill()
align_for_treadmill()
treadmill.treadon()

treadmill_to_row()
row.row()
row_to_weight()
# flip.flip_small()
