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

from robot_setup import left_motor
from robot_setup import right_motor
from robot_setup import robot
#from robot_setup import rack_motor
#from robot_setup import crane_motor
#from robot_setup import gyro
#from robot_setup import touch_sensor 
#from robot_setup import color_sensor_left
#from robot_setup import color_sensor_right
#from robot_setup import color_sensor_center
#from robot_setup import touch_sensor

#from robot_setup import SOUND_VOLUME
#from robot_setup import WHEEL_DIAMETER_MM
#from robot_setup import AXLE_TRACK_MM
#from robot_setup import SENSOR_TO_AXLE
#from robot_setup import WHEEL_CIRCUM_MM
from robot_setup import DEGREES_PER_MM
DEFAULT_SPEED=300
##### Do not change above this line ##########################################
def move_straight (distance_mm, speed_mm_s):
    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    robot.drive(speed_mm_s, 0)
    print ('done')

def turn( angle, speed_mm_s = DEFAULT_SPEED):

    if angle > 0:    # right turns are a bit under-steered
        angle = int(1.1 * angle)
    else:
        angle = int(angle / 1)

    robot.drive_time(0, angle, 1000)
    robot.stop(stop_type=Stop.BRAKE)

#move_straight(
#distance_mm=500,
#speed_mm_s=300,)
#wait(1000)
#robot.stop(stop_type=Stop.BRAKE)


turn(270)