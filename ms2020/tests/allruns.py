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
sys.path.append('../bus')
sys.path.append('../missions')
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
import bench, basket 
import slide, stepcounter, treadmill,row, weight, phone
import boccia as boccia
import bus_service_1, bus_service_2
import  Arnav_Bus as ArnavBus

def deepsweep():
        
    shared_all.calibrate_gyro(180)

    shared_all.log_string('bus_service_1.base_to_treadmill()')
    bus_service_1.base_to_treadmill()
    shared_all.log_string('treadmill.align()')
    treadmill.align()
    shared_all.log_string('treadmill.run()')
    treadmill.run()

                    # shared_all.log_string('bus_service_1.treadmill_to_row()')
                    # bus_service_1.treadmill_to_row()
                    # shared_all.log_string('row.align()')
                    # row.align()
                    # shared_all.log_string('row.run()')
                    # row.run()

    shared_all.log_string('bus_service_1.treadmill_to_weight()')
    bus_service_1.treadmill_to_weight()
    shared_all.log_string('weight.align()')
    weight.align()
    shared_all.log_string('weight.run()')
    weight.run()

    shared_all.log_string('bus_service_1.weight_to_phone()')
    bus_service_1.weight_to_phone()
    shared_all.log_string('phone.align()')
    phone.align()
    shared_all.log_string('phone.run()')
    phone.run()

    ArnavBus.boccia_slide_to_home()


def benchrun():
    shared_all.calibrate_gyro(-85)

    bus_service_2.base_to_bench()
    bench.align()
    bench.run()
    bus_service_2.bench_to_loading()
    bus_service_2.base_to_bench()
    bench.drop_cubes()
    bus_service_2.bench_to_base()


def innov_basket():
    shared_all.calibrate_gyro(-90)

    bus_service_2.base_to_innov()
    bus_service_2.innov_to_basket()
    basket.align()
    basket.run()
    bus_service_2.basket_to_base()

def sliderun():
    shared_all.calibrate_gyro(new_gyro_angle=-45)
    slide.alignfacing()
    slide.runfacing()


def bocciarun():
    shared_all.calibrate_gyro(-45)
    boccia.align()
    boccia.run()
    
def lastbow():
    shared_all.calibrate_gyro(0)
    bus_service_1.base_to_stepcounter()
    stepcounter.run()


while True:
    buttons = shared_all.any_button_pressed()

    shared_all.log_string('Button pressed ' + str(buttons))
    if  Button.UP in buttons: ## BUT 1
        bocciarun()
    if Button.RIGHT in buttons: ## BUT 2
        benchrun()
    if  Button.DOWN in buttons: ## BUT 3
        innov_basket()
    if Button.LEFT in buttons: ## button 4
        sliderun()

    if Button.CENTER in buttons: ## button center
        buttons = shared_all.any_button_pressed(waiting_color=Color.YELLOW)

        if  Button.UP in buttons: ## BUT 1
            deepsweep()
        if Button.RIGHT in buttons: ## BUT 2
            lastbow()


        
    

