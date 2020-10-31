#!/usr/bin/env pybricks-micropython
import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_1
import treadmill
import row
import weight, phone, slide


shared_all.calibrate_gyro(180)

shared_all.log_string('bus_service_1.base_to_treadmill()')
bus_service_1.base_to_treadmill()
shared_all.log_string('treadmill.align()')
treadmill.align()
shared_all.log_string('treadmill.run()')
treadmill.run()

# shared_all.log_string('bus_service_1.treadmill_to_row()')
# bus_service_1.treadmill_to_row()
# shared_all.log_string('row.align()')
# row.align()
# shared_all.log_string('row.run()')
# row.run()

# shared_all.log_string('bus_service_1.row_to_weight()')
# bus_service_1.row_to_weight()
# shared_all.log_string('weight.align()')
# weight.align()
# shared_all.log_string('weight.run()')
# weight.run()

# shared_all.log_string('bus_service_1.weight_to_phone()')
# bus_service_1.weight_to_phone()
# shared_all.log_string('phone.align()')
# phone.align()
# shared_all.log_string('phone.run()')
# phone.run()

# shared_all.log_string('bus_service_1.phone_to_slide()')
# bus_service_1.phone_to_slide()
# shared_all.log_string('slide.align()')
# slide.align()
# shared_all.log_string('slide.run()')
# slide.run()
