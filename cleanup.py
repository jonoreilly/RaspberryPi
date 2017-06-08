import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for x in range(3, 27):

	GPIO.setup(x, GPIO.IN)

time.sleep(1)

GPIO.cleanup()

