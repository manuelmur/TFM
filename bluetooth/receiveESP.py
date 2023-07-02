import struct
import asyncio
from bleak import BleakClient

async def run(address, service_uuid, char_uuid):
	async with BleakClient(address) as client:
		while True:
			value = await client.read_gatt_char(char_uuid)
			int_value = struct.unpack("i", value)[0]
			print("Dato: ", int(int_value))
			print("Byte_array: ", value)
			await asyncio.sleep(2)

address = "94:3C:C6:CD:E8:62" # Dirección del dispositivo
service_uuid = "19b10000-0000-537e-4f6c-d104768a1214" # UUID del servicio
char_uuid = "19b10000-2001-537e-4f6c-d104768a1214" # UUID de la característica

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, service_uuid, char_uuid))
