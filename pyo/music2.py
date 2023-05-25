from pyo import *

s = Server(audio="jack",duplex=0).boot()
#s = Server().boot()

s.start()

a = Sine(mul=0.01).out()
