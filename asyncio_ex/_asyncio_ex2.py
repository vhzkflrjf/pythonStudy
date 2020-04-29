import asyncio
from bleak import BleakClient

address = "D1:DA:74:18:4B:4F"
MODEL_NBR_UUID = '00002a29-e8f2-537e-4f6c-d104768a1214'

async def run(address):
    loop = asyncio.get_running_loop()
    async with BleakClient(address, loop=loop) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run(address, loop))

asyncio.run(run(address))