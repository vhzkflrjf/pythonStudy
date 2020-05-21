import asyncio
from bleak import discover
from bleak import BleakClient
import time

async def connect(address):
    #loop = asyncio.get_event_loop()
    #print(id(loop))
    client = BleakClient(address, loop=None)
    #client2 = BleakClient('C8:B8:E3:54:B7:B8', loop=loop)
    x = await client.connect(timeout = 5)
    model_number = await client.read_gatt_char('00002a00-0000-1000-8000-00805f9b34fb')
    print(model_number)
    #y = await client2.connect()
    #await loop.run_in_executor(None, functools.partial(print, 'wait', end='')
    #await loop.run_in_executor(None, print, address)    

async def run():
    start = time.time()
    done, pending = await asyncio.wait([
        connect('C6:D5:D6:D2:1A:1D'),
        connect('C8:B8:E3:54:B7:B8'),
    ])
    end = time.time()
    print(done)
    print(pending)

#devices = asyncio.run(discover(timeout=2.0))
#for d in devices:
#    print(d)
#loop = asyncio.get_event_loop()
#print(id(loop))
#loop.run_until_complete(run('C6:D5:D6:D2:1A:1D', loop))
asyncio.run(run())

