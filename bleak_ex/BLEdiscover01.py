import asyncio
from bleak import discover

async def run():
    devices = await discover(timeout=2.0)
    for d in devices:
        print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())