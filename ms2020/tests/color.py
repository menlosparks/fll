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

def print_colors():
    shared_all.log_string(
            # 'Bk:(' + str(color_sensor_back.color()) + ' ' + str(color_sensor_back.reflection())  
            #  +  ' ' + str(color_sensor_back.ambient()) + ')'
            #  + 
             ' Cent:(' + str(color_sensor_center.color()) + ' ' + str(color_sensor_center.reflection())  
             +  ' ' + str(color_sensor_center.ambient()) + ')'
             + ' Rt:(' + str(color_sensor_right.color()) + ' ' + str(color_sensor_right.reflection())
             +  ' ' + str(color_sensor_right.ambient()) + ')'  
            )


def color_test(distance_mm, speed_mm_s):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        print_colors()
        robot.drive(speed_mm_s, 0)
        wait(200)

    robot.stop(stop_type=Stop.BRAKE)
    print_colors()

color_test( distance_mm=100, speed_mm_s=30)
wait(999999)


# Low abient light
# ----------
# Cent:6(38)am=2) Rt:7(20) am=12)
# Cent:6(38)am=1) Rt:7(20) am=0)
# Cent:6(38)am=2) Rt:6(58) am=3)
# Cent:6(36)am=2) Rt:1(5) am=0)
# Cent:6(96)am=6) Rt:6(58) am=3)
# Cent:6(12)am=0) Rt:6(21) am=0)
# Cent:6(59)am=4) Rt:7(20) am=0)

# Low abient light(2)

# Cent:4(36)am=2) Rt:7(19) am=0)
# Cent:6(35)am=1) Rt:1(19) am=1)
# Cent:4(38)am=1) Rt:1(55) am=2)
# Cent:4(37)am=2) Rt:6(5) am=12)
# Cent:6(96)am=6) Rt:6(53) am=2)
# Cent:1(23)am=1) Rt:6(54) am=2)
# Cent:1(22)am=0) Rt:7(19) am=0)


# Strong ambient light
# ----------
# Cent:4(36)am=1) Rt:1(19) am=0)
# Cent:4(36)am=1) Rt:7(20) am=0)
# Cent:6(38)am=1) Rt:6(56) am=3)
# Cent:6(35)am=1) Rt:1(6) am=0)
# Cent:4(36)am=5) Rt:4(52) am=2)
# Cent:4(22)am=1) Rt:6(53) am=3)
# Cent:1(19)am=1) Rt:7(19) am=0)

