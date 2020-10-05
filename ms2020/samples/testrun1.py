#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
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
import testcode
import linefollow

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

from robot_setup import SOUND_VOLUME
from robot_setup import WHEEL_DIAMETER_MM
from robot_setup import AXLE_TRACK_MM
from robot_setup import SENSOR_TO_AXLE
from robot_setup import WHEEL_CIRCUM_MM
from robot_setup import DEGREES_PER_MM

##### Do not change above this line ##########################################
 
def returnhome():
    testcode.turn_to_angle(gyro=gyro, target_angle=0)
    testcode.move_straight(distance=1000, speed_mm_s=-500)

def traffic():

    # testcode.move_straight(450, 400)
    # testcode.move_crane_to_floor(crane_motor)
    # testcode.move_crane_up(crane_motor, 30)
    # testcode.turn_to_angle( gyro, 20)
 
    testcode.drive_raising_crane(duration_ms=900, 
        robot_distance_mm=30, 
        robot_turn_angle=25, 
        crane_motor=crane_motor, 
        crane_angle=90)



def swing():
    # testcode.move_straight(distance=1000, speed_mm_s=500)

    testcode.move_straight_target_direction(gyro=gyro, distance_mm=1000, speed_mm_s=400, target_angle=0)

def tower():
    # testcode.move_crane_up( crane_motor=crane_motor, degrees=30)
    # testcode.drive_raising_crane(duration_ms=1000, 
    #     robot_distance_mm=100, 
    #     robot_turn_angle=-3, 
    #     crane_motor=crane_motor, 
    #     crane_angle=70)
    # testcode.drive_raising_crane(duration_ms=1000, 
    #     robot_distance_mm=100, 
    #     robot_turn_angle=0, 
    #     crane_motor=crane_motor, 
    #     crane_angle=-30)
    testcode.drive_raising_crane(duration_ms=1000, 
        robot_distance_mm=100, 
        robot_turn_angle=0, 
        crane_motor=crane_motor, 
        crane_angle=-50)
    # testcode.move_crane_down( crane_motor=crane_motor, degrees=30)
    # testcode.turn(-40)

def bridge():
     testcode.move_straight_target_direction(gyro=gyro, 
     distance_mm=550, 
     speed_mm_s=300, 
     target_angle=0)
   

testcode.calibrate_gyro(0)    
# traffic()
# swing()
# returnhome()
# tower()
# bridge()

linefollow.follow_line_border(
    color_sensor=color_sensor_center,
    distance_mm=320,
    speed_mm_s=90)

wait(999999)