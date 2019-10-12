#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

class LineMaster:
    def __init__(self):
        self.shut_down = False
        # self.claw_motor
        self.left_motor = LargeMotor(OUTPUT_B)
        self.right_motor = LargeMotor(OUTPUT_C)
        self.both_motors = MoveTank(OUTPUT_B, OUTPUT_C)
        self.cs = ColorSensor()
        self.irs = InfraredSensor()

    def forward(self, speed, time):
        self.both_motors.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), time) # speed 0-100

    def turn (self, direction, speed, time):
        if direction == "left":
            while (cs.value() > 5):
                self.left_motor.on_for_rotations(SpeedPercent(speed), time)
        if direction == "right":
            while (cs.value() < 15):
                self.right_motor.on_for_rotations(SpeedPercent(speed), time)

    def turnDirection(self):
        ground = cs.value()
        if ground > 15 :
            return "left"
        elif ground < 5 :
            return "right"
        else:
            return "false"


    def run(self):
        # mode and asserts
        self.cs.mode = 'COL-REFLECT'  # measure light intensity
        # self.irs.mode = 'US-DIST-CM' # distance
        # claw; assert self.claw.connected  # medium motor
        # self.cs; assert self.cs.connected
        self.right_motor; assert self.right_motor.connected
        self.left_motor; assert self.left_motor.connected

        while not self.shut_down:
            forward(50, 0.1)
            turn(turnDirection(), 25, 0.1)
            print(cs.value())
            time.sleep(0.1)

# Main function
if __name__ == "__main__":
    robot = LineMaster()
    robot.run()