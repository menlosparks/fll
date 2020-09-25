import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')

import shared_all
import bus_service_1
import treadmill
import row
import weight
import phone
import slide

INITIAL_ANGLE=180
shared_all.calibrate_gyro(INITIAL_ANGLE)

bus_service_1.base_to_treadmill()
treadmill.align()
treadmill.run()

bus_service_1.treadmill_to_row()
row.align()
row.run()

bus_service_1.row_to_weight()
weight.align()
weight.run()

bus_service_1.weight_to_phone()
phone.align()
phone.run()

bus_service_1.phone_to_slide()
slide.align()
slide.run()

slide.take_slide_to_home()
