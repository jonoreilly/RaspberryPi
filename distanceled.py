import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

trig = 26
echo = 19

green = 21
yellow = 20
red = 16

dist_gy = 25
dist_yr = 10

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)


def green_light():
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)

def yellow_light():
    GPIO.output(green, GPIO.LOW)
    GPIO.output(yellow, GPIO.HIGH)
    GPIO.output(red, GPIO.LOW)

def red_light():
    GPIO.output(green, GPIO.LOW)
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(red, GPIO.HIGH)

def get_distance():

    GPIO.output(trig,True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == False:
        start = time.time()

    while GPIO.input(echo) == True:
        end = time.time()

    sig_time = end - start

    #cm
    distance = sig_time / 0.000058

    print("Distance: {} cm".format(distance))
    return distance

while True:
    distance = get_distance()
    time.sleep(0.05)

    if distance >= dist_gy:
        green_light()
    elif dist_gy > distance > dist_yr:
        yellow_light()
    elif dist_yr > distance:
        red_light()
