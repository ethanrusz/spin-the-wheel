import RPi.GPIO as GPIO
from time import sleep

# Configure board and set warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED output config
GPIO.setup(16, GPIO.OUT, initial = GPIO.LOW) # Green LED
GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW) # Red LED

# Input config
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Door Sensor
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Kill Button

# Blink green for 1s
def green():
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
    GPIO.output(16, GPIO.LOW)
    sleep(1)

# Double blink red 1s
def red():
    for _ in range(2):
        GPIO.output(18, GPIO.HIGH)
        sleep(1)
        GPIO.output(18, GPIO.LOW)
        sleep(.5)

def exit():
    for _ in range(25):
        GPIO.output(18, GPIO.HIGH)
        sleep(.075)
        GPIO.output(18, GPIO.LOW)
        sleep(.075)
        GPIO.output(16, GPIO.HIGH)
        sleep(.075)
        GPIO.output(16, GPIO.LOW)
        sleep(.075)

# Main, run forever
while True:
    doorOpen = GPIO.input(22)
    # Respond to door state
    if doorOpen == False:
        green()
    else:
        red()

    kill = GPIO.input(15)
    if kill == True: # Kill button is pushed
        exit()
