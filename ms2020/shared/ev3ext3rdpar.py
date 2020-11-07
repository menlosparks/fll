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


def pivot(robot, leftM, rightM, axle, wheelDiam, angle, speedDegS):

    wheelCircum=math.pi*wheelDiam
    axleTurnCircum=math.pi*axle
    degreesPerMM=360/wheelCircum

    wheelTgtDistanceMM = (angle/360.0) * axleTurnCircum
    wheelTgtAngle = degreesPerMM * wheelTgtDistanceMM

    wait(300)

    # rightMInitAngle = rightM.angle()
    # leftMInitAngle = leftM.angle()
    # log(' leftMInitAngle ' + str(leftMInitAngle) +' rightMInitAngle ' + str(rightMInitAngle) 
    #      +  ' wheelTgtAngle ' + str(wheelTgtAngle))
    # robot.drive(0, speedDegS if angle > 0 else -1 * speedDegS )
    # # while abs(leftM.angle() - leftMInitAngle) < abs(wheelTgtAngle) and abs(rightM.angle() - rightMInitAngle) < abs(wheelTgtAngle) :
    # while (abs(leftM.angle() - leftMInitAngle)+abs(rightM.angle() - rightMInitAngle))/2 < abs(wheelTgtAngle) :
    #     wait(10)
    #     # log('lft Chg ' + str(leftM.angle() - leftMInitAngle) + ' rgtChg ' + str(rightM.angle() - rightMInitAngle))
    # robot.stop(stop_type=Stop.BRAKE)

    timeSec= abs(angle/speedDegS)
    motorSpeedDegS = abs(wheelTgtAngle/timeSec)
    rightM.run_angle(-1*motorSpeedDegS,  wheelTgtAngle, Stop.BRAKE, False)
    leftM.run_angle(motorSpeedDegS, wheelTgtAngle, Stop.BRAKE, True)

## Angle -ve for pointing left, forward or backward
def arc(robot, leftM, rightM, axle, wheelDiam, distance,angle, speedMMs):
    wheelCircum=math.pi*wheelDiam
    axleTurnCircum=math.pi*axle
    degreesPerMM=360/wheelCircum

    circum = abs((360/angle) * distance)
    radius = circum/(2*math.pi)
    outerradius = radius + (axle/2)
    innerradius = radius - (axle/2)
    outercircum = outerradius * 2 * math.pi
    innercircum = innerradius * 2 * math.pi
    rightturn = True if angle*speedMMs > 0 else False

    outerarcMM = abs(angle) * outercircum / 360
    innerarcMM = abs(angle) * innercircum / 360

    outerAngleChg = degreesPerMM * outerarcMM
    innerAngleChg = degreesPerMM * innerarcMM

    leftMAngleChange = outerAngleChg if rightturn else innerAngleChg
    rightMAngleChange = innerAngleChg if rightturn else outerAngleChg

    time_sec= distance/speedMMs


    leftM.run_angle(leftMAngleChange/time_sec, abs(leftMAngleChange), Stop.BRAKE, False)
    rightM.run_angle(rightMAngleChange/time_sec,  abs(rightMAngleChange), Stop.BRAKE, True)


def calibrateGyro(gyro, newAngle=0):
    gyroSpeed = gyro.speed()
    gyroAngle = gyro.angle()
    log('calib sp: ' + str(gyroSpeed) + ' ang:' + str(gyroAngle))
    if gyroSpeed == 0 and gyroAngle == newAngle :
        log('No calibration needed')
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
    motor.run( speed * (-1 if maxDegrees < 0 else 1))
    angleChg = abs(motor.angle() - motorInitAngle)

    while(abs(motor.angle() - motorInitAngle) < abs(maxDegrees) and not motor.stalled()):
        wait(100)

    if ( motor.stalled() ):
        log('M  stalled')
        return True
    log('M sbrkg')
    motor.stop(Stop.BRAKE)
    log('M not stalled')
    return False


def moveToClr(
    robot,
    leftM, rightM, axle, wheelDiam,
    sensor,
    mainClr,
    altClr,
    speedMM,
    lowerIntens=0,
    upperIntens=100,
    maxDistMM=300):

    wheelCircum=math.pi*wheelDiam
    axleTurnCircum=math.pi*axle
    degreesPerMM=360/wheelCircum

    leftM.reset_angle(0)
    targetAngle = int(degreesPerMM * maxDistMM)

    altClr = altClr if altClr != None else mainClr
    robot.drive(speedMM, 0)
    # Check if color reached or the angle of the left motor reaches target.
    color=sensor.color()
    intensity=sensor.reflection()
    while ((not color in (mainClr, altClr)
        or not (intensity in range (lowerIntens, upperIntens)))
        and  (abs(leftM.angle()) < abs(targetAngle)))   :
        wait(10)
        color=sensor.color()
        intensity=sensor.reflection()

    robot.stop(stop_type=Stop.BRAKE)

    log('Clr seen:(' + str(color) 
        +' ' + str(intensity)
        +' ' + str(sensor.ambient()) + ')'
        + ' searching ' + str(mainClr) + '/' + str(altClr)
        + ' inte(' + str(lowerIntens) + '-' + str(upperIntens)
        )
    return  ((color == mainClr or color == altClr) 
                  and (intensity in range (lowerIntens, upperIntens)))

def pointGyro(robot,leftM, rightM, axle, wheelDiam,   gyro, tgtAngle, speedDegS):

    gyroAngle=gyro.angle()
    # target_angle = adjust_gyro_target_angle(target_angle, gyro_angle)

    tgtAngle = getNormalizedAngle(tgtAngle, gyroAngle)
    log('TTD  Adjtgt :' +str(tgtAngle) + ' gyr:' + str(gyroAngle))

    if (abs(tgtAngle-gyroAngle) > 15):
        pivot(robot,leftM, rightM, axle, wheelDiam, tgtAngle - gyroAngle, speedDegS)
        # turn(tgtAngle - gyroAngle)

    gyroAngle=gyro.angle()

    if (abs(tgtAngle-gyroAngle) <=1):
        log('TTD not needed gyr:' +str(gyroAngle))
        return tgtAngle

    log('TTD needed gyr:' +str(gyroAngle))

    maxAttempts=10 # limit oscialltions to 10, not forever
    kp=1.5
    ki=0.1
    kd=0.1
    integral=0
    prevErr=0

    while ( abs(tgtAngle - gyroAngle) > 1 and maxAttempts >0):
        error=tgtAngle - gyroAngle
        adj_angular_speed = error * kp   + (integral + error) * ki + (error - prevErr) * kd
        robot.drive(0, adj_angular_speed)
        wait(100)
        maxAttempts -= 1
        integral += error
        prevErr = error
        gyroAngle=gyro.angle()

    robot.stop(stop_type=Stop.BRAKE)

    log('TTD done-Adjted:' + str(tgtAngle) 
        + ' gy: ' + str(gyroAngle)
        + ' remain:' + str(maxAttempts)
        )
    return tgtAngle

def movePointingGyro(    robot,
    leftM, rightM, axle, wheelDiam, gyro, distMM, speedMM, tgtAngle):

    wheelCircum=math.pi*wheelDiam
    axleTurnCircum=math.pi*axle
    degreesPerMM=360/wheelCircum

    tgtAngle = pointGyro(robot,leftM, rightM, axle, wheelDiam,   gyro, tgtAngle, speedDegS=75)
    log('MSTD  Adjtgt :' +str(tgtAngle))

    leftM.reset_angle(0)
    leftMTgtAngle = int(degreesPerMM * distMM)
    kp=1.5
    ki=0.1
    kd=0.1
    integral=0
    prevErr=0
    accelLmt = 100
    absStartingSpeed = min(abs(speedMM), 150)
    direction = 1 if speedMM > 0 else -1
    absCurrSpeed = absStartingSpeed
    while (abs(leftM.angle()) < abs(leftMTgtAngle)):
        gyroAngle = gyro.angle()
        error = tgtAngle - gyroAngle
        # log('Gyro :' + stcurrSpeedr(gyroAngle) + ' err: '+ str(error))
        adjAngularSpeed =  error * kp   + (integral + error) * ki + (error - prevErr) * kd
        robot.drive(direction * absCurrSpeed, adjAngularSpeed)
        wait(50)
        if rightM.stalled() or leftM.stalled():
            log('MSTD motor stalled ')
            return
        integral += error
        prevErr = error
        if  ( abs(leftMTgtAngle) - abs(leftM.angle())) < 360:
            # deceleration
            #  absCurrSpeed = absCurrSpeed + (accelLmt/20 ) if absCurrSpeed < abs(speedMM) else abs(speedMM)
            # absCurrSpeed = max(absCurrSpeed - ((absCurrSpeed-accelLmt)/20 ) , abs(absStartingSpeed))
            absCurrSpeed = max(absCurrSpeed - ((accelLmt)/20 ) , abs(absStartingSpeed))
        else :
            # limit on speed increase i.e. acceleration
            absCurrSpeed = min(absCurrSpeed + (accelLmt/20 ) , abs(speedMM))
            # absCurrSpeed = absCurrSpeed + (accelLmt/20 ) if absCurrSpeed < abs(speedMM) else abs(speedMM)

    log('MSTD dne gy:' + str(gyro.angle()))

    robot.stop(stop_type=Stop.BRAKE)

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
        log('Lfol: (' + str(color) + ' ' + str(intensity) + ')' 
            + ' err:' + str(error)+ ' spd:' + str(angular_speed))
        robot.drive(speed_mm_s, angular_speed)
        wait(20)
        prev_error = error
        integral += error

    robot.stop(stop_type=Stop.BRAKE)


def turn_to_color(robot, 
    color_sensor,
    stop_on_color,
    rotate_dir,
    angular_speed_deg_s):
 
    robot.drive(0, rotate_dir * angular_speed_deg_s)
    # Check if color reached.
    while color_sensor.color() != stop_on_color:
        wait(10)
    robot.stop(stop_type=Stop.BRAKE)

def turn_to_color_right(robot, 
    color_sensor,
    stop_on_color,
    angular_speed_deg_s):
 
    turn_to_color(robot,  color_sensor, stop_on_color, 1, angular_speed_deg_s)

def turn_to_color_left(robot, 
    color_sensor,
    stop_on_color,
    angular_speed_deg_s):
 
    turn_to_color(robot,  color_sensor, stop_on_color, -1, angular_speed_deg_s )



def move_to_obstacle(
    robot,
    obstacle_sensor,
    stop_on_obstacle_at,
    speed_mm_s):
 
    robot.drive(speed_mm_s, 0)
    sign = -1 if speed_mm_s < 0 else 1
    # Check if obstacle too close.
    while sign * obstacle_sensor.distance() > sign * stop_on_obstacle_at:
        log('obstacle_sensor at ' + str(obstacle_sensor.distance()))
        wait(10)

    robot.stop(Stop.BRAKE)
    