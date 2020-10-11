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

def base_to_treadmill(adjust_for_mission=0):
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=1050, 
        speed_mm_s=150, 
        target_angle=0)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

def base_to_stepcounter_reverse(adjust_for_mission=0):
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=570, 
        speed_mm_s=-190, 
        target_angle=180)

def base_to_stepcounter_forward(adjust_for_mission=0):
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=550, 
        speed_mm_s=150, 
        target_angle=0)

def base_to_stepcounter(adjust_for_mission=0):
    base_to_stepcounter_reverse(adjust_for_mission)

def stepcounter_to_treadmill_reverse(adjust_for_mission=0):

    shared_all.move_straight(distance_mm=160,speed_mm_s=150)
    shared_all.turn( angle=-10)
    shared_all.turn_arc(distance=330 ,angle=-50, speed_mm_s=-150) 
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 400, 
        speed_mm_s= -170, 
        target_angle=180)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE,
         min_intensity=robot_setup.WHITE_MIN_INTENSITY[color_sensor_center],
         max_distance_mm=180)



def stepcounter_to_treadmill_forward(adjust_for_mission=0):

    # shared_all.turn( angle=-45)
    shared_all.turn_arc(distance=200,angle=-65, speed_mm_s=150) # turn in an arc
    shared_all.turn_arc(distance=200,angle=65, speed_mm_s=150) # turn in an arc


    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=170, 
            speed_mm_s=150, 
            target_angle=0)

    # back up and move at an angle to spine black line
    shared_all.turn(angle=40, speed_deg_s=90)
    shared_all.move_reverse(max_distance=50, speed_mm_s=110)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK, max_intensity=15)
    shared_all.move_reverse(max_distance=10, speed_mm_s=80)
    shared_all.turn(angle=-40, speed_deg_s=90)
    shared_all.turn_to_direction(gyro=gyro, target_angle=0)

def stepcounter_to_treadmill(adjust_for_mission=0):
    stepcounter_to_treadmill_reverse(adjust_for_mission)

def reuse_treadmill_align(adjust_for_mission=0):
    shared_all.turn( angle=-30)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=180)
    
    # shared_all.move_straight(distance_mm=10, speed_mm_s=30)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=180)


def treadmill_to_row_simple(adjust_for_mission=0):

    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE,
         min_intensity=robot_setup.WHITE_MIN_INTENSITY[color_sensor_center],
         max_distance_mm=180)
    # reuse_treadmill_align(adjust_for_mission)

def treadmill_to_row(adjust_for_mission=0):

    treadmill_to_row_simple(adjust_for_mission)

def treadmill_to_row_proper(adjust_for_mission=0):

    shared_all.turn_arc(distance=80,angle=85, speed_mm_s=100)
    shared_all.move_straight_target_direction(gyro=gyro,
        distance_mm=170, speed_mm_s=-160, target_angle=-90)
    shared_all.push_back_reset_gyro(distance_mm=40, reset_gyro = True, new_gyro_angle=-90)

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=130, 
        speed_mm_s=180, 
        target_angle=-90)
    shared_all.turn_to_direction( gyro=gyro, target_angle= 180 + adjust_for_mission)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=120)


def treadmill_to_row_nearrow(adjust_for_mission=0):

    shared_all.turn_arc(distance=110,angle=55, speed_mm_s=100) # turn in an arc
    shared_all.turn(angle=-55, speed_deg_s=120)

    shared_all.turn_to_direction( gyro=gyro, target_angle= 180 + adjust_for_mission)

    # shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission)
    shared_all.move_straight(180, -180)

    shared_all.push_back_reset_gyro(distance_mm=60, reset_gyro = True, new_gyro_angle=180)
    shared_all.move_straight(distance_mm=70, speed_mm_s=100)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=40)



def push_tires(adjust_for_mission=0):
    shared_all.turn_arc(distance=40,angle=-50, speed_mm_s=-100) # turn in an arc
    shared_all.turn_arc(distance=60,angle=-25, speed_mm_s=100) # turn in an arc
    shared_all.move_straight(distance_mm=130, speed_mm_s=-100)

def push_small_tire(adjust_for_mission=0):
    shared_all.move_crane_to_floor(rack_motor)
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=30, robot_turn_angle=-35, 
            motor=rack_motor, crane_angle=-5)
    shared_all.move_crane_to_top(rack_motor)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-70)
    shared_all.turn_arc(distance=90,angle=-20, speed_mm_s=140)


def row_to_weight(adjust_for_mission=0):

    shared_all.turn(angle=-40)
    shared_all.turn_arc(distance=50 , angle=-60, speed_mm_s=80)

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 70, 
        speed_mm_s= 160, 
        target_angle= -90+ adjust_for_mission)



def weight_to_phone(adjust_for_mission=0):
    shared_all.push_back_reset_gyro(distance_mm = 60, reset_gyro = True, new_gyro_angle =180 )
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 310, 
        speed_mm_s= 180, 
        target_angle= 180+ adjust_for_mission)


def phone_to_slide(adjust_for_mission=0):

    shared_all.turn_arc(distance=80, angle=-20, speed_mm_s =90)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 240, 
        speed_mm_s= 180, 
        target_angle= 180+ adjust_for_mission)
    shared_all.move_to_color(color_sensor=color_sensor_center,
     stop_on_color=Color.BLACK)



def bigtire_to_slide(adjust_for_mission=0):
    shared_all.move_straight(distance_mm=40, speed_mm_s=-100)
    shared_all.turn_arc(distance=30, angle = 30, speed_mm_s=-130)
    shared_all.turn_to_direction( gyro=gyro, target_angle=90+ adjust_for_mission) 

