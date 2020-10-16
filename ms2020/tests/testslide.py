#!/usr/bin/env pybricks-micropython

import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_1
import slide

INITIAL_ANGLE=180
shared_all.calibrate_gyro(INITIAL_ANGLE)

# bus_service_1.phone_to_slide()
slide.align()
# slide.rske_slide_to_home()
