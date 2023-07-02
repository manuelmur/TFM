from pyo import *
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
		a.mul = 0
		print("Muteado")
	if number==0:
		a.mul = 1
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
		print("11 recibido")
		
		
def procesarpitch(address, *args):
	number = args[0]
	print(number)
	

a = Sine(freq=freq, mul=amp).out()

s.start()

r = OscDataReceive(57120, "/estado", procesarestado)
#r2 = OscDataReceive(57120, "/pitch", procesarpitch)


