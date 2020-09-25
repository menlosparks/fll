#!/usr/bin/env pybricks-micropython

import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_2

INITIAL_ANGLE=180
shared_all.calibrate_gyro(INITIAL_ANGLE)

bus_service_2.base_to_basket()
## starts near yellow flower in gray area
basket.align(adjust_for_mission=-90)
basket.run()

