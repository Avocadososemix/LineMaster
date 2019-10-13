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
        self.ts = TouchSensor()

    def forward(self, speed, time):
        self.both_motors.on_for_seconds(SpeedPercent(speed), SpeedPercent(speed), time) # speed 0-100
            # speed = math.floor(speed*1.2) : 100
            # time = time*1.2

    def forwardpro(self, speed):
        # print(self.cs.value)
        self.both_motors.run_forever(speed_sp=SpeedPercent(speed))
        while True:
            ground = self.cs.value()
            if (ground > 40 or ground < 27):
                self.both_motors.stop(stop_action='brake')
            break

    def turn (self, speed, time):
        ground = self.cs.value()
        if ground > 30:
            while (self.cs.value() > 30):
                # print(self.cs.value)
                # speed = math.floor(speed*1.2) : 100
                # time = time*1.2
                self.both_motors.on_for_seconds(SpeedPercent(speed), SpeedPercent(-speed/3), time) # speed 0-100
        if ground < 30:
            while (self.cs.value() < 30):
                # print(self.cs.value)
                # speed = math.floor(speed*1.2) : 100
                # time = time*1.2
                self.both_motors.on_for_seconds(SpeedPercent(-speed/3), SpeedPercent(speed), time) # speed 0-100
                # self.right_motor.on_for_seconds(SpeedPercent(speed), time)

    def boost(self, speed, time):
        self.both_motors.on_for_seconds(SpeedPercent(speed), SpeedPercent(speed), time)

    def run(self):
        self.cs.mode = 'COL-REFLECT'  # measure light intensity
        self.both_motors.STOP_ACTION_COAST = 'coast'

        self.boost(50, 7)

        while not self.shut_down:
            self.turn(50, 0.1)
            # self.forwardpro(50)
            self.forward(50, 0.1)
            print(self.cs.value())

# Main function
if __name__ == "__main__":
    print("hello")
    robot = LineMaster()
    robot.run()