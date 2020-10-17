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

calibrate_gyro(0)   
# turn_to_angle( gyro, 65)
# move_straight(5000, 300)

def move_crane_to_top(crane_motor):
   crane_motor.run_until_stalled(-180, Stop.COAST, 35)
   move_crane_up( crane_motor, degrees = 5)

move_crane_to_top(crane_motor)