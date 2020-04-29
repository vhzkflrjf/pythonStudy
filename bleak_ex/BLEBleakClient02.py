import asyncio
from bleak import BleakClient

address = "C6:D5:D6:D2:1A:1D"
MODEL_NBR_UUID = '6e400003-b5a3-f393-e0a9-e50e24dcca9e'

async def run(address, loop):
    client = BleakClient(address, loop=loop)
    try:
        await client.connect()
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))
    except Exception as e:
        print(e)
    finally:
        await client.disconnect()

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))