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

def align():
   shared_all.move_straight(distance_mm=50, speed_mm_s=200)
   shared_all.turn(angle=90, speed_deg_s=200)
   shared_all.move_reverse(max_distance=65, speed_mm_s=75)
   shared_all.move_straight(distance_mm=450, speed_mm_s=175)
   shared_all.turn(angle=15, speed_deg_s=200)
   shared_all.turn_arc(distance=15,angle=15,speed_mm_s=50)
   shared_all.move_straight(distance_mm=138, speed_mm_s=200)
   

def run():
   shared_all.move_crane_to_top( motor=rack_motor, release_angle = 270)
   
   
## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
#shared_all.calibrate_gyro(0)

# align()
# run()
