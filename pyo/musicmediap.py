from pyo import *
import time
import asyncio

s = Server(audio="jack").boot() #,duplex=0).boot()

def procesarestado(address, *args):
	number = args[0]
	#print(number)
	if number==1:
		print("Distribucion weibull")
		pit.setDist('weibull')
	if number==0:
		print("Distribucion poisson")
		pit.setDist('poisson')
		
	#Eje Y
	if number==2:
		wav.setOrder(1)
	if number==3:
		wav.setOrder(2)
	if number==4:
		wav.setOrder(4)
	if number==5:
		wav.setOrder(6)
	if number==6:
		wav.setOrder(8)
	
	# Eje X
	if number==7:
		amp.setDur(2)
	if number==8:
		amp.setDur(1.5)
	if number==9:
		amp.setDur(1)
	if number==10:
		amp.setDur(.6)
	if number==11:
		amp.setDur(.25)

s.start()
wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.125, 12).play()
amp = TrigEnv(met, table=env, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
out = Osc(table=wav, freq=pit, mul=amp).out()



r = OscDataReceive(57120, "/estado", procesarestado)
