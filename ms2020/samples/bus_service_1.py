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

def base_to_stepcounter(adjust_for_mission=0):
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm=550, 
        speed_mm_s=150, 
        target_angle=0)

def stepcounter_to_treadmill(adjust_for_mission=0):

    # shared_all.turn( angle=-45)
    shared_all.turn_arc(distance=200,angle=-65, speed_mm_s=150) # turn in an arc
    shared_all.turn_arc(distance=200,angle=65, speed_mm_s=150) # turn in an arc

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=160, 
            speed_mm_s=150, 
            target_angle=0)


def align_for_treadmill(adjust_for_mission=0):

    #### go to pink and move back 3 cm
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)


    # shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=90+ adjust_for_mission)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW, speed_mm_s=25)

    # shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=100, 
            speed_mm_s=-100, 
            target_angle=180+ adjust_for_mission)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180)

def treadmill_to_row(adjust_for_mission=0):

    shared_all.turn_arc(distance=120,angle=90, speed_mm_s=100) # turn in an arc

    shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)

def align_to_row(adjust_for_mission=0):

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=160, 
            speed_mm_s=110, 
            target_angle= -90+ adjust_for_mission)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=120, 
            speed_mm_s=130, 
            target_angle= 180+ adjust_for_mission)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=120, 
            speed_mm_s=130, 
            target_angle= -90+ adjust_for_mission)
    shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=100, 
            speed_mm_s=-90, 
            target_angle= 0+ adjust_for_mission)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLUE, alternative_color=Color.BLUE)
    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=60, 
            speed_mm_s=-90, 
            target_angle= 0+ adjust_for_mission)

def align_to_oldrow(adjust_for_mission=0):
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.YELLOW, alternative_color=Color.YELLOW)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=100, 
            speed_mm_s=130, 
            target_angle= -90+ adjust_for_mission)

    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)

    shared_all.move_to_color(color_sensor=color_sensor_right,
        stop_on_color=Color.RED, alternative_color=Color.YELLOW)

    shared_all.move_straight_target_direction(gyro = gyro, 
            distance_mm=40, 
            speed_mm_s=-70, 
            target_angle= 0+ adjust_for_mission)

def row_to_flip(adjust_for_mission=0):


    shared_all.turn_arc(distance=30,angle=-60, speed_mm_s=100) # turn in an arc

    shared_all.move_straight(distance_mm=110, speed_mm_s=100)
    shared_all.turn(180)
    shared_all.move_straight(distance_mm=70, speed_mm_s=-100)

def push_tires(adjust_for_mission=0):
    shared_all.turn_arc(distance=40,angle=-50, speed_mm_s=-100) # turn in an arc
    shared_all.turn_arc(distance=60,angle=-40, speed_mm_s=100) # turn in an arc
    shared_all.move_straight(distance_mm=130, speed_mm_s=-100)

def row_to_weight(adjust_for_mission=0):

    shared_all.turn_arc(distance=90,angle=40, speed_mm_s=100)
    shared_all.turn_arc(distance=110,angle=-55, speed_mm_s=100)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission) 



def align_to_weight(adjust_for_mission=0):
    shared_all.move_crane_to_top(rack_motor)

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE)

    shared_all.move_straight(distance_mm=120, speed_mm_s=130)
    shared_all.turn(-90)
    # shared_all.move_crane_to_top(crane_motor)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 130, 
        speed_mm_s= -150, 
        target_angle= 180+ adjust_for_mission)

    shared_all.move_to_color_reverse(color_sensor=color_sensor_right,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)


    shared_all.move_straight(distance_mm=30, speed_mm_s=-130)
    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission) 
    shared_all.move_straight(distance_mm=50, speed_mm_s=-140)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission) 

def weight_to_phone(adjust_for_mission=0):
    shared_all.turn(-90)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 280, 
        speed_mm_s= 180, 
        target_angle= 180+ adjust_for_mission)

def align_to_phone(adjust_for_mission=0):
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-90+ adjust_for_mission) 

    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 80, 
        speed_mm_s= 100, 
        target_angle= -90+ adjust_for_mission)
    shared_all.turn(-5)
    shared_all.turn_to_direction( gyro=gyro, target_angle=-95+ adjust_for_mission) 


def phone_to_bigtire(adjust_for_mission=0):
    # shared_all.move_straight(distance_mm=30, speed_mm_s=-100)
    shared_all.turn_arc(distance=70, angle = 100, speed_mm_s=-150)
    shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission) 
    shared_all.move_straight(distance_mm=170, speed_mm_s=-160)
    shared_all.turn_arc(distance=60, angle = 80, speed_mm_s=150)

    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.GREEN, alternative_color=Color.GREEN)
    shared_all.move_straight(distance_mm=110, speed_mm_s=-160)

def bigtire_to_slide(adjust_for_mission=0):
    shared_all.move_straight(distance_mm=40, speed_mm_s=-100)
    shared_all.turn_arc(distance=30, angle = 30, speed_mm_s=-130)
    shared_all.turn_to_direction( gyro=gyro, target_angle=90+ adjust_for_mission) 

def align_to_slide(adjust_for_mission=0):
    shared_all.move_to_color_reverse(color_sensor=color_sensor_right,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)


    shared_all.turn(90)
    shared_all.turn_to_direction( gyro=gyro, target_angle=180+ adjust_for_mission) 
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 130, 
        speed_mm_s= 200, 
        target_angle= 180+ adjust_for_mission)


    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
    shared_all.move_straight(distance_mm=110, speed_mm_s=80)

    shared_all.turn(-30)
    shared_all.move_straight(distance_mm=110, speed_mm_s=-100)
    shared_all.turn_to_direction( gyro=gyro, target_angle=150+ adjust_for_mission) 



def slide_to_bench(adjust_for_mission=0):
    shared_all.turn(60)
    shared_all.turn_to_direction( gyro=gyro, target_angle=195+ adjust_for_mission) 
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 400, 
        speed_mm_s= 90, 
        target_angle= 195+ adjust_for_mission)



# import stepcounter
# import treadmill
# import row
# import flip
# import weight
# import slide
# import bench
# shared_all.calibrate_gyro()

# INITIAL_ANGLE=180
# adjust_for_mission=0 - INITIAL_ANGLE
# adjust_for_mission=adjust_for_mission

# base_to_stepcounter()
# stepcounter.step()
# stepcounter_to_treadmill()
# align_for_treadmill()
# treadmill.treadon(adjust_for_mission)


# treadmill_to_row()
# ####### align_to_row()
# row.row()
# push_tires()

# row_to_weight()
# align_to_weight()
# weight.raise_weight()

# weight_to_phone()
# align_to_phone()
# flip.shift_phone(adjust_for_mission)
# ################# flip.pull_phone_back()
# flip.flip_small()
# phone_to_bigtire()
# #################flip.do_flips_bigtire(adjust_for_mission)
# flip.flip_bigt()

# bigtire_to_slide()
# align_to_slide()
# slide.slide()
# slide.take_slide_to_home()
# slide_to_bench()


# bench.bench_knock_and_lift()

