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
from robot_setup import WHITE_MIN_INTENSITY
from robot_setup import BLACK_MAX_INTENSITY
 
import shared_all

##### Do not change above this line ##########################################


def base_to_bench():
    shared_all.calibrate_gyro(-85)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=180, 
            speed_mm_s=190, 
        target_angle= -85)


def bench_to_loading():
    shared_all.move_straight(distance_mm=200, 
            speed_mm_s=-140)
    shared_all.move_crane_to_top(crane_motor)
    shared_all.move_crane_down(crane_motor, 20)
    shared_all.sound_alarm()
    shared_all.any_button_pressed()

def bench_to_base():
    shared_all.turn_arc(distance=-250, angle=-30, speed_mm_s=190)

def loading_to_bench():
    base_to_bench()
    
def base_to_innov():
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=110, 
            speed_mm_s=190, 
            target_angle= -90)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.GREEN, alternative_color=Color.GREEN,
         max_distance_mm=30)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=10, 
            speed_mm_s=110, 
            target_angle= -90)        

def innov_to_basket(adjust_for_mission=0):

    # shared_all.move_straight(distance_mm=10,  speed_mm_s=-90)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=180, 
            speed_mm_s=130, 
        target_angle= -55 + adjust_for_mission)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity= robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=80)        
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=50, 
            speed_mm_s=130, 
        target_angle= -55 + adjust_for_mission)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity= robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=80)



    # shared_all.turn_arc(distance=-90, angle = -60, speed_mm_s=200)
    # shared_all.move_straight(distance_mm=40,  speed_mm_s=110)
    # shared_all.turn_arc(distance=320, angle = -60, speed_mm_s=230)

    # shared_all.move_to_color(color_sensor=color_sensor_center,
    #     stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
    #      max_intensity= robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
    #      max_distance_mm=80)
    # shared_all.turn_to_direction(gyro = gyro, 
    #         target_angle= -90)    
    # shared_all.move_crane_to_top(crane_motor)
    # shared_all.start_moving_crane_to_angle(crane_motor, 30)

    # shared_all.turn(40)
    # shared_all.move_straight(distance_mm=70, speed_mm_s=80)
    # shared_all.move_to_color(color_sensor=color_sensor_right,
    #     stop_on_color=Color.WHITE, alternative_color=Color.BLACK, speed_mm_s=30,
    #     min_intensity=robot_setup.WHITE_MIN_INTENSITY[color_sensor_right],
    #     max_distance_mm=60)


def base_to_basket(adjust_for_mission=0):

    shared_all.turn_arc(distance=620, angle = -90, speed_mm_s=230)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.turn_to_direction(gyro = gyro, 
            target_angle= -90, 
            speed_mm_s=120)    

def loading_to_basket():
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=120, 
            speed_mm_s=140, 
            target_angle= 0)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=120, 
            speed_mm_s=140, 
        target_angle= -90)


def basket_to_bench():
    shared_all.turn_arc(distance=90, angle = -55, speed_mm_s=-70)
    shared_all.move_crane_to_top( motor=rack_motor)

    shared_all.turn_to_direction( gyro=gyro, target_angle=180 + adjust_for_mission) 
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=120, 
            speed_mm_s=140, 
        target_angle= 180 + adjust_for_mission)
    shared_all.move_crane_to_top( motor=crane_motor)
    shared_all.turn(-60)


