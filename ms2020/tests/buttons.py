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
sys.path.append('../samples')
import robot_setup
 
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
from robot_setup import ultrasound
 
from robot_setup import SOUND_VOLUME
from robot_setup import WHEEL_DIAMETER_MM
from robot_setup import AXLE_TRACK_MM
from robot_setup import SENSOR_TO_AXLE
from robot_setup import WHEEL_CIRCUM_MM
from robot_setup import DEGREES_PER_MM
 
import shared_all

##### Do not change above this line ##########################################

shared_all.log_string('Buttons LEFT_DOWN ' + str(Button.LEFT_DOWN))
shared_all.log_string('Buttons DOWN ' + str(Button.DOWN))
shared_all.log_string('Buttons RIGHT_DOWN ' + str(Button.RIGHT_DOWN))
shared_all.log_string('Buttons LEFT ' + str(Button.LEFT))
shared_all.log_string('Buttons CENTER ' + str(Button.CENTER))
shared_all.log_string('Buttons RIGHT ' + str(Button.RIGHT))
shared_all.log_string('Buttons LEFT_UP ' + str(Button.LEFT_UP))
shared_all.log_string('Buttons UP ' + str(Button.UP))
shared_all.log_string('Buttons BEACON ' + str(Button.BEACON))
shared_all.log_string('Buttons RIGHT_UP ' + str(Button.RIGHT_UP))

while True:
    buttons = shared_all.any_button_pressed()

    shared_all.log_string('Button pressed ' + str(buttons))
    if Button.LEFT in buttons:
        shared_all.turn_arc(distance=15, angle=-90, speed_mm_s=130)
    if Button.RIGHT in buttons:
        shared_all.turn_arc(distance=15, angle=90, speed_mm_s=130)
    if  Button.UP in buttons:
        shared_all.move_straight(distance_mm=200, speed_mm_s=180)
    if  Button.DOWN in buttons:
        shared_all.move_straight(distance_mm=200, speed_mm_s=-180)

