import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)
state = 0
photo_trans = 6
GPIO.setup(photo_trans, GPIO.IN)

while True:
    state = GPIO.input(photo_trans)
    state = not state
    GPIO.output(led, state)