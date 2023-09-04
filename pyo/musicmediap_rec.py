from pyo import *
import time
import asyncio

s = Server(audio="jack").boot() #,duplex=0).boot()

def procesarestado(address, *args):
	number = args[0]
	
	# Mano abierta/cerrada
	if number==1:
		pit.setDist('weibull')
	if number==0:
		pit.setDist('poisson')

	#Eje Y
	if number==2:
		wav.setOrder(1)
	if number==3:
		wav.setOrder(2)

	...

	# Eje X
	if number==7:
		amp.setDur(2)
	if number==8:
		amp.setDur(1.5)


	# Gestos Nicla
	if number==49:
		print("recibido gesto 1")
		out.stop()
	if number==50:
		print("recibido gesto 2")
		out.out()
	if number==51:
		print("recibido gesto inconcluso")

s.start()
wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.125, 12).play()
amp = TrigEnv(met, table=env, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
out = Osc(table=wav, freq=pit, mul=amp).out()



r = OscDataReceive(57120, "/estado", procesarestado)
