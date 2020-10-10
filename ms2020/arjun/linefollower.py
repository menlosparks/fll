#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
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

##### Do not change above this line ##########################################
 

def follow_line_border(
    color_sensor,
    distance_mm,
    speed_mm_s):

    

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    target_intensity = color_sensor.reflection()

    # Keep moving till the angle of the left motor reaches target
    while (abs(left_motor.angle()) < abs(motor_target_angle)):

        darkness = target_intensity - color_sensor.reflection()
        if color_sensor.color() == Color.WHITE:
            robot.drive(speed_mm_s, 0)
        elif color_sensor.color() == Color.BLACK:
            robot.drive(speed_mm_s, 0.5 * abs(darkness))
        else :
            robot.drive(speed_mm_s,  -0.5 * abs(darkness))

        wait(50)

    robot.stop(stop_type=Stop.BRAKE)

follow_line_border(
        color_sensor=color_sensor_center,
        distance_mm=650,
        speed_mm_s=150)