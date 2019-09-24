# $ sudo pip3 install adafruit-blinka

import time
import board
import digitalio

# set up door sensor
door_sensor = digitalio.DigitalInOut(board.D23)
door_sensor.direction = digitalio.Direction.INPUT

while True:

    if door_sensor.value:
        print("DOOR ALARM!")

    time.sleep(0.5)
