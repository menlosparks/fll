import sys
import os
sys.path.append('../shared')
sys.path.append('../bus')
sys.path.append('../missions')
 
import shared_all
 
import trialbus
import pulluprobot


def execute():
    # Must always calib rate gyro
    shared_all.calibrate_gyro(0)

    # Do the sequence
    trialbus.base_to_pullup()
    pulluprobot.align()
    pulluprobot.run()
    trialbus.pullup_to_dance()


## Below lines only for testing
## Comment out when done testing. Do not upload to Git hub without commenting.
execute()

