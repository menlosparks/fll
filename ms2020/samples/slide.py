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
 
##### Do not change above this line ##########################################

def align(adjust_for_mission=0):

    SLIDE_ALIGN_DIRECTION=138
    shared_all.turn(-90, speed_deg_s=140)
    shared_all.move_straight(distance_mm=50, speed_mm_s=100)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
         stop_on_color=Color.BLACK, alternative_color=Color.BLACK, speed_mm_s=60,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=80)
    shared_all.move_straight(distance_mm=70, speed_mm_s=-100)

    shared_all.turn(90, speed_deg_s=140)
    shared_all.move_to_color(color_sensor=color_sensor_center,
        stop_on_color=Color.BLACK, alternative_color=Color.BLACK, speed_mm_s=60,
         max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
         max_distance_mm=60)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 40, 
        speed_mm_s= 130, 
        target_angle= 180+ adjust_for_mission)
    shared_all.turn(SLIDE_ALIGN_DIRECTION - 180, speed_deg_s=100)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 60, 
        speed_mm_s= -110, 
        target_angle= SLIDE_ALIGN_DIRECTION+ adjust_for_mission)
    shared_all.move_rack_to_floor()




    # shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
    #     stop_on_color=Color.BLACK, alternative_color=Color.BLACK, speed_mm_s=25,
    #      max_intensity=robot_setup.BLACK_MAX_INTENSITY[color_sensor_center],
    #      max_distance_mm=60)

    # shared_all.move_straight(distance_mm=50, speed_mm_s=-100)
    # shared_all.move_straight_target_direction(gyro = gyro, 
    #     distance_mm= 130, 
    #     speed_mm_s= 180, 
    #     target_angle= 180+ adjust_for_mission)
    # shared_all.move_straight_target_direction(gyro = gyro, 
    #     distance_mm= 130, 
    #     speed_mm_s= 160, 
    #     target_angle= 180+ adjust_for_mission)


    # shared_all.move_to_color_reverse(color_sensor=color_sensor_right,
    #     stop_on_color=Color.BLACK, alternative_color=Color.BLACK)





def run():
    shared_all.move_rack_to_floor()
    # shared_all.move_crane_up( motor = rack_motor, degrees = 30)
    shared_all.move_straight(distance_mm=55, speed_mm_s=100)

    while shared_all.did_motor_stall(motor =rack_motor , max_degrees =30 , speed = 80):
        shared_all.log_string('Stalled')
        shared_all.move_straight(distance_mm=4, speed_mm_s=-20)

    shared_all.drive_raising_crane(duration_ms=400, robot_distance_mm=30, robot_turn_angle=0, 
        motor=rack_motor, crane_angle=75)

    shared_all.turn_arc(distance = 60 ,angle = -7 , speed_mm_s=100)


def take_slide_to_home():
    shared_all.turn_arc(distance = 90 ,angle = 50 , speed_mm_s=100)
    shared_all.turn_arc(distance = 160 ,angle = -90 , speed_mm_s=100)
    shared_all.move_rack_to_floor()

    shared_all.drive_raising_crane(duration_ms=2200, robot_distance_mm=400, robot_turn_angle=15, 
        motor=rack_motor, crane_angle=-15)


# slide() 

def alignfacing():
    shared_all.move_straight_target_direction(gyro=gyro,
    distance_mm=480, speed_mm_s=170, target_angle=-45)

    shared_all.move_to_color(color_sensor=color_sensor_center, 
    stop_on_color=Color.GREEN, max_distance_mm=40)

    shared_all.move_straight(distance_mm=40, speed_mm_s=40)

def runfacing():
    shared_all.move_crane_down(rack_motor, 70)
    shared_all.move_hook_to_floor()
    shared_all.move_straight(distance_mm=20, speed_mm_s=-50)

    shared_all.drive_raising_crane (duration_ms=800, robot_distance_mm=-30, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=20)
    shared_all.drive_raising_crane (duration_ms=1900, robot_distance_mm=-90, robot_turn_angle=0, 
                        motor=rack_motor, crane_angle=20)
    # shared_all.move_straight(distance_mm=40, speed_mm_s=130)
    shared_all.move_crane_up(rack_motor, 70)
   
# shared_all.calibrate_gyro(new_gyro_angle=-45)
# alignfacing()
runfacing()