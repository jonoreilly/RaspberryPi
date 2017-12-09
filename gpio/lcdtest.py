import lcdlib

print ("all set")
while True:
	try:
		exec(input("\nclearscreen() or writestring(thestring):\n>"))
	except ValueError:
		print ("fail")

