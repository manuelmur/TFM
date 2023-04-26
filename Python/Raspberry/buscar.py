import asyncio
from bleak import BleakScanner

async def main():
    # Escanear dispositivos BLE cercanos durante 10 segundos
    devices = await BleakScanner.discover(timeout=10)

    # Imprimir información de los dispositivos encontrados
    for device in devices:
        print("Dispositivo encontrado: {0} ({1})".format(device.name, device.address))

# Ejecutar main
asyncio.run(main())
