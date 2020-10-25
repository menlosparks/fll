#!/usr/bin/env pybricks-micropython

import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_2
import basket

shared_all.calibrate_gyro(-90)

bus_service_2.base_to_innov()
bus_service_2.innov_to_basket()
basket.align()
basket.run()

