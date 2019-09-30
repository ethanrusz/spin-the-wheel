import RPi.GPIO as GPIO
from time import sleep
import os # You must manually install mpg123 first
from multiprocessing import Process # Import process for threads

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
flag = 1

# Double blink green
def green():
    for _ in range(2):
        GPIO.output(16, GPIO.HIGH)
        sleep(1)
        GPIO.output(16, GPIO.LOW)
        sleep(1)

# Double blink red
def red():
    for _ in range(2):
        GPIO.output(18, GPIO.HIGH)
        sleep(.5)
        GPIO.output(18, GPIO.LOW)
        sleep(.25)

# Play rattle me bones audio file
def bones():
        audio = "bones.mp3"
        os.system("mpg123 " + audio)

# Strobe red and green, then exit
def exit():
    for _ in range(20):
        GPIO.output(18, GPIO.HIGH)
        sleep(.075)
        GPIO.output(18, GPIO.LOW)
        sleep(.075)
        GPIO.output(16, GPIO.HIGH)
        sleep(.075)
        GPIO.output(16, GPIO.LOW)
        sleep(.075)
    sys.exit()

# Confirm code is under main function
if __name__ == "__main__":
    # Main, run forever
    while True:
        # Define door state and multiprocessing
        redPro = Process(target = red)
        bonesPro = Process(target = bones)
        doorOpen = GPIO.input(22)
        # Respond to door state
        if doorOpen == False:
            if flag == 1:
                green()
                flag = 0
        else: # Door is opened
            red()
            if flag == 0:
                # Start threaded functions
                redPro.start()
                bonesPro.start()
                # Join threads to sync blinking
                redPro.join()
                bonesPro.join()
                redPro.terminate()
            flag = 1

        kill = GPIO.input(15)
        if kill == False: # Kill button is pushed
            exit()
