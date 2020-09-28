#!/usr/bin/env pybricks-micropython
#chnage
import sys
import os
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Port
 
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


DEFAULT_SPEED=300
DEFAULT_COLOR_FIND_SPEED=50
DEFAULT_LINEFOLLOW_SPEED=100
DEFAULT_ANGULAR_SPEED=75


SOUND_VOLUME=7


def sound_happy():
    brick.sound.beep(1100, 80, SOUND_VOLUME)
    brick.sound.beep(900, 80, SOUND_VOLUME)

def sound_attention():
    brick.sound.beep(700, 80, SOUND_VOLUME)
    brick.sound.beep(1200, 80, SOUND_VOLUME)

def sound_start():
    brick.sound.beep(700, 80, SOUND_VOLUME)

def sound_alarm():
    brick.sound.beep(300, 90, SOUND_VOLUME)
    wait(200)
    brick.sound.beep(300, 90, SOUND_VOLUME)
    wait(200)
    brick.sound.beep(300, 90, SOUND_VOLUME)

def log_string(message):
    print(message)
    brick.display.text(message)

def calibrate_gyro(new_gyro_angle=0):
    brick.sound.beep(300, 90, SOUND_VOLUME)

    current_speed=gyro.speed()
    current_angle=gyro.angle()
    log_string('calibrating gyro speed ' + str(current_speed) + ' angle:' + str(current_angle))
    wait(30)
    gyro.reset_angle(new_gyro_angle)
    wait(40)
    current_speed=gyro.speed()
    current_angle=gyro.angle()
    log_string('After reset gyro speed ' + str(current_speed) + ' angle:' + str(current_angle))
    wait(40)

def push_back_reset_gyro(distance_mm, reset_gyro = True, new_gyro_angle = 0 ):
    move_straight(distance_mm = distance_mm , speed_mm_s= -80)
    left_motor.run_angle( -140,  60, Stop.BRAKE, True)
    right_motor.run_angle( -140,  60, Stop.BRAKE, True)
    if reset_gyro == True:
        calibrate_gyro(new_gyro_angle)

def turn_arc(distance,angle, speed_mm_s):

    duration_ms = 1000* abs(distance / speed_mm_s)
    steering_speed = (angle / duration_ms) * 1000
    robot.drive_time(speed_mm_s, steering_speed, duration_ms)




def turn_to_direction( gyro, target_angle, speed_mm_s = DEFAULT_SPEED):

    target_angle = adjust_gyro_target_angle(target_angle)
    log_string('turn_to_direction  Adjtgt :' +str(target_angle))

    turn(target_angle - gyro.angle())

    log_string('turn_to_direction  after turn :' +str(gyro.angle()))

    max_attempts=10 # limit oscialltions to 10, not forever
    while ( abs(target_angle - gyro.angle()) > 1 and max_attempts >0):
        error=target_angle - gyro.angle()
        adj_angular_speed = error * 1.5
        robot.drive(0, adj_angular_speed)
        wait(100)
        max_attempts -= 1

    robot.stop(stop_type=Stop.BRAKE)

    adjusted_angle = gyro.angle()
    log_string('turn_to_direction done-- Adjusted target: ' + str(target_angle) 
        + ' now: ' + str(adjusted_angle)
        + ' remain attempts : ' + str(max_attempts)
        )




def turn( angle, speed_deg_s = DEFAULT_ANGULAR_SPEED):

    if angle == 0 :
        return
    if angle > 0:    # right turns are a bit under-steered
        angle = int( angle)
    else:
        angle = int(angle / 1)

    speed_deg_s = -1 * speed_deg_s if angle < 0 else speed_deg_s
    # time=int(1000 * (floatspeed_deg_s(angle)/float(speed_deg_s)))
    time=abs(int(1000 * (angle/speed_deg_s)))
    log_string('Time of turn ' +str(time))
    robot.drive_time(0, speed_deg_s, time)
    robot.stop(stop_type=Stop.BRAKE)

def move_reverse(
    max_distance, 
    speed_mm_s = DEFAULT_SPEED):
    move_straight( -1 * max_distance, speed_mm_s)


def move_straight(distance_mm, speed_mm_s):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    # Keep moving till the angle of the left motor reaches target
    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        robot.drive(speed_mm_s, 0)
        wait(100)

    robot.stop(stop_type=Stop.BRAKE)


def did_motor_stall(motor, max_degrees, speed):
    motor.reset_angle(0)
    speed = speed * (-1 if max_degrees < 0 else 1)
    motor.run(speed)

    while(abs(motor.angle()) < abs(max_degrees)):
        if ( motor.stalled() == True):
            motor.stop(stop_type=Stop.BRAKE)
            return True
        wait(100)
    
    motor.stop(stop_type=Stop.BRAKE)
    return False


def turn_to_color(
    color_sensor,
    stop_on_color,
    rotate_dir = 1,
    angular_speed_deg_s = DEFAULT_ANGULAR_SPEED):
 
    robot.drive(0, rotate_dir * angular_speed_deg_s)
    # Check if color reached.
    while color_sensor.color() != stop_on_color:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)

def turn_to_color_right(
    color_sensor,
    stop_on_color,
    angular_speed_deg_s = DEFAULT_ANGULAR_SPEED):
 
    turn_to_color( color_sensor, stop_on_color, 1, angular_speed_deg_s)

def turn_to_color_left(
    color_sensor,
    stop_on_color,
    angular_speed_deg_s = DEFAULT_ANGULAR_SPEED):
 
    turn_to_color( color_sensor, stop_on_color, -1, angular_speed_deg_s )


def move_to_color(
    color_sensor,
    stop_on_color,
    alternative_color = None,
    speed_mm_s = DEFAULT_COLOR_FIND_SPEED):
 
    alternative_color = alternative_color if alternative_color != None else stop_on_color
    robot.drive(speed_mm_s, 0)
    # Check if color reached.
    while color_sensor.color() != stop_on_color and color_sensor.color() != alternative_color:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)
    log_string('Color found: ' + str(color_sensor.color()) +'(' + str(color_sensor.reflection()) + ')')



def move_to_color_reverse(
    color_sensor,
    stop_on_color,
    alternative_color = None,
    speed_mm_s = DEFAULT_COLOR_FIND_SPEED):
    move_to_color(
        color_sensor,
        stop_on_color,
        alternative_color,
        speed_mm_s = -1 * speed_mm_s)



# sweep and steop forward till color is found
def search_for_color(
    color_sensor,
    stop_on_color):

    if  color_sensor.color() == stop_on_color: # if already there
        return True

 
    forward_steps =0 
    while forward_steps < 3:
        sweep_width = 1
        sweep_attempts = 0
        sweep_speed = 45

        while sweep_attempts < 5:
            log_string('Sweep sweep_width ' + str(sweep_width))
            robot.drive_time(0, sweep_speed, sweep_width * 100) #sweep right
            if  color_sensor.color() == stop_on_color:
                robot.stop(stop_type=Stop.BRAKE)
                return True
            robot.drive_time(0, -1 * sweep_speed, sweep_width * 100) #sweep left
            if  color_sensor.color() == stop_on_color:
                robot.stop(stop_type=Stop.BRAKE)
                return True
           
            sweep_width += 1
            sweep_attempts += 1
        
        # reset to point at mid point
        robot.drive_time(0, sweep_speed, int(sweep_width * 100 / 2))
        # step forward by 1 cm to sweep again
        robot.drive_time(100, 0, 100)
        forward_steps += 1

    sound_alarm()
    return False



# Used by line follower to align with the general direction of the line
def align_with_line_to_left(
    color_sensor,
    line_color = Color.BLACK,
    border_color = Color.WHITE):

    #Find left white border of line
    move_to_color( color_sensor, border_color)
    move_to_color( color_sensor, line_color)
    move_to_color( color_sensor, border_color)
 
    #move forward half the length of tank and rotate
    move_straight( SENSOR_TO_AXLE)    
    turn_to_color_right( color_sensor, border_color) 

def align_with_line_to_right(
    color_sensor,
    line_color = Color.BLACK,
    border_color = Color.WHITE):

    #Find left white border of line
    move_to_color(color_sensor=color_sensor,
        stop_on_color=border_color)

    #move forward half the length of tank and rotate
    move_straight(distance_mm=SENSOR_TO_AXLE, speed_mm_s=50)
    turn_to_color_left( color_sensor, line_color) 
    turn_to_color_left( color_sensor, border_color) 




def follow_line_border(
    color_sensor,
    distance_mm,
    speed_mm_s):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    target_intensity = color_sensor.reflection()

    # Keep moving till the angle of the left motor reaches target
    while (abs(left_motor.angle()) < abs(motor_target_angle)):

        darkness = target_intensity - color_sensor.reflection()
        if color_sensor.color() == Color.WHITE:
            robot.drive(speed_mm_s, 0)
        elif color_sensor.color() == Color.BLACK:
            robot.drive(speed_mm_s, abs(darkness))
        else :
            robot.drive(speed_mm_s, -1 * abs(darkness))

        wait(250)

    robot.stop(stop_type=Stop.BRAKE)

def adjust_gyro_target_angle(target_angle):
    start_angle = gyro.angle()
    angle_change = target_angle - start_angle

    if (angle_change >180 ):
        angle_change = angle_change - 360
    if (angle_change < -180 ):
        angle_change = angle_change + 360
    target_angle = angle_change + start_angle
    log_string('adjust_gyro_target_angle start_angle:' + str(start_angle) 
        + ' angle_change:' +str(angle_change)
        + ' Adj :' +str(target_angle)
        )
    return target_angle

def move_straight_target_direction(gyro, distance_mm, speed_mm_s, target_angle):

    target_angle = adjust_gyro_target_angle(target_angle)
    log_string('move_straight_target_direction  Adjtgt :' +str(target_angle))

    turn_to_direction( gyro, target_angle)

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        error = target_angle - gyro.angle()
        log_string('Gyro :' + str(gyro.angle()) + ' err: '+ str(error))
        adj_angular_speed = error * 1.5
        robot.drive(speed_mm_s, adj_angular_speed)
        wait(50)
        if right_motor.stalled() or left_motor.stalled():
            log_string('move_straight_target_direction motor stalled ')
            return

    log_string('move_straight_target_direction -- done gyro.angle(): ' + str(gyro.angle()))

    robot.stop(stop_type=Stop.BRAKE)



def drive_raising_crane(duration_ms, robot_distance_mm, robot_turn_angle, 
                        motor, crane_angle):
    crane_angular_speed = int(1000 * crane_angle / duration_ms)
    turn_angular_speed_deg_s = int(1000 * robot_turn_angle / duration_ms)
    forward_speed = int(1000 * robot_distance_mm / duration_ms) 

    if forward_speed > 0 or turn_angular_speed_deg_s > 0 :
        robot.drive(forward_speed, turn_angular_speed_deg_s)
    motor.run(crane_angular_speed)
    wait(duration_ms)
    motor.stop(Stop.BRAKE)
    robot.stop(stop_type=Stop.BRAKE)
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)



def move_crane_to_top( motor):
    motor.run_until_stalled(500, Stop.COAST, 50)
    move_crane_down( motor, degrees = 5)

def move_crane_to_floor( motor):
    motor.run_until_stalled(-300, Stop.COAST, 35)
    move_crane_up( motor, degrees = 10)

def move_rack_to_top( ):
    rack_motor.run_until_stalled(500, Stop.COAST, 50)
    move_crane_down( rack_motor, degrees = 5)

def move_rack_to_floor( ):
    rack_motor.run_until_stalled(-300, Stop.COAST, 45)
    move_crane_up( rack_motor, degrees = 10)


def move_crane_up( motor, degrees):
    motor.run_angle(180,  degrees, Stop.BRAKE)

def move_crane_down( motor, degrees):
    motor.run_angle(180,  -1 * degrees)

def run_to_home():
    turn_to_direction(gyro, target_angle=190)
    robot.drive(400, 0)
    while left_motor.stalled() != True:
        wait(100)
    robot.stop()

def wiggle():
    left_motor.run_angle( 120,  10, Stop.BRAKE, True)
    right_motor.run_angle(120,  10, Stop.BRAKE, True)


### Run this at start up
#calibrate_gyro()
 
def move_to_obstacle(
    obstacle_sensor,
    stop_on_obstacle_at,
    speed_mm_s):
 
    robot.drive(speed_mm_s, 0)
    sign = -1 if speed_mm_s < 0 else 1
    # Check if obstacle too close.
    while sign * obstacle_sensor.distance() > sign * stop_on_obstacle_at:
        log_string('obstacle_sensor at ' + str(obstacle_sensor.distance()))
        wait(10)

    robot.stop(stop_type=Stop.BRAKE)
    
