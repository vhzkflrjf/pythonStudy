import asyncio
from bleak import BleakScanner

async def run():      #synchronous context manager way
    async with BleakScanner() as scanner:
        await asyncio.sleep(2.0)
        devices = await scanner.get_discovered_devices()
    for d in devices:
        print(d)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())

asyncio.run(run(), debug=False) # 항상 새 이벤트 루프를 만들고 끝에 이벤트 루프를 닫습니다. asyncio 프로그램의 메인 진입 지점으로 사용해야 하고, 이상적으로는 한 번만 호출