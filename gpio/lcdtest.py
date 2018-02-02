from lcdlib import clearscreen
from lcdlib import writestring
from lcdlib import start

start()

print ("all set")
while True:
    try:
        exec(input("\nclearscreen() or writestring(thestring):\n>"))
    except ValueError:
        print ("fail")
