# forked from: https://sites.google.com/site/ev3python/learn_ev3_python/remote-control

from time import sleep
from ev3dev.ev3 import *

lmotor = LargeMotor('outB')
rmotor = LargeMotor('outC')

mmotor = MediumMotor('outA')

# Connect remote control
rc = RemoteControl()

def roll(motor, direction):
    def on_press(state):
        if state:
            # Roll when button is pressed
            motor.run_forever(speed_sp=900*direction)
        else:
            # Stop otherwise
            motor.stop(stop_action='brake')
    return on_press



# Assign event handler to each of the remote buttons
rc.on_red_up    = roll(rmotor, 1)
rc.on_red_down  = roll(rmotor, -1)
rc.on_blue_up   = roll(lmotor,  1)
rc.on_blue_down = roll(lmotor, -1)



# Enter event processing loop
#while not button.any():   #not working so commented out
while True:   #replaces previous line so use Ctrl-C to exit
    rc.process()
    sleep(0.01)
# Press Ctrl-C to exit