wait = 0.001

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

pins = [21,20,16,12]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)




def setout(layout):
	global pins
	for i in range(0,len(layout)):
		GPIO.output(pins[i], layout[i])


def loop(layouts, delay):
	for step in layouts:
		start = time.time()
		setout(step)
		print (time.time()-start)
		time.sleep(delay)


set1 = [[1,0,0,0],[1,1,0,0],
	[0,1,0,0],[0,1,1,0],
	[0,0,1,0],[0,0,1,1],
	[0,0,0,1],[1,0,0,1]]

enter = int(input("1 for loop, 0 for clean"))

while enter:
	loop(set1, wait)
	

setout ([0,0,0,0])




