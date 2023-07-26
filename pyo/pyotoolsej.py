from pyo import *
from pyotools import *
import time
import asyncio

s = Server(audio="jack").boot() #,duplex=0).boot()

# Create a Sig object for controlling the frequency
freq = Sig(440)
amp = Sig(0.5)

# Create a Port object for smooth frequency transitions
#freq_port = Port(freq, risetime=0.01, falltime=0.01)

def procesarestado(address, *args):
	number = args[0]
	#print(number)
	if number==1:
		#a.mul = 0
		print("Muteado")
	if number==0:
		#a.mul = 1
		print("Sonando")
	if number==2:
		freq.value = 220
	if number==3:
		freq.value = 440
	if number==4:
		freq.value = 680
	if number==5:
		freq.value = 900
	if number==6:
		freq.value = 1120
	if number==7:
		amp.value = 1
	if number==8:
		amp.value = 0.8
	if number==9:
		amp.value = 0.6
	if number==10:
		amp.value = 0.4
	if number==11:
		amp.value = 0.2
		#print("11 recibido")
	if number==49:
		print("recibido gesto 1")
	if number==50:
		print("recibido gesto 2")
	if number==51:
		print("recibido gesto inconcluso")
	
		
		
def procesarpitch(address, *args):
	number = args[0]
	print(number)
	

#a = Sine(freq=freq, mul=amp).out()
#a = PWM(freq=freq, phase=amp, duty=0.5, damp=0, mul=0.4, add=0).out()

fade = Fader(fadein=0.5, mul=0.2).play()
a = PinkNoise(fade)

# These LFOs modulate the `freq`, `spread` and `q` arguments of
# the Phaser object. We give a list of two frequencies in order
# to create two-streams LFOs, therefore a stereo phasing effect.
lf1 = Sine(freq=[0.1, 0.15], mul=100, add=250)
lf2 = Sine(freq=[0.18, 0.13], mul=0.4, add=1.5)
lf3 = Sine(freq=[0.07, 0.09], mul=5, add=6)

# Apply the phasing effect with 20 notches.
# b = Phaser(a, freq=lf1, spread=lf2, q=lf3, num=20, mul=amp).out()

sf = SfPlayer("/home/pi/Desktop/pyo/samples/thursday-drone-3.wav", speed=1, loop=True, mul=amp)#.out()
b = Phaser(sf, freq=lf1, spread=lf2, q=lf3, num=20).out()

s.start()

r = OscDataReceive(57120, "/estado", procesarestado)
#r2 = OscDataReceive(57120, "/pitch", procesarpitch)


