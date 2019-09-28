import RPi.GPIO as GPIO
from time import sleep

# Configure board and set warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED output config
GPIO.setup(16, GPIO.OUT, initial = GPIO.LOW) # Green LED
GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW) # Red LED

# Blink green for 1s
def green():
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
    GPIO.output(16, GPIO.LOW)

# Double blink red 1s
def red():
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
    GPIO.output(16, GPIO.LOW)
    sleep(.5)
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
    GPIO.output(16, GPIO.LOW)

while True
    green()
    red()
    sleep(1)
