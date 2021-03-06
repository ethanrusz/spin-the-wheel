import RPi.GPIO as GPIO
from time import sleep
import os # You must manually install mpg123 first
import random
from multiprocessing import Process # Import process for threads
import sys

# Pin setup - Change this if your GPIO layout is different
greenLEDPin = 16
redLEDPin = 18
doorPin = 22
killPin = 15
mutePin = 37
randomPin = 13

# Configure board and set warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED output config
GPIO.setup(greenLEDPin, GPIO.OUT, initial = GPIO.LOW) # Green LED
GPIO.setup(redLEDPin, GPIO.OUT, initial = GPIO.LOW) # Red LED

# Input config
GPIO.setup(doorPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Door Sensor
GPIO.setup(killPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Kill Button
GPIO.setup(mutePin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Mute Button
GPIO.setup(randomPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Toggle random mode Button

# Flag to track audio - Do not alter these values manually
flag = 1
randomMode = False

# Double blink green
def green():
    for _ in range(2):
        GPIO.output(greenLEDPin, GPIO.HIGH)
        sleep(.5)
        GPIO.output(greenLEDPin, GPIO.LOW)
        sleep(.5)

# Double blink red
def red():
    for _ in range(2):
        GPIO.output(redLEDPin, GPIO.HIGH)
        sleep(.25)
        GPIO.output(redLEDPin, GPIO.LOW)
        sleep(.25)

# Play audio file
def bones():
    os.system("mpg123 " + audio)

# Strobe red and green, then exit
def exit():
    for _ in range(20):
        GPIO.output(redLEDPin, GPIO.HIGH)
        sleep(.075)
        GPIO.output(redLEDPin, GPIO.LOW)
        sleep(.075)
        GPIO.output(greenLEDPin, GPIO.HIGH)
        sleep(.075)
        GPIO.output(greenLEDPin, GPIO.LOW)
        sleep(.075)
    sys.exit()

# Disable rig for killPins
def muted():
    flag = 2
    GPIO.output(redLEDPin, GPIO.HIGH)
    sleep(killPin)
    GPIO.output(redLEDPin, GPIO.LOW)
    flag = 1
    green()

# Toggle random mode
def togRandom():
    global randomMode
    if not randomMode:
        randomMode = True
        print("[" + u'\u2713' "] Random Mode on.")
        green()
        return
    if randomMode:
        randomMode = False
        print("[" + u'\u2717' + "] Random Mode off.")
        red()

# Confirm code is under main function
if __name__ == "__main__":
    # Main, run forever
    while True:
        # Define door state and multiprocessing
        redPro = Process(target = red)
        bonesPro = Process(target = bones)
        doorOpen = GPIO.input(doorPin)
        # Respond to door state
        if doorOpen == False: # Door closed
            if flag == 1:
                audio = "./defaultAudio/bones.mp3"
                green()
                flag = 0
        else: # Door is opened
            red()
            if flag == 0:
                # Pick the audio
                if randomMode:
                    try:
                        audio = ("./audio/" + random.choice(os.listdir("./audio/")))
                        print("Audio set to " + audio + ".")
                    except:
                        "Oops! Something went wrong. Reverting to classic mode."
                # Start threaded functions
                bonesPro.start()
                # Blink red light while audio plays
                while bonesPro.is_alive():
                    red()
                # Wait for audio to end
                bonesPro.join()
            flag = 1

        kill = GPIO.input(killPin)
        if kill == False: # Kill button has been pushed
            exit()

        mute = GPIO.input(mutePin)
        if mute == False: # Mute button has been pushed
            muted()

        randomIn = GPIO.input(randomPin)
        if randomIn == False: # Random mode button has been pushed
            togRandom()
