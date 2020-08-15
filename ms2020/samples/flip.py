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
 
##### Do not change above this line ##########################################
import testcode
def flip_small():
    testcode.move_crane_to_floor(crane_motor)
    testcode.move_straight(distance_mm=30, speed_mm_s=60)
    testcode.drive_raising_crane(duration_ms=400, robot_distance_mm=20, robot_turn_angle=0, 
        crane_motor=crane_motor, crane_angle=80)

def flip_bigt():
    testcode.move_crane_to_floor(crane_motor)
    testcode.move_straight(distance_mm=50, speed_mm_s=50)
    left_motor.run_angle( 90,  8, Stop.BRAKE, True)
    right_motor.run_angle(90,  8, Stop.BRAKE, True)

    # wait(1000)
    testcode.drive_raising_crane(duration_ms=550, robot_distance_mm=50, robot_turn_angle=0, 
        crane_motor=crane_motor, crane_angle=100)
    # testcode.drive_raising_crane(duration_ms=400, robot_distance_mm=30, robot_turn_angle=0, 
    #     crane_motor=crane_motor, crane_angle=60)
    # testcode.drive_raising_crane(duration_ms=300, robot_distance_mm=30, robot_turn_angle=0, 
    #     crane_motor=crane_motor, crane_angle=60)
    testcode.drive_raising_crane(duration_ms=200, robot_distance_mm=30, robot_turn_angle=0, 
        crane_motor=crane_motor, crane_angle=20)

flip_small()
wait(6000)
flip_small()
wait(6000) 

flip_bigt()
