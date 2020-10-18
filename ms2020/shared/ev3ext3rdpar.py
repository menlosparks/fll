#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
import math
 
def log(message):
    print(message)
    brick.display.text(message)


def pivot(leftM, rightM, axle, wheelDiam, angle, speed_deg_s):

    wheelCircum=math.pi*wheelDiam
    axleTurnCircum=math.pi*axle
    degreesPerMM=360/wheelCircum

    wheelTgtDistanceMM = (angle/360.0) * axleTurnCircum
    wheelTgtAngle = degreesPerMM * wheelTgtDistanceMM

    time_sec= abs(angle/speed_deg_s)
    motor_speed_deg_s = abs(wheelTgtAngle/time_sec)
    leftM.run_angle(motor_speed_deg_s, wheelTgtAngle, Stop.BRAKE, False)
    rightM.run_angle(-1*motor_speed_deg_s,  wheelTgtAngle, Stop.BRAKE, True)


def arc(leftM, rightM, axle, wheelDiam, distance,angle, speed_mm_s):
    wheelCircum=math.pi*wheelDiam
    axleTurnCircum=math.pi*axle
    degreesPerMM=360/wheelCircum

    circum = abs((360/angle) * distance)
    radius = circum/(2*math.pi)
    outerradius = radius + (axle/2)
    innerradius = radius - (axle/2)
    outercircum = outerradius * 2 * math.pi
    innercircum = innerradius * 2 * math.pi
    rightturn = True if angle*speed_mm_s > 0 else False

    outerarcMM = abs(angle) * outercircum / 360
    innerarcMM = abs(angle) * innercircum / 360

    outer_angle_change = degreesPerMM * outerarcMM
    inner_angle_change = degreesPerMM * innerarcMM

    leftMAngleChange = outer_angle_change if rightturn else inner_angle_change
    rightMAngleChange = inner_angle_change if rightturn else outer_angle_change

    time_sec= distance/speed_mm_s

    leftM.run_angle(leftMAngleChange/time_sec, abs(leftMAngleChange), Stop.BRAKE, False)
    rightM.run_angle(rightMAngleChange/time_sec,  abs(rightMAngleChange), Stop.BRAKE, True)


def calibrateGyro(gyro, newAngle=0):
    gyroSpeed = gyro.speed()
    gyroAngle = gyro.angle()
    log('calib sp: ' + str(gyroSpeed) + ' ang:' + str(gyroAngle))
    if gyroSpeed == 0 and gyroAngle == newAngle :
        log('No calibration ')
        return

    brick.sound.beep(300, 30, 8)

    cntr=0
    while (gyro.speed() > 0 and cntr < 5):
        cntr +=1
        wait(10)
    gyro.reset_angle(newAngle)
    wait(40)
    log('Aft rst gy spd ' + str(gyro.speed()) + ' ang:' + str(gyro.angle()))

def getNormalizedAngle(targetAngle, currentAngle):
    start_angle = currentAngle
    angle_change = targetAngle - currentAngle

    if (angle_change >180 ):
        angle_change = angle_change - 360
    if (angle_change < -180 ):
        angle_change = angle_change + 360
    targetAngle = angle_change + currentAngle
    log('adjust start:' + str(currentAngle) 
        + ' ang chg:' +str(angle_change)
        + ' Adj:' +str(targetAngle)
        )
    return targetAngle



def didMotorStall(motor, maxDegrees, speed):
    motorInitAngle=motor.angle()
    speed = speed * (-1 if maxDegrees < 0 else 1)
    motor.run(speed)
    angleChg = abs(motor.angle() - motorInitAngle)

    while(angleChg < abs(maxDegrees) and not motor.stalled()):
        wait(100)
        # if ( motor.stalled() ):
        #    log('DMoS stlld spd:' + str(motor.speed()) + ' angch:'  + str(tgtAngleChg))
        # #    motor.stop(Stop.BRAKE)
        #    return True
        log('DMoS not stlld spd:' + str(motor.speed()) + ' angch:'  + str(angleChg))
        angleChg = abs(motor.angle() - motorInitAngle)


    if ( motor.stalled() ):
        log('DMoS stlld spd:' + str(motor.speed()) + ' angch:'  + str(angleChg))
        return True
    log('NOt stlld - brkg')
    motor.stop(Stop.BRAKE)
    log('Done brkg')
    return False


# sweep and steop forward till color is found
def search_for_color(
    robot,
    color_sensor,
    stop_on_color):

    if  color_sensor.color() == stop_on_color: # if already there
        return True

 
    forward_steps =0 
    while forward_steps < 3:
        sweep_width = 1
        sweep_attempts = 0
        sweep_speed = 45

        while sweep_attempts < 5:
            robot.drive_time(0, sweep_speed, sweep_width * 100) #sweep right
            if  color_sensor.color() == stop_on_color:
                robot.stop(stop_type=Stop.BRAKE)
                return True
            robot.drive_time(0, -1 * sweep_speed, sweep_width * 100) #sweep left
            if  color_sensor.color() == stop_on_color:
                robot.stop(stop_type=Stop.BRAKE)
                return True
           
            sweep_width += 1
            sweep_attempts += 1
        
        # reset to point at mid point
        robot.drive_time(0, sweep_speed, int(sweep_width * 100 / 2))
        # step forward by 1 cm to sweep again
        robot.drive_time(100, 0, 100)
        forward_steps += 1

    return False


def follow_line_border(
    color_sensor,
    distance_mm,
    speed_mm_s,
    border_on_right=True):

    left_motor.reset_angle(0)
    motor_target_angle = int(DEGREES_PER_MM * distance_mm)
    target_intensity = 100

    kp=0.05
    ki=kp * 0.000
    kd=kp * 0.000
    integral=0
    prev_error=0

    border_side = 1 if border_on_right else -1
    # Keep moving till the angle of the left motor reaches target
    while (abs(left_motor.angle()) < abs(motor_target_angle)):

        color = color_sensor.color()
        intensity = color_sensor.reflection()
        error = border_side * abs(target_intensity - intensity)
        if color not in (Color.WHITE,  Color.BLACK):
            error = -1 * error
        
        angular_speed = kp * error + ki*integral + kd*(error-prev_error)
        log_string('Lfol: (' + str(color) + ' ' + str(intensity) + ')' 
            + ' err:' + str(error)+ ' spd:' + str(angular_speed))
        robot.drive(speed_mm_s, angular_speed)
        wait(20)
        prev_error = error
        integral += error

    robot.stop(stop_type=Stop.BRAKE)
