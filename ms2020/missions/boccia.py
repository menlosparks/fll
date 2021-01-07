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

def align():
    # shared_all.move_straight(distance_mm=940, speed_mm_s=300)
    shared_all.calibrate_gyro(new_gyro_angle=-45)
    shared_all.move_straight_target_direction(gyro=gyro, distance_mm=1000, speed_mm_s=300, target_angle=-45)

def run():
    shared_all.move_crane_to_floor(motor=crane_motor)
    shared_all.move_crane_up(motor=crane_motor, degrees=60 )
    # shared_all.move_crane_down(motor=crane_motor, degrees=30)
    shared_all.move_straight(distance_mm=1080, speed_mm_s=-300)



## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
# shared_all.calibrate_gyro(-45) 
# align()
# run()

# def move_straight(duration, speed_mm_s):
#     robot.drive_time(speed_mm_s, 0, duration)
#     robot.stop(stop_type=Stop.BRAKE)
# move_straight(duration=3000, speed_mm_s=300)

# crane_motor=Motor(Port.D, Direction.COUNTERCLOCKWISE, [8,24])

# def move_crane_down( crane_motor, degrees):
#    crane_motor.run_angle(90,    -1 * degrees, Stop.BRAKE)
 
# move_crane_down(crane_motor, 30)