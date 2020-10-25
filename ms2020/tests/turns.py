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


import bus_service_1
import bus_service_2
import stepcounter
import treadmill
import row
import flip
import weight
import slide
import bench
import basket



def turn_arc_rev_90():
    shared_all.log_string('Arc reverse turns 90 deg 12 cm')
    shared_all.turn_arc(distance  =120 ,angle =90 , speed_mm_s=-130)
    wait(2000)
    shared_all.turn_arc(distance  =120 ,angle =-90 , speed_mm_s=-130)
    wait(2000)

def turn_arc_90():

    shared_all.log_string('Arc turns 90 deg 12 cm')
    shared_all.turn_arc(distance  =120 ,angle =90 , speed_mm_s=130)
    wait(2000)
    shared_all.turn_arc(distance  =120 ,angle =-90 , speed_mm_s=130)
    wait(2000)

def turn_smallarc_90():
    shared_all.turn_arc(distance  =50 ,angle =90 , speed_mm_s=130)
    wait(2000)
    shared_all.turn_arc(distance  =50 ,angle =-90 , speed_mm_s=130)
    wait(2000)

def turn_points_90():
    shared_all.move_straight(distance_mm=90, speed_mm_s=140)
    shared_all.turn(110, 190)
    wait(2000)
    shared_all.turn(-110, 190)
    wait(2000)
    shared_all.turn(90)

    wait(3000)
    shared_all.turn(-90)

#BUtton 1: Rev arc 90  BUt 2:
while True:
    buttons = shared_all.any_button_pressed()

    shared_all.log_string('Button pressed ' + str(buttons))
    if Button.UP in buttons: ## but 1
        turn_arc_rev_90()
    if Button.RIGHT in buttons: ## but 2
        turn_arc_90()
    if  Button.DOWN in buttons: ## but 3
        turn_smallarc_90()
    if  Button.LEFT in buttons: ## but 4
        turn_points_90()
    if  Button.CENTER in buttons: ## but 5
        turn_arc_rev_90()
        turn_arc_90()
        turn_smallarc_90()
        turn_points_90()

