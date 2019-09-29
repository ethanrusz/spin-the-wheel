import RPi.GPIO as GPIO
from time import sleep
import os # Install mpg123 first

# Configure board and set warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED output config
GPIO.setup(16, GPIO.OUT, initial = GPIO.LOW) # Green LED
GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW) # Red LED

# Input config
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Door Sensor
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Kill Button

# Flag to track audio
flag = 0

# Blink green for 1s
def green():
    flag = 0
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
    GPIO.output(16, GPIO.LOW)
    sleep(1)

# Double blink red 1s
def red():
    for _ in range(2):
        GPIO.output(18, GPIO.HIGH)
        sleep(.5)
        GPIO.output(18, GPIO.LOW)
        sleep(.25)

# Play rattle me bones audio file
def bones():
        audio = "spook.mp3"
        os.system("mpg123 " + audio)

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
    sys.exit()

# Main, run forever
while True:
    doorOpen = GPIO.input(22)
    # Respond to door state
    if doorOpen == False:
        green()
    else:
        red()
        if flag == 0:
            bones()

        flag = 1
        
    kill = GPIO.input(15)
    if kill == False: # Kill button is pushed
        exit()
