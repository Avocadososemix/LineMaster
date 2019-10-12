#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import InfraredSensor
import time

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
        #self.left_motor.on_for_seconds(SpeedPercent(speed), time)
        #self.right_motor.on_for_seconds(SpeedPercent(speed), time)
        self.both_motors.on_for_seconds(SpeedPercent(speed), SpeedPercent(speed), time) # speed 0-100

    def turn (self, direction, speed, time):
        if direction == "left":
            while (self.cs.value() > 10):
                print(self.cs.value)
                self.both_motors.on_for_seconds(SpeedPercent(speed), SpeedPercent(speed/2), time) # speed 0-100
                # self.left_motor.on_for_seconds(SpeedPercent(speed), time)
        if direction == "right":
            while (self.cs.value() < 20):
                print(self.cs.value)
                self.both_motors.on_for_seconds(SpeedPercent(speed/2), SpeedPercent(speed), time) # speed 0-100
                # self.right_motor.on_for_seconds(SpeedPercent(speed), time)

    def turnDirection(self):
        ground = self.cs.value()
        if ground > 20 :
            return "left"
        elif ground < 10 :
            return "right"
        else:
            return "false"


    def run(self):
        # mode and asserts
        self.cs.mode = 'COL-REFLECT'  # measure light intensity
        # self.irs.mode = 'US-DIST-CM' # distance

        while not self.shut_down:
            self.turn(self.turnDirection(), 25, 0.1)
            self.forward(50, 0.1)
            print(self.cs.value())
            # time.sleep(0.1)

# Main function
if __name__ == "__main__":
    robot = LineMaster()
    robot.run()