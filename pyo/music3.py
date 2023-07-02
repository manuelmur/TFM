from pyo import *
import time

s = Server(audio="jack").boot() #,duplex=0).boot()

a = Sine(mul=1).out()
#s.gui(locals())
s.start()

time.sleep(5)

s.stop()

time.sleep(2)

s.start()
