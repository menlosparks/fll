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

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)

    shared_all.move_straight(distance_mm=80, speed_mm_s=120)
    shared_all.move_crane_to_top(crane_motor)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 
    shared_all.move_straight(distance_mm=230, speed_mm_s=-200)

    shared_all.push_back_reset_gyro(distance_mm = 80,  reset_gyro = True,  new_gyro_angle =180 )
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 65, 
        speed_mm_s= 110, 
        target_angle= 180+ adjust_for_mission)

    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 30, 
        speed_mm_s= -110, 
        target_angle= -90+ adjust_for_mission)


def run(adjust_for_mission=0):
    

    shared_all.move_crane_to_floor(crane_motor)
    shared_all.move_crane_up( motor = crane_motor, degrees = 50)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)
    shared_all.turn_arc(distance= 30,angle = 15, speed_mm_s= 60)

    #lift weight and back up
    crane_motor.stop()
    crane_motor.run_time(270, 700)
    # shared_all.drive_raising_crane(duration_ms=700 , robot_distance_mm=0, robot_turn_angle=0, 
    #     motor=crane_motor, crane_angle=130)
    shared_all.move_crane_down( motor = crane_motor, degrees = 50)
    shared_all.move_straight(distance_mm=55, speed_mm_s=-120)

    shared_all.turn(-90)
    shared_all.move_crane_to_top(crane_motor)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 70, 
        speed_mm_s= -140, 
        target_angle= 180+ adjust_for_mission)


