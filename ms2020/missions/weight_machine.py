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

def align():
   shared_all.move_straight(distance_mm=85, speed_mm_s=100)
   shared_all.move_crane_to_floor(motor=crane_motor)
   #shared_all.move_crane_to_top(motor=rack_motor)
   shared_all.move_crane_up(motor=crane_motor, degrees=50)
   shared_all.move_straight(distance_mm=20, speed_mm_s=100)
   
   

def run():
   shared_all.turn_arc(distance=20, angle=0, speed_mm_s=50)
   shared_all.move_crane_to_top(motor=crane_motor)
   shared_all.drive_raising_crane(duration_ms=500, robot_distance_mm=1, robot_turn_angle=0, 
   motor=crane_motor, crane_angle=120)
   shared_all.move_crane_to_floor(motor=crane_motor)
   
   
## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
shared_all.calibrate_gyro(0)

align()
run()