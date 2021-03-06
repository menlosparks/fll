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

# shared_all.calibrate_gyro(0)
# shared_all.move_reverse(max_distance=20)
# shared_all.log_string('Gyr ang ' +str(gyro.angle()) )
# for x in range(20):
#     gyro.angle()
# shared_all.log_string('Aft 10 meas Gyr ang ' +str(gyro.angle()) )

# shared_all.log_string('Stright 40cm to 90 and back ' )

shared_all.move_straight_target_direction(gyro=gyro,
    distance_mm=1290, speed_mm_s=160, target_angle=0)


# wait(3000)
# shared_all.log_string('Aft strg Gyr ang ' +str(gyro.angle()) )

# shared_all.turn_to_direction(gyro, target_angle=60)
# wait(3000)
# shared_all.move_straight_target_direction(gyro=gyro,
#     distance_mm=150, speed_mm_s=160, target_angle=90)

# shared_all.log_string('Aft 90 Gyr ang ' +str(gyro.angle()) )


# wait(3000)
# shared_all.move_straight_target_direction(gyro=gyro,
#     distance_mm=150, speed_mm_s=160, target_angle=-90)
# shared_all.log_string('Aft uturn Gyr ang ' +str(gyro.angle()) )
# wait(3000)
# shared_all.move_straight_target_direction(gyro=gyro,
#     distance_mm=150, speed_mm_s=-160, target_angle=0)
# shared_all.log_string('Aft rev Gyr ang ' +str(gyro.angle()) )

