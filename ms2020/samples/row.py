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

def align(adjust_for_mission=0):
    shared_all.turn_to_direction( gyro=gyro, target_angle=10+ adjust_for_mission)


#     shared_all.move_straight(distance_mm=170, speed_mm_s=120)
#     shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
#         stop_on_color=Color.WHITE, alternative_color=Color.WHITE,
#          min_intensity=robot_setup.WHITE_MIN_INTENSITY[color_sensor_center],
#          max_distance_mm=110)
    
#     shared_all.move_straight_target_direction(gyro = gyro, 
#                 distance_mm= 220, 
#                 speed_mm_s= 140, 
#                 target_angle= -90+ adjust_for_mission)

#     shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)


def shake():
    shared_all.move_straight(distance_mm=10, speed_mm_s=20)

    left_motor.run_angle( 120,  30, Stop.BRAKE, True)
    shared_all.move_rack_to_floor()

    shared_all.move_straight(distance_mm=10, speed_mm_s=-20)
    right_motor.run_angle( 120,  30, Stop.BRAKE, True)
    shared_all.move_rack_to_floor(release_angle=0)

    shared_all.move_straight(distance_mm=10, speed_mm_s=-120)
    shared_all.move_rack_to_floor(release_angle=0)


def run(adjust_for_mission=0):
#     shared_all.turn_to_direction( gyro=gyro, target_angle=10)
    shared_all.move_rack_to_floor()
    shake()

    #pull bsck
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=-120, robot_turn_angle=-10, 
            motor=rack_motor, crane_angle=-40)
    #release
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=5, robot_turn_angle=0, 
            motor=rack_motor, crane_angle=15)
    shared_all.move_crane_up(rack_motor, 180)
    shared_all.move_rack_to_top()


## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
# shared_all.calibrate_gyro(0)
# align()
# run()

#### Old code ###############
def alignatangle(adjust_for_mission=0):
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 170, 
        speed_mm_s= 130, 
        target_angle= -130+ adjust_for_mission)
    shared_all.turn(angle=110, speed_deg_s=190)
    shared_all.turn_to_direction( gyro=gyro, target_angle=10+ adjust_for_mission)


def align_color_and_rightturns(adjust_for_mission=0):
    shared_all.move_straight(distance_mm=170, speed_mm_s=120)
    shared_all.move_straight_target_direction(gyro = gyro, 
        distance_mm= 80, 
        speed_mm_s= -140, 
        target_angle= -90+ adjust_for_mission)
    shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
        stop_on_color=Color.WHITE, alternative_color=Color.WHITE,
         min_intensity=robot_setup.WHITE_MIN_INTENSITY[color_sensor_center],
         max_distance_mm=110)
    
    shared_all.move_straight_target_direction(gyro = gyro, 
                distance_mm= 220, 
                speed_mm_s= 140, 
                target_angle= -90+ adjust_for_mission)

    shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)

def alignold(adjust_for_mission=0):
        shared_all.move_straight(distance_mm=180, speed_mm_s=150)
        shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)
        shared_all.move_to_color(color_sensor=color_sensor_center,
                stop_on_color=Color.BLACK, alternative_color=Color.BLACK)
        shared_all.move_straight(distance_mm=20, speed_mm_s=120)

def runold(adjust_for_mission=0):
    shared_all.turn_to_direction( gyro=gyro, target_angle=-37+ adjust_for_mission)
    shared_all.move_rack_to_floor()
    shake()
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=-80, robot_turn_angle=-20, 
            motor=rack_motor, crane_angle=-5)
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=25, robot_turn_angle=-50, 
            motor=rack_motor, crane_angle=-5)
    shared_all.turn(8)        
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=-10, robot_turn_angle=0, 
            motor=rack_motor, crane_angle=110)


def aligntonorth(adjust_for_mission=0):

        shared_all.turn_arc(distance=150, angle=-45, speed_mm_s=170)
        shared_all.turn_arc(distance=150, angle=45, speed_mm_s=170)

        shared_all.move_straight_target_direction(gyro = gyro, 
                distance_mm= 20, 
                speed_mm_s= 110, 
                target_angle= -90+ adjust_for_mission)
        shared_all.turn_to_direction( gyro=gyro, target_angle=0+ adjust_for_mission)
        shared_all.move_to_color_reverse(color_sensor=color_sensor_center,
                stop_on_color=Color.GREEN, alternative_color=Color.GREEN)
        shared_all.move_to_color(color_sensor=color_sensor_center,
                stop_on_color=Color.BLUE, alternative_color=Color.BLUE)
        shared_all.move_straight(distance_mm=10, speed_mm_s=-80)


def runfacingnorth():
    shared_all.move_rack_to_floor()
    shake()
    shared_all.drive_raising_crane(duration_ms=1900, robot_distance_mm=10, robot_turn_angle=-70, 
            motor=rack_motor, crane_angle=-15)

# brick.light(Color.YELLOW)
# runfacingnorth()
