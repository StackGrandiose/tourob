import time
import board
from analogio import AnalogIn
from adafruit_motorkit import MotorKit
kit = MotorKit()

analog_in = AnalogIn(board.A1)

commandList = (180, 90, 0, 0, 270, 0,
               180, 90, 180, 180, 270,
               180, 90, 270, 0, 90, 90, 90,
               0, 180, 270, 180, 90, 270, 0,
               270, 270, 180, 90)

DIRECTIONS = {0: 'Up',
              90: 'Right',
              180: 'Down',
              270: 'Left'}

robotDirection = 90


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


def turn(direction, amount):
    turnDuration = 0.6
    turnSpeed = 0.7
    if amount == 2:
        turnDuration = turnDuration * 2
    if direction == 'counterClockwise':
        turnSpeed = -(turnSpeed)
    kit.motor3.throttle = -turnSpeed
    kit.motor4.throttle = -turnSpeed
    time.sleep(turnDuration)
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = -0.0
    time.sleep(1.0)


def move():
    kit.motor3.throttle = -0.55
    kit.motor4.throttle = 0.85
    time.sleep(0.9)
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
    time.sleep(1.0)


def centerAtStart():
    kit.motor3.throttle = 0.6
    kit.motor4.throttle = -0.6
    time.sleep(0.45)
    kit.motor3.throttle = 0.0
    kit.motor4.throttle = 0.0
    time.sleep(1.0)


def runInstructions():
    global robotDirection
    v = 0
    while (v < 1.3):
        v = get_voltage(analog_in)
        print(v)
        time.sleep(0.05)

    print("Exited while loop.")

    for i in range(len(commandList)):
        turnIncrement = 0
        if commandList[i] == robotDirection:
            move()
            # print("Move Foward (Facing %s)" % (DIRECTIONS[robotDirection]))
        else:
            while robotDirection != commandList[i]:
                robotDirection += 90
                turnIncrement += 1
                if robotDirection == 360:
                    robotDirection = 0
            if turnIncrement == 0:
                # print("Move.")
                move()
            elif turnIncrement == 1:
                # print("Turn 90° clockwise to face %s." % (DIRECTIONS[robotDirection]))
                turn('clockwise', 1) # 1 represents 90 degrees
                # print("Move.")
                move()
            elif turnIncrement == 2:
                # print("Turn 180° clockwise to face %s." % (DIRECTIONS[robotDirection]))
                turn('clockwise', 2)
                # print("Move.")
                move()
            elif turnIncrement == 3:
                # print("Turn 90° counterclockwise to face %s." % (DIRECTIONS[robotDirection]))
                turn('counterClockwise', 1)
                # print("Move.")
                move()


# centerAtStart()
# turn('clockwise', 1)
# print("Hello World")
# runInstructions()
# move()


