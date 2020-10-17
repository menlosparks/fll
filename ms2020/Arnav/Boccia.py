#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor

##### Do not change above this line ##########################################

WHEEL_DIAMETER_MM=89
AXLE_TRACK_MM=135
 
 
#drive motors
left_motor=Motor(Port.B, Direction.CLOCKWISE)
right_motor=Motor(Port.C, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)
def move_straight(duration, speed_mm_s):
    robot.drive_time(speed_mm_s, 0, duration)
    robot.stop(stop_type=Stop.BRAKE)
move_straight(duration=3000, speed_mm_s=300)

crane_motor=Motor(Port.D, Direction.COUNTERCLOCKWISE, [8,24])

def move_crane_down( crane_motor, degrees):
   crane_motor.run_angle(90,    -1 * degrees, Stop.BRAKE)
 
move_crane_down(crane_motor, 30)