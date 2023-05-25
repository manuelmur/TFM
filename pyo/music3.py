from pyo import *
s = Server(audio="jack").boot() #,duplex=0).boot()

a = Sine(mul=1).out()
s.gui(locals())