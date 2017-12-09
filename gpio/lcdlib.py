import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#set pins
rspin = 26
GPIO.setup(rspin, GPIO.OUT)

epin = 19
GPIO.setup(epin, GPIO.OUT)

#datapin[0] is physical pin [0] which is the lowest value bit (0-1)
datapin = [21, 20, 16, 26, 19, 13, 6, 5]
for i in range(0, len(datapin)):
    GPIO.setup(datapin[i], GPIO.OUT)

#make a list of booleans with a number in hex or int
def numtobus (number, size):
	listy = list(str(bin(number)))
	listy.pop(0), listy.pop(0)
	while len(listy) < size:
		listy.insert(0, "0")
    finalist = []
    for i in range(0, len(listy))
        finalist.append(bool(bin(listy[i])))
    return finalist


def wait(mill):
    start = time.time()
    while time.time() < start + mill/1000:
        a = True
#LCD commands
def senddata (rs = True, msg = 0):
    global datapin, epin, rspin

    #turn LOW all pins transfering
    GPIO.output(epin, GPIO.LOW)
    GPIO.output(rspin, GPIO.LOW)
    for i in range(0, len(datapin)):
        GPIO.output(datapin[i], GPIO.LOW)

    #turn HIGH necesary pins
    if rs:
        GPIO.output(rspin, GPIO.HIGH)

    buslist = numtobus(msg, 8)
    for i in range(0, 8):
        if buslist[i]:
            GPIO.output(datapin[7-i], HIGH)
    wait(100)

    #activate
    GPIO.output(epin, HIGH)
    wait(1)
    GPIO.output(epin, LOW)
    wait(100)

#prints a string to the screen
def writestring (thestring):
    thestring = list(thestring)
    for item in thestring:
        try:
            senddata(True, characters[item])
        except KeyError:
            print("invalid character: ",item)
        senddata(False, moveright)

def clearscreen():
    senddata(False, cleardisplay)
    senddata(False, returnhome)


#commands
cleardisplay   = 0x01
returnhome     = 0x02
entrymodeset   = 0x04
displaycontrol = 0x08
cursorshift    = 0x10
moveright      = 0x04
moveleft       = 0x00

#characters
characters =   {"0": 0x30,
                "1": 0x31,
                "2": 0x32,
                "3": 0x33,
                "4": 0x34,
                "5": 0x35,
                "6": 0x36,
                "7": 0x37,
                "8": 0x38,
                "9": 0x39
                }
