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
from robot_setup import WHITE_MIN_INTENSITY
from robot_setup import BLACK_MAX_INTENSITY
 
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
import utime 

shared_all.calibrate_gyro(0)
time1=utime.ticks_ms()
for x in range(10):
    gyro.angle()

time2=utime.ticks_ms()
for x in range(10):
    a=time1+1

time3=utime.ticks_ms()
for x in range(10):
    a = color_sensor_center.color()
time4=utime.ticks_ms()
for x in range(10):
    a = color_sensor_center.reflection()
time5=utime.ticks_ms()
for x in range(10):
    shared_all.log_string('Log it s '+ str(time5) + ' ' + str(time4))
time6=utime.ticks_ms()

shared_all.log_string('Time for 10 angle reads '+ str(utime.ticks_diff(time2, time1)))
shared_all.log_string('Time for 10 adds '+ str(utime.ticks_diff(time3, time2)))
shared_all.log_string('Time for 10 color reads '+ str(utime.ticks_diff(time4, time3)))
shared_all.log_string('Time for 10 intensity reads '+ str(utime.ticks_diff(time5, time4)))
shared_all.log_string('Time for 10 logs '+ str(utime.ticks_diff(time6, time5)))

shared_all.move_reverse(max_distance=20)

shared_all.log_string('Stright 40cm to 0 and back')


shared_all.move_straight_target_direction(gyro=gyro,
    distance_mm=400, speed_mm_s=160, target_angle=10)
wait(3000)
shared_all.move_straight_target_direction(gyro=gyro,
    distance_mm=400, speed_mm_s=-160, target_angle=0)


wait(3000)
shared_all.move_straight_target_direction(gyro=gyro,
    distance_mm=150, speed_mm_s=160, target_angle=90)
wait(3000)
shared_all.move_straight_target_direction(gyro=gyro,
    distance_mm=150, speed_mm_s=160, target_angle=-90)
