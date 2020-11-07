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
import math
 
sys.path.append('../shared')
import robot_setup
import ev3ext3rdpar
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
    ev3ext3rdpar.log(message)

def any_button_pressed(waiting_color=Color.RED):
    brick.light(waiting_color)

    while not any(brick.buttons()):
        wait(150)
    brick.light(Color.BLACK)
    return brick.buttons().copy()

#(kp, ki, kd, tight_loop_limit, angle_tolerance, speed_tolerance, stall_speed, stall_time)

def set_drive_motors_tight():
    left_motor.set_pid_settings(500, 800, 5, 100, 3, 5, 2,200)
    right_motor.set_pid_settings(500, 800, 5, 100, 3, 5, 2,200)

def set_drive_motors_regular():
    left_motor.set_pid_settings(500, 800, 5, 100, 3, 5, 2,200)
    right_motor.set_pid_settings(500, 800, 5, 100, 3, 5, 2,200)

def set_motor_tight(motor):
    motor.set_pid_settings(400, 600, 5, 100, 3, 5, 2,200)

def set_motor_regular(motor):
    motor.set_pid_settings(400, 600, 5, 100, 3, 5, 2,200)

def calibrate_gyro(new_gyro_angle=0):
    ev3ext3rdpar.calibrateGyro(gyro, new_gyro_angle)


def push_back_reset_gyro(distance_mm, reset_gyro = True, new_gyro_angle = 0 ):
    move_straight(distance_mm = distance_mm , speed_mm_s= -80)
    left_motor.run_angle( -90,  60, Stop.BRAKE, True)
    right_motor.run_angle( -90,  60, Stop.BRAKE, True)
    if reset_gyro == True:
        calibrate_gyro(new_gyro_angle)


def turn( angle, speed_deg_s = DEFAULT_ANGULAR_SPEED):
    ev3ext3rdpar.pivot(robot, left_motor, right_motor,
        robot_setup.AXLE_TRACK_MM, robot_setup.WHEEL_DIAMETER_MM, angle, speed_deg_s)

def turn_arc(distance,angle, speed_mm_s):
    ev3ext3rdpar.arc(robot, left_motor, right_motor, robot_setup.AXLE_TRACK_MM,
        robot_setup.WHEEL_DIAMETER_MM, distance, angle, speed_mm_s)


def turn_arc_old(distance,angle, speed_mm_s):

    duration_ms = 1000* abs(distance / speed_mm_s)
    steering_speed = (angle / duration_ms) * 1000
    robot.drive_time(speed_mm_s, steering_speed, duration_ms)


def turn_to_direction( gyro, target_angle, speed_deg_s=DEFAULT_ANGULAR_SPEED):
    ev3ext3rdpar.pointGyro(robot,left_motor, right_motor, robot_setup.AXLE_TRACK_MM,
            robot_setup.WHEEL_DIAMETER_MM,
            gyro, target_angle, speed_deg_s )
    # gyro_angle=gyro.angle()
    # # target_angle = adjust_gyro_target_angle(target_angle, gyro_angle)

    # target_angle = ev3ext3rdpar.getNormalizedAngle(target_angle, gyro_angle)
    # log_string('TTD  Adjtgt :' +str(target_angle) + ' gyr:' + str(gyro_angle))

    # if (abs(target_angle-gyro_angle) > 15):
    #     turn(target_angle - gyro_angle)

    # gyro_angle=gyro.angle()

    # if (abs(target_angle-gyro_angle) <=1):
    #     log_string('TTD not needed gyr:' +str(gyro_angle))
    #     return target_angle

    # log_string('TTD needed gyr:' +str(gyro_angle))

    # max_attempts=10 # limit oscialltions to 10, not forever
    # kp=1.5
    # ki=0.1
    # kd=0.1
    # integral_error=0
    # prev_error=0

    # while ( abs(target_angle - gyro_angle) > 1 and max_attempts >0):
    #     error=target_angle - gyro_angle
    #     adj_angular_speed = error * kp   + (integral_error + error) * ki + (error - prev_error) * kd
    #     robot.drive(0, adj_angular_speed)
    #     wait(100)
    #     max_attempts -= 1
    #     integral_error += error
    #     prev_error = error
    #     gyro_angle=gyro.angle()

    # robot.stop(stop_type=Stop.BRAKE)

    # log_string('TTD done-Adjted:' + str(target_angle) 
    #     + ' gy: ' + str(gyro_angle)
    #     + ' remain:' + str(max_attempts)
    #     )
    # return target_angle




#mstd MSTD
def move_straight_target_direction(gyro, distance_mm, speed_mm_s, target_angle):

    ev3ext3rdpar.movePointingGyro(robot,left_motor, right_motor, robot_setup.AXLE_TRACK_MM,
            robot_setup.WHEEL_DIAMETER_MM,
            gyro, distance_mm, speed_mm_s, target_angle)

    # target_angle = turn_to_direction( gyro, target_angle)
    # log_string('MSTD  Adjtgt :' +str(target_angle))

    # left_motor.reset_angle(0)
    # motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    # kp=1.5
    # ki=0.1
    # kd=0.1
    # integral_error=0
    # prev_error=0

    # while (abs(left_motor.angle()) < abs(motor_target_angle)):
    #     gyro_angle = gyro.angle()
    #     error = target_angle - gyro_angle
    #     log_string('Gyro :' + str(gyro_angle) + ' err: '+ str(error))
    #     adj_angular_speed =  error * kp   + (integral_error + error) * ki + (error - prev_error) * kd
    #     robot.drive(speed_mm_s, adj_angular_speed)
    #     wait(50)
    #     if right_motor.stalled() or left_motor.stalled():
    #         log_string('MSTD motor stalled ')
    #         return
    #     integral_error += error
    #     prev_error = error

    # log_string('MSTD dne gy:' + str(gyro.angle()))

    # robot.stop(stop_type=Stop.BRAKE)

def move_straight(distance_mm, speed_mm_s):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    # Keep moving till the angle of the left motor reaches target
    robot.drive(speed_mm_s, 0)
    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        wait(40)

    robot.stop(stop_type=Stop.BRAKE)

def move_reverse(
    max_distance, 
    speed_mm_s = DEFAULT_SPEED):
    move_straight( max_distance,  -1 *speed_mm_s)



def did_motor_stall(motor, max_degrees, speed):
    return ev3ext3rdpar.didMotorStall(motor, max_degrees, speed)


def move_to_color(
    color_sensor,
    stop_on_color,
    alternative_color = None,
    speed_mm_s = DEFAULT_COLOR_FIND_SPEED,
    min_intensity=0,
    max_intensity=100,
    max_distance_mm=300):

    return ev3ext3rdpar.moveToClr(
        robot,
        left_motor, right_motor, robot_setup.AXLE_TRACK_MM, robot_setup.WHEEL_DIAMETER_MM,
        color_sensor,
        stop_on_color,
        alternative_color,
        speed_mm_s,
        min_intensity,
        max_intensity,
        max_distance_mm)

    # left_motor.reset_angle(0)
    # motor_target_angle = int(DEGREES_PER_MM * max_distance_mm)

    # alternative_color = alternative_color if alternative_color != None else stop_on_color
    # robot.drive(speed_mm_s, 0)
    # # Check if color reached or the angle of the left motor reaches target.
    # color=color_sensor.color()
    # intensity=color_sensor.reflection()
    # while ((not color in (stop_on_color, alternative_color)
    #     or not (intensity in range (min_intensity, max_intensity)))
    #     and  (abs(left_motor.angle()) < abs(motor_target_angle)))   :
    #     wait(10)
    #     color=color_sensor.color()
    #     intensity=color_sensor.reflection()

    # robot.stop(stop_type=Stop.BRAKE)

    # log_string('Cor fnd:(' + str(color) 
    # +' ' + str(intensity) + ')'
    # +' ' + str(color_sensor.ambient()) + ')'
    # + ' find ' + str(stop_on_color) + ' or ' + str(alternative_color)
    # + ' in range(' + str(min_intensity) + '-' + str(max_intensity)
    # )



def move_to_color_reverse(
    color_sensor,
    stop_on_color,
    alternative_color = None,
    speed_mm_s = DEFAULT_COLOR_FIND_SPEED,
    min_intensity=0,
    max_intensity=100,
    max_distance_mm=9999):
    return move_to_color(
        color_sensor,
        stop_on_color,
        alternative_color,
        speed_mm_s = -1 * speed_mm_s,
        min_intensity=min_intensity,
        max_intensity=max_intensity,
        max_distance_mm=max_distance_mm)






def drive_raising_crane(duration_ms, robot_distance_mm, robot_turn_angle, 
                        motor, crane_angle):
    crane_angular_speed = int(1000 * crane_angle / duration_ms)
    turn_angular_speed_deg_s = int(1000 * robot_turn_angle / duration_ms)
    forward_speed = int(1000 * robot_distance_mm / duration_ms) 

    if abs(forward_speed) > 0 or abs(turn_angular_speed_deg_s) > 0 :
        robot.drive(forward_speed, turn_angular_speed_deg_s)
    motor.run(crane_angular_speed)
    wait(duration_ms)
    motor.stop(Stop.BRAKE)
    robot.stop(stop_type=Stop.BRAKE)
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

def start_moving_crane_to_angle(motor, target_angle):
    speed_deg_s = 210 if target_angle > 90 else 130 
    motor.run_target(speed_deg_s, target_angle, Stop.BRAKE, False)

def move_crane_to_angle(motor, target_angle):
    speed_deg_s = 210 if target_angle > 90 else 130 
    motor.run_target(speed_deg_s, target_angle, Stop.BRAKE, True)

def start_moving_crane_to_top(motor):
    top_angle = robot_setup.get_top_angle(motor)
    start_moving_crane_to_angle(motor, top_angle - 10 )

def move_crane_to_top( motor, release_angle = 5):
    motor.run_until_stalled(400, Stop.COAST, 40)
    if release_angle > 0:
        move_crane_down( motor, degrees = release_angle)
    motor.reset_angle(robot_setup.get_top_angle(motor))
    log_string('Reset mot ang:' + str(motor.angle()))

def move_crane_to_floor( motor, release_angle = 5):
    motor.run_until_stalled(-300, Stop.COAST, 35)
    if release_angle > 0:
        move_crane_up( motor, degrees = release_angle)
    motor.reset_angle(0)
    log_string('Reset mot ang 0')

def move_rack_to_top(release_angle = 5 ):
    rack_motor.run_until_stalled(500, Stop.COAST, 50)
    if release_angle > 0:
        move_crane_down( rack_motor, degrees = release_angle)
    rack_motor.reset_angle(robot_setup.get_top_angle(rack_motor))
    log_string('Reset rack ang:' + str(rack_motor.angle()))

def move_rack_to_floor(release_angle = 5 ):

    log_string('setting motr duty')
    motor_duty = 80 if rack_motor.angle() > 140 else 50
    log_string('do run_until_stalled')
    rack_motor.run_until_stalled(-300, Stop.COAST, motor_duty)
    if release_angle > 0:
        move_crane_up( rack_motor, degrees = release_angle)
    rack_motor.reset_angle(0)
    log_string('REset mot ang 0')

def move_hook_to_floor(release_angle = 5 ):


    rack_motor.run_until_stalled(-300, Stop.COAST, 40)
    if release_angle > 0:
        move_crane_up( rack_motor, degrees = release_angle)
    rack_motor.reset_angle(0)
    log_string('REset mot ang 0')

def move_crane_up( motor, degrees):
    motor.run_angle(180,  degrees, Stop.BRAKE)

def move_crane_down( motor, degrees):
    motor.run_angle(180,  -1 * degrees, Stop.BRAKE)

def run_to_home():
    turn_to_direction(gyro, target_angle=190)
    robot.drive(400, 0)
    while left_motor.stalled() != True:
        wait(100)
    robot.stop()

def wiggle():
    left_motor.run_angle( 120,  10, Stop.BRAKE, True)
    right_motor.run_angle(120,  10, Stop.BRAKE, True)


def fastflip():
    shared_all.move_crane_down( motor=crane_motor, degrees=20)
    crane_motor.run_angle(720, 100)
    

    
    
# def adjust_gyro_target_angle(target_angle, current_gyro_angle):
#     start_angle = current_gyro_angle
#     angle_change = target_angle - start_angle

#     if (angle_change >180 ):
#         angle_change = angle_change - 360
#     if (angle_change < -180 ):
#         angle_change = angle_change + 360
#     target_angle = angle_change + start_angle
#     log_string('adjust start:' + str(start_angle) 
#         + ' ang chg:' +str(angle_change)
#         + ' Adj:' +str(target_angle)
#         )
#     return target_angle



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


