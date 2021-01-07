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
sys.path.append('../bus')
sys.path.append('../missions')
import robot_setup
import shared_all
import adhya_bus
import Arnav_Bus
import ArjunBus
import cell_phone
import weight_machine, black_tire, tread
import row_machine

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

def execute():
     # Must always calib rate gyro
    shared_all.calibrate_gyro(180)

    ArjunBus.basetotread()
    tread.align()
    tread.run()

    weight_machine.tread_to_weight()
    weight_machine.align()
    weight_machine.run()

    # adhya_bus.tread_to_row()
    # row_machine.align()
    
    # adhya_bus.row_to_weight()
    # weight_machine.align()

    adhya_bus.weight_to_cell()
    cell_phone.align()

    adhya_bus.cell_to_black()
    black_tire.align()

    # Arnav_Bus.black_to_bocciaslide()
    # bocciaslide.run()

    



## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
# execute()
