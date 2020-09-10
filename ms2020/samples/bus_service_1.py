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

def base_to_stepcounter():
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=560, 
        speed_mm_s=150, 
        target_angle=0)

def stepcounter_to_treadmill():

    shared_all.turn( angle=-45)
    shared_all.turn_arc(distance=310,angle=45, speed_mm_s=150) # turn in an arc

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=170, 
            speed_mm_s=150, 
            target_angle=0)


def align_for_treadmill():

    #### go to pink and move back 3 cm
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

    #####shared_all.move_straight(distance_mm=20, speed_mm_s=70)

    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=90)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW, speed_mm_s=25)

    ###### shared_all.move_straight(distance_mm=10, speed_mm_s=90)

    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=110, 
            speed_mm_s=-100, 
            target_angle=180)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180)

def treadmill_to_flip():
    shared_all.turn_arc(distance=80,angle=45, speed_mm_s=100) # turn in an arc
    shared_all.turn_arc(distance=80,angle=-45, speed_mm_s=100) # turn in an arc
    shared_all.move_straight(distance_mm=100, speed_mm_s=-90)

    shared_all.move_to_color_reverse(color_sensor=color_sensor_right,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight(distance_mm=130, speed_mm_s=150)
    shared_all.turn(-90)
    shared_all.turn_to_direction( gyro=gyro,
    ####  Change yo 90
       target_angle=     -90)

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=250, 
            speed_mm_s=-100, 
            ####  Change yo 90
            target_angle=     -90)
    shared_all.turn(70)
    shared_all.move_straight(distance_mm=30, speed_mm_s=-100)




def treadmill_to_row():
    shared_all.move_straight(distance_mm=100, speed_mm_s=130)
    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + ADJUST_FOR_MISSION)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)

    shared_all.move_straight(distance_mm=100, speed_mm_s=130)
    shared_all.turn(-90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180 + ADJUST_FOR_MISSION)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)


    shared_all.move_straight(distance_mm=100, speed_mm_s=130)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180 + ADJUST_FOR_MISSION)

    shared_all.turn(90)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=100, 
            speed_mm_s=130, 
            target_angle= -90 + ADJUST_FOR_MISSION)

def align_to_row():
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.YELLOW, alternative_color=Color.YELLOW)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=100, 
            speed_mm_s=130, 
            target_angle= -90 + ADJUST_FOR_MISSION)

    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=0 + ADJUST_FOR_MISSION)

    shared_all.move_to_color(color_sensor=color_sensor_right,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=40, 
            speed_mm_s=-70, 
            target_angle= 0 + ADJUST_FOR_MISSION)


def treadmill_to_rowold():
    shared_all.turn_arc(distance=70,angle=60, speed_mm_s=100) # turn in an arc
    shared_all.turn_arc(distance=70,angle=-60, speed_mm_s=100) # turn in an arc
    shared_all.move_straight(distance_mm=100, speed_mm_s=-90)

    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight(distance_mm=100, speed_mm_s=150)

    shared_all.turn(-90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=90 + ADJUST_FOR_MISSION)

    shared_all.move_to_color(color_sensor=color_sensor_right,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    # shared_all.move_to_color(color_sensor=color_sensor_center,
    #     stop_on_color=Color.RED, alternative_color=Color.YELLOW)
    # shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
    #     stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    # shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
    #     stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=165, 
            speed_mm_s=-100, 
            ####  Change yo 90
            target_angle=     90 + ADJUST_FOR_MISSION)

    shared_all.turn(-90)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=80, 
            speed_mm_s=-100, 
        ####  Change yo 0(final) (or 180)
        target_angle= 0 + ADJUST_FOR_MISSION)

def row_to_flip():


    shared_all.turn_arc(distance=30,angle=-60, speed_mm_s=100) # turn in an arc

    shared_all.move_straight(distance_mm=110, speed_mm_s=100)
    shared_all.turn(180)
    shared_all.move_straight(distance_mm=70, speed_mm_s=-100)

def push_tires():
    shared_all.turn_arc(distance=40,angle=-50, speed_mm_s=-100) # turn in an arc
    shared_all.turn_arc(distance=60,angle=-40, speed_mm_s=100) # turn in an arc


    shared_all.move_straight(distance_mm=130, speed_mm_s=-100)
    # shared_all.turn(-55)
    # shared_all.move_straight(distance_mm=150, speed_mm_s=-150)
    # shared_all.move_straight(distance_mm=150, speed_mm_s=120)


def row_to_weight():

    shared_all.turn_arc(distance=100,angle=30, speed_mm_s=100)
    shared_all.turn_arc(distance=120,angle=-45, speed_mm_s=100)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + ADJUST_FOR_MISSION) 



def align_to_weight():
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)

    shared_all.move_straight(distance_mm=120, speed_mm_s=130)
    shared_all.turn(-90)
    # shared_all.move_crane_to_top(crane_motor)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 130, 
        speed_mm_s= -300, 
        target_angle= 180 + ADJUST_FOR_MISSION)

    shared_all.move_to_color_reverse(color_sensor=color_sensor_right,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)


    shared_all.move_straight(distance_mm=30, speed_mm_s=-125)
    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + ADJUST_FOR_MISSION) 
    shared_all.move_straight(distance_mm=50, speed_mm_s=-140)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + ADJUST_FOR_MISSION) 

def weight_to_phone():
    shared_all.turn(-90)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 280, 
        speed_mm_s= 200, 
        target_angle= 180 + ADJUST_FOR_MISSION)

def align_to_phone():
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + ADJUST_FOR_MISSION) 
    ##### shared_all.move_straight(distance_mm=30, speed_mm_s=60)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 80, 
        speed_mm_s= 100, 
        target_angle= -90 + ADJUST_FOR_MISSION)
    shared_all.turn(-5)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-95 + ADJUST_FOR_MISSION) 



    # shared_all.turn(90)
    # shared_all.turn_to_direction( gyro=gyro, target_angle=-90 + ADJUST_FOR_MISSION) 

    # shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
    #     stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    # shared_all.move_straight(distance_mm=30, speed_mm_s=60)
       
    # shared_all.turn(-90)
    # shared_all.turn_to_direction( gyro=gyro, target_angle=180 + ADJUST_FOR_MISSION) 
    # shared_all.move_to_color(color_sensor=color_sensor_center,
    #     stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

def phone_to_bigtire():
    shared_all.move_straight(distance_mm=30, speed_mm_s=-100)
    shared_all.turn_arc(distance=170, angle = -90, speed_mm_s=-150)
    shared_all.move_straight(distance_mm=30, speed_mm_s=100)
    shared_all.turn_arc(distance=170, angle = 75, speed_mm_s=150)

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

def bigtire_to_slide():
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 300, 
        speed_mm_s= 200, 
        target_angle= 180 + ADJUST_FOR_MISSION)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 50, 
        speed_mm_s= 90, 
        target_angle= 180 + ADJUST_FOR_MISSION)
    shared_all.turn(-90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=90 + ADJUST_FOR_MISSION) 
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
 

def align_to_slide():
    shared_all.turn(-45)
    shared_all.move_straight(distance_mm=30, speed_mm_s=-60)
    shared_all.turn_to_direction( gyro=gyro, target_angle=135 + ADJUST_FOR_MISSION) 


def slide_to_bench():
    shared_all.turn(60)
    shared_all.turn_to_direction( gyro=gyro, target_angle=195 + ADJUST_FOR_MISSION) 
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 400, 
        speed_mm_s= 90, 
        target_angle= 195 + ADJUST_FOR_MISSION)



import stepcounter
import treadmill
import row
import flip
import weight
import slide
import bench
shared_all.calibrate_gyro()

INITIAL_ANGLE=-90
ADJUST_FOR_MISSION=0 - INITIAL_ANGLE


# base_to_stepcounter()
# stepcounter.step()
# stepcounter_to_treadmill()
# align_for_treadmill()
# treadmill.treadon(ADJUST_FOR_MISSION)


# treadmill_to_row()
# align_to_row()
# row.row()
# push_tires()

# row_to_weight()
# align_to_weight()
# weight.raise_weight()

weight_to_phone()
align_to_phone()
flip.shift_phone(ADJUST_FOR_MISSION)
# flip.flip_small()
# phone_to_bigtire()
# flip.do_flips_bigtire(ADJUST_FOR_MISSION)


# bigtire_to_slide()
# align_to_slide()
# slide.slide()

# slide_to_bench()


# bench.bench_knock_and_lift()

