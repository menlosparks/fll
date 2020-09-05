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
 
##### Do not change above this line ##########################################


def move_crane_up( crane_motor, degrees):
   crane_motor.run_angle(90,  degrees, Stop.BRAKE)
 
def move_crane_down( crane_motor, degrees):
   crane_motor.run_angle(90,    -1 * degrees, Stop.BRAKE)

def move_crane_to_floor(crane_motor):
   crane_motor.run_until_stalled(-180, Stop.COAST, 35)
   move_crane_up( crane_motor, degrees = 5)

def move_crane_to_top(crane_motor):
    crane_motor.run_until_stalled(180, Stop.COAST, 35)
move_crane_to_floor(crane_motor)

robot.drive(100, 0)
