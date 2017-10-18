import time
import math
import RPi.GPIO as GPIO

#set GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#pins [0] is the highest resistance(lowest significance) bit. pinstatus states pin values
datapin = [21, 20, 16, 26, 19, 13]
pinstatus = []
for i in range(0, len(datapin)):
    pinstatus.append(0)
    GPIO.setup(datapin[i], GPIO.OUT)


#output function sets the datapins[] from a given array
def writearray(data, bus):
    global pinstatus
    for i in range(0, len(bus)):
        if data[i] and not pinstatus[i]:
            GPIO.output(bus[i], GPIO.HIGH)
            pinstatus[i] = int(data[i])
        elif pinstatus[i] and not data[i]:
            GPIO.output(bus[i], GPIO.LOW)
            pinstatus[i] = int(data[i])


#output function sends data array from numerical values
def writenumber(number, bus):
    listholder = list(str(bin(int(number))))
    listholder.pop(0), listholder.pop(0)
    finalist = []
    for i in range(0, len(listholder)):
        finalist.append(listholder[len(listholder)-(i+1)])
    while len(bus) > len(finalist):
        finalist.append(0)
    writearray(finalist,bus)




def mainloop(f, bus, maxnum):
    start = time.time()
    while True:
        newtime = time.time()
        number = (math.sin((newtime-start)*f)+1)*(maxnum/2)
        number = number * (sizemult/2)
        writenumber(number,bus)




#desired frequency
freq = 440 #440Hz = Do
anglspeed = 2*440*3.141592



#max number depending on bus size
sizemult = 63  #6bits 


mainloop(anglspeed, datapin, sizemult)














