#!/usr/bin/env pybricks-micropython
import sys
import os
import inspect
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor

sys.path.append('../shared')
 
import robot_setup

from robot_setup import robot
from robot_setup import left_motor
from robot_setup import right_motor
from robot_setup import WHEEL_DIAMETER_MM
from robot_setup import AXLE_TRACK_MM
from robot_setup import WHEEL_CIRCUM_MM
from robot_setup import DEGREES_PER_MM

##### Do not change above this line ##########################################
def move_straight (distance_mm, speed_mm_s):
    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    robot.drive(speed_mm_s, 0)
    print ('done1')
    wait(2700)
    robot.stop(stop_type=Stop.BRAKE)

move_straight(
distance_mm=2700,
speed_mm_s=300,)

    