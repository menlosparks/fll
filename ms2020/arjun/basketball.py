#!/usr/bin/env pybricks-micropython
import sys
import os
import inspect
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
from robot_setup import crane_motor
from robot_setup import robot
from robot_setup import WHEEL_DIAMETER_MM
from robot_setup import AXLE_TRACK_MM
from robot_setup import WHEEL_CIRCUM_MM
from robot_setup import DEGREES_PER_MM
DEFAULT_SPEED=300
##### Do not change above this line ##########################################
def move_rack_up( rack_motor, degrees):
    log_string('Angle at start ' + str(rack_motor.angle()))
    wait(100)
    rack_motor.run_angle(90,  degrees, Stop.BRAKE)
    log_string('Angle at end ' + str(rack_motor.angle()))

def move_rack_to_top( rack_motor):
    rack_motor.run_until_stalled(180, Stop.COAST, 50)
    move_rack_up( rack_motor, degrees = 5)

def log_string(message):
    print(message)
    brick.display.text(message)

def move_crane_up( crane_motor, degrees):
    log_string('Angle at start ' + str(crane_motor.angle()))
    wait(100)
    crane_motor.run_angle(90,  degrees, Stop.BRAKE)
    log_string('Angle at end ' + str(crane_motor.angle()))

def move_crane_down( crane_motor, degrees):
    log_string('Down Angle at start ' + str(crane_motor.angle()))
    wait(100)
    crane_motor.run_angle(90,  -1 * degrees)
    log_string('down Angle at end ' + str(crane_motor.angle()))

def move_crane_to_floor( crane_motor):
    crane_motor.run_until_stalled(-180, Stop.COAST, 50)
    
def move_crane_to_top( crane_motor):
    crane_motor.run_until_stalled(180, Stop.COAST, 50)
    
def move_reverse(
    max_distance, 
    speed_mm_s = DEFAULT_SPEED):
    move_straight( -1 * max_distance, speed_mm_s)

def move_straight(max_distance, speed_mm_s = DEFAULT_SPEED):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    log_string('Move stratight at speed '+ str(speed_mm_s) + ' dist ' + str(max_distance))
    duration = abs(int(1000 * max_distance / speed_mm_s))
    robot.drive_time(speed_mm_s, 0, duration)
    robot.stop(stop_type=Stop.BRAKE)

def turn( angle, speed_mm_s = DEFAULT_SPEED):

    if angle > 0:    # right turns are a bit under-steered
        angle = int(1.1 * angle)
    else:
        angle = int(angle / 1)

    robot.drive_time(0, angle, 1000)
    robot.stop(stop_type=Stop.BRAKE)




move_crane_to_floor( crane_motor)
wait(10)
move_straight(max_distance=100, speed_mm_s=-300)
wait(1000)
move_crane_down(crane_motor, degrees=45)
wait(10)
move_straight(max_distance=100, speed_mm_s=300)
move_crane_to_top(crane_motor)
wait(10)
turn(270)
move_rack_to_top( rack_motor)

    
