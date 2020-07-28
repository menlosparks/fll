

WHEEL_DIAMETER_MM=89
AXLE_TRACK_MM=135
 
 
#drive motors
left_motor=Motor(Port.B, Direction.CLOCKWISE)
right_motor=Motor(Port.C, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)


def bus_base_to_mis_1: 

    def move_straight(duration, speed_mm_s):
    robot.drive_time(speed_mm_s, 0, duration)
    robot.stop(stop_type=Stop.BRAKE)

move_straight(duration=5000, speed_mm_s=300)

