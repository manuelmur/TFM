import asyncio
from bleak import BleakClient

# Dirección MAC de la placa Nicla Sense ME
DEVICE_ADDRESS = "90:01:71:96:EC:D3"

async def run():
    # Conectarse a la placa Nicla Sense ME
    async with BleakClient(DEVICE_ADDRESS) as client:
        # Obtener las características disponibles
        services = await client.get_services()

        # Imprimir los UUID de las características disponibles
        for service in services:
            print("Servicio UUID: {}".format(service.uuid))
            for characteristic in service.characteristics:
                print("  Característica UUID: {}".format(characteristic.uuid))

# Ejecutar el bucle principal de eventos de asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
