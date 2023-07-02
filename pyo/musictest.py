from pyo import *
import time
import asyncio

s = Server(audio="jack").boot() #,duplex=0).boot()
path = "/home/pi/Desktop/pyo/samples"

# Create a Sig object for controlling the frequency
freq = Sig(440)
amp = Sig(0.5)

#env = Adsr(attack=0.001, decay=0.1, sustain=0.3, release=0.1, dur=1, mul=amp)

a = Sine(freq=freq, mul=amp).out()

piano = [path + "piano"+str(i)+".wav" for i in range(2,9)]
dursPiano = [36,15,21,15,16,23,60]

s.start()

time.sleep(5)
amp.value= 0.2

time.sleep(5)
amp.value= 1
