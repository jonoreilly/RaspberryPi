import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 21

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, GPIO.HIGH)
time.sleep(5)
GPIO.output(led, GPIO.LOW)
GPIO.cleanup()
