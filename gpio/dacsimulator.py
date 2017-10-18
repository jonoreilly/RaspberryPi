import math


def divide(voltage, rl, rh):
    return voltage*(rh/(rl+rh))


digital = [0,0,0,0,0]

start = 100
resistances = [start,start*2,start*4,start*8,start*16,start*32]
rgnd = start*3
gnd = 0
vcc = 5
old = vcc

def mainloop():
    global old
    resistor = 0
    for i in range (0,len(digital)):
        if not digital[i]:
            resistor += resistances[i]
    if resistor == 0:
        new = vcc
        print(new)
        old = float(new)
    else:
        new = divide(vcc-gnd, resistor, rgnd)
        print(new, new-old)
        old = float(new)

def adddigit():
    end = False
    contar = 0
    while not end:
        if digital[contar]:
            digital[contar] = 0
            contar += 1
        elif not digital[contar]:
            digital[contar] = 1
            end = True
        if contar >= len(digital):
            end = True
            
        

def loopvalues():
    counter = 0
    while True:
        mainloop()
        adddigit()
        if digital == [1,1,1,1,1]:
            break
        
    

while True :
    exec(input("mainloop() prints the analog value,\nloopvalues() to see the changes\nChange digital[] if u want\n"))
            


