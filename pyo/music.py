from pyo import *
from random import random

s = Server(audio="jack",midi="jack").boot()
#s = Server().boot()


path = "/home/pi/Desktop/pyo/samples"

piano = [path + "piano"+str(i)+".wav" for i in range(2,9)]
dursPiano = [36,15,21,15,16,23,60]

sine = [path + "sine"+str(  i)+".wav" for i in range(1,9)]
dursSine = [36,16,31,21,15,18,19,20]

drone = [path + "thursday-drone-"+str(i)+".wav" for i in range(1,4)]

k = SfPlayer(drone[0]).out()

sfDrone = [SfPlayer(drone[i], speed=[1, 1], loop=True, mul=0.1) for i in range(len(drone))]
[d.out() for d in sfDrone]


sf = [SfPlayer(p, speed=[1, 1], loop=False, mul=0.5) for p in piano] +\
     [SfPlayer(s, speed=[1, 1], loop=False, mul=0.5) for s in sine]
durs = dursPiano + dursSine

def new_player(i):
    sf[i].out()

pat = []
for i in range(len(sf)):
    p = Pattern(function=new_player, arg=i, time=durs[i]).play()
    pat.append(p)



s.gui(locals())

