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

def align_arp():

    shared_all.move_straight(distance_mm=290, speed_mm_s=150)

    shared_all.move_to_color(color_sensor=color_sensor_right, stop_on_color=Color.GREEN,
                        max_distance_mm=600)
    shared_all.move_straight(distance_mm=35, speed_mm_s=100)                    
    # wait(1000)
    # wait(10)

def run_arp():
    shared_all.move_crane_to_top(crane_motor)
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.turn(-10)

    shared_all.move_straight(distance_mm=300, speed_mm_s=-190,)


def align():

    shared_all.calibrate_gyro(-85)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=200, 
            speed_mm_s=190, 
        target_angle= -85)

    # shared_all.move_crane_to_floor( motor=crane_motor)
    # shared_all.move_crane_up( motor=crane_motor, degrees=60)
    shared_all.move_to_color(color_sensor = color_sensor_right,
        stop_on_color = Color.GREEN,
        alternative_color = Color.GREEN, speed_mm_s=40, max_distance_mm=60)
    shared_all.move_straight(distance_mm=50, speed_mm_s=40)



def run():
    ##lift 
    shared_all.move_crane_up(crane_motor, 55)
    # shared_all.move_crane_down(crane_motor, 10)
    # shared_all.drive_raising_crane(duration_ms=600, robot_distance_mm=0, robot_turn_angle=0, 
    #     motor=crane_motor, crane_angle=110)
    # shared_all.move_crane_down(crane_motor, 80)

    #knock
    # shared_all.move_straight(distance_mm=18, speed_mm_s=-90)
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=10, robot_turn_angle=-30, 
        motor=crane_motor, crane_angle=-20)

    #backup
    shared_all.start_moving_crane_to_angle(crane_motor, 70)
    shared_all.turn_to_direction(gyro=gyro, target_angle=-85)
    shared_all.move_straight(distance_mm=450, speed_mm_s=-220)

def aligncubes():
    shared_all.move_straight(distance_mm=290, speed_mm_s=150)

    shared_all.move_to_color(color_sensor=color_sensor_right, stop_on_color=Color.GREEN,
                        max_distance_mm=600)
    shared_all.move_straight(distance_mm=10, speed_mm_s=-100)

def dropcubes():
    shared_all.move_crane_to_floor(crane_motor)
    shared_all.start_moving_crane_to_angle(crane_motor, 70)
    shared_all.move_straight(distance_mm=300, speed_mm_s=-190)

## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
# shared_all.calibrate_gyro(-90)
# align()
# run()
#aligncubes()
#dropcubes()
