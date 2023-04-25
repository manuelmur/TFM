import struct
import asyncio
from bleak import BleakClient

# Dirección MAC de la placa Nicla Sense ME
DEVICE_ADDRESS = "FCFF050A-49D1-1C73-83FF-C1BF1E319E1F"

# UUID del servicio BLE que proporciona los datos
SERVICE_UUID = "19b10000-0000-537e-4f6c-d104768a1214"

# UUID de la característica que contiene los datos
CHARACTERISTIC_UUID = "19b10000-2001-537e-4f6c-d104768a1214"

async def run():
    # Conectarse a la placa Nicla Sense ME
    async with BleakClient(DEVICE_ADDRESS) as client:
        while True:
            # Obtener la característica que contiene los datos
            characteristic = await client.read_gatt_char(CHARACTERISTIC_UUID)

            # Convertir la característica en un número de punto flotante de 32 bits
            f = struct.unpack("<f", characteristic)[0]

            # Convertir el número de punto flotante a un entero
            data = int(f)

            # Imprimir el entero
            print(data)

            # Esperar 2 segundos antes de volver a leer los datos
            await asyncio.sleep(2)

# Ejecutar el bucle principal de eventos de asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
