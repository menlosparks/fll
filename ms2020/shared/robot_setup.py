#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
# import pybricks.nxtdevices as nxt
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
import math
 
SOUND_VOLUME=7
WHEEL_DIAMETER_MM=89
AXLE_TRACK_MM=130
SENSOR_TO_AXLE=68

# Get wheel circumference
WHEEL_CIRCUM_MM=math.pi*WHEEL_DIAMETER_MM
AXLE_TURN_CIRCUM=math.pi*AXLE_TRACK_MM
# 360 degrees -> WHEEL_CIRCUM_MM so   1 degree -> ?
DEGREES_PER_MM=360/WHEEL_CIRCUM_MM

ARM_TOP_ANGLE=190
CRANE_TOP_ANGLE=95
 
#drive motors
right_motor= Motor(Port.C, Direction.CLOCKWISE)
left_motor= Motor(Port.D, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)
crane_motor= Motor(Port.B, Direction.CLOCKWISE, [12,36])
rack_motor= Motor(Port.A, Direction.CLOCKWISE,  [8,8,40])
crane_motor.set_dc_settings(90, 30)
gyro= GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
color_sensor_right = ColorSensor(Port.S2)
color_sensor_center = ColorSensor(Port.S3)

#Discarded sensors
touch_sensor= None ##TouchSensor(Port.S3)
ultrasound=  None## nxt.UltrasonicSensor(Port.S2)
color_sensor_back =  None ##ColorSensor(Port.S2)



crane_motor.reset_angle(CRANE_TOP_ANGLE)
rack_motor.reset_angle(ARM_TOP_ANGLE)

def get_top_angle(motor):
    return CRANE_TOP_ANGLE if motor == crane_motor else ARM_TOP_ANGLE

WHITE_MIN_INTENSITY = {
  color_sensor_back: 50,
  color_sensor_right: 70,
  color_sensor_center:  70
}
BLACK_MAX_INTENSITY = {
  color_sensor_back: 20,
  color_sensor_right: 20,
  color_sensor_center:  20
}

def set_motor_medium_params(motor, kp=400, ki=600, kd=5, tight_loop_limit=100, angle_tolerance=2, 
  speed_tolerance=5, stall_speed=2,
  stall_time=200):

  motor.set_pid_settings(kp, ki, kd, tight_loop_limit, angle_tolerance, 
      speed_tolerance, stall_speed,stall_time)


def set_motor_large_params(motor, kp=500, ki=800, kd=5, tight_loop_limit=100, angle_tolerance=3, 
  speed_tolerance=5, stall_speed=2,
  stall_time=200):

  motor.set_pid_settings(kp, ki, kd, tight_loop_limit, angle_tolerance, 
      speed_tolerance, stall_speed,stall_time)


def set_motor_medium_run_settings(motor, max_speed=400, acceleration = 800):
    motor.set_run_settings(max_speed, acceleration)


# crane motor 
# ------------------------
# Run settings:      Max speed        400       Acceleration     800
# DC settings:    Duty limit       90     Duty offset      30
# PID settings:
# kp               400    ki               600    kd               5
# Tight Loop       100
# Angle tolerance  3    Speed tolerance  5
# Stall speed      2     Stall time       200


def set_motor_large_params(motor, kp=500, ki=800, kd=5, tight_loop_limit=100, angle_tolerance=3, 
  speed_tolerance=5, stall_speed=2,
  stall_time=200):

  motor.set_pid_settings(kp, ki, kd, tight_loop_limit, angle_tolerance, 
      speed_tolerance, stall_speed,stall_time)

def set_motor_large_run_settings(motor, max_speed=800, acceleration = 1600):
    motor.set_run_settings(max_speed, acceleration)

set_motor_large_run_settings(left_motor, acceleration=600)
set_motor_large_run_settings(right_motor, acceleration=600)

# right large motor 
# ------------------------
# Run settings: Max speed        800    Acceleration     1600

# DC settings: Duty limit       100    Duty offset      0

# PID settings: kp   500   ki     800      kd    5
# Tight Loop       100   Angle tolerance  3    Speed tolerance  5
# Stall speed      2                 Stall time       200
