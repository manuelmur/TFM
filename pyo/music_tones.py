from pyo import *
import time

s = Server(audio="jack").boot() #,duplex=0).boot()

# Define the sound objects for different tones
tone1 = Sine(mul=0.3).out()
tone2 = Noise(mul=0.3).out()
tone3 = FM(mul=0.3).out()

def printnum(address, *args):
	number = args[0]
	print(address)
	print(number)
    
	if number == 1:
		tone1.play()
		time.sleep(1)
		tone1.stop
	elif number == 2:
		tone2.play()
		time.sleep(1)
		tone2.stop
	else:
		tone3.play()
		time.sleep(1)
		tone3.stop
    
r = OscDataReceive(57120, "/number", printnum)

s.gui(locals())
