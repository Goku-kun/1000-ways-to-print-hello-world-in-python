# print Hello, World! using asyncio library 

import asyncio
async def hello():
    await asyncio.sleep(3)
    print('Hello,', end=' ')

async def world():
    await asyncio.sleep(3)
    print('World!')

a = [hello(), world()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*a))     # 'Hello, ' and 'World!' are printed synchronously one after the other  
                                                # after a time-interval of 3 seconds  
loop.close()
