import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(led)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define button pins
led = 12
button = 16

# Turn LED on
def ledOn():
    GPIO.output(led, GPIO.HIGH)

# Turn LED off
def ledOff():
    GPIO.output(led, GPIO.LOW)

while True:
    buttonState = GPIO.input(button)

    if buttonState == False:
        ledOn()
    else:
        ledOff()
