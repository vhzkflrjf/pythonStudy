import asyncio
from bleak import BleakClient

address = "D1:DA:74:18:4B:4F"
MODEL_NBR_UUID = '00002a29-e8f2-537e-4f6c-d104768a1214'

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

'''
'00001800-0000-1000-8000-00805f9b34fb'
'00002a00-0000-1000-8000-00805f9b34fb'

'00001800-0000-1000-8000-00805f9b34fb'
'00002a01-0000-1000-8000-00805f9b34fb'

'00001801-0000-1000-8000-00805f9b34fb'
'00002a05-0000-1000-8000-00805f9b34fb'

'0000180a-0000-0001-5251-d10203042000'
'00002a29-e8f2-537e-4f6c-d104768a1214'

'0000183b-e8f2-537e-4f6c-d104768a1214'
'00002a38-e8f2-537e-4f6c-d104768a1214'

'0000183b-e8f2-537e-4f6c-d104768a1214'
'00002a39-e8f2-537e-4f6c-d104768a1214'

'00002a00-0000-1000-8000-00805f9b34fb'

'00002a01-0000-1000-8000-00805f9b34fb'

'00002a04-0000-1000-8000-00805f9b34fb'

'00002aa6-0000-1000-8000-00805f9b34fb'

'6e400002-b5a3-f393-e0a9-e50e24dcca9e'

'6e400003-b5a3-f393-e0a9-e50e24dcca9e'

'''