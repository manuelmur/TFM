# Codigo para suscribirse a la caracteristica y recibir el dato cuando cambie
# Hay que ejecutarlo varias veces hasta que consigue conectar

import struct
import asyncio
import logging
import time
from bleak import BleakClient
from pythonosc import osc_message_builder
from pythonosc import udp_client

async def notif_handler(uuid, value: bytearray):
	int_value = struct.unpack("<f", value)[0]
	print("Dato: ", int(int_value))
	print("Byte_array: ", value)
	sender.send_message("/number", int(int_value))
	

async def run(address, service_uuid, char_uuid):
	async with BleakClient(address) as client:
		await client.start_notify(char_uuid, notif_handler)			
		
		while True:
			await asyncio.sleep(1)
			
address = "90:01:71:96:EC:D3" # Dirección del dispositivo
service_uuid = "19b10000-0000-537e-4f6c-d104768a1214" # UUID del servicio
char_uuid = "19b10000-2001-537e-4f6c-d104768a1214" # UUID de la característica

# Set up the OSC client
sender = udp_client.SimpleUDPClient("127.0.0.1", 57120)

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, service_uuid, char_uuid))
