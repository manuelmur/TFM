from pyo import *
import time

s = Server(audio="jack").boot() #,duplex=0).boot()

def printnum(address, *args):
	number = args[0]
	print(address)
	print(number)
    
#r = OscDataReceive(57120, "/number", printnum)
r = OscDataReceive(57120, "/amp", printnum)

s.gui(locals())
