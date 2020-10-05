#!/usr/bin/env pybricks-micropython
import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_1
import treadmill

INITIAL_ANGLE=0
shared_all.calibrate_gyro(INITIAL_ANGLE)

treadmill.align()
treadmill.run()
bus_service_1.treadmill_to_row()

import row
row.align()
row.run()
