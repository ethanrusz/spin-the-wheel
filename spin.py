import RPi.GPIO as GPIO
from time import sleep

# Configure board and set warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED output config
GPIO.setup(16, GPIO.OUT, initial = GPIO.LOW) # Green LED
GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW) # Red LED
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Door Sensor

# Blink green for 1s
def green():
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
    GPIO.output(16, GPIO.LOW)
    sleep(1)

# Double blink red 1s
def red():
    GPIO.output(18, GPIO.HIGH)
    sleep(1)
    GPIO.output(18, GPIO.LOW)
    sleep(.5)
    GPIO.output(18, GPIO.HIGH)
    sleep(1)
    GPIO.output(18, GPIO.LOW)
    sleep(1)

# Main, run forever
while True:
    doorOpen = GPIO.input(22)
    # Respond to door state
    if doorOpen == False:
        green()
    else:
        red()
