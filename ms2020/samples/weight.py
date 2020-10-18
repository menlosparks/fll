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

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 15, 
        speed_mm_s= 110, 
        target_angle= 180+ adjust_for_mission)

    shared_all.move_crane_to_top(motor=crane_motor)
    shared_all.turn(90, speed_deg_s=160)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 10, 
        speed_mm_s= -110, 
        target_angle= -90+ adjust_for_mission)


def run(adjust_for_mission=0):
    
    shared_all.start_moving_crane_to_angle(motor = crane_motor, target_angle = 25)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.GREEN, alternative_color=Color.GREEN, max_distance_mm=60)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW, max_distance_mm=170)
    shared_all.turn_arc(distance= 30,angle = 15, speed_mm_s= 60)

    #lift weight and back up
    crane_motor.stop()
    shared_all.move_crane_down( motor = crane_motor, degrees = 10)
    crane_motor.run_time(600, 900)

    # shared_all.move_crane_to_floor(crane_motor)
    # shared_all.move_crane_up( motor = crane_motor, degrees = 40)
    shared_all.start_moving_crane_to_angle(motor = crane_motor, target_angle = 25)
    shared_all.move_straight(distance_mm=70, speed_mm_s=-120)

    # turn west and back up
    shared_all.turn(-140, speed_deg_s=200)
    shared_all.start_moving_crane_to_top(motor = crane_motor)
    shared_all.move_straight(distance_mm=70, speed_mm_s=-150)
    shared_all.turn_arc(distance=50, angle=60, speed_mm_s=190)

def align_right_turns(adjust_for_mission=0):


    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=70)


    shared_all.move_straight(distance_mm=100, speed_mm_s=140)
    shared_all.move_crane_to_top(crane_motor)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 
    shared_all.move_straight(distance_mm=390, speed_mm_s=-200)

    shared_all.push_back_reset_gyro(distance_mm = 60,  reset_gyro = True,  new_gyro_angle =180 )
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 15, 
        speed_mm_s= 110, 
        target_angle= 180+ adjust_for_mission)

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 30, 
        speed_mm_s= -110, 
        target_angle= -90+ adjust_for_mission)

