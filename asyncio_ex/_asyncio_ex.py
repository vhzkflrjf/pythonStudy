from time import time, sleep
from urllib.request import Request, urlopen
import asyncio
 
urls = [i for i in range(1,10)]
 
def add(a,b):
    print('add: {0} + {1}'.format(a, b))
    #await asyncio.sleep(1.0)    # 1초 대기. asyncio.sleep도 네이티브 코루틴
    sleep(1)
    return a + b    # 두 수를 더한 결과 반환

# async def add(a,b):
#     print('add: {0} + {1}'.format(a, b))
#     #await asyncio.sleep(1.0)    # 1초 대기. asyncio.sleep도 네이티브 코루틴
#     sleep(1)
#     return a + b    # 두 수를 더한 결과 반환

async def fetch(a):    
    
    #result = await add(a,1)                # add가 코루틴 함수일 경우 그냥 불러주면 된다.
    result = await loop.run_in_executor(None, add, a, 2)     #add가 코루틴 함수가 아닌 경우 loop.run_in_executor로 코루틴 함수로 만들어야 한다.
    #response = await loop.run_in_executor(None, urlopen, request)    # run_in_executor 사용
    #page = response.read()
    print('print_add: {0} + {1} = {2}'.format(a, 2, result))
    return result


async def main():
    futures = [asyncio.ensure_future(fetch(a)) for a in urls]
                                                           # 태스크(퓨처) 객체를 리스트로 만듦
    result = await asyncio.gather(*futures)                # 결과를 한꺼번에 가져옴
    print(result)
 
async def main2():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
                                                           # 태스크(퓨처) 객체를 리스트로 만듦
    result = await asyncio.gather(*futures)                # 결과를 한꺼번에 가져옴
    print(result)

begin = time()
loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(main())          # main이 끝날 때까지 기다림
loop.run_until_complete(main2())          # main이 끝날 때까지 기다림
loop.close()                             # 이벤트 루프를 닫음
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))