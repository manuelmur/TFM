import asyncio
from bleak import discover

async def run():
    # Escanear dispositivos BLE cercanos durante 10 segundos
    devices = await discover(timeout=10)

    # Imprimir información de los dispositivos encontrados
    for device in devices:
        print("Dispositivo encontrado: {0} ({1})".format(device.name, device.address))

# Ejecutar el bucle principal de eventos de asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
