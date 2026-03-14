#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

ev3 = EV3Brick()

# moteurs bras
arm_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# moteur irrigation
water_motor = Motor(Port.C)

fruit_sensor = ColorSensor(Port.S1)

server = BluetoothMailboxServer()
command_box = TextMailbox('command', server)

print("Attente connexion MASTER...")

server.wait_for_connection()

print("MASTER connecté")

def grab():
    gripper_motor.run_target(200, -90)

def release():
    gripper_motor.run_target(200, 0)

def lift():
    arm_motor.run_target(200, -120)

def drop():
    arm_motor.run_target(200, 20)

def irrigate():
    water_motor.run_target(200, 90)
    wait(1500)
    water_motor.run_target(200, 0)

def classify_fruit():
    c = fruit_sensor.color()

    if c == Color.RED:
        return "GOOD"

    if c == Color.BLACK:
        return "BAD"

    if c == Color.GREEN:
        return "UNRIPE"

    return "UNKNOWN"

while True:
    command = command_box.read()

    if command == "GRAB":
        grab()
        lift()

    elif command == "DROP":
        drop()
        release()

    elif command == "IRRIGATE":
        irrigate()

    wait(50)