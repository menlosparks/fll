 
def move_straight(distance, speed_mm_s):
 
   # calculate the time (duration) for which robot needs to run
   duration = abs(int(1000 * distance / speed_mm_s))
   robot.drive_time(speed_mm_s, 0, duration)
   robot.stop(stop_type=Stop.BRAKE)

move_straight(
distance=50  
speed_mm_s=100)

def move_crane_to_top(crane_motor):
   crane_motor.run_until_stalled(-180, Stop.COAST, 35)
   move_crane_up( crane_motor, degrees = 5)

move_crane_to_top(crane_motor)

