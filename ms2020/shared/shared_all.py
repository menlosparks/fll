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
    print(message)
    brick.display.text(message)

def any_button_pressed():
    brick.light(Color.RED)

    while not any(brick.buttons()):
        wait(150)
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
    gyro_speed = gyro.speed()
    gyro_angle = gyro.angle()
    log_string('calib sp: ' + str(gyro_speed) + ' ang:' + str(gyro_angle))
    if gyro_speed == 0 and gyro_angle == new_gyro_angle :
        log_string('No calibration ')
        return

    brick.sound.beep(300, 30, SOUND_VOLUME)

    cntr=0
    while (gyro.speed() > 0 and cntr < 5):
        cntr +=1
        wait(10)
    gyro.reset_angle(new_gyro_angle)
    wait(40)
    log_string('Aft rst gy spd ' + str(gyro.speed()) + ' ang:' + str(gyro.angle()))

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

    gyro_angle=gyro.angle()

    target_angle = adjust_gyro_target_angle(target_angle, gyro_angle)
    log_string('turn_to_direction  Adjtgt :' +str(target_angle) + ' gyro:' + str(gyro_angle))

    if (abs(target_angle-gyro_angle) > 15):
        turn(target_angle - gyro_angle)

    gyro_angle=gyro.angle()

    if (abs(target_angle-gyro_angle) <=1):
        return target_angle

    log_string('turn_to_direction  after turn :' +str(gyro_angle))

    max_attempts=10 # limit oscialltions to 10, not forever
    kp=1.5
    ki=0.1
    kd=0.1
    integral_error=0
    prev_error=0

    while ( abs(target_angle - gyro_angle) > 1 and max_attempts >0):
        error=target_angle - gyro_angle
        adj_angular_speed = error * kp   + (integral_error + error) * ki + (error - prev_error) * kd
        robot.drive(0, adj_angular_speed)
        wait(100)
        max_attempts -= 1
        integral_error += error
        prev_error = error
        gyro_angle=gyro.angle()

    robot.stop(stop_type=Stop.BRAKE)

    log_string('TTD done-Adjted:' + str(target_angle) 
        + ' gy: ' + str(gyro_angle)
        + ' remain:' + str(max_attempts)
        )
    return target_angle




def turn( angle, speed_deg_s = DEFAULT_ANGULAR_SPEED):


    wheel_target_distance_mm = (angle/360.0) * robot_setup.AXLE_TURN_CIRCUM
    wheel_target_angle = robot_setup.DEGREES_PER_MM * wheel_target_distance_mm;
    time=abs(int(1000 * (angle/speed_deg_s)))
    time_sec=abs(int((angle/speed_deg_s)))
    motor_speed_deg_s = abs(wheel_target_angle/time_sec)
    left_motor.run_angle(motor_speed_deg_s, wheel_target_angle, Stop.BRAKE, False)
    right_motor.run_angle(-1*motor_speed_deg_s,  wheel_target_angle, Stop.BRAKE, True)




def turnold( angle, speed_deg_s = DEFAULT_ANGULAR_SPEED):

    if angle == 0 :
        return
    if angle > 0:    # right turns are a bit under-steered
        angle = int( angle)
    else:
        angle = int(angle / 1)

    speed_deg_s = -1 * speed_deg_s if angle < 0 else speed_deg_s
    # time=int(1000 * (floatspeed_deg_s(angle)/float(speed_deg_s)))
    time=abs(int(1000 * (angle/speed_deg_s)))
    robot.drive_time(0, speed_deg_s, time)
    robot.stop(stop_type=Stop.BRAKE)



def move_straight_target_direction(gyro, distance_mm, speed_mm_s, target_angle):

    # gyro_angle = gyro.angle()
    # target_angle = adjust_gyro_target_angle(target_angle, gyro_angle)

    target_angle = turn_to_direction( gyro, target_angle)
    log_string('MSTD  Adjtgt :' +str(target_angle))

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    kp=1.5
    ki=0.1
    kd=0.1
    integral_error=0
    prev_error=0

    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        gyro_angle = gyro.angle()
        error = target_angle - gyro_angle
        log_string('Gyro :' + str(gyro_angle) + ' err: '+ str(error))
        adj_angular_speed =  error * kp   + (integral_error + error) * ki + (error - prev_error) * kd
        robot.drive(speed_mm_s, adj_angular_speed)
        wait(50)
        if right_motor.stalled() or left_motor.stalled():
            log_string('MSTD motor stalled ')
            return
        integral_error += error
        prev_error = error

    log_string('MSTD dne gy:' + str(gyro.angle()))

    robot.stop(stop_type=Stop.BRAKE)





def move_reverse(
    max_distance, 
    speed_mm_s = DEFAULT_SPEED):
    move_straight( max_distance,  -1 *speed_mm_s)


def move_straight(distance_mm, speed_mm_s):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)

    # Keep moving till the angle of the left motor reaches target
    robot.drive(speed_mm_s, 0)
    while (abs(left_motor.angle()) < abs(motor_target_angle)):
        wait(40)

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
    speed_mm_s = DEFAULT_COLOR_FIND_SPEED,
    min_intensity=0,
    max_intensity=100,
    max_distance_mm=300):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * max_distance_mm)

    alternative_color = alternative_color if alternative_color != None else stop_on_color
    robot.drive(speed_mm_s, 0)
    # Check if color reached or the angle of the left motor reaches target.
    color=color_sensor.color()
    intensity=color_sensor.reflection()
    while ((not color in (stop_on_color, alternative_color)
        or not (intensity in range (min_intensity, max_intensity)))
        and  (abs(left_motor.angle()) < abs(motor_target_angle)))   :
        wait(10)
        color=color_sensor.color()
        intensity=color_sensor.reflection()

    robot.stop(stop_type=Stop.BRAKE)

    log_string('Cor fnd:(' + str(color) 
    +' ' + str(intensity) + ')'
    +' ' + str(color_sensor.ambient()) + ')'
    + ' find ' + str(stop_on_color) + ' or ' + str(alternative_color)
    + ' in range(' + str(min_intensity) + '-' + str(max_intensity)
    )



def move_to_color_reverse(
    color_sensor,
    stop_on_color,
    alternative_color = None,
    speed_mm_s = DEFAULT_COLOR_FIND_SPEED,
    min_intensity=0,
    max_intensity=100,
    max_distance_mm=9999):
    move_to_color(
        color_sensor,
        stop_on_color,
        alternative_color,
        speed_mm_s = -1 * speed_mm_s,
        min_intensity=min_intensity,
        max_intensity=max_intensity,
        max_distance_mm=max_distance_mm)



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
    speed_mm_s,
    border_on_right=True):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    target_intensity = 100

    kp=0.05
    ki=kp * 0.000
    kd=kp * 0.000
    integral=0
    prev_error=0

    border_side = 1 if border_on_right else -1
    # Keep moving till the angle of the left motor reaches target
    while (abs(left_motor.angle()) < abs(motor_target_angle)):

        color = color_sensor.color()
        intensity = color_sensor.reflection()
        error = border_side * abs(target_intensity - intensity)
        if color not in (Color.WHITE,  Color.BLACK):
            error = -1 * error
        
        angular_speed = kp * error + ki*integral + kd*(error-prev_error)
        log_string('Lfol: (' + str(color) + ' ' + str(intensity) + ')' 
            + ' err:' + str(error)+ ' spd:' + str(angular_speed))
        robot.drive(speed_mm_s, angular_speed)
        wait(20)
        prev_error = error
        integral += error

    robot.stop(stop_type=Stop.BRAKE)

def adjust_gyro_target_angle(target_angle, current_gyro_angle):
    start_angle = current_gyro_angle
    angle_change = target_angle - start_angle

    if (angle_change >180 ):
        angle_change = angle_change - 360
    if (angle_change < -180 ):
        angle_change = angle_change + 360
    target_angle = angle_change + start_angle
    log_string('adjust start:' + str(start_angle) 
        + ' ang chg:' +str(angle_change)
        + ' Adj:' +str(target_angle)
        )
    return target_angle


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

def start_moving_crane_to_top(motor):
    top_angle = robot_setup.get_top_angle(motor)
    start_moving_crane_to_angle(motor, top_angle - 10 )

def move_crane_to_top( motor, release_angle = 5):
    motor.run_until_stalled(500, Stop.COAST, 50)
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

    if rack_motor.angle() > 140:
        move_crane_down(rack_motor, 70)
    rack_motor.run_until_stalled(-300, Stop.COAST, 50)
    if release_angle > 0:
        move_crane_up( rack_motor, degrees = release_angle)
    rack_motor.reset_angle(0)
    log_string('REset mot ang 0')

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
    
def fastflip():
    shared_all.move_crane_down( motor=crane_motor, degrees=20)
    crane_motor.run_angle(720, 100)
    

    