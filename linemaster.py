#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import InfraredSensor
import time
import math

class LineMaster:
    def __init__(self):
        self.shut_down = False
        # self.claw_motor
        self.left_motor = LargeMotor('outB')
        self.right_motor = LargeMotor('outC')
        self.both_motors = MoveTank('outB', 'outC')
        self.cs = ColorSensor()
        self.irs = InfraredSensor()

    def forward(self, speed, time):
#        while (self.go_forward):
        self.both_motors.on_for_seconds(SpeedPercent(speed), SpeedPercent(speed), time) # speed 0-100
            # speed = math.floor(speed*1.2) : 100
            # time = time*1.2

    def turn (self, speed, time):
        ground = self.cs.value()
        if ground > 20:
            while (self.cs.value() > 10):
                print(self.cs.value)
                # speed = math.floor(speed*1.2) : 100
                # time = time*1.2
                self.both_motors.on_for_seconds(SpeedPercent(speed), SpeedPercent(speed/6), time) # speed 0-100
        if ground < 10:
            while (self.cs.value() < 20):
                print(self.cs.value)
                # speed = math.floor(speed*1.2) : 100
                # time = time*1.2
                self.both_motors.on_for_seconds(SpeedPercent(speed/6), SpeedPercent(speed), time) # speed 0-100
                # self.right_motor.on_for_seconds(SpeedPercent(speed), time)

#    def go_left(self)
#        if self.cs.value() > 20:
#            return True
#        return False
#
#    def go_right()
#        if self.cs.value() > 10:
#            return True
#        return False
#
#    def go_forward():
#        ground = self.cs.value()
#        if (ground <= 20 and ground >= 10):
#            return True
#        return False

    def run(self):
        # mode and asserts
        self.cs.mode = 'COL-REFLECT'  # measure light intensity
        self.both_motors.STOP_ACTION_COAST = 'coast'
        # self.irs.mode = 'US-DIST-CM' # distance

        while not self.shut_down:
            self.turn(50, 0.1)
            self.forward(50, 0.1)
            print(self.cs.value())

# Main function
if __name__ == "__main__":
    robot = LineMaster()
    robot.run()