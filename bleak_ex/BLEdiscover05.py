import asyncio
from bleak import discover

devices = asyncio.run(discover(timeout=2.0))

for d in devices:
    print(d)

