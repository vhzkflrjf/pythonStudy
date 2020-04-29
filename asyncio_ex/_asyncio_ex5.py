import asyncio
from bleak import discover
from bleak import BleakClient

address1 = "D1:DA:74:18:4B:4F"
address2 = "C6:D5:D6:D2:1A:1D"
MODEL_NBR_UUID1 = '00002a29-e8f2-537e-4f6c-d104768a1214'
MODEL_NBR_UUID2 = '00002a00-0000-1000-8000-00805f9b34fb'

async def run(address, uuid):
    loop = asyncio.get_running_loop()
    client = BleakClient(address, loop=loop)
    await client.connect()
    model_number = await client.read_gatt_char(uuid)
    print("Model Number: {0}".format("".join(map(chr, model_number))))
    return client

async def InputService(services):   # set InputMessage
    for cur_ser in services:
        print("[Service] {0} {1}".format(cur_ser.uuid, cur_ser.description))
    while True:
        Service_uuid = input("Select Service above: ")
        if Service_uuid in services.services.keys():
            return services.services[Service_uuid]

async def InputCharacteristic(characteristics):  
    for cur_char in characteristics:
        print("[Characteristic] {0} {1}".format(cur_char.uuid, cur_char.description))    
    while True:
        Char_uuid = input("Select Characteristic above: ")
        for char in characteristics:
            if Char_uuid == char.uuid:
                return char

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run(address, loop))

devices = asyncio.run(discover())
for dev in devices:
    print(dev)

client1 = asyncio.run(run(address1, MODEL_NBR_UUID1))
client2 = asyncio.run(run(address2, MODEL_NBR_UUID2))
service1 = asyncio.run(InputService(client1.services))
service2 = asyncio.run(InputService(client2.services))
characteristic1 = asyncio.run(InputCharacteristic(service1.characteristics))
characteristic2 = asyncio.run(InputCharacteristic(service2.characteristics))

