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
sys.path.append('../missions')
sys.path.append('../bus')
import robot_setup
import boccia
import bench
import shared_all
import basketball
import slide
import long_run
import innov
import ArjunBus 

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

while True:
    buttons = shared_all.any_button_pressed(waiting_color=Color.RED)
    if Button.UP in buttons:
        boccia.align()
        boccia.run()
    if Button.RIGHT in buttons:
        bench.align()
        bench.run()
    if Button.DOWN in buttons:
        innov.hometoinnov()
        ArjunBus.inovtobball()
        basketball.align()
        basketball.run()
    if Button.LEFT in buttons:
        # slide.align()
        slide.run()
    if Button.CENTER in buttons:
        buttons = shared_all.any_button_pressed(waiting_color=Color.YELLOW)
        if Button.UP in buttons:
            long_run.execute()
