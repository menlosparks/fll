import sys
import os
sys.path.append('../shared')
sys.path.append('../samples')
sys.path.append('../bus')
sys.path.append('../missions')
 
import shared_all
 
import trialbus
import treadmill
import pulluprobot
import row
import weight
import phone
import slide

shared_all.calibrate_gyro(0)

trialbus.base_to_pullup()
pulluprobot.align()
pulluprobot.run()
trialbus.pullup_to_dance()
