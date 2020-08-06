#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
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

##### Do not change above this line ##########################################

# def move_straight(duration, speed_mm_s):
#     robot.drive_time(speed_mm_s, 0, duration)
#     robot.stop(stop_type=Stop.BRAKE)

def log_string(message):
    print(message)
    brick.display.text(message)

def move_straight(distance_mm, speed_mm_s):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    # Keep moving till the angle of the left motor reaches target
    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        robot.drive(speed_mm_s, 0)
        wait(100)

    robot.stop(stop_type=Stop.BRAKE)

# move_straight(distance_mm=300, speed_mm_s=300)


def turn(angle):
    robot.drive_time(0, angle, 1000)


# turn(90)

def turn_arc(distance,angle):
    robot.drive_time(distance, angle, 1000)


# turn_arc(distance=200,angle=-120)


def drive_raising_crane(duration_ms, robot_distance_mm, robot_turn_angle, 
                        crane_motor, crane_angle):
    crane_angular_speed = int(1000 * crane_angle / duration_ms)
    turn_angular_speed_deg_s = abs(int(1000 * robot_turn_angle / duration_ms))
    forward_speed = int(1000 * robot_distance_mm / duration_ms) 
    robot.drive(forward_speed, turn_angular_speed_deg_s)
    crane_motor.run(crane_angular_speed)
    wait(duration_ms)
    crane_motor.stop(Stop.BRAKE)
    robot.stop(stop_type=Stop.BRAKE)

# drive_raising_crane(duration_ms=1000, 
#     robot_distance_mm=100, 
#     robot_turn_angle=30, 
#     crane_motor=crane_motor, 
#     crane_angle=-50)

def move_to_color(
    color_sensor,
    stop_on_color,
    speed_mm_s):
 
    robot.drive(speed_mm_s, 0)
    # Check if color reached.
    while color_sensor.color() != stop_on_color:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)


# move_to_color(color_sensor=color_sensor_center, stop_on_color=Color.BLACK, speed_mm_s=100)

# obstacle_sensor = UltrasonicSensor(Port.S4)

def move_to_obstacle(
    obstacle_sensor,
    stop_on_obstacle_at,
    speed_mm_s):

    robot.drive(speed_mm_s, 0)
    # Check if obstacle too close.
    while obstacle_sensor.distance() > stop_on_obstacle_at:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)
    
# move_to_obstacle(obstacle_sensor=obstacle_sensor, stop_on_obstacle_at=50, speed_mm_s=300)


def move_to_wall(touch_sensor, speed_mm_s):
    robot.drive(speed_mm_s, 0)
    # Check if touch sensore pressed.
    while touch_sensor.pressed() == False :
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)
       
# move_to_wall(touch_sensor=touch_sensor, speed_mm_s=100)


def calibrate_gyro(new_angle=0):
    current_speed=gyro.speed()
    current_angle=gyro.angle()
    wait(60)
    gyro.reset_angle(new_angle)
    wait(20)

def turn_to_angle( gyro, target_angle):

    error = target_angle - gyro.angle()
    while ( abs(error) >= 4):
        adj_angular_speed = error * 1.5
        robot.drive(0, adj_angular_speed)
        wait(100)
        error=target_angle - gyro.angle()

    robot.stop(stop_type=Stop.BRAKE)

# calibrate_gyro(new_angle=0)    
# turn_to_angle( gyro=gyro, target_angle=-65)
# move_straight(5000, 300)


 
def move_crane_up( crane_motor, degrees):
   crane_motor.run_angle(90,  degrees, Stop.BRAKE)
 
def move_crane_down( crane_motor, degrees):
   crane_motor.run_angle(90,    -1 * degrees, Stop.BRAKE)


# move_crane_up(crane_motor=crane_motor, degrees=120)
# move_crane_down(crane_motor=crane_motor, degrees=90)

def move_crane_to_floor(crane_motor):
   crane_motor.run_until_stalled(-360, Stop.COAST, 35)
   move_crane_up( crane_motor, degrees = 10)

def move_crane_to_top(crane_motor):
   crane_motor.run_until_stalled(360, Stop.COAST, 35)
   move_crane_down( crane_motor, degrees = 10)

# move_crane_to_floor(crane_motor)
# move_crane_to_top(crane_motor)


def turn_to_color(color_sensor, stop_on_color, angular_speed_deg_s):
 
    robot.drive(0, angular_speed_deg_s)
    # Check if color reached.
    while color_sensor.color() != stop_on_color:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)

# turn_to_color(color_sensor_left, Color.RED, 45)

def turn_to_color_right(color_sensor, stop_on_color, angular_speed_deg_s):
 
    robot.drive(0, angular_speed_deg_s)
    # Check if color reached.
    while color_sensor.color() != stop_on_color:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)

def turn_to_color_left(color_sensor, stop_on_color, angular_speed_deg_s):
 
    robot.drive(0, -1 * angular_speed_deg_s)
    # Check if color reached.
    while color_sensor.color() != stop_on_color:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)


# turn_to_color_left(color_sensor_center, Color.BLUE, 45)


# Used by line follower to align with the general direction of the line

def align_with_line_to_left(color_sensor, line_color):

    #Find left white border of line
    move_to_color( color_sensor, line_color, 300)
 
    #move forward half the length of tank and rotate
    move_straight( SENSOR_TO_AXLE, 300)    
    turn_to_color_right( color_sensor, line_color, 45) 

def align_with_line_to_right(color_sensor, line_color):

    #Find left white border of line
    move_to_color( color_sensor, line_color, 300)
 
    #move forward half the length of tank and rotate
    move_straight( SENSOR_TO_AXLE, 300)    
    turn_to_color_left( color_sensor, line_color, 45) 

# align_with_line_to_left(color_sensor_left, Color.BLACK)
# align_with_line_to_right(color_sensor_right, Color.BLACK)



def move_straight_target_direction(gyro, distance_mm, speed_mm_s, target_angle):

    turn_to_angle( gyro, target_angle)
    duration = abs(int(1000 * distance_mm / speed_mm_s))
    time_spent=0
    while (time_spent<duration):
        error = target_angle - gyro.angle()
        adj_angular_speed = error * 1.5
        robot.drive(speed_mm_s, adj_angular_speed)
        wait(200)
        time_spent = time_spent + 200

    robot.stop(stop_type=Stop.BRAKE)


# Similar to the above function but check the distance traveled by 
# checking the motor angle. This will be a more accurate way of checking 
# distance traveled
# Dont confuse motor angle (rotations) with gyro angle (direction)
def move_straight_target_direction_motor_angle(gyro, distance_mm, speed_mm_s, target_angle):

    turn_to_angle( gyro, target_angle)

    # Use a different variable name for gyro so you dont get confused
    gyro_target_angle = target_angle
    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        error = target_angle - gyro.angle()
        log_string('Gyro :' + str(gyro.angle()) + ' err: '+ str(error))
        adj_angular_speed = error * 1.5
        robot.drive(speed_mm_s, adj_angular_speed)
        wait(50)

    robot.stop(stop_type=Stop.BRAKE)


# calibrate_gyro(new_angle=0)
# move_straight_target_direction_motor_angle(gyro=gyro,
#        distance_mm=600, speed_mm_s=240, target_angle=0)
# move_straight(distance=600, speed_mm_s=300)
# wait(999999)

# log_string('Running robot now done')
# wait(10)

# log_string('The color on left is ' + str(color_sensor_left.color()))

def color_test(color_sensor, distance_mm, speed_mm_s):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        log_string('Color : ' + str(color_sensor.color()) + ' Intense:' + str(color_sensor.reflection()))
        robot.drive(speed_mm_s, 0)
        wait(300)

    robot.stop(stop_type=Stop.BRAKE)

# color_test(color_sensor=color_sensor_center, distance_mm=100, speed_mm_s=50)
# wait(999999)

def follow_line_border(
    color_sensor,
    distance_mm,
    speed_mm_s, 
    border_color,
    color_on_left):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    # Keep moving till the angle of the left motor reaches target
    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        error = 100 - color_sensor.reflection()
        if color_sensor.color() == border_color:
            robot.drive(speed_mm_s, 0)
        elif color_sensor.color() == color_on_left:
            robot.drive(speed_mm_s, 0.5 * error)
        else :
            robot.drive(speed_mm_s,  -0.5 * error)
        wait(50)

    robot.stop(stop_type=Stop.BRAKE)

# follow_line_border(
#     color_sensor=color_sensor_right,
#     distance_mm=650,
#     speed_mm_s=150, 
#     border_color=Color.WHITE,
#     color_on_left=Color.BLACK)
