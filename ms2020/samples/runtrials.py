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
shared_all.calibrate_gyro()

INITIAL_ANGLE=0
adjust_for_mission=0 - INITIAL_ANGLE


# bus_service_1.base_to_stepcounter()
# stepcounter.step()
# bus_service_1.stepcounter_to_treadmill()
# bus_service_1.align_for_treadmill()
# treadmill.treadon(adjust_for_mission)

# bus_service_1.treadmill_to_row(adjust_for_mission)
# shared_all.push_back_reset_gyro(distance_mm = 80, new_gyro_angle =0 )
adjust_for_mission=90
bus_service_1.align_to_row(adjust_for_mission)


row.row(adjust_for_mission)
# bus_service_1.push_tires(adjust_for_mission)

# bus_service_1.row_to_weight(adjust_for_mission)
# bus_service_1.align_to_weight(adjust_for_mission)
# bus_service_1.weight.raise_weight(adjust_for_mission)
# shared_all.push_back_reset_gyro(distance_mm = 60, new_gyro_angle =0 )
adjust_for_mission=180

# bus_service_1.weight_to_phone(adjust_for_mission)
# bus_service_1.align_to_phone(adjust_for_mission)
# flip.shift_phone(adjust_for_mission)
# flip.flip_small()
# bus_service_1.phone_to_bigtire()
# flip.flip_bigt()

# bus_service_1.bigtire_to_slide()
# bus_service_1.align_to_slide()
# slide.slide()
# slide.take_slide_to_home()
