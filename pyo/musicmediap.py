from pyo import *
import time
import asyncio

s = Server(audio="jack").boot() #,duplex=0).boot()

# Create a Sig object for controlling the frequency
freq = Sig(440)

# Create a Port object for smooth frequency transitions
#freq_port = Port(freq, risetime=0.01, falltime=0.01)

def procesarestado(address, *args):
	number = args[0]
	#print(number)
	if number==1:
		#a.mul = 0
		print("Muteado")
		pit.setDist('weibull')
	if number==0:
		#a.mul = 1
		print("Sonando")
		pit.setDist('cauchy')
	if number==2:
		#freq.value = 220
		wav.setOrder(1)
	if number==3:
		#freq.value = 440
		wav.setOrder(2)
	if number==4:
		#freq.value = 680
		wav.setOrder(4)
	if number==5:
		#freq.value = 900
		wav.setOrder(6)
	if number==6:
		#freq.value = 1120
		wav.setOrder(8)
		

#a = Sine(freq=freq, mul=1).out()
#s.start()

s.start()
wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.125, 12).play()
amp = TrigEnv(met, table=env, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
out = Osc(table=wav, freq=pit, mul=amp).out()



r = OscDataReceive(57120, "/estado", procesarestado)
#r2 = OscDataReceive(57120, "/pitch", procesarpitch)
