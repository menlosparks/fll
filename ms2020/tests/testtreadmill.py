#!/usr/bin/env pybricks-micropython
import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_1
import treadmill
import row

shared_all.calibrate_gyro(0)

# bus_service_1.stepcounter_to_treadmill()
treadmill.align()
treadmill.run()
bus_service_1.treadmill_to_row()

row.align()
row.run()
