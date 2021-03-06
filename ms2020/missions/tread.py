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





def align(adjust_for_mission=0):

    # shared_all.move_straight(max_distance=700, speed_mm_s=100)
    # wait(1000)
    # shared_all.move_crane_to_top(crane_motor)
    # wait(10)
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
    # shared_all.move_straight(distance_mm=190, speed_mm_s=-210)

    # left_motor.run_angle( -210,  3*360, Stop.BRAKE, True)
    shared_all.turn(5)
# 
    shared_all.move_straight(distance_mm=190, speed_mm_s=-210)
    right_motor.run_angle( -90,  50, Stop.BRAKE, True)

    left_motor.run_angle( -270,  3*360, Stop.BRAKE, True)

    shared_all.move_straight(distance_mm=230, speed_mm_s=180)
    # shared_all.move_straight(distance_mm=20, speed_mm_s=90)
    shared_all.turn_to_direction( gyro=gyro, target_angle= 180 + adjust_for_mission)

    shared_all.turn(90)
    shared_all.push_back_reset_gyro(distance_mm=150,reset_gyro=True, new_gyro_angle=-90)



## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
# shared_all.calibrate_gyro(-90)
# align()
# run()

