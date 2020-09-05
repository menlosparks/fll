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
 
sys.path.append(os.path.abspath('../shared'))
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
 
from robot_setup import SOUND_VOLUME
from robot_setup import WHEEL_DIAMETER_MM
from robot_setup import AXLE_TRACK_MM
from robot_setup import SENSOR_TO_AXLE
from robot_setup import WHEEL_CIRCUM_MM
from robot_setup import DEGREES_PER_MM

# Get wheel circumference
WHEEL_CIRCUM_MM=3.149*89
# 360 degrees -> WHEEL_CIRCUM_MM so   1 degree -> ?
DEGREES_PER_MM=360/WHEEL_CIRCUM_MM

motor_target_angle = int(DEGREES_PER_MM * distance_mm)
left_motor.reset_angle(0)
while (abs(left_motor.angle()) < abs(motor_target_angle)):
    error = target_angle - gyro.angle()
    robot.drive(speed_mm_s, error)

Stop.BRAKE

