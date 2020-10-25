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
from robot_setup import WHITE_MIN_INTENSITY
from robot_setup import BLACK_MAX_INTENSITY
 
import shared_all

##### Do not change above this line ##########################################


def align(adjust_for_mission=0):
    shared_all.turn( angle=-30)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=90)
    
    # shared_all.move_straight(distance_mm=10, speed_mm_s=30)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=180)


def run(adjust_for_mission=0):
    shared_all.turn(5)
# 
    shared_all.move_straight(distance_mm=190, speed_mm_s=-210)
    right_motor.run_angle( -90,  50, Stop.BRAKE, True)

    left_motor.run_angle( -210,  3*360, Stop.BRAKE, True)

    shared_all.move_straight(distance_mm=120, speed_mm_s=180)
    shared_all.move_straight(distance_mm=20, speed_mm_s=90)
    shared_all.turn_to_direction( gyro=gyro, target_angle= 180 + adjust_for_mission)




def alignreverse(adjust_for_mission=0):
    shared_all.turn( angle=-30)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=180)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 


def alignold(adjust_for_mission=0):
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

    shared_all.move_straight(distance_mm=10, speed_mm_s = 70)

    shared_all.turn(-90)
    shared_all.move_straight(distance_mm=170, speed_mm_s = -170)
    shared_all.push_back_reset_gyro(distance_mm = 60, reset_gyro = False, new_gyro_angle =0 )
    shared_all.move_straight(distance_mm=160, speed_mm_s = 150)

    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

        
def alignheadon(adjust_for_mission=0):
    shared_all.turn(180, 210)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

