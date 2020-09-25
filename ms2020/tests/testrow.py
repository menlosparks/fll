#!/usr/bin/env pybricks-micropython

import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_1
import row


INITIAL_ANGLE=-90
shared_all.calibrate_gyro(INITIAL_ANGLE)

row.align(adjust_for_mission=0)
row.run()
bus_service_1.row_to_weight()


# bus_service_1.push_small_tire()


