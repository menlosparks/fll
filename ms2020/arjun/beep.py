#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
import pybricks.nxtdevices as nxt
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
 
#print(ColorSensor(Port.S4).color())
 
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
SOUND_VOLUME=7
brick.sound.beep(700, 80, SOUND_VOLUME)