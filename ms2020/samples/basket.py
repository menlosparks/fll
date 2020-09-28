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
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=110, 
            speed_mm_s=120, 
        target_angle= -90 + adjust_for_mission)
    shared_all.move_to_color(color_sensor=color_sensor_right,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE, speed_mm_s=30)
    shared_all.move_straight(distance_mm=7, speed_mm_s=-90)
    shared_all.turn_to_direction(gyro = gyro, 
            target_angle= -137 + adjust_for_mission,
            speed_mm_s=80)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_right,
        stop_on_color=Color.GREEN, alternative_color=Color.GREEN, speed_mm_s=30)
    shared_all.move_straight(distance_mm=10, speed_mm_s=-100)

def putcube():
    shared_all.drive_raising_crane(duration_ms = 1000, 
            robot_distance_mm = 70, 
            robot_turn_angle = 0, 
            motor = crane_motor, 
            crane_angle = -80)
    shared_all.move_straight(distance_mm=60, speed_mm_s=-90)


def level1():
    shared_all.move_crane_to_top( motor=crane_motor)
    shared_all.move_crane_down(rack_motor, 50)
    shared_all.move_rack_to_floor()
    shared_all.turn(angle=-10, speed_deg_s=90)
    shared_all.move_straight(distance_mm=50, speed_mm_s=90)
    shared_all.turn(angle=20, speed_deg_s=90)
    rack_motor.stop(Stop.BRAKE)
    shared_all.drive_raising_crane(duration_ms = 600, 
        robot_distance_mm = -40, 
        robot_turn_angle = 8, 
        motor = rack_motor, 
        crane_angle = 120)
    shared_all.move_crane_down( motor=rack_motor, degrees=40)
    # shared_all.drive_raising_crane(duration_ms = 600, 
    #     robot_distance_mm = -25, 
    #     robot_turn_angle = 7, 
    #     motor = rack_motor, 
    #     crane_angle = 120 )
    shared_all.move_straight(distance_mm=60, speed_mm_s=-90)

    # shared_all.drive_raising_crane(duration_ms = 250, 
    #     robot_distance_mm = -5, 
    #     robot_turn_angle = 2, 
    #     motor = rack_motor, 
    #     crane_angle = 40)


def level2():
    shared_all.move_rack_to_floor( )
    shared_all.log_string('Moved racktotop')
    shared_all.move_crane_up( motor=rack_motor, degrees=40)
    shared_all.turn(angle=20)
    shared_all.drive_raising_crane(duration_ms = 500, 
        robot_distance_mm = 20, 
        robot_turn_angle = 0, 
        motor = rack_motor, 
        crane_angle = 190)
    shared_all.move_straight(distance_mm=40, speed_mm_s=-90)
    shared_all.move_crane_down( motor=rack_motor, degrees=90)
    shared_all.log_string('MOtor is ' + str(crane_motor))

# all.move_crane_up( motor=rack_motor, degrees=110)

def run():
    putcube()
    level1()
    # level2()


    ## Below lines only for testing
# Comment out when done testing. Do not upload to Git hub without commenting.
# shared_all.calibrate_gyro(-90)
# align()
# run()

#########################

def alignold(adjust_for_mission=0):

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=90, 
            speed_mm_s=100, 
        target_angle= -90 + adjust_for_mission)
    # shared_all.turn(-90)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=85, 
            speed_mm_s=-120, 
        target_angle= 180 + adjust_for_mission)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=75, 
            speed_mm_s=110, 
        target_angle= 180 + adjust_for_mission)

    shared_all.turn_to_direction(gyro = gyro, 
            target_angle= -135 + adjust_for_mission,
            speed_mm_s=80)

def level1crane():
    shared_all.move_crane_to_floor( motor=crane_motor)
    shared_all.move_crane_up( motor=crane_motor, degrees=35)
    shared_all.move_straight(distance_mm=60, speed_mm_s=90)
    shared_all.move_crane_down( motor=crane_motor, degrees=15)
    shared_all.move_straight(distance_mm=8, speed_mm_s=90)
    shared_all.drive_raising_crane(duration_ms = 700, 
        robot_distance_mm = -10, 
        robot_turn_angle = 0, 
        motor = crane_motor, 
        crane_angle = 120)
    shared_all.move_crane_down( motor=crane_motor, degrees=30)
    shared_all.move_straight(distance_mm=30, speed_mm_s=-90)

def level2crane():
    shared_all.move_rack_to_floor( )
    shared_all.log_string('Moved racktotop')
    shared_all.move_crane_up( motor=rack_motor, degrees=40)
    shared_all.turn(angle=20)
    shared_all.drive_raising_crane(duration_ms = 500, 
        robot_distance_mm = 20, 
        robot_turn_angle = 0, 
        motor = rack_motor, 
        crane_angle = 190)
    shared_all.move_straight(distance_mm=40, speed_mm_s=-90)
    shared_all.move_crane_down( motor=rack_motor, degrees=90)
    shared_all.log_string('MOtor is ' + str(crane_motor))
