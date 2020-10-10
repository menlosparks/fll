#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
import sys
import os
import inspect
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch


sys.path.append('../shared')
 

from robot_setup import color_sensor_right


from robot_setup import SOUND_VOLUME


#darkness = target_intensity - color_sensor_right.reflection()
if color_sensor_right.color() == Color.WHITE:
            SOUND_VOLUME=7
            brick.sound.beep(700, 80, SOUND_VOLUME)
elif color_sensor_right.color() == Color.BLACK:
            brick.sound.beep(700, 80, SOUND_VOLUME)
            wait(1000)
            brick.sound.beep(700, 80, SOUND_VOLUME)
else :
            brick.sound.beep(700, 80, SOUND_VOLUME)
            wait(1000)
            brick.sound.beep(700, 80, SOUND_VOLUME)
            wait(1000)
            brick.sound.beep(700, 80, SOUND_VOLUME)